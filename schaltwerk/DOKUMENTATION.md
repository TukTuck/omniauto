# SCHALTWERK / BWO — Sprint-Dokumentation

**Stand:** 2026-09-08 · **Zweig:** `sprint/polish` · **Ausgangspunkt:** Commit `6b0a126` (v1.0.0)
**Diese Datei dokumentiert den kompletten Sprint: alles, was geändert, gebaut und entschieden wurde.**

---

## 1. Was Schaltwerk ist

Ein lokales Werkzeug (Browser-UI + Python-Server) zwischen freien Proxy-Listen und
OmniRoute: Proxies holen, selbst gegen echte HTTPS-Ziele prüfen, tote eigene Einträge
entfernen, Lebendige als **manuelle** Registry-Proxies nach OmniRoute schreiben —
nie in die 1proxy-/Free-Kategorie (Costs Credits), nie eigene Benutzer-Proxies anfassen
(Erkennung: `notes` enthält `proxy-exchange` oder Name beginnt mit `px-`).

Seit diesem Sprint ist Schaltwerk außerdem die erste **Seite im BWO-Hub** und hat eine
Marken-Figur: **Bad Wolf** (siehe Abschnitt 6).

---

## 2. Sprint-Verlauf (Commits auf `sprint/polish`)

| Commit | Inhalt |
| --- | --- |
| `8449c0b` | **v1.1.0 „Stabilität + Hub-Vorbereitung"** — P1-Fixes (XSS, Doppelstart-Sperre, Job-Status-Reload, connect-Validierung), komplette UI-Erneuerung, geplanter Austausch, manuelles Übernehmen, Live-Traffic, Quellenauswahl, 25 Tests |
| `93187a2` | **Hub-Start** — Übersichtsseite (`/api/hub-summary`) als Startseite, Provider-Seite mit Aktiv-Schaltern |
| `66c714f` | **Design-Audit + De-Scale-Pass** — KI-Look-Signatur gemessen und entfernt |
| `357db8d` | **Marken-Theme „Bad Wolf in der Sternennacht"** — Wolf-Glyph, Ablage (`/api/tray`), Nachtblau |
| `0ef6aab` | **Bad-Wolf-Porträt nach Referenz** — Frauenfigur statt Wolf, Ablage-Prüfung (`/api/tray/check`) |
| `78203b5` | **Partikel-Hologramm** — Canvas-Porträt aus ~1.300 goldenen Partikeln |
| `25a1afc` | **Schlieren-Hologramm** — ~7.000 feine Partikel, seitlich entweichende Schlieren, starke Augen |
| `c5eac08` | **Bad Wolf wird wach** — Wachdienst (Bereitschaftsmeldung), Connect-Begrüßung, Traffic-Beobachter (alle 60 s, Anti-Spam) |
| *(auf main)* | **Stimme** — `/api/bw-log`, Stimmband in der Sidebar, Bad-Wolf-Karte auf der Übersicht |
| `b6e2c72` | **Porträt v2 + Parameter** — Brauen/Nase/Wangen-Skulptur, volleres Haar, Goldschleier; Austausch-Parameter-Menü im UI |

**Merge-Status:** `main` trägt den ganzen Sprint (b6e2c72, Fast-forward von 6b0a126).
**GitHub-Push steht noch aus** (Credentials in der Agenten-Shell nicht verfügbar) —
einmal manuell: `git push origin main sprint/polish`.

---

## 3. Architektur

Unverändert am Grundprinzip: **ein Python-File (server.py), ein UI-File (static/index.html),
keine Datenbank, alles im RAM, kein Build-Schritt, keine CDN-Abhängigkeit.**

```
Browser ──► Schaltwerk :8765 (bzw. Test :8766)
                │
                ├── GET/POST/DELETE ──► OmniRoute (Docker, Host-Port 24615 → Container 20128)
                │     /api/v1/management/proxies        (Registry: lesen, anlegen, löschen)
                │     /api/v1/management/proxies/health (Proxy-Statistiken)
                │     /api/v1/management/proxies/bulk-assign (Provider-Zuordnung)
                │     /api/providers                    (Provider-Connections)
                │     /api/settings/oneproxy            (NUR lesen — nie schreiben)
                │     /api/usage/proxy-logs             (Proxy-Telemetrie, read-only)
                ├── GET ──► öffentliche Proxy-Listen (10 Quellen)
                └── Prüf-Requests DURCH jeden Proxy → api.ipify.org / icanhazip.com
```

