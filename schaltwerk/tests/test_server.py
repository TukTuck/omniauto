"""Tests für die reinen Funktionen und die API-Oberfläche von server.py.

Läuft ohne Netz und ohne OmniRoute: pytest tests/
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server  # noqa: E402


# ── Zeilen-Parser ────────────────────────────────────────────────────

class TestParseProxyLine:
    def test_einfach_http(self):
        p = server.parse_proxy_line("1.2.3.4:8080")
        assert p["host"] == "1.2.3.4" and p["port"] == 8080 and p["type"] == "http"

    def test_mit_schema(self):
        p = server.parse_proxy_line("socks5://5.6.7.8:1080")
        assert p["type"] == "socks5" and p["host"] == "5.6.7.8"

    def test_mit_auth(self):
        p = server.parse_proxy_line("user:pw@9.9.9.9:3128")
        assert p["username"] == "user" and p["password"] == "pw"

    def test_socks4_wird_verworfen(self):
        assert server.parse_proxy_line("socks4://1.1.1.1:1080") is None

    def test_kommentare_und_leer(self):
        assert server.parse_proxy_line("# Kommentar") is None
        assert server.parse_proxy_line("") is None
        assert server.parse_proxy_line("   ") is None

    def test_ipv6_wird_verworfen(self):
        assert server.parse_proxy_line("[::1]:8080") is None

    def test_port_bereich(self):
        assert server.parse_proxy_line("1.1.1.1:0") is None
        assert server.parse_proxy_line("1.1.1.1:99999") is None

    def test_muell(self):
        assert server.parse_proxy_line("kein proxy hier") is None


# ── Schlüssel / Dedupe ───────────────────────────────────────────────

class TestProxyKeyUndMerge:
    def test_key_enhaelt_typ_host_port(self):
        assert server.proxy_key({"type": "http", "host": "1.2.3.4", "port": 80}) == "http://1.2.3.4:80"

    def test_merge_dedupliziert(self):
        store: dict = {}
        server.merge_proxy(store, {"type": "http", "host": "h", "port": 1, "country": None}, "a")
        server.merge_proxy(store, {"type": "http", "host": "h", "port": 1, "country": "DE"}, "b")
        assert len(store) == 1
        assert store["http://h:1"]["country"] == "DE"
        assert store["http://h:1"]["source"] == "a"  # erste Quelle gewinnt


# ── OmniRoute-Hilfen ─────────────────────────────────────────────────

class TestOmniHelpers:
    def test_unwrap_list_variants(self):
        assert server.unwrap_list([1]) == [1]
        assert server.unwrap_list({"proxies": [1]}) == [1]
        assert server.unwrap_list({"items": [2]}) == [2]
        assert server.unwrap_list(None) == []
        assert server.unwrap_list({"x": 1}) == []

    def test_is_harvest_ueber_notes_und_name(self):
        assert server.is_harvest({"notes": "proxy-exchange https_ok"}) is True
        assert server.is_harvest({"name": "px-de-1.2.3.4"}) is True
        assert server.is_harvest({"name": "Mein Proxy", "notes": ""}) is False

    def test_latency_aus_notes(self):
        assert server.proxy_latency_ms({"notes": "x latency=230ms y"}) == 230
        assert server.proxy_latency_ms({"notes": ""}) == 9999

    def test_schemes_https_fallback(self):
        assert server.schemes_to_try("https") == ["https", "http"]
        assert server.schemes_to_try("http") == ["http"]
        assert server.schemes_to_try("socks5") == ["socks5"]

    def test_clean_types(self):
        assert server.clean_types(["HTTP", "socks5", "quatsch"]) == ["http", "socks5"]
        assert server.clean_types(None) == ["http", "https"]
        assert server.clean_types([]) == ["http", "https"]


# ── API-Oberfläche (ohne OmniRoute) ──────────────────────────────────

@pytest.fixture()
def client(monkeypatch):
    server.settings["api_key"] = ""
    server.settings["omni_url"] = "http://127.0.0.1:20128"
    server.scheduler_state.update(enabled=False, next_run=None, last_error=None)
    server.job_state.update(running=False, error=None)
    server.tray.clear()
    server.bw_log.clear()
    with TestClient(server.app) as c:
        yield c


class TestApi:
    def test_meta(self, client):
        r = client.get("/api/meta")
        assert r.status_code == 200
        body = r.json()
        assert body["harvest_tag"] == "proxy-exchange"
        assert any(s["id"] == "geonode" for s in body["sources"])

    def test_connect_validiert_url(self, client):
        r = client.post("/api/connect", json={"omni_url": "nicht-eine-url", "api_key": "x"})
        assert r.status_code == 400
        # kaputte URL darf Zustand nicht überschreiben
        assert server.settings["omni_url"] == "http://127.0.0.1:20128"
        assert server.settings["api_key"] == ""

    def test_connect_behaelt_key_bei_leerem_feld(self, client):
        server.settings["api_key"] = "alter-key"
        client.post("/api/connect", json={"omni_url": "http://127.0.0.1:20128", "api_key": ""})
        assert server.settings["api_key"] == "alter-key"

    def test_connect_erkenn_403_als_auth_fehler(self, client, monkeypatch):
        """OmniRoute antwortet bei ungueltigem Token mit 403, nicht 401 —
        connect darf das nicht als Erfolg melden."""
        class FakeResp:
            status_code = 403
            text = '{"error":{"message":"Invalid management token"}}'
        async def fake(method, path, **kw):
            return FakeResp()
        monkeypatch.setattr(server, "omni_request", fake)
        r = client.post("/api/connect", json={"omni_url": "http://127.0.0.1:20128", "api_key": "tot"})
        body = r.json()
        assert body["auth_ok"] is False
        assert body["ok"] is False

    def test_job_status(self, client):
        r = client.get("/api/job-status")
        assert r.status_code == 200
        assert "running" in r.json()

    def test_schedule_validierung(self, client):
        r = client.post("/api/schedule", json={"enabled": True, "interval_min": 1})
        assert r.status_code == 400
        r = client.post("/api/schedule", json={"enabled": True, "interval_min": 30})
        assert r.status_code == 200
        assert r.json()["enabled"] is True
        assert r.json()["next_run"] is not None
        r = client.post("/api/schedule", json={"enabled": False, "interval_min": 30})
        assert r.json()["next_run"] is None

    def test_push_selected_ohne_proxies(self, client):
        r = client.post("/api/push-selected", json={"proxies": []})
        assert r.status_code == 400

    def test_push_selected_skippt_ungepruefte(self, client):
        r = client.post("/api/push-selected", json={
            "proxies": [{"host": "1.2.3.4", "port": 80, "type": "http", "https_ok": False}]
        })
        assert r.status_code == 200
        assert r.json()["counts"]["skipped"] == 1
        assert r.json()["counts"]["pushed"] == 0

    def test_push_selected_skippt_riskante(self, client):
        """TLS-Intercept-Proxies dürfen nie ins Register — der Proxy könnte
        Provider-API-Keys im Klartext mitlesen."""
        r = client.post("/api/push-selected", json={
            "proxies": [{"host": "6.6.6.6", "port": 8080, "type": "http", "https_ok": True,
                         "risk": "tls-intercept"}]
        })
        assert r.status_code == 200
        assert r.json()["counts"]["skipped"] == 1
        assert r.json()["counts"]["pushed"] == 0
        assert "tls" in r.json()["skipped"][0]["reason"]

    def test_hub_summary_ohne_key(self, client):
        r = client.get("/api/hub-summary")
        assert r.status_code == 200
        body = r.json()
        assert body["has_key"] is False
        assert body["providers"] is None
        assert "job" in body


class TestTray:
    """Die Wölfin — Ablage der Hub-KI."""

    def test_add_list_remove(self, client):
        r = client.post("/api/tray", json={"items": [{"kind": "text", "text": "hallo wolf"}]})
        assert r.status_code == 200
        assert r.json()["added"] == 1
        tid = r.json()["items"][-1]["id"]
        r = client.get("/api/tray")
        assert any(i["id"] == tid for i in r.json()["items"])
        r = client.delete("/api/tray", params={"id": tid})
        assert all(i["id"] != tid for i in r.json()["items"])

    def test_leere_items_werden_ignoriert(self, client):
        r = client.post("/api/tray", json={"items": [{"text": "   "}, {"text": "ok"}]})
        assert r.json()["added"] == 1

    def test_clear_all(self, client):
        client.post("/api/tray", json={"items": [{"text": "a"}, {"text": "b"}]})
        r = client.delete("/api/tray")
        assert r.json()["items"] == []

    def test_text_wird_ggekuerzt(self, client):
        r = client.post("/api/tray", json={"items": [{"text": "x" * 9999}]})
        assert len(r.json()["items"][-1]["text"]) == 4000

    def test_check_bekannter_id_fehlt(self, client):
        r = client.post("/api/tray/check", params={"id": "gibt-es-nicht"}, json={})
        assert r.status_code == 404

    def test_stimme_bei_ablage_und_pruefung(self, client):
        """Bad Wolf spricht, wenn sie sammelt und urteilt."""
        r = client.post("/api/tray", json={"items": [{"kind": "proxy", "text": "192.0.2.9:9999"}]})
        log = client.get("/api/bw-log").json()["lines"]
        assert any("Ablage" in l["text"] for l in log)
        tid = r.json()["items"][-1]["id"]
        client.post("/api/tray/check", params={"id": tid}, json={})
        log = client.get("/api/bw-log").json()["lines"]
        assert any("tot" in l["text"] for l in log)

    def test_check_ablehnt_nicht_proxy(self, client):
        r = client.post("/api/tray", json={"items": [{"kind": "text", "text": "nur ein Satz"}]})
        tid = r.json()["items"][-1]["id"]
        r = client.post("/api/tray/check", params={"id": tid}, json={})
        assert r.status_code == 400

    def test_push_selected_max_100(self, client):
        proxies = [{"host": f"1.2.3.{i % 256}", "port": 80, "https_ok": True} for i in range(101)]
        r = client.post("/api/push-selected", json={"proxies": proxies})
        assert r.status_code == 400

    def test_exchange_409_bei_laufendem_job(self, client):
        server.job_state["running"] = True
        r = client.post("/api/exchange", json={})
        assert r.status_code == 409
        server.job_state["running"] = False

    def test_proxy_logs_ohne_key(self, client):
        r = client.get("/api/omni/proxy-logs")
        assert r.status_code == 400