### 3.1 HTTP-API (vollständig)

| Endpunkt | Methode | Zweck |
| --- | --- | --- |
| `/` · `/api/meta` | GET | UI · Quellen, Tag, ob Key gesetzt |
| `/api/connect` | POST | OmniRoute-URL + Key im RAM verbinden; **validiert URL vor dem Speichern**; leerer Key löscht gespeicherten Key nicht |
| `/api/omni/inventory` | GET | Bestand in drei Töpfen (harvest / manual / oneproxy) |
| `/api/harvest` | POST | Freie Listen holen (Typ- **und** Quellen-Filter) |
| `/api/check` | POST | Proxies parallel prüfen — inkl. **Schadensprüfung** (siehe 4.2) |
| `/api/exchange` | POST (SSE) | Kompletter Austausch-Lauf; **409 bei Doppelstart** |
| `/api/job-status` | GET | Phase/Zähler/Fehler des letzten/laufenden Jobs |
| `/api/assign-providers` | POST | Beste `px-*`-Proxies den Providern zuordnen (Pool-Erkennung zur Laufzeit, Rück-Verifikation) |
| `/api/push-selected` | POST | **Manuell ausgewählte** Proxies schreiben (nur https_ok, kein Risiko) |
| `/api/omni/proxy-logs` | GET | Letzte Proxy-Requests aus OmniRoute (Live-Traffic-Tab) |
| `/api/omni/proxy-logs`-Rohformat | — | OmniRoute liefert teils nacktes Array — wird serverseitig zu `{logs:[…]}` vereinheitlicht |
| `/api/omni/providers` | GET | Provider-Connections (read-only) |
| `/api/omni/provider-status` | POST | Verbindungen aktivieren/deaktivieren (PATCH `isActive`) |
| `/api/schedule` | GET/POST | Geplanter Austausch (5–1440 min, Hintergrund-Task, nutzt die 409-Sperre) |
| `/api/hub-summary` | GET | Ein Request für die ganze Übersichtsseite (Provider/Pool/Health/Traffic/Job) |
| `/api/tray` | GET/POST/DELETE | **Bad Wolfs Ablage** (RAM, max. 200 Einträge); DELETE mit `?id=` einzeln, ohne alles |
| `/api/tray/check` | POST | Ablage-Proxy prüfen & bei Bestehen direkt übernehmen |
| `/api/bw-log` | GET | **Bad Wolfs Stimme** — Ringpuffer (60 Zeilen) ihrer letzten Taten |

### 3.2 Prüf-Logik (`probe_one`)

1. Deklarierten Typ prüfen; `https` fällt auf `http` zurück (Listen lügen oft), SOCKS4 wird verworfen.
2. Nur HTTPS-Bestehen zählt für den Upload; Klartext-HTTP wird als Diagnose gemeldet.
3. **TLS-Intercept-Check:** derselbe Request mit `verify=True` — scheitert die Zertifikatsprüfung,
   fängt der Proxy TLS ab (= könnte Provider-API-Keys im Klartext lesen) → `risk: "tls-intercept"`.
4. **Exit-IP-Konsistenz:** zweiter Echo-Dienst muss dieselbe IP melden → sonst `risk: "ip-mismatch"`.
5. **Riskante Proxies werden konsequent NIE geschrieben** — weder im Austausch noch manuell;
   in der Kandidaten-Liste mit Warn-Pill markiert, sortiert nach (lebendig, sauber, schnell).

### 3.3 Sicherheits-Fixes dieses Sprints

- **XSS behoben:** `exit_ip`, `error`, `country` aus unverifizierten Proxy-Antworten wurden
  ungefiltert per `innerHTML` ins DOM geschrieben (localhost-Kontext, hätte den eingegebenen
  API-Key lesen können). Jetzt HTML-Escaping (`esc()`) an **allen** dynamischen Feldern.
- **Doppelstart-Sperre:** `POST /api/exchange` antwortet 409, wenn ein Lauf aktiv ist —
  synchron im Handler geprüft/gesetzt (keine Race zwischen zwei schnellen Requests).
- **`/api/connect`:** URL-Validierung **vor** dem Speichern; leerer Key überschreibt den
  gespeicherten Key nicht mehr (Auto-Connect beim Seitenladen ist dadurch harmlos).
- **Key-Handling unverändert:** Key lebt nur im RAM des Server-Prozesses, nie auf Disk.

---

## 4. UI (static/index.html, eine Datei, kein Build)

### 4.1 Struktur

- **Sidebar links** (Hub-tauglich): Abschnitt **Hub** (Übersicht · Provider · Einstellungen „bald"),
  Abschnitt **Schaltwerk** (Austausch · Traffic · Zeitplan), darunter das **Bad-Wolf-Porträt**
  (Ablage-Ziel, Klick öffnet das Feld), **Stimmband**, `BAD WOLF`-Stencil, Fußnote.
- **Kopfbereich:** Seitentitel + OmniRoute-Verbindung (URL, Key, Status-Punkt).
- **Tabs:** Übersicht (Startseite) · Austausch · Traffic · Zeitplan · Provider.
- **Ablage-Panel:** schiebt von rechts, nimmt Proxies (Drag & Drop), Text, Links und
  Datei-Inhalte auf; Einzeln-Löschen, Leeren; Proxy-Einträge mit „Prüfen & übernehmen".

### 4.2 Funktionen im Detail

- **Übersicht:** Live-KPI-Statuszeile (OmniRoute, Provider aktiv, Pool, Requests, Fehler, Job),
  Live-Aktivität, System-Karte, **Bad-Wolf-Karte** (ihre letzten 8 Taten), Schnellsprünge. Poll 5 s.
- **Austausch:** Statuszeile, Typ-Checkboxen, **Quellen-Menü** (je Quelle an/aus), Aktionen
  (Bestand · Listen holen · Kandidaten prüfen · Austausch · **Parameter-Menü**
  (Timeout/Parallelität/Limits) · Ausgewählte übernehmen · Provider zuordnen), zwei Tabellen — **Kandidaten-Zeilen sind Drag-fähig** (in den Bestand ziehen =
  übernehmen; auf Bad Wolf ziehen = ablegen), Checkboxen für Mehrfachauswahl, Risiko-Pills,
  Log-Panel. Job-Status wird beim Laden geholt und alle 5 s gepollt (Reload-verlustfrei,
  409-fest, deckt Scheduler-Läufe ab).
- **Traffic:** Proxy-Telemetrie aus OmniRoute, **Filter** (Freitext) + „nur echter Proxy-Traffic",
  Poll 5 s, Tag in der Sidebar zeigt live/leer.
- **Zeitplan:** Aktiv-Schalter + Intervall, Status mit nächstem/letztem Lauf und Fehler.
- **Provider:** Liste aller Connections, **Aktiv-Schalter** je Connection (mit Bestätigung),
  live gegen OmniRoute verifiziert (an→aus→an).
- Auto-Connect beim Laden; alle `fetch`-Aufrufe über einen Wrapper mit Fehlerbehandlung;
  Buttons deaktivieren sich während ihrer Aktion; `busy()` merkt sich Labels doppelt-sicher.

### 4.3 Design-System (nach Audit)

Das Ausgangs-Design hatte messbare KI-Look-Signatur: 89 Pills, 22 Kästchen-Elemente,
Blaustich in allen Grundfarben, vier Radius-Stufen. Daraus entstanden:

- **Tokens:** Nachtblau-Graphit (`--bg #0d0e12`, Panel `#13141a`, Linie `#262833`),
  Ink `#d6d7dd`, Muted `#8a8c99`, **`--eye #d9a441`** (Bernstein — ausschließlich Augen,
  Tränen, Sterne, Badge), Statusfarben gedämpft und nur semantisch (grün/rot/gelb).
- **Radius einheitlich 3 px**, keine Gradient-Karten, KPI-Kärtchen durch eine dichte
  Mono-**Statuszeile** ersetzt, Pills nur noch für echte Stati.
- Typografie: Inter/system-ui für Text, JetBrains Mono für Daten; Labels 9–10 px Uppercase.

### 4.4 Bad Wolf (Marken-Figur, Hub-KI)

- **Referenzen des PO:** Rose Tyler als Bad Wolf / die Moment (blonde Frau, glühende Augen,
  weinend) + Van-Gogh-Sternennacht + **Partikel-Hologramme + goldene Energie** („sie ist
  kurzzeitig reine gelbe Energie/Zeit"). Schematisch wegen BBC-Copyright, aber erkennbar.
- **Umsetzung:** Canvas-**Partikel-Hologramm** (~7.000 Partikel): eine gezeichnete
  Gesichts-Maske (Haarpartien, Gesicht, Lippen, Tränenströme, Augen-Blobs) wird per
  Pixel-Sampling in Partikel zerlegt — Helligkeit der Maske steuert Dichte, Größe und
  Farbe. Gesicht = dichtes flimmerndes Staubfeld; **Haar-/Randpartikel entweichen als
  feine goldene Schlieren seitlich** (Motion-Streaks) und formieren sich neu; **Augen**
  sind eine eigene Ebene: pulsierende Glow-Sterne, der hellste Punkt im UI; **Tränen**
  laufen übers Gesicht und werden zu funkelnden Sternen, die in die Nacht fallen
  (Starry-Night-Verankerung).
- **Performance:** ~71 fps bei 7k Partikeln (gemessen); Standbild-Fallback bei
  `prefers-reduced-motion`, pausiert bei `document.hidden`.
- **Ablage (Agenten-Instinkt):** alles auf sie gezogene wird gesammelt; Proxy-Einträge kann
  sie selbst prüfen und übernehmen; ihre Taten erzählt sie in der **Stimme** (siehe 4.5).
- **Porträt v2:** Brauen und Nase als Partikel-Strukturen, Wangen über
  Dichte-Skulptur (weniger Partikel = Schattenwurf), volleres Haar (breitere Masse,
  mehr Ströme), weicher Goldschleier als Glow-Grundierung.
- **Bekannte offene Design-Punkte:** Grundrichtung abgesegnet („geht in die richtige
  Richtung"), aber laut PO noch nicht ideal — Feinschliff Mensch-Erkennbarkeit/Haar/Glow
  auf später verschoben.

### 4.5 Die Stimme

- Server-seitiger Ringpuffer (`bw_log`, 60 Zeilen, RAM-only), gefüllt bei: Ablage
  („Neu in meiner Ablage: 3"), Ablage-Prüfung („… lebt (812 ms) — übernommen." /
  „Vorsicht … tls-intercept. Verworfen." / „… ist tot. Fallen gelassen."),
  Austausch-Abschluss („Austausch fertig: N tote entfernt, M neue geboren …") und
  Austausch-Abbruch, Zeitplan („Ich tausche jetzt alle 60 Minuten." / „… ruht.").
- UI: **Stimmband** unter dem Porträt (letzte Tat, Puls-Dot) + **Bad-Wolf-Karte** auf der
  Übersicht (letzte 8 Taten mit Zeit). Poll alle 8 s, sofortige Aktualisierung nach
  eigenen Aktionen.
- **Wachdienst** (`_bw_watcher_loop`, asyncio-Task im Lifespan):
  - Beim Start: Bereitschaftsmeldung mit Pool-/Register-Stand bzw. „aber blind" ohne Key.
  - Nach dem ersten erfolgreichen Connect: „Verbunden. Ich sehe alles."
  - Alle 60 s: liest die Proxy-Telemetrie; **fehlgeschlagene Proxy-Requests** werden sofort
    gemeldet, laufender Traffic max. einmal pro 10 Minuten (Anti-Spam).

---

## 5. Tests

`tests/test_server.py` — **34 Tests, alle grün**, laufen ohne Netz und ohne OmniRoute:

- Parser (Zeilenformate, SOCKS4-Verwerfen, IPv6-Verwerfen, Portbereiche, Müll)
- Dedupe/Merge-Logik, `proxy_key`, `unwrap_list`, `is_harvest`, `latency aus notes`,
  `schemes_to_try`, `clean_types`
- Connect-Validierung (kaputte URL überschreibt Zustand nicht; leerer Key löscht Key nicht)
- Schedule-Validierung (Intervallgrenzen, next_run)
- Push-selected-Grenzen (leer, >100, ungeprüfte übersprungen, **riskante übersprungen**)
- 409-Doppelstart-Sperre, job-status, hub-summary ohne Key
- Tray: add/list/remove, leere Items, Kürzung auf 4.000 Zeichen, check 404/400
- **Stimme:** Ablage und Prüfung erzeugen Log-Zeilen

Ausführen: `pip install -r requirements-dev.txt && pytest tests/`

---

## 6. Betrieb (dieser Rechner)

- **OmniRoute:** Docker-Container `omniroute`, Host-Port **24615** → Container 20128.
  Dashboard-Login: Passwort wurde beim Onboarding gesetzt (nicht `CHANGEME`).
  Zwei weitere OmniRoute-Container laufen ohne Port-Mapping (`modest_gould`, `jovial_dirac`) —
  vermutlich Überbleibsel, nicht angerührt.
- **Schaltwerk-Server:** produktiv über `STARTEN.bat` (Port 8765) oder manuell
  `python server.py` (Standard 8765, `PORT=`/`HOST=` überschreibbar; der Sprint hat auf
  Port 8766 getestet, weil die alte Instanz auf 8765 lief).
- **Management-API-Key:** Name „schaltwerk", manage-Scope, Prefix `sk-500f3…`;
  liegt in `BWO\backups\omniroute-20260908\.schaltwerk_api_key` (außerhalb des Repos).
  Nach jedem Server-Neustart einmal in der UI eintragen (URL `http://127.0.0.1:24615`).
- **Backup vor allen Tests:** komplettes Container-Datenverzeichnis (`/app/data`:
  storage.sqlite + WAL + server.env mit JWT_SECRET/STORAGE_ENCRYPTION_KEY/API_KEY_SECRET)
  via `docker cp` nach `BWO\backups\omniroute-20260908\`, **plus** API-Snapshots
  (providers, keys, proxy-settings) und gefälschter Session-JWT + API-Key — alles
  außerhalb jedes Git-Repos. Provider-Verbindungen (7 Stück: openrouter, uncloseai,
  opencode, duckduckgo-web, cloudflare-playground, chipotle, aihorde) wurden nie
  verändert (ein An/Aus-Test wurde sofort zurückgenommen).

---

## 7. Bekannte Lücken / nächste Schritte

1. **Porträt-Feinschliff** (PO hat bewusst aufgeschoben): noch zu schemenhaft,
   Mensch-Erkennbarkeit, Haarmenge, Glow-Feinheit. Grundrichtung abgesegnet.
2. **Stimme ausbauen:** Variantenreichtum der Sätze, Bad Wolf kommentiert auch den
   Live-Traffic („Da läuft gerade etwas über 140.99…").
3. **Traffic-Tab:** Zähler je Proxy, Zeitfenster-Filter.
4. **Austausch-Parameter im UI** (max_push, timeout, concurrency) sind hartcodiert.
5. **Export** (CSV / OmniRoute-Backup-JSON) — altbekannte Lücke, weiterhin offen.
6. **IPv6-Proxies** werden weiterhin verworfen (Parser).
7. **GitHub-Push steht aus** (`git push origin main sprint/polish` — Credentials waren in
   der Agenten-Shell nicht verfügbar; lokal ist alles auf `main` gesichert).
8. Die alte Instanz auf Port 8765 läuft noch auf altem Code und zeigt auf den toten
   Port 20128 — beim nächsten Start aus dem Projektordner erledigt sich das.

---

## 8. Goldene Regeln (unverändert, hier gesichert)

- Nie in die 1proxy-/Free-Kategorie schreiben; eigene Benutzer-Proxies unangetastet lassen.
- `HARVEST_TAG = "proxy-exchange"` / `px-`-Präfix nicht umbenennen (sonst verliert der
  nächste Lauf den eigenen Pool aus den Augen).
- Proxy-`type` nie pauschal auf http zwingen — der geprüfte Dialekt wird geschrieben.
- `STARTEN.bat` mit CRLF lassen; UI ohne CDN (Offline-fähig).
- API-Key nie auf Disk; alles im RAM ist Absicht.
