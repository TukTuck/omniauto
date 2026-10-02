# Omnia Atelier — Produkt-, UX- und Architekturkonzept

**Stand:** 2026-10-02 · **Repository:** `TukTuck/omniauto` · **Basis-Commit:** `60dd9040afe117e729fc5ac6dc59f434a9833730` ("Add files via upload")
**Zweig dieser Arbeit:** `arena/01a0fe6e-omniauto`

---

## 0. Methodik und Kennzeichnung

Dieses Dokument unterscheidet konsequent vier Ebenen der Gewissheit. Jede Aussage trägt eine Markierung, wo sie nicht offensichtlich ist.

| Marke | Bedeutung |
| --- | --- |
| **BEKANNT** | Geht aus der Aufgabenstellung oder aus im Repository tatsächlich gelesenem Inhalt sicher hervor. |
| **ZU PRÜFEN** | Muss durch Untersuchung von Code, Konfiguration, laufender Instanz oder Dokumentation erst verifiziert werden. Hier stehen **keine** Behauptungen. |
| **ANNAHME** | Plausible, aber unbestätigte Voraussetzung. Wird nie als Grundlage einer irreversiblen Entscheidung benutzt. |
| **VORSCHLAG** | Neue Produkt-, UX- oder Architekturentscheidung. Bewusst gesetzt, nicht abgeleitet. |

Zusätzlich gilt: **PSEUDOCODE – NICHT VERIFIZIERTE SYNTAX** über jedem Codeblock, dessen Syntax nicht aus dem Repository oder einer verifizierten Quelle stammt.

### 0.1 Was dieses Dokument zuerst tut

Die Aufgabenstellung enthält Prämissen über das Repository. Diese Prämissen wurden zuerst geprüft, nicht zuerst bedient. Das Ergebnis steht in Abschnitt 1.6: **drei Prämissen sind falsch**, eine ist unbelegt. Das verändert das Produktmodell nicht, aber es verändert die Reihenfolge der Arbeit und die Ehrlichkeit der Architektur.

---

# TEIL I — BEFUND: WAS DAS REPOSITORY WIRKLICH IST

## 1.1 Inventar (BEKANNT — gelesen und gemessen)

Das Repository hat genau **einen** Commit und **12** versionierte Dateien (38 MB Arbeitsgröße). Es ist **kein** Monorepo mit bestehender Anwendung. Es ist eine **Materialablage** mit drei sehr unterschiedlichen Inhalten.

```
omniauto/
├── .git/
├── Kurz-main (1).zip        1.145.614 Bytes   → 79 Dateien, entpackt 2,1 MB
├── LibreChat-main.zip      18.934.608 Bytes   → 6.303 Dateien, entpackt 66,8 MB
└── schaltwerk/                  194.146 Bytes → 10 Dateien
    ├── CHANGELOG.md              9.975
    ├── DOKUMENTATION.md         16.066
    ├── README.md                 2.269
    ├── STARTEN.bat              1.214
    ├── WEITERARBEITEN.txt       22.163
    ├── requirements-dev.txt         24
    ├── requirements.txt             64
    ├── server.py               57.318
    ├── static/index.html       74.270
    └── tests/test_server.py    10.783
```

Es gibt: **keine** `package.json` im Wurzelverzeichnis, **keine** CI/CD-Datei (`.github/` existiert nur im LibreChat-ZIP, nicht im Repo), **keine** `docker-compose.yml`, **keinen** `.env`-Beispielstand, **keine** Datenbank, **keine** Migrationen, **kein** Build-Schritt außerhalb der ZIPs.

**Konsequenz (BEKANNT):** Omnia Atelier ist ein **Greenfield-Produkt mit drei Materialquellen**, kein Umbau einer bestehenden App. Das ist eine gute Nachricht für die Eigenständigkeit und eine schlechte Nachricht für jede Annahme über "bestehende Funktionalität, die geschützt werden muss" — es gibt fast keine. Der Preservation Contract (Abschnitt 4) muss deshalb schmal und ehrlich sein.

## 1.2 `schaltwerk/` — die einzige lauffähige Anwendung im Repository (BEKANNT)

`schaltwerk` ist **kein Node-Editor, kein Graph-System, keine AI-Anwendung.**

Es ist ein lokales, single-purpose Werkzeug für **Proxy-Logistik**: Es holt freie Proxy-Listen aus 10 öffentlichen Quellen, prüft sie selbst gegen echte HTTPS-Ziele, entfernt tote eigene Einträge aus OmniRoute und schreibt lebendige als **manuelle** Registry-Proxies zurück — ausdrücklich nie in die kostenpflichtige 1proxy-/Free-Kategorie.

Fakten (alle aus `README.md`, `DOKUMENTATION.md`, `WEITERARBEITEN.txt`, `CHANGELOG.md`, `server.py`, `static/index.html`, `tests/test_server.py` gelesen):

| Aspekt | Befund |
| --- | --- |
| Stack | Python 3.11+, **FastAPI**, **uvicorn**, `httpx[socks]`; UI: **eine einzige HTML-Datei** (HTML+CSS+JS inline) |
| Start | `STARTEN.bat` (Windows 10, `chcp 65001`, findet `py`/`python`, `pip install -r requirements.txt`, startet Server, öffnet Browser) |
| Port | Standard `8765`, überschreibbar per `HOST=`/`PORT=`; **bindet ausdrücklich nur `127.0.0.1`** |
| Zustand | **komplett im RAM**, keine Datenbank, keine Datei-Persistenz, kein Login |
| API-Key | lebt **nur im RAM des Server-Prozesses**, wird nie auf Disk geschrieben (explizite Regel) |
| Struktur | `server.py` (ein File, ~1.500 Zeilen, 21 Routen) + `static/index.html` (ein File, 74 KB) |
| Tests | `tests/test_server.py`, laut `DOKUMENTATION.md` **34 Tests, alle grün**, laufen ohne Netz und ohne OmniRoute |
| Streaming | Server-Sent Events über FastAPI `StreamingResponse` (`POST /api/exchange`) |
| Nebenläufigkeit | `asyncio`-Tasks im Lifespan (`_scheduler_loop`, `_bw_watcher_loop`), 409-Doppelstart-Sperre |
| Plattform-Ziel | Windows 10 zuerst; läuft auch unter Linux |
| Sonstiges | kein Build, keine CDN-Abhängigkeit, Offline-fähig |

### 1.2.1 Das für Omnia Atelier wichtigste Detail: "Bad Wolf" (BEKANNT)

`schaltwerk` enthält **bereits eine native Leitfiguren-Instanz**. Das ist der wertvollste Fund dieses Repositories für die Aufgabe — kein erfundenes Konzept, sondern vorhandener, dokumentierter Repository-Content:

- **Eine Persona mit Handlungsregeln.** `DOKUMENTATION.md`, Abschnitt 8, definiert "Goldene Regeln" (z. B. nie in die 1proxy-Kategorie schreiben, eigene Benutzer-Proxies unangetastet lassen, `HARVEST_TAG = "proxy-exchange"` nicht umbenennen, Proxy-`type` nie pauschal erzwingen).
- **Eine Stimme, die Taten protokolliert.** Serverseitiger **Ringpuffer** `bw_log` (60 Zeilen, RAM-only); Einträge entstehen bei Ablage, Prüfung, Austausch-Abschluss, Abbruch, Zeitplanänderung. UI: "Stimmband" unter dem Porträt + Karte mit den letzten 8 Taten.
- **Ein Wachdienst.** `_bw_watcher_loop` (asyncio-Task im Lifespan): Bereitschaftsmeldung beim Start, Begrüßung nach dem ersten erfolgreichen Connect, danach alle 60 s Telemetrie-Lesen mit **Anti-Spam-Regel** (Fehler sofort, laufender Traffic maximal eine Meldung pro 10 Minuten).
- **Eine Ablage mit Agency.** `POST /api/tray` nimmt Proxies, Text, Links, Dateiinhalte auf (max. 200 Einträge, Kürzung auf 4.000 Zeichen); `POST /api/tray/check` prüft einen abgelegten Proxy **selbst** und übernimmt ihn nur bei Bestehen — bei Risiko (`tls-intercept`, `ip-mismatch`) oder Tod wird er **verworfen und das gemeldet**.
- **Ein Risiko-Modell, das Schreibzugriffe blockiert.** `probe_one` erkennt TLS-Interception und Exit-IP-Inkonsistenz; riskante Proxies werden **konsequent nie geschrieben**, weder automatisch noch manuell.

**Bewertung (VORSCHLAG, aber repo-begründet):** Die Leitassistenz von Omnia Atelier ist die produkthafte, erwachsen gewordene Weiterentwicklung genau dieses Musters — nicht eine Neuerfindung und nicht ein importierter Chatbot. Die vier übernehmbaren Prinzipien heißen:
1. **Stimme = protokollierte Tat, nicht generierte Plauderei.**
2. **Ablage = der Nutzer gibt Material, die Instanz handelt nur innerhalb geprüfter Grenzen.**
3. **Wachdienst = proaktiv, aber mit Anti-Spam- und Relevanzschwelle.**
4. **Goldene Regeln = handlungsbegrenzend, nicht kosmetisch.**

### 1.2.2 Vorhandenes Design-System (BEKANNT)

`DOKUMENTATION.md`, Abschnitt 4.3, dokumentiert einen expliziten **De-Scale-Pass** gegen "KI-Look-Signatur" (Ausgangslage gemessen: 89 Pills, 22 Kästchen, Blaustich, vier Radius-Stufen). Ergebnis — diese Tokens sind wörtlich in `static/index.html` (Zeilen 11–21) vorhanden:

```css
:root {
  --bg: #0d0e12;      /* Nachtblau-Graphit */
  --panel: #13141a;
  --panel-2: #191a21;
  --line: #262833;
  --line-2: #33353f;
  --ink: #d6d7dd;
  --muted: #8a8c99;
  --eye: #d9a441;     /* Bernstein — ausschließlich für Augen/Tränen/Sterne/Badge */
  --eye-dim: #8a6a34;
}
```

Regeln: **Radius einheitlich 3 px**, keine Gradient-Karten, KPI-Kärtchen ersetzt durch eine dichte **Mono-Statuszeile**, Pills **nur für echte Stati**, Typografie Inter/system-ui für Text und JetBrains Mono für Daten, Labels 9–10 px uppercase.

**Das ist eine bereits erprobte, dokumentierte Anti-Dashboard-Sprache im eigenen Haus.** Sie ist der gegebene Ausgangspunkt für Omnia Atelier — kein erfundenes Theme.

**Offener Konflikt (ZU PRÜFEN / Entscheidung nötig):** Dieselbe Codebasis enthält ein **Canvas-Partikel-Hologramm** (~7.000 Partikel, ~71 fps gemessen, Standbild-Fallback bei `prefers-reduced-motion`, Pause bei `document.hidden`). Die Aufgabenstellung verbietet "Partikel ohne Funktion". In `schaltwerk` haben die Partikel eine **Funktion** (Persona-Präsenz, Markenfigur). Für Omnia Atelier gilt die in Abschnitt 7.7 festgelegte Regel: **Bewegung trägt Zustand, nichts sonst.** Das Partikel-Porträt wird nicht übernommen; die *Disziplin* dahinter (gemessene Performance, Reduced-Motion-Fallback, Hintergrund-Pause) schon.

## 1.3 `LibreChat-main.zip` (BEKANNT)

| Aspekt | Befund |
| --- | --- |
| Version | **v0.8.8** (root `package.json`) |
| Umfang | **6.303 Dateien**, 66,8 MB entpackt |
| Lizenz | **MIT** (`LICENSE`, "Copyright (c) 2026 LibreChat"); Workspace-Pakete teils `ISC` (`@librechat/api` 1.7.52, `librechat-data-provider` 0.8.527), `@librechat/data-schemas` 0.0.74 `MIT`, `@librechat/client` 0.4.82 ohne Lizenzfeld |
| Struktur | Monorepo (turbo): `api/` (legacy Express), `packages/api` (**TypeScript, neues Backend**), `packages/data-schemas` (Mongo-Methoden), `packages/data-provider` (Shared-Typen/Services), `client/` (React-App), `packages/client` (Shared-Primitives) |
| Infrastruktur | MongoDB (`mongo:8.0.20`), Meilisearch (`v1.35.1`), pgvector (`0.8.0-pg15`), `rag_api`, optional Clickhouse-Admin-Panel |
| Frontend | React 18.2, `@tanstack/react-query` 4.28, **recoil + jotai**, `framer-motion` 12.40, `@radix-ui/react-dialog`, `@ariakit/react`, `react-router-dom` 7.18, `react-hook-form`, `lucide-react`, i18next — **102 Abhängigkeiten im `client`-Paket** |

Für diese Aufgabe relevante, **verifiziert vorhandene** Teilbereiche (Verzeichnisse und Schemas gelesen):

- **Memory**: `packages/data-schemas/src/schema/memory.ts` (Key/Value je User, `key` validiert durch `^[a-z_]+$`, `value`, optionale `agentId`-Partition "shared personal pool", `tokenCount`, `updated_at`, `tenantId`) + `api/server/routes/memories.js` (`GET /`, `POST /`, `PATCH /preferences` mit `checkMemoryOptOut`, `DELETE /`, `PATCH /:key`, `DELETE /:key`) + `packages/api/src/memory/` (`authorization.ts`, `config.ts`, `handlers.ts`, `protection.ts`).
- **Konversation/Versionierung**: `message.ts` führt `messageId`, `conversationId`, `model`, `endpoint`, **`parentMessageId`**, `tokenCount`, `sender`, `text`, `summary` — also ein **Nachrichtenbaum**, keine flache Liste.
- **Authentifizierung**: `api/strategies/` mit `localStrategy`, `jwtStrategy`, `google`, `github`, `discord`, `facebook`, `apple`, `openidStrategy`/`openIdJwtStrategy`, `samlStrategy`, `ldapStrategy` — plus `packages/api/src/auth/` (`oidc.ts`, `saml.ts`, `password.ts`, `refresh.ts`, `reuse.ts`, `domain.ts`, `ip.ts`, `invite.ts`, `openidRoleSync.ts`).
- **Run-/Stream-Steuerung**: `packages/api/src/stream/` mit `GenerationJobManager.ts`, `ApprovalLifecycle.ts`, `SteeringLifecycle.ts`, `SteerRecovery.ts`, `checkpoints.ts`, `persistence.ts`, `terminalProjection.ts`, `abortContent.ts`.
- **Agenten/Tools**: `packages/api/src/agents/`, `packages/api/src/mcp/`, `packages/api/src/tools/`, `packages/api/src/skills/`, `packages/api/src/schedules/`, `packages/api/src/code/`, Schemas u. a. `agent.ts`, `mcpServer.ts`, `toolCall.ts`, `auditLog.ts`, `queuedTurn.ts`, `schedule.ts`, `subagent.spec.ts`, `chatProject.ts`.
- **Dateien/Kontext**: `packages/api/src/files/` (`context.ts`, `extract.ts`, `documents/`, `code/`, `citations.ts`, `mime.spec.ts`, …).
- **OpenAI-kompatible Endpunkte**: `librechat.example.yaml` → `endpoints.custom` mit `name`, `apiKey`, `baseURL`, `models.default` / `models.fetch`, `titleConvo`, `titleModel`, `modelDisplayLabel`, `provider: 'anthropic'`, `headers`, `activityLabel`, `activityModel`. **Genau diese Struktur ist der natürliche Anschlusspunkt für OmniRoute** — sofern OmniRoute OpenAI-kompatible Endpunkte anbietet (siehe 1.5).

**Warnung aus `AGENTS.md`/`CONTEXT.md` (BEKANNT, gelesen):** LibreChats Domänenbegriffe (Agent run envelope, execution enrollment, event actor fork, capability shield, …) beschreiben ein **sehr weit entwickeltes, auf Mehrbenutzer-, Mehrprozess- und Redis-/Mongo-Koordination ausgelegtes System**. Wer dieses Vokabular importiert, importiert die Komplexität. Für ein lokales Single-User-Produkt ist das der falsche Import.

## 1.4 `Kurz-main (1).zip` — das ist "Mesh AI" (BEKANNT, und eine Prämissen-Korrektur)

Die Aufgabenstellung spricht von **"Mesh AI"**. Im Repository liegt **MashAI** (`github.com/Avaxerrr/MashAI`). Nach Namensähnlichkeit, Kontext (AI-Workspace) und dem Umstand, dass keine andere KI-Referenz im Repository existiert, ist **ANNAHME: mit "Mesh AI" ist MashAI gemeint**. Diese Zuordnung ist **ZU PRÜFEN** (Rückfrage beim Product Owner), weil sie die falsche oder eine zufällige Schreibweise sein könnte.

Fakten aus dem ZIP (alle gelesen):

| Aspekt | Befund |
| --- | --- |
| Name/Version | `mash-ai` / MashAI **v1.0.0-beta** |
| Claim | "Your Unified AI Workspace — Stop losing work in browser tabs." |
| Lizenz | **MPL-2.0** |
| Stack | Electron **39.2**, React **18.3**, TypeScript **5.9**, Vite **6**, Tailwind **3.4**, Ghostery Adblocker, Vitest |
| Plattform | **Windows 10/11 supported**, macOS/Linux "Coming Soon" |
| Teststand | `docs/REVIEW.md`: **66 Tests**, `npm run lint` 0 Fehler, Produktionsbuild grün; Branch `arena/01a0e39c-kurz`, Commit `9e6d88e` — also **Ergebnis einer früheren Arbeit an diesem Repository-Ökosystem** |

**Was MashAI wirklich ist — und was nicht:** Es ist **kein intelligentes System mit Gedächtnis**. Es ist ein **Electron-Browser für die Web-Oberflächen von ChatGPT, Claude, Gemini, Perplexity, Grok, DeepSeek** plus Organisationsschichten:

- **Profile** (Work/Personal/Research), je eigenes Session/Cookie/LocalStorage — "Complete data isolation between profiles".
- **Tab-Management** inkl. Drag&Drop, Reopen, Kind-Tab-Historie, Favicon-Cache.
- **Smart Tab Suspension** (Auto-Suspend nach 1–120 min, media-aware, "Never suspend this tab", Tray-Optimierung).
- **Side Panel**: beliebigen Tab links oder rechts anpinnen, **zwei Assistenten gleichzeitig sehen**, Ziehteiler, Seiten tauschen — persistiert über Sessions.
- **Quick Search (Ctrl+K)** und **Open Tab Search (Ctrl+Shift+K)** mit dokumentiertem Ranking: exakt > Präfix > Wortanfang > Teilstring, 27 Tests.
- **Session Persistence**: Tabs, Fensterposition/-größe, Profilzustand über Neustarts.
- **SettingsManager** mit Defaults, Merge und **Migrationen** (10 Tests), Shortcut-Validierung, Adblock-Whitelist.
- **Roadmap (explizit offen):** Bring Your Own Keys, Local AI (Ollama/LM Studio), **"Unified Chat Interface — single interface for all AI providers via API"**.

**Produktbedeutung für Omnia Atelier (VORSCHLAG):** MashAI ist nicht die Vorlage für die *Intelligenz*, sondern der **Beweis für das Bedürfnis**: Menschen verlieren Arbeit zwischen KI-Oberflächen. MashAI löst das durch *Ordnung* (Tabs, Profile). Omnia Atelier löst es durch *Kontinuität des Arbeitsstücks*. Die drei übernehmbaren Ideen sind:
1. **Profile → Arbeitsräume**: Kontexttrennung als erstklassiges Objekt (nicht als Chat-Ordner).
2. **Side Panel → Gegenüberstellung**: zwei Modellpositionen gleichzeitig sichtbar machen, statt nacheinander wegzuklicken.
3. **Session Persistence + Settings-Migrationen**: der Arbeitsraum wird nie "neu geladen", er wird **wieder betreten**.

Nicht übernommen wird: die Tab-/Browser-Metapher selbst (sie hält das Material in fremden Oberflächen gefangen), Electron als Laufzeit für v1 (ZU PRÜFEN, siehe 11.4), Adblocking, Ghostery-Abhängigkeit.

## 1.5 OmniRoute — verifiziert vs. nicht verifiziert (TEILS BEKANNT, TEILS ZU PRÜFEN)

`schaltwerk` ruft OmniRoute **tatsächlich** auf. Folgende Angaben sind **BEKANNT** (aus `server.py` und `DOKUMENTATION.md` gelesen, keine Erfindung):

**Verbindung**
- Basis-URL: konfigurierbar, Standard `http://127.0.0.1:20128`; in der dokumentierten Installation Docker-Container `omniroute`, **Host-Port 24615 → Container 20128**.
- Authentifizierung: **beide** Header werden gesetzt — `Authorization: Bearer <key>` **und** `x-api-key: <key>` (`server.py`, `omni_headers()`).
- Key-Anforderung: Management-API-Key mit **`manage`-Scope** (im dokumentierten Fall Name `schaltwerk`, Präfix `sk-500f3…`, Ablage **außerhalb** des Repos).
- OmniRoute-Konfiguration liegt in `/app/data` (`storage.sqlite` + WAL + `server.env` mit `JWT_SECRET`, `STORAGE_ENCRYPTION_KEY`, `API_KEY_SECRET`).

**Verifizierte Endpunkte (so im Code verwendet)**

| Methode | Pfad | Zweck |
| --- | --- | --- |
| GET | `/api/v1/management/proxies?limit=&offset=` | Registry-Proxies lesen |
| POST | `/api/v1/management/proxies` | Proxy anlegen (legt `source=manual` an) |
| DELETE | `/api/v1/management/proxies?id=&force=1` | Proxy löschen |
| GET | `/api/v1/management/proxies/health` | Proxy-Statistiken |
| PUT / POST | `/api/v1/management/proxies/bulk-assign` | Provider-Zuordnung |
| GET | `/api/v1/management/proxies/assignments?scope=&scope_id=&limit=` | Zuordnungen lesen |
| GET | `/api/providers?limit=200` | Provider-Connections lesen |
| PATCH | `/api/providers` (`{ids, isActive}`) | Verbindungen aktivieren/deaktivieren |
| GET | `/api/settings/oneproxy?action=stats` und `?limit=&offset=` | Marktplatz-Kategorie — **nur lesend** |
| GET | `/api/usage/proxy-logs?limit=50` | Proxy-Telemetrie |

**Dokumentierte Provider-Connections** (7): `openrouter`, `uncloseai`, `opencode`, `duckduckgo-web`, `cloudflare-playground`, `chipotle`, `aihorde`.

**Format-Besonderheit (BEKANNT):** OmniRoute liefert bei `/api/usage/proxy-logs` **teils ein nacktes Array** statt eines Objekts; `server.py` vereinheitlicht das serverseitig zu `{logs: [...]}`. **Das ist ein Hinweis auf eine inkonsistente API-Oberfläche** — der Adapter muss defensiv normalisieren.

**ZU PRÜFEN — hier wird nichts behauptet:**
1. Ob OmniRoute überhaupt eine **Modell-Inferenz-API** anbietet (`/v1/chat/completions` oder kompatibel). **Im Repository gibt es dafür keinen Beleg.** Eine Suche über `schaltwerk` nach `chat/completions`, `/v1/models`, `embeddings` ergab **keinen Treffer**.
2. Falls ja: genaue Pfade, Authentifizierung, Streaming-Format (SSE?), Modell-ID-Format, ob `stream: true` unterstützt wird.
3. Ob OmniRoute **eigene Routing-/Fallback-Logik** hat (Regeln, Gewichte, Kosten-/Latenz-Steuerung) oder nur **Provider-Passthrough** macht.
4. Ob **Multimodalität**, Dateien, Audio, Video, Embeddings, **MCP** oder **A2A** real unterstützt und konfiguriert sind.
5. Wie Kosten-/Usage-Telemetrie pro Request abrufbar ist (über `/api/usage/proxy-logs` hinaus?).
6. Welche Version konkret läuft (Image-Tag, Build-Datum).
7. Ob es Ratenbegrenzungen, Quoten oder parallele Request-Limits gibt.

> **Dieser Abschnitt ist der wichtigste des ganzen Dokuments.** Die Aufgabenstellung setzt OmniRoute als "zentrale Infrastruktur für Modelle, Provider und Routing" voraus. **Verifiziert ist derzeit nur die Infrastruktur-Verwaltungsebene** (Proxies, Provider, Usage-Logs). Die Modellebene ist eine begründete Erwartung (die Provider-Namen `openrouter`, `opencode` und die Aussage in `WEITERARBEITEN.txt` "OmniRoute schickt fast alles zu HTTPS-APIs (OpenAI, Anthropic…)" stützen sie), aber **kein verifizierter Befund**. Phase 4 beginnt deshalb zwingend mit einem Capability-Probe (Abschnitt 12.4), nicht mit Implementierung.

## 1.6 Prämissen-Korrektur (BEKANNT — Konsequenz aus 1.1–1.5)

| Prämisse der Aufgabenstellung | Befund | Konsequenz |
| --- | --- | --- |
| "Das bisherige Schaltwerk-/Node-/Graph-Prinzip", "bisherige Schaltwerk-Logik", "Node-/Graph-Daten" | **`schaltwerk` enthält keinen Node-Editor, keinen Graphen, keine visuellen Verbindungen.** Es ist Proxy-Logistik mit Tabellen, SSE-Job und RAM-Ringpuffern. | Abschnitt 5 wird **nicht** als "Umbau eines Node-Editors" geschrieben, sondern als **Lehre aus zwei Graphen, die es nicht gibt**: Dem Nutzer wird keine Infrastruktur-Topologie gezeigt, sondern ein **Beziehungsgraph zwischen Aussagen** (stützt / widerspricht / blockiert). Die Analyse in Abschnitt 5 bleibt inhaltlich vollständig, richtet sich aber auf das *Ziel*-Prinzip, nicht auf vorhandenen Code. |
| "Mesh AI" als Inspirationsrichtung für "persönlichere, vernetztere, kontextbewusstere, kontinuierlichere AI-Erfahrung" | MashAI ist ein **Tab-/Profil-Organizer für fremde KI-Weboberflächen**, kein Memory-System. Der "persönliche" Anteil besteht aus **Profilen und Session-Persistenz**, nicht aus Wissen über den Nutzer. | Die "Kontinuität" wird in Abschnitt 9.3 **aus dem Arbeitsstück** abgeleitet (Was wurde schon geklärt? Was wurde verworfen?), **nicht** aus einem impliziten Nutzer-Gedächtnis. Das ist technisch ehrlicher und entspricht der Forderung der Aufgabenstellung nach Transparenz. |
| OmniRoute "verbindlich als zentrale Infrastruktur für Modelle, Provider und Routing" | Verifiziert: Verwaltungs- und Provider-Ebene. **Nicht verifiziert:** Inferenz-/Routing-/Fallback-Ebene. | Architektur wird so gebaut, dass der **Router-Port austauschbar** ist (Abschnitt 11.3). Fällt der Capability-Probe negativ aus, bleibt das Produktmodell intakt — es verliert dann nur seinen bevorzugten Motor, nicht seinen Sinn. |
| "Bestehende funktionierende Logik … muss zuerst verstanden werden" (Preservation Contract) | Es existiert genau **eine** funktionierende Anwendung (`schaltwerk`, 34 Tests) und zwei **unveränderte Fremdarchive**. | Der Preservation Contract (Abschnitt 4.2) ist bewusst kurz und besteht im Kern aus der Regel: **`schaltwerk` wird nicht angefasst** (es ist produktiv für Proxy-Logistik und hat dokumentierte Goldene Regeln), und **die ZIPs werden nicht Teil der Anwendung**. |

---

# TEIL II — DAS PRODUKTMODELL

## 2. Die zentrale Produktfrage (VORSCHLAG, aus dem Befund begründet)

Die Frage "Wie sieht ein OmniRoute-Dashboard aus?" ist die falsche Frage. Sie führt zu einer Oberfläche, die Infrastruktur verwaltet. Die richtige Frage ist:

> **Was entsteht hier, das es ohne diese App nicht gäbe?**

### 2.1 Antwort in einem Satz

**Omnia Atelier ist ein Arbeitsraum, in dem aus Material ein Arbeitsstück entsteht, das belastbar ist: jedes Ergebnis trägt seine Quellen, seine verworfenen Alternativen, seine offenen Fragen und seine Routing-Geschichte bei sich — und bleibt bearbeitbar, versionierbar und fortsetzbar.**

### 2.2 Die Fragen der Aufgabenstellung, einzeln beantwortet

| Frage | Antwort |
| --- | --- |
| Was macht der Nutzer hier? | Er bringt Material herein, formuliert eine Absicht, korrigiert die Interpretation der Leitassistenz, lässt arbeiten, greift ein, und nimmt ein **Arbeitsstück** mit — nicht eine Antwort. |
| Welche Tätigkeit steht im Mittelpunkt? | **Urteilen.** Nicht Fragen stellen. Der Nutzer entscheidet, was trägt und was nicht. |
| Was gibt er hinein? | Material (Repo-Dateien, Code, Doku, Notizen, Aufgaben, frühere Arbeitsstücke, Entscheidungen, Quellen) + eine **Absicht** ("Beurteile, ob…" / "Erarbeite eine Entscheidung zu…" / "Spezifiziere…"). |
| Was entsteht daraus? | Ein **Arbeitsstück**: strukturiertes Dokument mit These/Kernaussage, Begründung, belegten Quellen, Risiken, verworfenen Alternativen, offenen Fragen, Routing-Protokoll, Versionen. |
| Wie unterscheidet sich das von einer Chat-Antwort? | Eine Chat-Antwort ist eine **Äußerung ohne Haftung**. Ein Arbeitsstück ist ein **Objekt mit Struktur, Herkunft, Version und Status** — es kann zitiert, kritisiert, versioniert, fortgesetzt und übergeben werden, ohne dass die Entstehung neu verhandelt werden muss. |
| Welche Rolle spielt Repository-Content? | Er ist **das bevorzugte Material ersten Ranges**: prüfbar, versioniert, real. Der Repo-Inhalt liefert dem Arbeitsstück seine Bodenhaftung. (BEKANNT: im aktuellen Repo sind das `schaltwerk`, die Dokumentation, die Tests, die beiden Archive.) |
| Welche Rolle spielt die Leitassistenz? | Sie ist die **Werkstattmeisterin**: sie ordnet Material, schlägt einen Arbeitsplan vor, wählt Fähigkeiten, führt Ergebnisse zusammen, benennt Konflikte und Routing-Ereignisse — und sie **fragt, statt zu raten**, wenn eine Information nicht geprüft werden konnte. |
| Wann wird OmniRoute sichtbar? | Wenn eine Routing-Entscheidung **die Qualität, die Kosten, die Latenz, den Datenschutz oder die Fähigkeiten** des Ergebnisses beeinflusst — also bei Fallback, bei Modellwechsel zwischen Versionen, bei abgelehnten Fähigkeiten, bei Budgetgrenzen. |
| Wann bleibt es unsichtbar? | Immer dann, wenn der Nutzer nur verstehen muss, **was** herauskam, nicht **wo** es herkam. Ein gerader Lauf ohne Anomalie erzeugt **keine Router-Meldung**. |
| Wann sind mehrere Modelle sinnvoll? | Bei **Urteilen mit Konfliktpotenzial**: wenn eine zweite, unabhängige Position Widersprüche, Risiken oder blinde Flecken finden soll. Nicht bei faktischen Extraktionen. |
| Wann sind Tools/Agenten sinnvoll? | Wenn eine Behauptung nur durch **Zugriff** belegbar ist (Datei lesen, Code suchen, Version vergleichen). Nicht, um Beschäftigung zu demonstrieren. |
| Welche Entscheidungen kann der Nutzer beeinflussen? | Materialauswahl, Absicht, Arbeitsplan, Fähigkeiten/Modelle, Budgetgrenzen, Bestätigung aller externen oder schreibenden Aktionen, Inhalt des Arbeitsstücks, Versionierung, Memory. |
| Was passiert automatisch? | Material-Indexierung, Arbeitsplan-Vorschlag, Fähigkeitsauswahl innerhalb der Policy, Routing, Fallback innerhalb der Policy, Quellenverknüpfung, Status- und Eventprotokoll, Versionierung. |
| Warum kein Chatbot? | Weil die primäre Einheit nicht die Nachricht ist, sondern das **Arbeitsstück**. Der Chat ist ein Eingabekanal, kein Aufbewahrungsort. |
| Warum kein Agent-Dashboard? | Weil Aktivität nicht zum Selbstzweck angezeigt wird. Es gibt keine "Agenten-Karten", sondern **Spuren am Arbeitsstück**: was wurde geprüft, was stützt was. |
| Warum kein Node-Editor? | Weil die Verbindungen, die hier zählen, **semantisch** sind (stützt / widerspricht / blockiert), nicht technisch (Ausgang A → Eingang B). Der Nutzer verdrahtet keine Infrastruktur, er **begründet ein Ergebnis**. |
| Warum fühlt es sich eigenständig an? | Weil drei Dinge zusammenkommen, die es so nicht gibt: **prüfbares Material** (Repo), **haftendes Ergebnis** (Arbeitsstück) und **eine Instanz, die den Überblick behält** (Leitassistenz), während die Infrastruktur darunter austauschbar bleibt. |

### 2.3 Die drei Objekte des Produkts (VORSCHLAG)

```
MATERIAL          →  ARBEITSSTÜCK  →  ÜBERGABE
(hereingebracht)     (bearbeitet)      (wirksam gemacht)

Repo-Datei           Kernaussage        Version
Notiz                Begründung         Freigabe
Quelle               Quellenbezug       Export
früheres Werkstück   Alternativen      Briefing
Aufgabe              Risiken           PR-Vorschlag (später, bestätigt)
Entscheidung         offene Fragen
                     Routing-Protokoll
```

**Regel:** Ohne Material gibt es kein Arbeitsstück. Die Leitassistenz darf eine Absicht **nicht** in einen Lauf überführen, wenn kein Material benannt ist — sie muss nach Material fragen oder eines vorschlagen. Das verhindert, dass das Atelier zum Chatbot degeneriert.

---

## 3. Drei wirklich unterschiedliche Produktmodelle

Drei Modelle mit **unterschiedlicher Kernhandlung**, nicht drei Oberflächen derselben Idee:
**A = herstellen**, **B = prüfen**, **C = übergeben**.

---

### 3.A — **Omnia Atelier** (Kernhandlung: *herstellen*)

**Kernidee.** Eine Werkstatt. Material liegt an der Wand, in der Mitte steht ein Werkstück auf der Bank. Die Leitassistenz ist die Meisterin, die weiß, was schon bearbeitet wurde. Ergebnis ist ein **Arbeitsstück**, nicht eine Antwort.

**Zentrale Nutzerhandlung.** Material an die Werkbank legen → Absicht formulieren → Arbeitsplan bestätigen oder korrigieren → arbeiten lassen → eingreifen → Arbeitsstück nehmen.

**Startbild.** Kein Dashboard. Der Raum ist **leer bis auf die Materialwand**: eine low-detail Fläche mit dem inventarisierten Material (Repo-Dateien als "Bögen", Notizen als "Zettel", frühere Arbeitsstücke als "Mappen"). Die Werkbank ist leer und trägt die Zeile: *"Lege Material an oder formuliere, was entstehen soll."* Unten liegt die **Fragenleiste** (leer, aber vorhanden — sie ist der Grund, warum der Raum kein leeres Blatt ist).

**Was der Nutzer einbringt.** Repository-Inhalte, Dateien, Notizen, frühere Arbeitsstücke, Aufgaben, Entscheidungen — plus eine Absicht in einem Satz.

**Was geschieht danach.** Die Leitassistenz schlägt einen **Arbeitsplan** vor: Abschnittsstruktur des Werkstücks, benötigte Fähigkeiten, geschätzte Komplexität, offene Vorfragen. Der Nutzer korrigiert (Abschnitte streichen, Material ergänzen, Fähigkeit verbieten). Dann läuft der Run — sichtbar als **Werkzeugspur** an der Oberkante der Werkbank: ein Slot pro aktiver Fähigkeit, füllt sich, wird grau bei Abschluss, wird **bernsteinfarben** bei Fallback. Das Arbeitsstück **wächst sichtbar in seine Abschnitte**, Abschnitt für Abschnitt.

**Rolle der Leitassistenz.** Werkstattmeisterin. Sie ordnet, plant, delegiert, widerspricht, erinnert an verworfene Alternativen. Sie schreibt **nichts** ohne Materialbezug.

**Rolle von OmniRoute.** Motorraum hinter der Werkzeugspur. Unsichtbar im Normalfall; sichtbar als **Fallback-Karte** an der Stelle, wo die Qualität betroffen ist.

**Rolle der Modelle.** Fähigkeiten, nicht Persönlichkeiten: *Strukturleser*, *Risikoprüfer*, *Synthetisierer*, *Quellensucher*. Gleiche Fähigkeit = austauschbares Modell.

**Rolle der LibreChat-Module.** Reine Unterbau-Referenz: Memory-Semantik (Key/Value + Opt-out), Nachrichtenbaum als Versionsmodell, Stream-Job-Muster. Kein UI, kein Express.

**Rolle der MashAI-inspirierten Kontinuität.** **Arbeitsräume statt Profile**: ein Raum = ein Thema mit seinem Material, seinem Verlauf, seinen Entscheidungen. Wiederbetreten statt neu laden.

**Rolle des Repository-Contents.** Primärmaterial ersten Ranges; der Materialwand-Eintrag zeigt **Herkunft und Prüfstatus** (gelesen / nicht gelesen / geändert seit letztem Lauf).

**Wie Aktivität sichtbar wird.** Nicht als Agentenliste, sondern als **Spur am Werkstück**: jeder Abschnitt zeigt, welche Fähigkeit ihn erzeugt hat, welche Quellen ihn stützen, welche Gegenposition geprüft wurde.

**Typische Nutzung.** "Beurteile, ob `schaltwerk` als Hintergrunddienst erhalten bleiben kann." → Material: `server.py`, `DOKUMENTATION.md`, `tests/test_server.py`, `CHANGELOG.md` → Arbeitsplan → Run mit Strukturleser + Risikoprüfer parallel → Synthese → Arbeitsstück "Entscheidung: Erhalt mit drei Auflagen" mit 12 Quellenbezügen, 2 verworfenen Alternativen, 3 offenen Fragen.

**Unterschied zum alten Schaltwerk.** `schaltwerk` zeigt **Infrastruktur als Tabelle** (Proxies, Provider, Logs). Das Atelier zeigt **Arbeit als Objekt**. Es gibt keine Tabelle von Ressourcen, es gibt ein Werkstück mit Spuren.

**Risiken.** (1) Das Werkstück-Format kann zur Textvorlage erstarren. (2) "Materialwand" kann zur Dateiliste verkommen. (3) Wenn OmniRoute keine Inferenz-API bietet, fehlt der Motor — das Produkt wird zur Schreibfläche. (4) Der Arbeitsplan kann als bürokratische Hürde empfunden werden. (5) Hoher Anspruch an die Synthese-Qualität; schwache Synthese entwertet alles.

**Chancen.** (1) Das Ergebnis ist **zitierfähig** — der stärkste Unterschied zum Chat. (2) Natürlicher Ort für Repository-Wissen. (3) Routing-Transparenz wird zum Qualitätsmerkmal statt zur Technik-Show. (4) Versionierung erzeugt echten Wiederbesuchswert. (5) Erweiterbar ohne Bruch: neue Fähigkeit = neues Werkzeug, nicht neues UI-Paradigma.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ STIMME  · „Plan steht. Zwei Prüfungen laufen. Quelle 4 widerspricht 2.“   │
├───────────────┬──────────────────────────────────────┬───────────────────┤
│ MATERIALWAND  │            WERKBANK                  │   ABLAGE          │
│               │  ┌────────────────────────────────┐  │                   │
│ ▣ server.py   │  │ ARBEITSSTÜCK v3                │  │ ◫ v1 · v2 · v3    │
│ ▣ DOKU.md     │  │                                │  │                   │
│ ▣ tests       │  │ 1 Kernaussage      ● fertig    │  │ ▸ Export          │
│ ▤ Notiz       │  │ 2 Begründung       ● fertig    │  │ ▸ Briefing        │
│ ▥ Werkstück#7 │  │ 3 Quellen          ◐ läuft     │  │ ▸ Übergabe        │
│               │  │ 4 Alternativen     ○ offen     │  │                   │
│ + Material    │  │ 5 Risiken          ◐ läuft     │  │ FREIGABE          │
│               │  └────────────────────────────────┘  │ (bestätigt)       │
│               │   Werkzeugspur: [Struktur ✓][Risiko ◐] │                 │
├───────────────┴──────────────────────────────────────┴───────────────────┤
│ FRAGENLEISTE (blockierend): „Ist Port 24615 dauerhaft?“ · „Key-Rotation?“ │
└──────────────────────────────────────────────────────────────────────────┘
```

---

### 3.B — **Der Beweisraum** (Kernhandlung: *prüfen*)

**Kernidee.** Kein Raum zum Erzeugen, sondern zum **Verhören von Behauptungen**. Der Nutzer bringt eine Behauptung (eigene oder gefundene) — das System macht daraus eine **Beweisakte**: jede Teilaussage bekommt einen Status *belegt / widerlegt / unbelegt / unbelegbar / widersprüchlich*.

**Zentrale Nutzerhandlung.** Behauptung auf den Tisch legen → das System zerlegt sie in prüfbare Teilaussagen → jede Teilaussage wird gegen Material geprüft → der Nutzer sieht die **Beweislast** und entscheidet, was als Hypothese stehen bleibt.

**Startbild.** Ein Tisch mit einer leeren Akte: *"Welche Behauptung soll geprüft werden?"* Darunter die Materialwand (identisch zu A, aber als "Beweismittel" beschriftet).

**Was der Nutzer einbringt.** Eine Behauptung + Beweismittel.

**Was geschieht danach.** Zerlegung in Teilaussagen (sichtbar als nummerierte Karten). Jede Karte bekommt maximal einen Belegstatus; **unbelegte Karten bleiben sichtbar rot-markiert stehen** und werden nie stillschweigend gelöscht. Der Run sucht gezielt **Gegenbeweise**, nicht Bestätigung.

**Rolle der Leitassistenz.** Staatsanwältin und Verteidigerin zugleich: sie sucht aktiv die widerlegende Quelle.

**Rolle von OmniRoute.** Zwei Rollen mit absichtlich **unterschiedlichen** Modellen: *Belegsucher* (präzise, billig) und *Gegenprüfer* (kritisch, teurer). Fallback ist hier **besonders kritisch** und wird immer gemeldet, weil ein schwächeres Modell die Beweislast verfälscht.

**Rolle der LibreChat-Module.** Zitat-/Quellenverarbeitung (`packages/api/src/files/citations.ts` — **BEKANNT vorhanden**) und der Nachrichtenbaum als Beweiskette.

**Rolle der MashAI-Kontinuität.** Wiederaufnahme offener Beweisakten; Erinnerung an früher verworfene Behauptungen.

**Rolle des Repository-Contents.** Gerichtsfester Beleg: Code und Tests sind die stärkste Beweisart, Doku die schwächste (und wird als solche markiert).

**Wie Aktivität sichtbar wird.** Als **Beweisstatus je Karte**, nicht als laufende Agenten.

**Typische Nutzung.** "Stimmt die Annahme, dass OmniRoute Modell-Routing selbst übernimmt?" → Prüfung gegen `server.py`/`DOKUMENTATION.md` → Ergebnis: **unbelegbar aus diesem Repository** (kein Inferenz-Aufruf auffindbar) → die Akte hält das als offenen Befund fest, statt ihn zu schließen.

**Unterschied zum alten Schaltwerk.** `schaltwerk` prüft **Proxies** (technisch, binär: lebt/tot). Der Beweisraum prüft **Aussagen** (semantisch, graduell: belegt/widersprüchlich/unbelegbar).

**Risiken.** (1) Schwache Zerlegung erzeugt Scheinprüfung. (2) "Unbelegbar" ist ein unbefriedigendes Ergebnis, obwohl es das ehrlichste ist. (3) Kann sich kalt und juristisch anfühlen. (4) Hoher Aufwand für Gegenbeweissuche. (5) Verleitet zur Illusion von Objektivität.

**Chancen.** (1) Extrem starker Wahrheitsanspruch — der schärfste Kontrast zu Chatbots. (2) Nutzt Repository-Content optimal. (3) Macht Modellunterschiede **messbar** relevant. (4) "Unbelegbar" ist ein echtes Produktversprechen gegen Halluzination. (5) Perfekt für Code- und Architekturentscheidungen.

```
┌──────────────────────────────────────────────────────────────────┐
│ BEWEISAKTE  ·  „OmniRoute routet Modelle selbst“                  │
├──────────────────────────────────────────────────────────────────┤
│ [1] Management-API ist erreichbar        ● BELEGT   server.py:534 │
│ [2] Provider-Connections existieren      ● BELEGT   /api/providers│
│ [3] Inferenz-Endpunkt wird aufgerufen    ✗ UNBELEGBAR             │
│ [4] Routing-Regeln sind konfigurierbar   ? OFFEN                  │
│ [5] Fallback passiert in OmniRoute       ✗ WIDERSPROCHEN  n.v.    │
├──────────────────────────────────────────────────────────────────┤
│ BEWEISLAST: 2/5 belegt · 1 offen · 1 unbelegbar · 1 widersprochen │
│ ▸ Schlussfolgerung NICHT freigegeben — [3] und [5] blockieren     │
└──────────────────────────────────────────────────────────────────┘
```

---

### 3.C — **Die Werkbrief-Gießerei** (Kernhandlung: *übergeben*)

**Kernidee.** Das Ziel ist nicht Erkenntnis für den Nutzer, sondern **Ausführbarkeit für einen anderen**. Das Produkt ist ein **Werkbrief**: ein Dokument, das so vollständig ist, dass ein anderer Mensch — oder ein anderes Modell, oder ein anderes Repository — es **ohne Rückfrage** ausführen kann.

**Zentrale Nutzerhandlung.** Empfänger benennen (Mensch / Modell / Repo / Team) → Material + Absicht → das System erzeugt den Brief und prüft ihn anschließend **blind**: ein zweiter Durchgang versucht, aus dem Brief allein die Aufgabe zu rekonstruieren. Was dabei fehlt, wird als **Lücke** markiert.

**Startbild.** Ein leerer Briefbogen mit drei Feldern oben: **An:** · **Soll:** · **Woran du merkst, dass es fertig ist:**.

**Was der Nutzer einbringt.** Empfänger + Material + Absicht.

**Was geschieht danach.** Der Brief entsteht in festen Abschnitten (Kontext, Auftrag, Material, Grenzen, Abnahmekriterien, Nicht-Ziele). Danach der **Blindtest**: der Synthetisierer bekommt nur den Brief und muss die Aufgabe zurückformulieren. Abweichungen → Lückenliste. Erst wenn die Lückenliste leer oder akzeptiert ist, gilt der Brief als gießbar.

**Rolle der Leitassistenz.** Redakteurin, die auf **Vollständigkeit für einen Dritten** besteht, nicht auf Eleganz.

**Rolle von OmniRoute.** Zwei Pflichtrollen: *Verfasser* und *Gegentester* — hier ist Parallelität **kein Luxus, sondern der Kernmechanismus**.

**Rolle der LibreChat-Module.** Preset-/Rollenlogik (`presets.js` — **BEKANNT vorhanden**) als Empfängerprofile.

**Rolle der MashAI-Kontinuität.** Empfängerprofile und wiederkehrende Abnahmekriterien.

**Rolle des Repository-Contents.** Material für Kontext und Grenzen; Code-Änderungsvorschläge werden als **Anhang zum Brief**, nie als stiller Schreibzugriff.

**Wie Aktivität sichtbar wird.** Als **Lückenliste**, die schrumpft. Das ist die Fortschrittsanzeige.

**Typische Nutzung.** "Schreib einen Werkbrief, damit ein anderer Agent `schaltwerk` auf Linux-Autostart umstellen kann, ohne Windows zu brechen." → Brief → Blindtest findet 4 Lücken (kein Hinweis auf `chcp 65001`-Abhängigkeit, kein Testpfad, …) → Lücken geschlossen → Brief freigegeben.

**Unterschied zum alten Schaltwerk.** `schaltwerk` **führt aus** (es schreibt Proxies). Die Gießerei **führt nicht aus** — sie produziert Ausführbarkeit und übergibt.

**Risiken.** (1) Der Blindtest kann zur Endlosschleife werden. (2) Sehr stark textlastig. (3) Nutzen erst bei wiederholter Übergabe hoch. (4) Verleitet zu Formalismus ohne Substanz. (5) Empfänger-Modellierung kann zu komplex werden.

**Chancen.** (1) Klarster Nachweis von Modellqualität (Blindtest = eingebautes Qualitätsmaß). (2) Natürlicher Weg zu PR-Vorschlägen mit Begründung. (3) Perfekt für Teams später. (4) Macht "Kontext" zum Produkt. (5) Sehr gut testbar.

```
┌──────────────────────────────────────────────────────────────────┐
│ WERKBRIEF  ·  An: Implementierer  ·  Status: 4 Lücken offen       │
├──────────────────────────────────────────────────────────────────┤
│ KONTEXT                    ✓ vollständig                          │
│ AUFTRAG                    ✓ vollständig                          │
│ MATERIAL                   ✓ vollständig                          │
│ GRENZEN                    ✗ LÜCKE: keine Aussage zu Windows-Pfad │
│ ABNAHMEKRITERIEN           ✗ LÜCKE: kein Testbefehl genannt       │
│ NICHT-ZIELE                ✗ LÜCKE: 1proxy-Regel nicht erwähnt    │
│ RÜCKFRAGE-REGEL            ✗ LÜCKE: wer entscheidet bei Konflikt? │
├──────────────────────────────────────────────────────────────────┤
│ BLINDTEST „Was soll ich tun?“ → 71 % Übereinstimmung (Ziel ≥ 90)  │
└──────────────────────────────────────────────────────────────────┘
```

---

### 3.D Vergleich und Empfehlung

| Kriterium | A · Atelier | B · Beweisraum | C · Werkbrief |
| --- | --- | --- | --- |
| Kernhandlung | herstellen | prüfen | übergeben |
| Primäres Objekt | Arbeitsstück | Beweisakte | Werkbrief |
| Stärke | größte Breite, echter Wiederbesuchswert | höchste epistemische Schärfe | messbare Qualität |
| Schwäche | Format kann erstarren | unbefriedigende "unbelegbar"-Ergebnisse | Formalismus-Risiko |
| Nutzt Repo-Content | sehr hoch | **am höchsten** | hoch |
| Nutzt Mehrere-Modelle | ja, bei Konflikt | ja, zwingend | ja, zwingend (Verfasser/Gegentester) |
| Nutzt OmniRoute-Routing | mittel (nur bei Relevanz) | hoch (Beweislast) | hoch (Blindtest) |
| MashAI-Kontinuität | Arbeitsräume | offene Akten | Empfängerprofile |
| Eigenständigkeit vs. Chatbot | hoch | **sehr hoch** | hoch (aber textnah) |
| Skalierbarkeit des Modells | **sehr hoch** | mittel (eng) | mittel |

**Empfehlung: Modell A — Omnia Atelier.** Begründung in Abschnitt 16. Der Beweisraum und die Gießerei gehen **nicht verloren**: der **Beweisstatus** wird zum Qualitätsmaßstab *innerhalb* des Ateliers (Abschnitt 6.4: jede Kernaussage trägt einen Belegstatus), und der **Werkbrief** wird zur **Übergabeform** eines fertigen Arbeitsstücks (Abschnitt 3.C als Exportart, nicht als eigene App). Damit ist A nicht das Sieger-Design unter dreien, sondern **der Rahmen, der B und C als Werkzeuge aufnimmt**.

---

# TEIL III — REPOSITORY-FIRST DISCOVERY UND PRESERVATION CONTRACT

## 4. Discovery-Plan

### 4.1 Prüfbereiche

Jede Zeile: Was konkret geprüft wird · Warum · Welche Entscheidung daran hängt · Voraussichtliche Haltung.

| # | Bereich | Konkret zu prüfen | Warum | Entscheidung hängt daran | Haltung (Vorschlag) |
| --- | --- | --- | --- | --- | --- |
| 1 | Verzeichnisstruktur | Vollständige Dateiliste beider ZIPs, Duplikate, versteckte Konfigurationen | Umfang und Abhängigkeitsrisiken sind sonst unbekannt | Ob ZIPs entpackt, gemountet oder unangetastet bleiben | **NICHT ANFASSEN** (nicht entpacken; nur lesend inspizieren) |
| 2 | Root-Dateien | Nur 3 Einträge + `.git`; keine App, kein CI, keine Compose | Klärt "Greenfield vs. Umbau" | Architektur-Startpunkt | **BEKANNT** — abgeschlossen |
| 3 | Monorepo vs. Single-App | Kein Workspace im Repo; LibreChat *ist* ein Monorepo (turbo) | Bestimmt, ob wir einen Workspace erben | Ob Omnia Atelier ein Monorepo wird | **NEU INTERPRETIEREN**: eigener kleiner Workspace, kein turbo-Erbe |
| 4 | Build/Start | `STARTEN.bat` (Windows, pip, Port 8765) vs. `npm run dev` (MashAI) vs. LibreChat-Compose | Legt die lokale Entwicklungsumgebung fest | Entwickler-Workflow | **NEU**: eigenes Startskript, beide Plattformen |
| 5 | Lokale Entwicklung | Python-Venv vs. Node; welche Runtimes real verfügbar sind | Verhindert einen Stack, der hier nicht läuft | Sprachwahl App-Layer | **ZU PRÜFEN** (Abschnitt 11.4) |
| 6 | Deployment | Keines vorhanden; `schaltwerk` = lokaler Einzelplatz; LibreChat = Compose-Cluster | Bestimmt Betriebsmodell | Local-first vs. Server | **VORSCHLAG**: Local-first, Single-User |
| 7 | CI/CD | Keine Repo-CI; MashAI hat `npm test`/`lint`/`build`; LibreChat hat `.github/` | Bestimmt Qualitätsuntergrenze | Teststrategie | **ERWEITERN**: minimale eigene CI (Tests + Lint) |
| 8 | Frontend | MashAI React/TS/Tailwind/Vite; LibreChat React 18 + recoil + jotai + framer-motion (102 Deps); `schaltwerk` Vanilla-Einzeldatei | Bestimmt UI-Ansatz und Abhängigkeitslast | Frontend-Stack | **NEU INTERPRETIEREN**: schlankes React/TS, **kein** recoil/jotai/framer-motion |
| 9 | Backend | `schaltwerk` FastAPI-Einzeldatei; LibreChat Express + TS-Pakete + Mongo | Bestimmt App-Layer-Sprache | Python vs. Node | **VORSCHLAG**: FastAPI (siehe 11.4) |
| 10 | Frameworks | FastAPI/uvicorn/httpx (real); Electron 39 (MashAI); Nest-ähnliche Struktur bei LibreChat | Kompatibilität und Lernkurve | Stack-Festlegung | teils **BEIBEHALTEN** (FastAPI) |
| 11 | Routen | 21 FastAPI-Routen in `server.py`; LibreChat-Routenvielfalt | Namens- und Strukturkonventionen | Eigene API-Namensgebung | **NUR ALS REFERENZ** |
| 12 | Komponenten | Keine React-Komponenten im Repo selbst (nur in ZIPs) | Klärt "wiederverwendbar" vs. "Archiv" | Build vs. Kopie | **NICHT ÜBERNEHMEN** (kein Kopieren aus ZIPs in die App) |
| 13 | Styling | Repo-Tokens in `static/index.html`; Tailwind bei MashAI und LibreChat | Designkontinuität | Design-System-Entscheidung | **ERWEITERN** (Repo-Tokens als Basis) |
| 14 | UI-Bibliotheken | Radix/Ariakit/framer-motion (LibreChat), Lucide (beide) | Abhängigkeitsrisiko | Ob eine UI-Library nötig ist | **VORSCHLAG**: keine UI-Library für v1, nur Tokens + eigene Primitive |
| 15 | Design Tokens | 10 Tokens verifiziert (Abschnitt 1.2.2) | Eine vorhandene, gemessene Anti-KI-Look-Sprache | Visuelle Identität | **BEIBEHALTEN + ERWEITERN** |
| 16 | Zustandverwaltung | `schaltwerk`: RAM-Dicts + Ringpuffer; MashAI: React-State + IPC; LibreChat: recoil/jotai | Bestimmt State-Architektur | Client-State-Modell | **NEU**: explizite Zustandsmaschine (Abschnitt 10.2) |
| 17 | Datenmodelle | LibreChat-Schemas (convo, message, memory, project, agent, toolCall, auditLog…); `schaltwerk`: keine | Liefert erprobte Feldmodelle | Arbeitsstück-/Run-Modell | **ADAPTIERT ÜBERNEHMEN** (Konzepte, nicht Code) |
| 18 | Datenbank | Keine im Repo; LibreChat = Mongo + Meili + pgvector | Persistenzentscheidung | SQLite vs. Mongo | **VORSCHLAG**: SQLite für v1 |
| 19 | ORM | Keiner im Repo; LibreChat = Mongoose | Werkzeugwahl | SQLAlchemy vs. Roh-SQL | **ZU PRÜFEN** |
| 20 | API-Struktur | FastAPI mit Pydantic-Modellen (`ConnectBody`, `HarvestBody`, `ExchangeBody`…); LibreChat REST + SSE | Eigene API-Form | Vertragsdesign | **BEIBEHALTEN** (Pydantic-Muster) |
| 21 | Authentifizierung | **Keine** in `schaltwerk` (explizit: kein Login); LibreChat: 10 Strategien | Single-User vs. Multi-User | Ob v1 Login braucht | **NICHT ANFASSEN** für v1 → lokaler Single-User, Loopback-Bindung wie `schaltwerk` |
| 22 | Berechtigungen | Keine im Repo; LibreChat: ACL/Rollen (`accessPermissions.ts`, `PermissionBits`, `AccessRoleIds`) | Grenzen der Leitassistenz | Rechte-Modell | **NUR ALS REFERENZ** (Rollen erst bei Teams) |
| 23 | Persistenz | `schaltwerk`: RAM-only, bewusst; LibreChat: Mongo | Datenhaltbarkeit | Arbeitsstück-Speicherung | **ERSETZEN** (RAM → SQLite, aber RAM-Disziplin als Tugend behalten) |
| 24 | Caching | `proxy_latency_ms`, Favicon-Cache (MashAI), LibreChat `cache/` | Performance | Material-Cache | **VORSCHLAG**: Material-Index-Cache mit Hash |
| 25 | Hintergrundjobs | `_scheduler_loop`, `_bw_watcher_loop` (asyncio-Tasks im Lifespan), 409-Sperre | Run-Ausführung | Orchestrierung | **ADAPTIERT ÜBERNEHMEN** (Muster, nicht Code) |
| 26 | Streaming | SSE via `StreamingResponse` (`/api/exchange`); LibreChat hat eigene Stream-Architektur | Live-Aktivität | Event-Transport | **BEIBEHALTEN** (SSE; `schaltwerk` beweist es hier) |
| 27 | WebSocket/SSE | Nur SSE vorhanden; kein WebSocket | Transportwahl | SSE vs. WS | **BEIBEHALTEN** (SSE reicht; Rückkanal ist HTTP) |
| 28 | Logging | `[job]`-Zeilen in der Konsole (`schaltwerk`), `bw_log`-Ringpuffer | Nachvollziehbarkeit | Run-Log-Design | **ERWEITERN** (Ringpuffer → persistiertes Run-Log) |
| 29 | Monitoring | `/api/job-status` Polling alle 5 s; `/api/hub-summary`; LibreChat: otel, langfuse, traces | Beobachtbarkeit | Status-API | **ADAPTIERT ÜBERNEHMEN** (`job-status`-Muster) |
| 30 | Error Handling | HTTPException, `unwrap_list`-Normalisierung, defensive Parser, XSS-Fix mit `esc()` | Robustheit | Fehlerklassen | **BEIBEHALTEN** (Prinzip: externe Antworten nie vertrauen) |
| 31 | Tests | 34 Tests (FastAPI, offline); MashAI 66; LibreChat umfangreich + e2e | Qualitätsuntergrenze | Teststrategie | **BEIBEHALTEN + ERWEITERN** |
| 32 | Sicherheitsmechanismen | XSS-Fix, URL-Validierung vor Speichern, Key nur im RAM, Doppelstart-Sperre, Risiko-Ausschluss beim Schreiben, Loopback-Bindung | Vertrauensbasis | Sicherheitsmodell | **BEIBEHALTEN** (direkt als Regeln übernommen) |
| 33 | Umgebungsvariablen | `HOST`/`PORT` (schaltwerk); `${VAR}`-Platzhalter in LibreChat-YAML | Konfiguration | Konfigurationsmodell | **ADAPTIERT ÜBERNEHMEN** |
| 34 | Secret-Verwaltung | Key nur im RAM (`schaltwerk`); OmniRoute `server.env` + `STORAGE_ENCRYPTION_KEY` | Schutzbedarf | Kein Secret im Frontend | **BEIBEHALTEN** (als harte Architekturregel) |
| 35 | Provider-Anbindungen | 7 OmniRoute-Connections dokumentiert; LibreChat `endpoints.custom` mit `baseURL`/`apiKey` | Anschlussfähigkeit | Adapter-Form | **ZU PRÜFEN** (Inferenz-Ebene!) |
| 36 | OmniRoute-Anbindung | 10 verifizierte Endpunkte (Abschnitt 1.5) | Adapter-Vertrag | Router-Port | **ERWEITERN** (neue, gekapselte Schicht) |
| 37 | OmniRoute-Version/Config | Image-Tag, Build, `/app/data/server.env`, Routing-Regeln | Fähigkeitsklärung | Ob Routing/Fallback in OmniRoute oder bei uns liegt | **ZU PRÜFEN — höchste Priorität** |
| 38 | LibreChat-Anteile | Nur als ZIP; keine Integration im Repo | Reuse-Entscheidung | Reuse-Matrix | **ADAPTIERT ÜBERNEHMEN** (Konzepte) |
| 39 | Agenten/Tool/MCP-Logik | LibreChat: agents, mcp, tools, skills, code — alles vorhanden; Repo selbst: keine | Fähigkeitenmodell | Fähigkeitskatalog | **NUR ALS REFERENZ** für v1 |
| 40 | Custom Content | Bad-Wolf-Persona, Goldene Regeln, Design-Tokens, `WEITERARBEITEN.txt`, `CHANGELOG.md`, `DOKUMENTATION.md` | Eigene Identität statt Import-Design | Produktidentität | **BEIBEHALTEN + NEU INTERPRETieren** |
| 41 | Wissensquellen | `DOKUMENTATION.md` (16 KB), `WEITERARBEITEN.txt` (22 KB), `CHANGELOG.md`, `README.md` | Primäres Material für das erste Arbeitsstück | MVP-Material | **BEIBEHALTEN** (und als Material inventarisieren) |
| 42 | Dateien/Assets | Zwei ZIPs (19,9 MB), Logo-Assets (MashAI, MPL-2.0!) | Lizenzrisiko | Keine Asset-Übernahme | **NICHT ANFASSEN** |
| 43 | Bestehende UI | `static/index.html`: Sidebar, Tabs, Tabellen, Statuszeile, Partikel-Porträt, Ablage | Referenz für Anti-Patterns | Was wir *nicht* bauen | **NUR ALS REFERENZ** (Anti-Pattern-Katalog) |
| 44 | Bestehende Workflows | Harvest → Check → Exchange → Assign; Zeitplan; Tray | Domänenwissen | Ob Proxy-Logistik ins Atelier kommt | **NICHT ANFASSEN** (nicht Teil von v1) |
| 45 | Schaltwerk-Logik | Kein Graph; aber Job-Phasen, 409-Sperre, SSE, Ringpuffer, Risiko-Ausschluss | Wiederverwendbare Laufzeitmuster | Run-Engine | **ADAPTIERT ÜBERNEHMEN** (Muster) |
| 46 | Node-/Graph-Daten | **Keine vorhanden** | Korrigiert die Prämisse | Kein Graph-Import nötig | **NICHT ANFASSEN** (existiert nicht) |
| 47 | Abhängigkeiten | `schaltwerk`: 4 Pakete (sehr schlank); MashAI 6 + 20 Dev; LibreChat 102 Client-Deps | Risiko | Abhängigkeitsbudget | **BEIBEHALTEN** (Schlankheit als Prinzip) |
| 48 | Technische Schulden | `schaltwerk`: 8 dokumentierte offene Punkte (Porträt-Feinschliff, Traffic-Zähler, Parameter hartcodiert, Export fehlt, IPv6 verworfen, Push steht aus) | Realismus | Was wir *nicht* zusätzlich aufmachen | **NICHT ANFASSEN** (fremde Schulden) |
| 49 | Lizenz/Copyright | LibreChat **MIT**; MashAI **MPL-2.0**; `schaltwerk` ohne Lizenzdatei; Bad-Wolf-Figur bewusst "schematisch wegen BBC-Copyright" | Rechtliche Klärheit | Reuse-Freigabe | **ZU PRÜFEN** (`schaltwerk` hat keine Lizenzdatei!) |
| 50 | Dokumentation | Drei Qualitätsdokumente + `AGENTS.md`/`CONTEXT.md` (LibreChat) | Arbeitsweise | Dokumentationsstandard | **BEIBEHALTEN** (Standard: `DOKUMENTATION.md` + `CHANGELOG.md`) |
| 51 | Offene Risiken | OmniRoute-Inferenz unbelegt; Port-/Instanz-Wirrwarr (drei Container, zwei ohne Port-Mapping); API-Key-Rotation nach Neustart; Windows-Fokus | Realismus | Reihenfolge | **ZU PRÜFEN** |

### 4.2 Preservation Contract

**BEIBEHALTEN (unverändert, mit Schutzring)**
- `schaltwerk/` als Ganzes: alle 10 Dateien, inkl. `HARVEST_TAG = "proxy-exchange"`, `px-`-Präfix-Konvention, 1proxy-Schreibverbot, RAM-only-Key-Disziplin, Loopback-Bindung, `STARTEN.bat` mit CRLF.
- Die 8 Goldenen Regeln aus `DOKUMENTATION.md`, Abschnitt 8 — sie werden zur Keimzelle des Leitassistenz-Contracts (Abschnitt 9.4).
- Design-Tokens und Anti-KI-Look-Regeln (Radius 3 px, Mono-Statuszeile, Pills nur für echte Stati).
- Dokumentationsstandard: `DOKUMENTATION.md` als Wahrheitsdatei, `CHANGELOG.md` als Änderungshistorie, nichts davon im README.
- Die 34 Tests als Regressionnetz für `schaltwerk`.

**ERWEITERN**
- Tokens um semantische Statusfarben und drei Raum-Zonen (Material/Werkbank/Ablage).
- SSE-/Job-Muster zu einer echten Run-Zustandsmaschine mit 11 Zuständen.
- Ringpuffer (`bw_log`) zu einem **persistierten, abfragbaren Run-Log**.
- FastAPI-App von einer Einzeldatei zu einem kleinen, klar geschnittenen Paket (Router, Adapter, Policy, Persistenz) — unter Beibehaltung der Pydantic- und `StreamingResponse`-Muster.

**NEU INTERPRETieren**
- **Bad Wolf → Leitassistenz.** Aus der Persona mit Stimme und Ablage wird die Anwendungsrolle mit Contract, Intent-Typen und Bestätigungsgrenzen. Die Stimme bleibt (protokollierte Tat), aber sie spricht über **Arbeitsstücke**, nicht über Proxies.
- **Ablage → Materialwand.** Aus dem RAM-Feld für Proxy-Zeilen wird die inventarisierte Materialseite mit Hash, Prüfstatus und Herkunft.
- **Hub-Gedanke → Arbeitsräume.** Aus "erste Seite im BWO-Hub" wird die Raum-Metapher für Kontexttrennung.
- **Wachdienst → Proaktivität mit Schwelle.** Aus "alle 60 s Telemetrie" wird "Hinweis nur bei Relevanzwechsel" (Abschnitt 9.3).

**ERSETZEN**
- RAM-only-Zustand → **SQLite** (Arbeitsstücke, Runs, Material-Index, Memory). *Begründung:* Arbeitsstücke müssen versionierbar und wiederbetretbar sein; RAM-only widerspricht dem Produktkern. Die RAM-*Disziplin* für **Secrets** bleibt.
- Tabellen-UI → Raum-UI. *Begründung:* Das Produkt zeigt Arbeit, nicht Ressourcen.
- Kein Login → weiterhin kein Login, **aber** mit expliziter Rechteprüfung an der Schreibgrenze (Abschnitt 11.3, Regel R6).

**NICHT ANFASSEN**
- Die beiden ZIP-Dateien (kein Entpacken ins Repo, keine Code-Kopie daraus, keine Assets — MPL-2.0-Risiko bei MashAI).
- OmniRoute selbst, ihre Provider-Connections, ihr Datenverzeichnis, ihre Container (inkl. der zwei unmapped Container `modest_gould`, `jovial_dirac`).
- Die laufende `schaltwerk`-Instanz und ihr Port.
- Das Windows-zuerst-Prinzip von `schaltwerk` (Omnia Atelier ist plattformneutral, aber `schaltwerk` wird nicht "modernisiert").
- Die offenen Punkte 1–8 aus `DOKUMENTATION.md`, Abschnitt 7 (fremde Schulden).

---

## 5. Schaltwerk kritisch neu denken — Regeln für Sichtbarkeit

### 5.1 Die ehrliche Ausgangslage

**BEKANNT:** Es gibt keine Schaltwerk-Node-Logik im Repository. Abschnitt 5 beantwortet die Frage der Aufgabenstellung deshalb als **Zielprinzip**, nicht als Umbau:
*Was wäre eine Verbindung wert, wenn es sie gäbe — und was darf deshalb niemals als Verbindung gezeigt werden?*

### 5.2 Wann Nodes helfen (und wann nicht)

| Vorteil von Nodes | Gilt hier? | Begründung |
| --- | --- | --- |
| Zeigen Datenfluss | **Nein** | Datenfluss ist Infrastruktur, nicht Arbeit. |
| Zeigen Abhängigkeit | **Teils** | Nur wenn die Abhängigkeit eine **Aussage** betrifft. |
| Ermöglichen direkte Manipulation | **Nein** | Der Nutzer will kein System bauen, sondern ein Ergebnis beurteilen. |
| Erzeugen Übersicht über Komplexität | **Nein** | Sie verlagern Komplexität nur auf die Fläche. |
| Machen Parallelität sichtbar | **Teils** | Aber Parallelität ist hier ein **Zustand**, kein Diagramm. |
| Räumliche Arbeitsfläche | **Ja** | Räumlichkeit hilft — aber als **Atelier**, nicht als Graph. |

**Kernsatz:** Ein Arbeitsraum wird dann zum technischen Diagramm, wenn die sichtbaren Verbindungen **Infrastruktur** beschreiben statt **Bedeutung**.

### 5.3 Die vier sichtbaren Beziehungsarten (VORSCHLAG)

Nur diese vier Kanten existieren in der Oberfläche. Jede hat eine eigene visuelle Form und eine eigene Frage, die sie beantwortet.

| Kante | Bedeutung | Frage, die sie beantwortet |
| --- | --- | --- |
| **STÜTZT** | Dieses Material stützt diese Aussage. | *Warum soll ich das glauben?* |
| **WIDERSPRICHT** | Diese Quelle widerspricht dieser Annahme (oder: dieses Ergebnis dieser Erwartung). | *Was spricht dagegen?* |
| **BLOCKIERT** | Diese offene Frage blockiert diese Freigabe. | *Was fehlt noch?* |
| **ENTSTAND AUS** | Dieses Arbeitsstück entstand aus diesem Material / dieser Version. | *Wo kommt das her?* |

Alle vier Kanten sind **zwischen Inhaltsobjekten**, nie zwischen Rechenschritten.

### 5.4 Was standardmäßig nicht sichtbar ist

| Information | Warum verborgen | Wann sie trotzdem erscheint |
| --- | --- | --- |
| jeder einzelne Modellaufruf | trägt keine Bedeutung | bei Fehler, Fallback oder auf ausdrückliches Verlangen (Werkstattbericht) |
| interne HTTP-Requests | reine Infrastruktur | nie in der Produktansicht; nur im technischen Run-Log |
| Token-Zähler pro Request | erzeugt Kontrollwahn ohne Entscheidungswert | aggregiert **pro Run** und nur bei Budgetgrenze |
| jeder Retry | Rauschen | nur wenn Retries die Latenz oder das Ergebnis beeinflussen |
| interne Provider-IDs | ohne Bedeutung für den Nutzer | nur als Klarname im Werkstattbericht |
| rohe Stacktraces | nicht verständlich | nie; stattdessen Fehlerklasse + Handlungsoption |
| Hintergrundentscheidungen ohne Relevanz | Dekoration | nie |

**Regel:** *Der Nutzer sieht, was er verstehen, beeinflussen, prüfen oder später begründen muss.* Alles andere existiert, aber im Run-Log.

### 5.5 Was aus einer bestehenden Schaltwerk-Logik technisch wertvoll bliebe (BEKANNT bewertet)

Auch ohne Graphen enthält `schaltwerk` **genau die Laufzeitmuster**, die ein Run-System braucht:

| Muster in `schaltwerk` | Wert für die Run-Engine |
| --- | --- |
| **Job-Phasen + `/api/job-status`** mit 5-s-Polling und Reload-Verlustfreiheit | Zustandsabfrage, die einen Neustart der UI überlebt |
| **409-Doppelstart-Sperre**, synchron im Handler geprüft | verhindert doppelte, teure Läufe |
| **SSE-Eventstrom** (`_exchange_events`, `StreamingResponse`) | Live-Aktivität ohne WebSocket |
| **Ringpuffer mit Anti-Spam-Regel** (`bw_log`, 60 Zeilen) | Protokoll mit begrenztem Wachstum |
| **Risiko-Ausschluss vor dem Schreiben** (`tls-intercept`, `ip-mismatch` → nie schreiben) | Vorbild für "Schreibzugriff nur nach Prüfung" |
| **`unwrap_list`-Normalisierung** | defensiver Adapter-Umgang mit inkonsistenten APIs — **direkt auf OmniRoute anwendbar** (Abschnitt 1.5) |
| **Validierung vor dem Speichern** (`/api/connect`) | Zustandswechsel erst nach Prüfung |
| **`probe_one` mit harter Deadline pro Einzelcheck** | Timeouts pro Teilschritt, nicht pro Gesamtlauf |

**Übersetzungsregel:** Technische Graphen werden zu **semantischen Spuren**. Statt "Node A → Node B" heißt es: *"Diese Aussage stützt sich auf diese drei Quellen; diese Quelle widerspricht; diese Prüfung steht noch aus."* Die Topologie verschwindet, die **Begründung** bleibt.

---

## 6. Visuelle Sprache (VORSCHLAG, aus dem Repo-Token-System entwickelt)

### 6.1 Raumprinzip

Drei Zonen, ein Rand, eine Stimme. Keine Sidebar-Navigation als Dauermöbel; Navigation ist **Aufgabe**, nicht Einrichtung.

- **Materialwand (links, schmal, vertikal):** hereingebrachtes Material. Kein Dateibaum, sondern **Objekte mit Herkunft und Prüfstatus** (Bogen = Datei, Zettel = Notiz, Mappe = früheres Arbeitsstück). Jedes Objekt zeigt: Name, Herkunft, Hash-Kürzel, Status (gelesen / geändert seit letztem Lauf / nicht gelesen).
- **Werkbank (Mitte, dominant, ~60 % der Fläche):** das aktuelle Arbeitsstück als **bearbeitbares Dokument**. Abschnitte sind keine Karten, sondern **Fortlauftext mit Rändern**. Jeder Abschnitt hat einen Statuspunkt und, bei Bedarf, eine aufklappbare Beweisleiste.
- **Ablage (rechts, schmal):** Versionen, Exporte, Übergaben, Freigaben. Das ist der Ort, an dem Arbeit **wirksam** wird — und der einzige Ort mit bestätigungspflichtigen Knöpfen.
- **Fragenleiste (unten, persistent):** offene Fragen und Spannungen. **Persistent sichtbar**, weil Blockaden die Arbeit steuern. Eine Frage verschwindet erst, wenn sie beantwortet oder bewusst akzeptiert wurde.
- **Stimme (oben, eine Zeile):** die Leitassistenz. Kein Chatfenster. Eine Zeile, die den **aktuellen Stand** sagt; bei Bedarf klappt der **Werkstattbericht** auf (Routing, Fallback, Kosten) — sonst nicht.

### 6.2 Warum das kein Dashboard ist

| Dashboard-Muster | Warum es hier fehlt |
| --- | --- |
| KPI-Kartenraster | Es gibt keine Kennzahlen, die für sich stehen. Zahlen erscheinen **im Satz**, in der Mono-Statuszeile — wie in `schaltwerk` nach dem De-Scale-Pass. |
| Permanente Sidebar mit Navigation | Navigation ist kein Dauerzustand. Der Raum **ist** die Navigation. |
| Kartenraster | Das Arbeitsstück ist **ein** zusammenhängendes Dokument, keine Sammlung gleichwertiger Kacheln. |
| Status-Badges überall | Status nur dort, wo er eine Handlung auslöst. |
| Zwei-Spalten-Formulare | Eingaben geschehen **am Objekt**, nicht in einer Randspalte. |

### 6.3 Farben (aus `--bg/--panel/--ink/--muted` entwickelt)

| Farbe | Wert | Funktion | Sonstiges Verbot |
| --- | --- | --- | --- |
| Grund | `#0d0e12` | Raum | — |
| Werkbank | `#13141a` | Arbeitsfläche | — |
| Materialwand / Ablage | `#0f1015` (eine Stufe dunkler als die Bank) | **Rand** > Bank = die Bank ist der hellste Ort | keine Gradienten |
| Linie | `#262833` | Struktur | — |
| Text | `#d6d7dd` | Prosa | — |
| Sekundär | `#8a8c99` | Metadaten, Herkunft | — |
| **Bernstein** | `#d9a441` | **Aufmerksamkeit der Leitassistenz**: offene Fragen, Blockaden, begründete Hinweise | kein Glow, kein Deko-Gebrauch |
| Stützt | gedämpftes Grün | Belegstatus **belegt** | nur als Punkt/Linie, nie als Fläche |
| Widerspricht | gedämpftes Rot | Belegstatus **widersprochen** | nie als Alarm-Fläche |
| Offen | gedämpftes Gelb | Belegstatus **unbelegt/offen** | — |
| Unbelegbar | Grau mit Diagonalschraffur | Belegstatus **unbelegbar** | nie farbig — es ist kein Fehler |

**Regel:** Farbe trägt **Status**, niemals Stimmung. Kein Neon, kein Glass, kein Glow außer an exakt den beiden Stellen, an denen Aufmerksamkeit eine Handlung verlangt (Blockade, Bestätigung).

### 6.4 Belegstatus als durchgehendes Qualitätsmaß (aus Modell B übernommen)

Jede **Kernaussage** eines Arbeitsstücks trägt einen Belegstatus, sichtbar als kleines Zeichen am Abschnittsanfang:

```
●  belegt          — mindestens eine geprüfte Quelle stützt die Aussage
◐  teilweise       — Quelle stützt, aber mit Einschränkung
?  offen           — noch nicht geprüft / Material fehlt
✗  widersprochen   — mindestens eine Quelle widerspricht
╱  unbelegbar      — aus dem vorhandenen Material nicht entscheidbar (kein Fehler!)
```

Ein Arbeitsstück mit `╱`-Aussagen ist **nicht** fehlerhaft — es ist ehrlich. Freigabe ist bei `✗` und ungelöstem `?` gesperrt, bei `╱` erlaubt.

### 6.5 Typografie

- **Prosa des Arbeitsstücks:** eine **Serifenschrift** (System-Serif, z. B. `Iowan Old Style/Georgia`-Fallback). *Funktion:* Der Text soll sich wie ein **Werkstück** lesen, nicht wie eine Chatnachricht. Das ist der stärkste einzelne anti-chatbotische Eingriff im ganzen Design.
- **Metadaten, IDs, Hashes, Logs:** JetBrains Mono (Repo-Kontinuität).
- **UI-Labels:** Inter/system-ui, 9–10 px, uppercase, `--muted` (Repo-Kontinuität).
- **Maße:** Basis 13 px (Repo), Lesebreite des Arbeitsstücks auf ~68 Zeichen begrenzt.

### 6.6 Bewegung

Prinzip: **Bewegung trägt Zustand.** Alles andere steht still.

| Bewegung | Bedeutung |
| --- | --- |
| Werkzeugspur füllt sich | Fortschritt einer Fähigkeit |
| Abschnitt erscheint von oben, setzt sich | ein Ergebnisabschnitt wurde erzeugt |
| Bernstein-Puls an der Fragenleiste | eine neue Blockade ist entstanden |
| Kanten zeichnen sich ein (200 ms) | eine neue Beziehung wurde erkannt |
| Werkstattbericht klappt auf | Routing wird relevant |
| Sonst: **nichts** | — |

Aus dem Repo übernommen: **`prefers-reduced-motion` → Standbild**, Pause bei `document.hidden`, Performance-Budget wie beim Partikel-Porträt gemessen, nicht geschätzt.

### 6.7 Zustände, Fehler, Fallback, Fortschritt

| Situation | Darstellung |
| --- | --- |
| Leer | Werkbank leer, Materialwand gefüllt, ein Satz: *"Lege Material an oder formuliere, was entstehen soll."* Kein Tutorial-Overlay. |
| Vorbereitet | Arbeitsplan sichtbar, Startknopf trägt **Kostenschätzung und Fähigkeitsliste** (vorher, nicht nachher). |
| Laufend | Werkzeugspur + wachsendes Dokument; **keine** Spinner-Wolke, kein "Agent denkt nach…". |
| Wartet auf Nutzereingabe | Bernstein-Rand an der betroffenen Stelle + eine konkrete Frage in der Fragenleiste. **Kein** modaler Dialog, der die Arbeit verdeckt. |
| Erfolgreich | Alle Statuspunkte geschlossen; Ablage zeigt neue Version. |
| Erfolgreich mit Einschränkung | Statuspunkt `◐` im betroffenen Abschnitt + ein Satz in der Stimme. |
| **Fallback aktiv** | **Immer sichtbar, am betroffenen Abschnitt**, als eigene Karte: *"Fähigkeit X war nicht verfügbar. Übernommen von Y. Auswirkung: …"* + Option *"Mit X erneut versuchen"*. Nie als Toast, nie als Logzeile. |
| Fehlgeschlagen | Fehlerklasse in Klartext + **konkrete Handlungsoption** (Material ergänzen / Grenze anheben / Fähigkeit wechseln / abbrechen). Kein Stacktrace. |
| Abgebrochen | Zustand bleibt **erhalten**; Stimme sagt, was bereits gesichert ist. |
| Wiederaufnehmbar | Version in der Ablage mit Knopf *"Weiterarbeiten"*; der Run-Stand wird mitgeladen. |
| Archiviert | Aus der Werkbank entfernt, in der Ablage als geschlossene Mappe, weiterhin zitierfähig. |

### 6.8 Interaktion und Übergänge

- **Material an die Werkbank ziehen** = Material ist für diesen Lauf verbindlich. (Direkte Fortführung der `schaltwerk`-Ablage-Geste, diesmal mit Inhalt statt Proxy-Zeilen.)
- **Kante anklicken** = beide Objekte werden hervorgehoben, alles andere tritt zurück (kein Modal).
- **Abschnitt bearbeiten** = Inline-Edition; der Abschnitt verliert seinen Belegstatus und wird `?`, bis er neu geprüft wird. **Die App merkt sich, dass der Nutzer eingegriffen hat** — und zeigt das in der Version.
- **Versionen** sind nicht "Speicherstände" sondern **Zustände des Werks**: `v3 (bearbeitet)`, `v2 (geprüft)`, `v1 (Entwurf)`.

### 6.9 Accessibility und Responsivität

- Tastatur: `Strg+K` (Material/Arbeitsstück suchen — MashAI-Kontinuität), `Strg+Enter` (Lauf starten), `Esc` (Werkstattbericht schließen), alle Kanten fokussierbar und mit `aria-label` in Klartext (*"Beziehung: stützt"*).
- Kein Status allein durch Farbe: jeder Belegstatus hat **Zeichen + Text**.
- Kontrast: Text auf `--bg` ≥ 7:1 (Prüfung Pflicht, da `#8a8c99` auf `#0d0e12` knapp ist — nur für Metadaten, nie für Prosa).
- `prefers-reduced-motion`, `prefers-contrast`, Fokusringe in `--ink`, keine rein hover-basierten Informationen.
- Responsiv: **Werkbank zuerst.** ≥1440 px drei Zonen; 1024–1440 px Materialwand als einziehbare Schublade; <1024 px **nur** Werkbank + Fragenleiste, Randzonen als Registerkarten. Kein Zusammenschieben zu einem Dashboard-Gitter.

---

# TEIL IV — TECHNIK

## 7. OmniRoute technisch einordnen

### 7.1 Zieldatenfluss

```
Nutzer
  │  Material + Absicht
  ▼
Omnia Atelier UI                (React/TS · kennt keine Secrets, keine Provider)
  │  REST + SSE
  ▼
Application Layer               (FastAPI · Autorisierung, Validierung, Persistenz)
  │
  ├─► Leitassistenz             (Intent- und Kontextlogik · Anwendungsrolle)
  │      │
  │      ▼
  │   Orchestrierungs-Policy    (Fähigkeitsbedarf, Parallelität, Budget, Grenzen)
  │      │
  │      ▼
  │   OmniRoute Adapter         (Normalisierung, Zeitlimits, Fehlerklassen, Secrets)
  │      │
  │      ▼
  │   OmniRoute ──► Provider ──► Modelle / Fähigkeiten
  │      │
  │      ◄── Ergebnisse · Events · Telemetrie
  │
  ├─► Repository-/Content-Layer (read-only, Hash-Index, Snapshot)
  └─► Persistenz / Memory / Audit
  │
  ▼
UI  ──► Nutzer
```

**Harte Regel:** Kein Pfeil führt von der UI zu OmniRoute. Kein Secret verlässt den Application Layer.

### 7.2 End-to-End-Workflow (konkret)

**Aufgabe:** *"Beurteile, ob die `schaltwerk`-Logik als Hintergrundorchestrierung für Omnia Atelier erhalten bleiben kann."*

```
1  Material wählen        server.py, DOKUMENTATION.md, tests/test_server.py,
                          CHANGELOG.md, WEITERARBEITEN.txt
                            ↓
2  Materialanalyse        read-only: Größe, Struktur, Abhängigkeiten, Hash je Datei
                            ↓
3  Leitassistenz          Arbeitsplan-Vorschlag:
                          · Abschnitte: Bestand, Kopplung, Risiken, Empfehlung
                          · Fähigkeiten: Strukturleser + Risikoprüfer (parallel)
                          · Vorfrage: "Nur Repo-Material oder auch Laufzeitbefunde?"
                            ↓
4  Nutzer                 korrigiert: Abschnitt "Kopplung" streichen,
                          Risikoprüfer auf Kostenaspekt verengen
                            ↓
5  Policy                 prüft: Material vorhanden ✓ · Budgetgrenze ✓ ·
                          Repo-Zugriff read-only ✓ → Freigabe
                            ↓
6  Adapter → OmniRoute    zwei Anfragen parallel (siehe PSEUDOCODE 14.2)
                            ↓
7  Modell A               Struktur & Abhängigkeiten (21 Routen, 2 Loops, RAM-State)
   Modell B               Risiken & Gegenargumente (RAM-only, keine DB,
                          kein Login, Windows-Fokus, Single-File-Monolith)
                            ↓
8  Fallback (Beispiel)    Modell B nicht verfügbar → Policy wählt Ersatzmodell;
                          Adapter meldet FALLBACK mit Auswirkungsangabe
                            ↓
9  Synthese               Leitassistenz führt zusammen, markiert Widersprüche
                            ↓
10 Qualitätsprüfung       Belegstatus je Kernaussage · unbelegbare Aussagen bleiben ╱
                            ↓
11 Arbeitsstück           "Entscheidung: Erhalt als Referenz, nicht als Basis"
                          + 12 Quellenbezüge · 2 verworfene Alternativen ·
                          3 offene Fragen · Routing-Protokoll mit 1 Fallback
                            ↓
12 Version + Verlauf      v1 gespeichert, Run-Log persistiert, wiederaufnehmbar
```

### 7.3 Modellwahl: wann ein Modell, wann mehrere, wann parallel

| Situation | Entscheidung | Begründung |
| --- | --- | --- |
| Extraktion (Struktur lesen, Inventar, Hash-Index) | **ein** Modell, billig | KeinUrteil nötig. |
| Formulierung (Abschnitt texten, Zusammenfassung) | **ein** Modell, mittel | Parallelität bringt hier nur Redundanz. |
| **Urteil mit Konfliktpotenzial** (Entscheidung, Risiko, Architektur) | **zwei** Modelle, **parallel** | Unabhängige Positionen finden blinde Flecken. |
| **Beweisprüfung** (Behauptung gegen Material) | **zwei** Modelle mit **unterschiedlicher Rolle** (Belegsucher / Gegenprüfer) | Gleichartige Modelle bestätigen sich gegenseitig. |
| Synthese mehrerer Teilergebnisse | **ein** Modell, stark | Synthese braucht Kontextfülle, nicht Vielfalt. |
| Nutzer hat eine Fähigkeit verboten | **kein** Ersatz ohne Nachfrage | Verbot ist eine Nutzerentscheidung. |
| Ergebnis ist kritisch (Schreibvorschlag, Übergabe) | **zwei** Modelle + **Nutzerbestätigung** | Kosten zweitrangig vor Richtigkeit. |

**Parallelisierung ist unnötig**, wenn (a) kein Urteil, sondern Extraktion gefragt ist, (b) die Teilaufgaben voneinander abhängen, (c) das Budget unter dem Schwellwert liegt, (d) der Nutzer eine Fähigkeit festgelegt hat.

### 7.4 Fallback-Regeln

**Grundregel: Ein Fallback verändert die Ergebnisqualität. Deshalb ist er nie unsichtbar.**

| Ebene | Verhalten | Sichtbarkeit |
| --- | --- | --- |
| Modell innerhalb derselben Fähigkeit, gleiche Qualitätsklasse | automatisch, still | **nur im Run-Log** |
| Modell in **niedrigerer** Qualitätsklasse | automatisch, aber markiert | **Fallback-Karte am Abschnitt** |
| Anderer Provider mit anderem Datenschutzniveau | **nur nach Rückfrage**, wenn Daten das Repo verlassen würden | **Blockade + Frage** |
| Fähigkeit vollständig unavailable | Abschnitt bleibt `?`, Lauf wird **nicht** künstlich abgeschlossen | **offene Frage + Option "erneut versuchen"** |
| Budgetgrenze erreicht | Lauf stoppt kontrolliert, Stand bleibt erhalten | **Status "abgebrochen · wiederaufnehmbar"** |

**Wie verhindert wird, dass ein Fallback die Qualität unbemerkt verändert:**
1. Jede Fähigkeit hat eine **Qualitätsklasse** in der Policy. Ein Wechsel **zwischen** Klassen ist immer ein meldepflichtiges Ereignis.
2. Jeder Abschnitt des Arbeitsstücks speichert, **welche Fähigkeit und welches Modell ihn erzeugt hat** — unveränderlich in der Version.
3. Das Arbeitsstück trägt einen **Klassen-Vermerk**: *"Erzeugt mit mindestens einer Fähigkeit unterhalb der Zielklasse."*
4. Der Nutzer kann jeden betroffenen Abschnitt **gezielt neu erzeugen** — nicht das ganze Werk.

### 7.5 Fehlerklassen (VORSCHLAG, für Adapter und UI verbindlich)

| Klasse | Bedeutung | Automatisch? | UI |
| --- | --- | --- | --- |
| `UNAVAILABLE` | Fähigkeit/Modell nicht erreichbar | Fallback erlaubt | Fallback-Karte |
| `TIMEOUT` | Zeitlimit überschritten | Retry nach Policy, dann Fallback | Status +Option |
| `RATE_LIMITED` | Rate-Limit erreicht | Warten/Retry mit Backoff | Wartezeit sichtbar |
| `AUTH_INVALID` | Key fehlt/ungültig | **kein** Fallback | Blockade + Handlungsanweisung |
| `BUDGET_EXCEEDED` | Kosten-/Token-Grenze | **kein** Fallback | kontrollierter Stopp |
| `MALFORMED_RESPONSE` | Antwort nicht parsebar (Repo-Präzedenz: nacktes Array!) | Retry, dann Fallback | Fallback-Karte |
| `CAPABILITY_MISSING` | gewünschte Fähigkeit existiert in der Installation nicht | **kein** Fallback ohne Nutzer | Blockade |
| `MATERIAL_UNREADABLE` | Quelle nicht lesbar | — | Abschnitt `╱ unbelegbar` |
| `POLICY_VETO` | Policy verweigert (z. B. Datenschutz, verbotene Fähigkeit) | **nie** automatisch | Blockade + Begründung |

### 7.6 Abbruch, Wiederaufnahme, Grenzen

- **Abbruch** ist jederzeit möglich und ist **nie** destruktiv: bereits erzeugte Abschnitte bleiben als Version erhalten.
- **Wiederaufnahme** setzt am letzten **abgeschlossenen Abschnitt** an, nicht am letzten Token. Der Run speichert: Material-Hashes, Abschnittsstände, verbrauchte Fähigkeiten, Budgetverbrauch, Routing-Ereignisse.
- **Zeitlimits** gelten **pro Teilschritt** (Vorbild `probe_one` mit harter Deadline), nicht nur pro Gesamtlauf.
- **Kosten- und Latenzgrenzen** werden **vor** dem Lauf angezeigt und sind vom Nutzer einstellbar. Erreicht der Lauf 80 % des Budgets, erscheint eine **Vorwarnung**; bei 100 % stoppt er kontrolliert.
- **Routing-Dokumentation:** Jeder Run schreibt ein Routing-Protokoll (Fähigkeit → Modell → Grund → Dauer → Ereignisse). Es ist Teil des Arbeitsstücks und damit zitierfähig.

### 7.7 Was die UI zeigt, was verborgen bleibt

| Zeigen | Verbergen |
| --- | --- |
| Belegstatus je Kernaussage | interner Request-Verlauf |
| Fallback mit Auswirkung | erfolgreiche Einzel-Retries |
| offene Fragen (blockierend) | interne Provider-IDs |
| Kosten **pro Run** (und bei 80 %) | Token-Zähler pro Request |
| Routing **als Zusammenfassung** ("2 Fähigkeiten, 1 Wechsel") | vollständige Header |
| Fähigkeitsnamen in Klartext | Modell-Interna, Sampling-Parameter |
| Begründete Hinweise der Leitassistenz | jede Hintergrundentscheidung ohne Relevanz |

---

## 8. Reuse-Matrix: LibreChat und MashAI

### 8.1 LibreChat-Reuse-Matrix

**Rahmenbedingungen (BEKANNT):** MIT-Lizenz (freizügig), aber **TypeScript + MongoDB + Meilisearch + pgvector + Express-Legacy + 102 Client-Abhängigkeiten**. Direkte Code-Übernahme in eine lokale Single-User-App ist teuer, nicht weil die Lizenz es verbietet, sondern weil die **Datenmodell- und Laufzeitkopplung** es tut.

| Bereich (verifiziert vorhanden) | Bewertung | Begründung |
| --- | --- | --- |
| **Memory-Modell** (`memory.ts`: Key/Value, `^[a-z_]+$`, `agentId`-Partition, `tokenCount`; Routen mit Opt-out, Einzel-Key-Update/Löschen) | **ADAPTIERT ÜBERNEHMEN** | Genau die Semantik, die die Aufgabenstellung fordert: transparent, begrenzt, korrigierbar, löschbar, partitioniert. Nur die *Form* wird übernommen (SQLite statt Mongo), nicht der Code. |
| **Nachrichtenbaum** (`parentMessageId`) | **ADAPTIERT ÜBERNEHMEN** | Perfekte Grundlage für Versionierung und verworfene Alternativen unseres Arbeitsstücks. |
| **Run-/Stream-Architektur** (`GenerationJobManager`, `ApprovalLifecycle`, `SteeringLifecycle`, `checkpoints`, `terminalProjection`, `abortContent`) | **NUR ALS REFERENZ** | Konzeptionell exzellent, aber auf Mehrprozess-/Redis-/Mongo-Koordination ausgelegt. Wir übernehmen die **Begriffe** (Approval, Checkpoint, terminale Projektion, Abbruch), nicht die Implementierung. |
| **Authentifizierung** (10 Strategien: local, jwt, google, github, discord, facebook, apple, openid, saml, ldap) | **NICHT ÜBERNEHMEN** (v1) | Single-User, Loopback. Später: JWT/Refresh-Referenz. |
| **Berechtigungen/ACL** (`PermissionBits`, `AccessRoleIds`, `accessPermissions.ts`) | **NUR ALS REFERENZ** | Erst relevant bei Teams. Unser v1-Rechtemodell ist eine einzige Grenze: **Schreiben = bestätigungspflichtig**. |
| **Endpunkt-Konfiguration** (`endpoints.custom` mit `baseURL`, `apiKey`, `models.default/fetch`, `headers`) | **ADAPTIERT ÜBERNEHMEN** | Das ist die gedankliche Schablone für den OmniRoute-Adapter — **sofern** OmniRoute OpenAI-kompatibel ist (**ZU PRÜFEN**). |
| **Datei-/Kontextverarbeitung** (`files/`: `context.ts`, `extract.ts`, `documents/`, `citations.ts`) | **NUR ALS REFERENZ** | Wir brauchen nur Text/Code/Doku. Ein RAG-Stack mit pgvector wäre für v1 Overkill. |
| **Agenten/Tools/MCP/Skills/Code-Environments** | **NUR ALS REFERENZ** | Fähigkeits-*Konzept* ja, Implementierung nein. |
| **Zitat-/Quellenverarbeitung** (`citations.ts`) | **ADAPTIERT ÜBERNEHMEN** (Konzept) | Unser Belegstatus braucht Zitatanknüpfung. |
| **Presets/Rollenlogik** (`presets.js`) | **NUR ALS REFERENZ** | Als Empfängerprofil für Werkbriefe später. |
| **Projekte** (`chatProject.ts`) | **NUR ALS REFERENZ** | Unser "Arbeitsraum" ist enger und materialbezogener. |
| **Audit-Log** (`auditLog.ts`) | **ADAPTIERT ÜBERNEHMEN** (Konzept) | WirAuditieren Runs, Aktionen und Memory-Zugriffe. |
| **Streaming-Client-Muster** | **NUR ALS REFERENZ** | Wir nutzen SSE, das `schaltwerk` hier bereits beweist. |
| **Frontend-Komponenten / UI** | **NICHT ÜBERNEHMEN** | Explizite Aufgabe: darf nicht wie LibreChat aussehen. 102 Abhängigkeiten sind ein Risiko, kein Gewinn. |
| **Datenbankmuster (Mongo/Mongoose)** | **NICHT ÜBERNEHMEN** | SQLite für v1. |
| **Schedules/Triggers/Subagents** | **NICHT ÜBERNEHMEN** | Nicht Teil des Produktkerns. |

**Kriterienbewertung (Zusammenfassung):**

| Kriterium | Bewertung für LibreChat-Code-Übernahme |
| --- | --- |
| Lizenz | **günstig** (MIT) |
| Sicherheit | **neutral** (erprobt, aber mehr Angriffsfläche als wir brauchen) |
| Datenmodell-Kompatibilität | **ungünstig** (Mongo-Dokumente vs. relationale Arbeitsstück-Versionen) |
| Abhängigkeitsrisiko | **hoch** (102 Client-Deps, Cluster-Infrastruktur) |
| UI-Kopplung | **hoch** (Rechteck: wir wollen sie ausdrücklich nicht) |
| Migrationsaufwand | **hoch** |
| Testbarkeit | **schwer** (Cluster nötig) |
| Langfristige Wartbarkeit | **gut, aber nicht für unsere Größe** |

**Ergebnis:** LibreChat ist für Omnia Atelier eine **Referenz- und Musterquelle, kein Code-Lieferant.** Das ist keine Abwertung — es ist die richtige Entscheidung für ein lokales Single-User-Produkt.

### 8.2 MashAI-Reuse-Matrix (MPL-2.0 — Vorsicht!)

| Bereich | Bewertung | Begründung |
| --- | --- | --- |
| **Profil-/Arbeitsraum-Modell** | **ADAPTIERT ÜBERNEHMEN** (Konzept) | Die stärkste Idee: Kontexttrennung mit vollständiger Isolation. |
| **Session-Persistenz** (Tabs, Fensterzustand, Wiederbetreten) | **ADAPTIERT ÜBERNEHMEN** (Konzept) | Unser "Raum wird wieder betreten, nicht neu geladen". |
| **Side Panel** (zwei Ansichten gleichzeitig, Ziehteiler) | **ADAPTIERT ÜBERNEHMEN** (Konzept) | Wird zur Gegenüberstellung von Modellpositionen. |
| **Quick Search / Command Palette (Ctrl+K)** | **ADAPTIERT ÜBERNEHMEN** | Günstig, erwartbar, funktional. |
| **Ranking-Logik** (exakt > Präfix > Wortanfang > Teilstring, 27 Tests) | **NUR ALS REFERENZ** | Für Materialsuche anpassbar. |
| **SettingsManager** (Defaults, Merge, **Migrationen**) | **ADAPTIERT ÜBERNEHMEN** (Muster) | Migrationen sind Pflicht, sobald Daten persistiert werden. |
| **Smart Suspension** (Ressourcen schonen, media-aware) | **NUR ALS REFERENZ** | Übertragbar als "Hintergrundläufe drosseln". |
| **Electron-Runtime** | **NICHT ÜBERNEHMEN** (v1) | Web-App genügt; v1 läuft lokal im Browser wie `schaltwerk`. **ZU PRÜFEN** für später. |
| **Adblocker (Ghostery)** | **NICHT ÜBERNEHMEN** | Ohne Produktbezug. |
| **Tab-/Browser-Metapher** | **NICHT ÜBERNEHMEN** | Sie hält Material in fremden Oberflächen — das Gegenteil unseres Ziels. |
| **Logo/Assets** | **NICHT ANFASSEN** | **MPL-2.0** und fremde Marke. |
| **Violettes Dark-Theme** | **NICHT ÜBERNEHMEN** | Wir haben ein eigenes, gemessenes Token-System. |

**Lizenz-Warnung (BEKANNT):** MPL-2.0 ist **file-level copyleft**. Kopierte Dateien müssten MPL-2.0 bleiben. Deshalb: **keine Code-Kopie aus `Kurz-main`, nur Konzeptübernahme.** Gleiches gilt für das `schaltwerk`-Paket: **es hat keine Lizenzdatei (ZU PRÜFEN)** — ohne Klärung darf daraus nichts in ein neues Produkt kopiert werden; wir übernehmen *Muster*, nicht Dateien.

### 8.3 MashAI-inspirierte Kontinuität — kontrolliertes Konzept

Die Aufgabenstellung verlangt Präzision zu neun Fragen. Antworten (VORSCHLAG, bewusst restriktiv):

| Frage | Antwort |
| --- | --- |
| Was heißt "persönlich"? | **Arbeitsbezogen, nicht personenbezogen.** Das System erinnert **Arbeitsräume, Entscheidungen, verworfene Alternativen und Arbeitsweisen** — keine biografischen Merkmale, keine Stimmungsprofile, keine "Nutzer-Psychologie". |
| Erinnert sie sich an Arbeitsstücke? | **Ja.** Das ist der Kern: Versionen, Verlauf, offene Fragen, verworfene Alternativen. Vollständig einsehbar, vollständig löschbar. |
| Erinnert sie sich an Präferenzen? | **Ja, aber nur an explizit gesetzte Arbeitseinstellungen**: Standard-Fähigkeiten, Budgetgrenzen, Schreibverbote, Materialquellen, Ausgabeformate. |
| Gibt sie proaktive Hinweise? | **Ja, mit drei Schwellen:** (1) eine Blockade entsteht, (2) Material hat sich seit dem letzten Lauf geändert, (3) eine frühere Entscheidung wird durch neues Material berührt. **Nie** ohne Bezug zu einem konkreten Objekt. |
| Was darf dauerhaft gespeichert werden? | Arbeitsstücke, Versionen, Runs, Material-Hashes, Routing-Protokolle, **explizit bestätigte** Arbeitseinstellungen, Audit-Einträge. |
| Was muss temporär bleiben? | Alles, was nur für einen Lauf gilt: Zwischenergebnisse, Kandidaten, Kontextfenster, nicht bestätigte Vorschläge. Ende des Laufs → verwerfen, außer der Nutzer übernimmt sie. |
| Wie sieht der Nutzer Erinnerungen? | Ein eigenes Register **"Gedächtnis"** im Arbeitsraum: Liste mit Schlüssel, Wert, Herkunft ("gesetzt von dir" / "vorgeschlagen am …"), Datum, Verwendung. Keine versteckte Speicherung. |
| Wie korrigiert/löscht er? | Jeder Eintrag einzeln bearbeitbar und löschbar; **Sammellöschung** ("Alles vergessen") mit Bestätigung; Löschung ist **hart** (kein Soft-Delete, kein Wiederherstellen) und wird im Audit vermerkt. |
| Wann darf sie proaktiv handeln? | Bei **reinen Lese- und Analysehandlungen innerhalb eines bestätigten Arbeitsplans**. Nie bei Schreibzugriffen, externen Aktionen, Deployments, Repository-Änderungen. |
| Wann muss sie fragen? | Bei jeder **Schreibhandlung**, jeder **externen** Wirkung, jedem **Übergang in eine niedrigere Qualitätsklasse**, jedem **Datenschutzwechsel**, jedem **Speichervorschlag für Gedächtnis**. |

**Anti-Illusions-Regel (Verpflichtend):** Die UI darf **nie** den Eindruck erwecken, das System "kenne" den Nutzer. Es gibt keine Sätze wie "Du bevorzugst normalerweise…", es sei denn, die Quelle ist ein sichtbarer Gedächtnis-Eintrag mit Datum und Bearbeiten-Knopf.

### 8.4 Leitassistenz-Contract (VORSCHLAG — verbindlich für Implementierung)

**1 · Intent-Typen (erschöpfend für v1)**

| Intent | Bedeutung | Ergebnis |
| --- | --- | --- |
| `ANALYZE_MATERIAL` | Material strukturieren und einordnen | Inventar/Strukturabschnitt |
| `ASSESS_QUESTION` | eine Beurteilungsfrage beantworten | Arbeitsstück mit Belegstatus |
| `DRAFT_SPECIFICATION` | etwas spezifizieren | Spezifikations-Arbeitsstück |
| `COMPARE_OPTIONS` | Alternativen gegenüberstellen | Vergleich mit verworfenen Positionen |
| `CONTINUE_WORKPIECE` | bestehendes Arbeitsstück fortsetzen | neue Version |
| `REVISE_SECTION` | einen Abschnitt überarbeiten | Version mit Änderungsvermerk |
| `EXPLAIN_RUN` | erklären, was im letzten Lauf geschah | Werkstattbericht |
| `PREPARE_HANDOFF` | Arbeitsstück übergabefähig machen | Werkbrief (aus 3.C) |

Nicht unterstützt in v1: autonomes Handeln, Repository-Schreibzugriff, Deployment, Web-Recherche, Multi-User-Handlungen.

**2 · Erlaubt ohne Bestätigung**
- Material **lesen** (read-only), indexieren, hashen, strukturieren.
- Arbeitspläne **vorschlagen**.
- Fähigkeiten innerhalb der **freigegebenen Policy** auswählen und aufrufen.
- Fallback innerhalb **derselben Qualitätsklasse**.
- Abschnitte erzeugen, Belegstatus setzen, Versionen **anlegen** (nicht veröffentlichen).
- Offene Fragen und Blockaden benennen.

**3 · Bestätigungspflichtig (nie automatisch)**
- Jeder **Schreibzugriff** auf Dateien, Repository oder Konfiguration.
- Jede **externe** Wirkung (Netzwerk jenseits des konfigurierten Routers, Uploads, Tickets, PRs).
- Jeder **Gedächtnis-Eintrag** (Anlegen, Ändern, Löschen).
- Jede **Übergabe** (Export, Werkbrief, Freigabe).
- Jeder Fallback in eine **niedrigere Qualitätsklasse** oder über eine **Datenschutzgrenze** hinweg.
- Jedes Überschreiten einer vom Nutzer gesetzten **Grenze** (Kosten, Zeit, Fähigkeiten).
- Jede Änderung an **Goldenen Regeln**.

**4 · Memory-Regeln**
Vier Stufen, **Standard ist Stufe 1**:
1. `SESSION` — nur für diesen Lauf (Standard).
2. `WORKSPACE` — für diesen Arbeitsraum, sichtbar im Gedächtnis-Register.
3. `GLOBAL` — für alle Arbeitsräume, nur nach ausdrücklicher Bestätigung.
4. `NEVER` — nichts speichern (Funktion ist pro Arbeitsraum abschaltbar).
Regeln: Schlüssel immer `^[a-z_]+$` (LibreChat-Präzedenz), Wertlänge begrenzt, **Herkunft und Zeitstempel obligatorisch**, keine Inferenz über nicht abgelegte Inhalte, **kein** implizites Lernen aus Arbeitsinhalten.

**5 · Kontextregeln**
- Kontext = **Material + Arbeitsstück + Arbeitsplan + Laufstand + bestätigte Einstellungen**.
- Kein Kontext aus Dateien, die nicht explizit an der Werkbank liegen.
- Kontextfenster werden **begrenzt und dokumentiert**: das Arbeitsstück zeigt, welche Materialteile tatsächlich berücksichtigt wurden.

**6 · Quellenregeln (streng)**
- Jede Kernaussage braucht einen Belegstatus. Ohne Beleg ist sie `?`, nicht wahr.
- **Es ist verboten zu behaupten, Material geprüft zu haben, wenn kein Zugriff stattfand.** Fehlt der Zugriff, lautet der Status `╱ unbelegbar` — und die Leitassistenz sagt das ausdrücklich.
- Zitate werden mit **Datei + Zeile/Hash** angegeben, nie mit "laut Dokumentation".

**7 · Modell-/Routing-Transparenz**
- Auf Nachfrage (`EXPLAIN_RUN`) vollständige Auskunft: Fähigkeit, Modell, Grund, Dauer, Kosten, Ereignisse.
- Unaufgefordert: **nur** bei qualitäts-, kosten-, latenz- oder datenschutzrelevanten Abweichungen.
- Modellwechsel zwischen Versionen eines Arbeitsstücks werden **immer** vermerkt.

**8 · Fehlerregeln**
- Fehler werden in **Klartext + Handlungsoption** übersetzt (Klassen nach 7.5).
- Kein Stacktrace in der Produktoberfläche.
- Kein "Weitermachen als ob": ein fehlgeschlagener Abschnitt bleibt **sichtbar leer**.

**9 · Fallback-Regeln**
- Nur innerhalb der Policy; Klassenwechsel immer gemeldet; Abschnitt bleibt gezielt neu erzeugbar; Protokollpflicht.

**10 · Audit-Regeln**
- Protokolliert werden: alle Runs, alle Routing-Ereignisse, alle bestätigungspflichtigen Aktionen (mit Bestätigungsnachweis), alle Gedächtnis-Operationen, alle Materialzugriffe mit Hash.
- Das Audit ist **nur lesbar, nicht editierbar**, und pro Arbeitsraum exportierbar.

**11 · Rechte- und Sicherheitsgrenzen**
- Repository-Zugriff startet **immer** read-only; Schreiben nur mit Diff, Rechteprüfung und Bestätigung.
- Keine Secrets im Frontend; Secrets nur im Application Layer, bevorzugt nur im Prozessspeicher (`schaltwerk`-Präzedenz).
- Bindung an Loopback für v1 (`schaltwerk`-Präzedenz).
- **Goldene Regeln** (aus `DOKUMENTATION.md` übersetzt): nie in Kategorien/Systeme schreiben, die dem Nutzer gehören, ohne dessen ausdrückliche Freigabe; Erkennungsmarken des Systems nie umbenennen; geprüfte Zustände nie pauschal überschreiben; externe Antworten niemals ungeprüft in die Oberfläche schreiben (`esc()`-Präzedenz).

---

## 9. Vollständiger Benutzerablauf

### 9.1 Der Ablauf in 24 Schritten

| # | Schritt | Sichtbare Reaktion |
| --- | --- | --- |
| 1 | **Leerer Zustand.** Nutzer öffnet einen neuen Arbeitsraum. | Leere Werkbank, gefüllte Materialwand (aus Arbeitsraum-Voreinstellung oder leer mit "+ Material"). Ein Satz, kein Tutorial. |
| 2 | **Erster Einstieg.** Nutzer zieht `server.py` auf die Werkbank. | Materialwand-Eintrag wechselt auf "an der Werkbank"; Stimme: *"server.py · 57 KB · 21 Routen · noch nicht gelesen."* |
| 3 | **Material hinzufügen.** Weitere Dateien: `DOKUMENTATION.md`, `tests/test_server.py`, `CHANGELOG.md`. | Materialwand zeigt Herkunft und Prüfstatus; Hash-Kürzel erscheinen. |
| 4 | **Repository-Content auswählen.** Nutzer markiert einen Ordner; das System inventarisiert nur erlaubte Dateitypen. | Inventar-Liste mit "gelesen/noch nicht gelesen"; ausgeschlossene Typen werden **genannt**, nicht verschwiegen. |
| 5 | **Arbeitsabsicht formulieren.** *"Beurteile, ob die `schaltwerk`-Logik als Hintergrundorchestrierung taugt."* | Die Absicht erscheint **als Titel des Arbeitsstücks**, nicht in einem Chatfeld. |
| 6 | **Interpretation durch die Leitassistenz.** Arbeitsplan: Abschnitte, Fähigkeiten, Schätzung, Vorfragen. | Arbeitsplan erscheint als Vorschau **auf der Werkbank**, Abschnitte sind einzeln abwählbar. |
| 7 | **Korrektur durch den Nutzer.** Streicht Abschnitt "Kopplung", ergänzt Material, verbietet eine Fähigkeit. | Plan aktualisiert sich; das Verbot wird als **Regel** im Arbeitsplan sichtbar (nicht als ausgegraute Option). |
| 8 | **Start.** Knopf trägt Schätzung und Bestätigung. | Status → **laufend**; Werkzeugspur erscheint. |
| 9 | **Parallele Verarbeitung.** Strukturleser und Risikoprüfer laufen gleichzeitig. | Zwei Slots füllen sich; die Stimme meldet **Zwischenstände mit Bedeutung**, keine Token-Statistik. |
| 10 | **Verständliche Aktivitätsanzeige.** | Abschnitte erscheinen nacheinander; jede Kernaussage bekommt sofort ihren Belegstatus. |
| 11 | **Widerspruch erkannt.** | Eine `WIDERSPRICHT`-Kante wird gezeichnet; Fragenleiste ergänzt eine blockierende Frage. |
| 12 | **Fallback.** Risikoprüfer nicht verfügbar. | Bernstein-Karte am betroffenen Abschnitt: *"Nicht verfügbar. Übernommen von … Auswirkung: kürzere Risikoliste."* + *"Erneut versuchen"*. |
| 13 | **Fehler.** Ein Material ist nicht lesbar. | Abschnitt bleibt `╱ unbelegbar`; **keine** Ersatzbehauptung. |
| 14 | **Warten auf Nutzereingabe.** | Status → **wartet**; eine konkrete Frage, kein Modal. |
| 15 | **Nutzer antwortet / ergänzt Material.** | Lauf setzt fort, ohne bereits fertige Abschnitte neu zu erzeugen. |
| 16 | **Abbruch** (optional). | Sofortiger Stopp; Stand als Version `v1 (abgebrochen)` gesichert; Stimme nennt, was gesichert ist. |
| 17 | **Wiederaufnahme.** | Knopf "Weiterarbeiten" lädt Material-Hashes, Abschnittsstände, Budgetverbrauch; geändertes Material wird **markiert**. |
| 18 | **Ergebnis.** | Vollständiges Arbeitsstück mit Abschnitten, Belegstatus, Kanten, Routing-Zusammenfassung. |
| 19 | **Quellenprüfung.** Nutzer klickt einen Beleg an. | Sprung zur Materialstelle (Datei + Zeile/Hash); Kante leuchtet; Kontext bleibt sichtbar. |
| 20 | **Eingriff in das Ergebnis.** Nutzer formuliert einen Abschnitt um. | Abschnitt verliert seinen Belegstatus → `?`; Version vermerkt "bearbeitet". |
| 21 | **Versionierung.** | `v1 (Entwurf)` → `v2 (geprüft)` → `v3 (bearbeitet)`; Versionen bleiben einzeln öffenbar und vergleichbar. |
| 22 | **Speichern / Verlauf.** | Arbeitsstück im Arbeitsraum; Run-Log jederzeit einsehbar (Routing, Kosten, Dauer, Ereignisse). |
| 23 | **Erneute Nutzung.** Nutzer öffnet das Arbeitsstück Wochen später. | Material-Hashes werden geprüft; geändertes Material → Bernstein-Hinweis: *"3 Quellen haben sich geändert. Neu prüfen?"* |
| 24 | **Kontrollierte Übergabe** (später, bestätigt). | `PREPARE_HANDOFF` erzeugt einen **Werkbrief**; jeder Schreibvorschlag (z. B. Code-Änderung) erscheint **als Diff zur Bestätigung**, nie als ausgeführte Änderung. |

### 9.2 Zustandsmaschine eines Runs (verbindlich)

```
                    ┌─────────────────────────────────────────────┐
                    │                                             │
  [LEER] ──Material/Absicht──► [VORBEREITET]                      │
                                    │ starten                     │
                                    ▼                             │
                               [LAUFEND] ◄──── fortsetzen ───┐    │
                                │   │   │                    │    │
              Blockade/Frage ───┘   │   └─── Fehler ───► [FEHLGESCHLAGEN]
                    │               │                        │    │
                    ▼               │ Fallback                │    │
        [WARTET AUF NUTZEREINGABE]  │                    neu starten
                    │               ▼                         │    │
              beantwortet    [FALLBACK AKTIV] ──► zurück LAUFEND  │
                    │                                             │
                    └──────────► [ERFOLGREICH]                   │
                                 oder                             │
                                 [ERFOLGREICH MIT EINSCHRÄNKUNG]  │
                                        │                         │
              abbrechen (aus LAUFEND/WARTEN/FALLBACK)             │
                                        ▼                         │
                                 [ABGEBROCHEN]                    │
                                        │                         │
                                        ▼                         │
                              [WIEDERAUFNEHMBAR] ─────────────────┘
                                        │
                                   archivieren
                                        ▼
                                  [ARCHIVIERT]
```

**Invarianten:**
- Kein Zustand verliert bereits erzeugte Abschnitte.
- `FALLBACK AKTIV` ist **kein** Endzustand, sondern läuft weiter — und ist am Ergebnis **dauerhaft** vermerkt.
- `FEHLGESCHLAGEN` ist nur dann erreichbar, wenn der Lauf **nicht** durch Nutzerentscheidung beendet wurde; Nutzerende heißt immer `ABGEBROCHEN`.
- `ARCHIVIERT` bleibt zitierfähig, aber nicht mehr fortsetzbar.

### 9.3 Proaktivität mit Schwelle (aus dem Wachdienst abgeleitet)

| Ereignis | Meldung? |
| --- | --- |
| Lauf abgeschlossen | Ja (einmal) |
| Neue Blockade entstanden | Ja (sofort) |
| Fallback mit Klassenwechsel | Ja (sofort, am Abschnitt) |
| Material seit letztem Lauf geändert | Ja (beim Wiederbetreten, **maximal ein Hinweis pro Arbeitsraum und Tag**) |
| Frühere Entscheidung durch neues Material berührt | Ja (mit Verweis auf das betroffene Arbeitsstück) |
| Laufender Fortschritt ohne Besonderheit | **Nein** (Anti-Spam-Regel aus `bw_log`) |
| Erfolgreiche Retries | **Nein** |
| Einzelne Routing-Entscheidungen ohne Relevanz | **Nein** |

---

## 10. Zielarchitektur

### 10.1 Schichten

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ FRONTEND  React + TypeScript + Vite                                           │
│   Raum-UI (Materialwand · Werkbank · Ablage · Fragenleiste · Stimme)          │
│   UI-State: explizite Zustandsmaschine (11 Zustände) · SSE-Client · Optimistic │
│   kennt: KEINE Secrets · KEINE Provider · KEINE OmniRoute-URLs                │
└───────────────────────────────┬───────────────────────────────────────────────┘
                                │ REST + SSE (Loopback, v1)
┌───────────────────────────────▼───────────────────────────────────────────────┐
│ APPLICATION LAYER  FastAPI (Python)                                           │
│  ┌──────────────┬──────────────┬───────────────┬──────────────┬────────────┐  │
│  │ Arbeitsraum  │ Material-    │ Leitassistenz │ Orchestrier.-│ Run-Engine │  │
│  │ & Arbeitsst. │ Index        │ (Intent/      │ Policy       │ (SSE,      │  │
│  │ Versionierung│ (read-only)  │  Kontext)     │ (Budget,     │  Abbruch,  │  │
│  │              │              │               │  Klassen,    │  Resume)   │  │
│  │              │              │               │  Grenzen)    │            │  │
│  └──────────────┴──────────────┴───────────────┴───────┬──────┴────────────┘  │
│  ┌──────────────────────┐  ┌───────────────────────┐   │                      │
│  │ Memory (4 Stufen,    │  │ Audit (append-only)   │   │                      │
│  │ sichtbar/löschbar)   │  │ Konfiguration/Secrets │   │                      │
│  └──────────────────────┘  └───────────────────────┘   │                      │
└────────────────────────────────────────────────────────┼──────────────────────┘
                                                         │ RouterPort (Interface)
┌────────────────────────────────────────────────────────▼──────────────────────┐
│ OMNIROUTE ADAPTER   Normalisierung · Zeitlimits · Fehlerklassen · Secrets      │
│   implementiert: RouterPort   →   austauschbar ohne Produktänderung            │
└───────────────────────────────────────────────────────┬───────────────────────┘
                                                        │
┌───────────────────────────────────────────────────────▼───────────────────────┐
│ OMNIROUTE  (Docker, lokal)  ──►  Provider  ──►  Modelle / Fähigkeiten          │
│   verifiziert: Management/Proxy/Provider/Usage · Inferenz: ZU PRÜFEN           │
└───────────────────────────────────────────────────────────────────────────────┘

PERSISTENZ: SQLite (Arbeitsstücke · Versionen · Runs · Material-Index · Memory · Audit)
            Dateisystem: Material-Snapshots (read-only Kopien mit Hash)
OBSERVABILITY: strukturiertes Run-Log · SSE-Events · Routing-Protokoll je Run
```

### 10.2 Architekturprinzipien (verbindlich)

| # | Prinzip |
| --- | --- |
| R1 | Das Frontend kennt **keine** Provider-Secrets und **keine** OmniRoute-Endpunkte. |
| R2 | Das Frontend ruft OmniRoute **nie** direkt auf. |
| R3 | Die Leitassistenz ist eine **Anwendungsrolle**, kein Modell. Sie kann mehrere Fähigkeiten über OmniRoute nutzen. |
| R4 | Repository-Zugriffe starten **immer read-only**. |
| R5 | Schreibzugriffe erfordern **Diff + Rechteprüfung + Bestätigung** — in dieser Reihenfolge. |
| R6 | Jeder Run ist **nachvollziehbar**: Material-Hashes, Fähigkeiten, Modelle, Ereignisse, Kosten, Dauer. |
| R7 | Fallbacks sind **erkennbar**, sobald sie Qualität, Kosten, Datenschutz oder Fähigkeiten beeinflussen. |
| R8 | Memory ist **transparent, begrenzt, korrigierbar und löschbar** — Standard ist die flüchtigste Stufe. |
| R9 | Provider- und Routerdetails sind **hinter einem Port austauschbar**, ohne das Produktmodell zu berühren. |
| R10 | Bestehende Repository-Funktionalität (`schaltwerk`) wird **nicht** verändert; Änderungen an gemeinsam genutzten Mustern nur mit Schutztests. |
| R11 | Externe Antworten werden **niemals ungeprüft** in die Oberfläche geschrieben (`esc()`-Präzedenz). |
| R12 | Ein Lauf endet **nie** mit einer Behauptung, die nicht belegt, als offen markiert oder als unbelegbar gekennzeichnet ist. |
| R13 | Kein Secret verlässt den Prozessspeicher in eine Datei, solange es nicht ausdrücklich gewünscht ist (`schaltwerk`-Präzedenz). |
| R14 | Die Anwendung bindet in v1 an **Loopback**. |

### 10.3 Der Router-Port (Schnittstelle, die R9 trägt)

Die Anwendung kennt **nur** dieses Interface. Alles OmniRoute-Spezifische liegt dahinter. (Details in Abschnitt 14.1.)

```
Frontend → Application Layer → Leitassistenz → Policy → RouterPort → [OmniRouteAdapter]
                                                                    → [DirectProviderAdapter] (Notbetrieb)
                                                                    → [MockAdapter] (Tests, offline)
```

**Warum drei Implementierungen?** Weil der **Capability-Probe** (Abschnitt 12.4) negativ ausgehen kann. Ein Mock-Adapter erlaubt außerdem die 34-Tests-Philosophie von `schaltwerk`: Tests ohne Netz und ohne OmniRoute.

### 10.4 Stack-Entscheidung (VORSCHLAG mit Begründung, eine offene Frage)

| Schicht | Entscheidung | Begründung | Alternative (ZU PRÜFEN) |
| --- | --- | --- | --- |
| App-Layer | **Python + FastAPI** | Im Repo vorhanden und erprobt (`schaltwerk`: Pydantic, `StreamingResponse`, asyncio-Loops, httpx). Nachbarschaft zum OmniRoute-Tooling. Schlank: 4 Abhängigkeiten. | Node + TypeScript (bessere LibreChat-Code-Wiederverwendung) |
| Persistenz | **SQLite** | Lokal, dateibasiert, versionierbar, keine Cluster-Infrastruktur. | Postgres erst bei Mehrbenutzer |
| Frontend | **React + TypeScript + Vite**, **keine** UI-Library, **kein** State-Framework | MashAI zeigt den Stack; LibreChat zeigt, wohin 102 Abhängigkeiten führen. Unsere 11-Zustände-Maschine braucht kein recoil/jotai. | Vanilla-Einzeldatei (`schaltwerk`-Stil) — zu arm für das Raummodell |
| Transport | **SSE** (+ REST) | In `schaltwerk` bereits real; Rückkanal ist normales HTTP. | WebSocket nicht nötig |
| Tests | **pytest** (Backend) + **Vitest** (Frontend) | Entspricht beiden Repo-Präzedenzen (34 bzw. 66 Tests) | — |

**Offene Entscheidung (ZU PRÜFEN, bewusst noch nicht getroffen):** Ob die Leitassistenz-Logik in Python oder gegen ein Node-Subsystem implementiert wird, hängt davon ab, ob später LibreChat-Code **direkt** übernommen werden soll. Für v1 (LibreChat = Referenz) ist Python konsistent. Siehe Abschnitt 16, "Welche Entscheidung noch nicht getroffen werden darf".

---

## 11. Technische Beispiele

> **Alle Codeblöcke in diesem Abschnitt sind VORSCHLAG.**
> OmniRoute-Blöcke tragen zusätzlich: **PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX**.
> Verifiziert ist ausschließlich die Verwaltungsebene aus Abschnitt 1.5.

### 11.1 Router-Port-Interface (PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX)

```python
# VORSCHLAG. Die Anwendung kennt nur dieses Interface.
class RouterPort(Protocol):
    def capabilities(self) -> list[Capability]:
        """Welche Fähigkeiten bietet die Installation real an?"""

    async def invoke(
        self,
        capability: Capability,
        payload: InvocationPayload,      # Material-Auszüge, Aufgabe, Grenzen
        *,
        quality_class: QualityClass,     # Zielklasse der Policy
        budget: BudgetLimit,             # max_tokens / max_cost / max_latency_ms
        on_event,                        # Callback: Stream-Ereignisse
        cancel: asyncio.Event,
    ) -> InvocationResult: ...

    async def abort(self, invocation_id: str) -> None: ...

@dataclass(frozen=True)
class InvocationResult:
    text: str
    model_used: str
    provider_used: str | None
    quality_class_achieved: QualityClass
    events: list[RoutingEvent]          # inkl. Fallback-Ereignisse
    usage: Usage                        # tokens, kosten, dauer
    raw_response_shape: str             # für MALFORMED_RESPONSE-Diagnose
```

**Wichtig:** `capabilities()` ist kein Wunschzettel. Es ist eine **Laufzeitabfrage an die reale Installation**. Behauptet die Policy eine Fähigkeit, die `capabilities()` nicht liefert, entsteht `CAPABILITY_MISSING` — und **kein** stiller Ersatz.

### 11.2 OmniRoute-Adapter (PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX)

```python
# PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX
# Der gezeigte Request-Pfad ist eine ANNAHME. Verifiziert sind nur die
# Verwaltungsendpunkte aus Abschnitt 1.5. Vor Implementierung: Capability-Probe.

class OmniRouteAdapter(RouterPort):
    def __init__(self, base_url: str, api_key: str, *, client: httpx.AsyncClient):
        self._base = base_url.rstrip("/")
        self._key = api_key                     # NUR im Prozessspeicher (R13)
        self._client = client

    def _headers(self) -> dict[str, str]:
        # BEKANNT: schaltwerk setzt BEIDE Header. Für Inferenz ZU PRÜFEN.
        return {"Authorization": f"Bearer {self._key}",
                "x-api-key": self._key,
                "Content-Type": "application/json"}

    async def invoke(self, capability, payload, *, quality_class, budget, on_event, cancel):
        model = self._select_model(capability, quality_class)
        body = {
            "model": model,
            "messages": payload.as_messages(),
            "stream": True,
            "max_tokens": budget.max_tokens,
        }
        # PSEUDOCODE: exakter Pfad/Format NICHT verifiziert.
        async with self._client.stream(
            "POST", f"{self._base}/v1/chat/completions",
            json=body, headers=self._headers(), timeout=budget.max_latency_ms / 1000,
        ) as resp:
            if resp.status_code == 401:
                raise RouterError(ErrorClass.AUTH_INVALID)      # kein Fallback
            if resp.status_code == 429:
                raise RouterError(ErrorClass.RATE_LIMITED)
            if resp.status_code >= 500:
                raise RouterError(ErrorClass.UNAVAILABLE)
            async for line in resp.aiter_lines():
                if cancel.is_set():
                    raise RouterError(ErrorClass.ABORTED)
                if not line.startswith("data: "):
                    continue
                chunk = self._parse_chunk(line)                 # defensiv!
                if chunk is None:
                    raise RouterError(ErrorClass.MALFORMED_RESPONSE)
                on_event(chunk)

    def _parse_chunk(self, line: str) -> dict | None:
        # PRÄZEDENZ aus schaltwerk: `unwrap_list()` normalisiert inkonsistente
        # OmniRoute-Formate (nacktes Array statt Objekt). Dieselbe Defensive hier.
        raw = line.removeprefix("data: ").strip()
        if raw in ("[DONE]", ""):
            return None
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return None
        if isinstance(data, list):                 # OmniRoute liefert teils Listen
            data = {"choices": data}
        return normalize_chunk(data)
```

### 11.3 Datenmodelle (VORSCHLAG — produktbezogen, von keiner OmniRoute-Struktur abhängig)

```python
# Arbeitsstück
@dataclass
class Workpiece:
    id: str
    workspace_id: str
    title: str                       # = die Absicht des Nutzers
    intent: IntentType
    sections: list[Section]          # geordnet, bearbeitbar
    relations: list[Relation]        # STÜTZT / WIDERSPRICHT / BLOCKIERT / ENTSTAND_AUS
    open_questions: list[Question]   # blockierend oder notiert
    versions: list[VersionRef]
    status: WorkpieceStatus
    quality_note: str | None         # „mit Fähigkeit unter Zielklasse erzeugt"

@dataclass
class Section:
    id: str
    heading: str
    text: str
    evidence: EvidenceStatus         # BELEGT | TEILWEISE | OFFEN | WIDERSPROCHEN | UNBELEGBAR
    citations: list[Citation]        # material_id + zeile/hash
    produced_by: Provenance          # fähigkeit, modell, qualitätsklasse, lauf_id
    edited_by_user: bool             # Wahrheit: Nutzer hat eingegriffen

# Materialreferenz (Repository-Content, Dateien, Notizen, frühere Arbeitsstücke)
@dataclass
class MaterialRef:
    id: str
    workspace_id: str
    kind: Literal["repo_file", "note", "workpiece", "source", "task", "decision"]
    origin: str                      # Pfad/URL/ID
    content_hash: str                # SHA-256 des Inhalts → Änderungserkennung
    byte_size: int
    read_state: Literal["read", "unread", "changed_since_last_run"]
    excerpt_policy: str              # wie viel davon in den Kontext darf
    license_note: str | None         # z. B. „MPL-2.0 · nur als Material, kein Code-Import"

# Run
@dataclass
class Run:
    id: str
    workpiece_id: str
    status: RunStatus                # 11 Zustände, siehe 9.2
    plan: Plan
    steps: list[RunStep]             # je Abschnitt: fähigkeit, modell, status, dauer
    routing_events: list[RoutingEvent]
    budget: BudgetLimit
    budget_used: BudgetUsed
    material_hashes: dict[str, str]  # Material → Hash zum Zeitpunkt des Laufs
    resume_point: str | None         # letzter abgeschlossener Abschnitt
    started_at: str
    ended_at: str | None
```

### 11.4 Event-/Statusmodell (SSE)

```jsonc
// VORSCHLAG — SSE-Event, das die UI konsumiert (kein OmniRoute-Format!)
{"type":"run.status",     "run_id":"r_01", "status":"running", "step":"risks"}
{"type":"section.draft",  "run_id":"r_01", "section_id":"s3", "text":"…", "evidence":"offen"}
{"type":"relation.added", "run_id":"r_01", "kind":"widerspricht",
 "from":"material:DOKUMENTATION.md#L201", "to":"section:s2"}
{"type":"question.added", "run_id":"r_01", "question_id":"q1",
 "text":"Ist Port 24615 dauerhaft?", "blocking":true}
{"type":"routing.fallback", "run_id":"r_01",
 "from_capability":"risk_reviewer", "to_model":"…",
 "quality_class_before":"high", "quality_class_after":"medium",
 "reason":"UNAVAILABLE", "impact":"kürzere Risikoliste",
 "retryable":true}
{"type":"budget.warning", "run_id":"r_01", "used_pct":80}
{"type":"run.status",     "run_id":"r_01", "status":"waiting_for_user"}
{"type":"run.status",     "run_id":"r_01", "status":"succeeded_with_limits"}
```

**Regel:** Die UI abonniert **Bedeutungsereignisse**, keine Tokenströme. Tokens fließen intern; nach außen nur Zustandswechsel, die eine Handlung rechtfertigen.

### 11.5 Frontend-State (VORSCHLAG)

```ts
// VORSCHLAG. Kein globales State-Framework nötig — die Zustandsmaschine ist der State.
type RunStatus =
  | 'empty' | 'prepared' | 'running' | 'waiting_for_user'
  | 'succeeded' | 'succeeded_with_limits' | 'fallback_active'
  | 'failed' | 'aborted' | 'resumable' | 'archived';

type AtelierState = {
  workspaceId: string;
  material: MaterialRef[];          // Materialwand
  onBench: string[];                // Material an der Werkbank
  workpiece: Workpiece | null;      // Werkbank
  run: { status: RunStatus; steps: StepState[]; activeCapabilities: string[] } | null;
  questions: Question[];            // Fragenleiste (blockierend zuerst)
  voice: { lastAction: string; at: string } | null;   // Stimme (eine Zeile)
  workshopReportOpen: boolean;      // Routing nur auf Verlangen/bei Relevanz
};
```

### 11.6 Berechtigungs- und Schreibprüfung (VORSCHLAG)

```python
# VORSCHLAG — eine Grenze, drei Stufen (R5)
async def apply_change(change: Change, ctx: UserContext, repo: RepoAccess) -> ApplyResult:
    diff = repo.preview(change)                       # 1 · Diff VOR jeder Aktion
    if not permissions.may_write(ctx, change.target): # 2 · Rechteprüfung
        raise PolicyVeto("keine Schreibrechte für dieses Ziel")
    if change.affects_foreign_owned(                  # Goldene Regel aus schaltwerk:
        marker=("proxy-exchange", "px-")):            # fremdes Eigentum nie anfassen
        raise PolicyVeto("Ziel gehört einem anderen System/Nutzer")
    confirmation = await request_confirmation(diff)   # 3 · Bestätigung mit Diff
    if not confirmation.approved:
        return ApplyResult(status="aborted", diff=diff)
    return repo.commit(change, audit=ctx.audit_entry())
```

### 11.7 Repository-Read-only-Zugriff (VORSCHLAG)

```python
# VORSCHLAG. Immer read-only, immer mit Hash, immer mit Auswahlregel.
ALLOWED_SUFFIXES = {".py", ".md", ".txt", ".json", ".yaml", ".yml", ".ts", ".tsx", ".js", ".css", ".html"}
DENIED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "dist", "build", "release"}

def inventory(root: Path) -> list[MaterialRef]:
    refs, skipped = [], []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if any(part in DENIED_DIRS for part in p.parts):
            skipped.append(str(p)); continue          # wird GENANNT, nicht verschwiegen
        if p.suffix not in ALLOWED_SUFFIXES:
            skipped.append(str(p)); continue
        data = p.read_bytes()
        refs.append(MaterialRef(
            kind="repo_file", origin=str(p),
            content_hash=hashlib.sha256(data).hexdigest(),
            byte_size=len(data), read_state="unread", excerpt_policy="auto"))
    return refs
```

### 11.8 Gespeicherte Ergebnisversion (VORSCHLAG)

```jsonc
{
  "workpiece_id": "w_17",
  "version": 3,
  "status": "succeeded_with_limits",
  "title": "Beurteilung: schaltwerk als Hintergrundorchestrierung",
  "sections": [
    { "id": "s1", "heading": "Kernaussage",
      "evidence": "belegt",
      "produced_by": { "capability": "synthesizer", "model": "…",
                       "quality_class": "high", "run_id": "r_01" },
      "edited_by_user": false },
    { "id": "s4", "heading": "Risiken",
      "evidence": "teilweise",
      "produced_by": { "capability": "risk_reviewer", "model": "…",
                       "quality_class": "medium",     // FALLBACK
                       "run_id": "r_01" },
      "fallback": { "reason": "UNAVAILABLE", "retryable": true },
      "edited_by_user": false }
  ],
  "quality_note": "Abschnitt 'Risiken' unter Zielklasse erzeugt.",
  "material_hashes": { "m_01": "9f2c…", "m_02": "41ab…" },
  "budget_used": { "tokens": 18420, "cost_estimate": null, "duration_ms": 51300 },
  "created_at": "2026-10-02T18:44:12Z"
}
```

---

# TEIL V — UMSETZUNG

## 12. Entwicklungsstrategie (Phasen 1–9)

### 12.1 Phase 1 — Repository Discovery (abgeschlossen, nachführbar)

**Geleistet:** Vollständige Inventarisierung (12 Dateien, 38 MB), Lektüre aller 10 `schaltwerk`-Dateien, Stichproben-Analyse beider ZIPs (Struktur, Lizenzen, Versionen, Schlüsselmodule), Prüfung aller OmniRoute-Belege im Code.

**Dokumentierte Befunde:** Abschnitte 1.1–1.6 dieses Dokuments, insbesondere die **Prämissen-Korrektur** (kein Node-Editor; MashAI ≠ Memory-System; OmniRoute-Inferenz unbelegt; `schaltwerk` ohne Lizenzdatei).

**Sichtbar gewordene Risiken:**
1. **OmniRoute-Inferenz-API unbelegt** (höchstes Risiko — entscheidet über den Motor).
2. **OmniRoute liefert inkonsistente Antwortformate** (nacktes Array belegt) → Adapter muss defensiv sein.
3. **`schaltwerk` hat keine Lizenzdatei** → Code-Kopie rechtlich ungeklärt; nur Muster übernehmen.
4. **MashAI ist MPL-2.0** → keine Datei-Kopie; Assets tabu.
5. **Drei OmniRoute-Container, einer mit Port-Mapping, API-Key muss nach Neustart neu eingetragen werden** → Instabilität der Umgebung einplanen.
6. **Windows-Fokus der dokumentierten Umgebung** vs. hier verfügbares Linux → Cross-Platform von Anfang an.

**Preservation Contract:** Abschnitt 4.2 — mit der zentralen Regel: **`schaltwerk` unangetastet.**

**Regressionstests (vor jeder Änderung an gemeinsam genutzten Mustern):**
```bash
cd schaltwerk && pip install -r requirements-dev.txt && pytest tests/   # 34 Tests, offline
```

### 12.2 Phase 2 — Produktdefinition

| Festlegung | Entscheidung |
| --- | --- |
| Erste Zielgruppe | Der **Technik-Entscheider mit eigenem KI-Setup** — eine Person, die OmniRoute, Repos und Agenten selbst betreibt und belastbare Entscheidungen braucht (kein Team, kein Enterprise). |
| Wichtigste Nutzerhandlung | **Beurteilen**: Material + Frage → Arbeitsstück mit Belegstatus. |
| Erstes Arbeitsstück | *"Beurteilung: Kann `schaltwerk` als Hintergrundorchestrierung dienen?"* — weil das Material real, vollständig und im Repo vorhanden ist. |
| Erste Materialtypen | `repo_file` · `note` · `workpiece` (früheres Arbeitsstück). Später: `source`, `task`, `decision`. |
| Erste Intent-Typen | `ASSESS_QUESTION` · `ANALYZE_MATERIAL` · `CONTINUE_WORKPIECE` · `EXPLAIN_RUN`. |
| Grenzen der Leitassistenz | Abschnitt 8.4 verbindlich; nichts außerhalb der 8 Intent-Typen. |
| Datenschutz-/Memory-Regeln | 4 Stufen, Standard `SESSION`; Gedächtnis-Register Pflicht; harte Löschung. |
| Zustandsmaschine | 11 Zustände nach 9.2, inkl. Invarianten. |

### 12.3 Phase 3 — UX-Prototyp (mit simulierten Events)

**Was simuliert wird:** alle SSE-Ereignisse aus 11.4, erzeugt von einem `MockAdapter` — **kein** Netz, **keine** OmniRoute.

**Klickbar sein müssen:**
- Leerer Raum → Material an die Werkbank ziehen → Absicht formulieren.
- Arbeitsplan anzeigen, Abschnitt abwählen, Fähigkeit verbieten.
- Lauf starten; Werkzeugspur und wachsende Abschnitte.
- **Fallback-Karte** (bewusst auslösbar).
- **Blockierende Frage** (Zustand `waiting_for_user`) und Beantwortung.
- Abbruch → `aborted` → Wiederaufnahme aus `resumable`.
- Quellenprüfung: Beleg anklicken → Sprung ins Material.
- Eingriff in einen Abschnitt → Belegstatus fällt auf `?` → Version `bearbeitet`.
- Gedächtnis-Register: Eintrag ansehen, korrigieren, löschen.

**Wie geprüft wird, dass es kein Dashboard geworden ist — fünf Fragen an den Prototyp:**
1. Gibt es eine Fläche, auf der **ein zusammenhängendes Dokument** steht? (Nein → falsch.)
2. Erscheinen Zahlen **im Satz** statt in Kästchen? (Nein → falsch.)
3. Ist die **Fragenleiste** wichtiger als jede Kennzahl? (Nein → falsch.)
4. Kann der Nutzer eine beliebige Aussage **bis zur Quelle** zurückverfolgen? (Nein → falsch.)
5. Sieht man **keine** Infrastruktur, solange sie nicht relevant ist? (Doch → falsch.)

### 12.4 Phase 4 — OmniRoute-Integration

**Zuerst angebunden wird:** nicht das Routing, sondern die **Fähigkeitsfeststellung**.

```
Schritt 1 · Capability-Probe (read-only, dokumentiert)
   a) Welche Endpunkte antworten?  (z. B. GET /v1/models, GET /api/models, /health, /api/health)
   b) Ist ein Inferenz-Endpunkt erreichbar?  (PSEUDOCODE-Pfad aus 11.2 testen)
   c) Antwortformat und Streaming-Verhalten notieren (SSE? Chunk-Format?)
   d) Authentifizierung verifizieren (Bearer / x-api-key / anderes)
   e) Fehlerverhalten bei 401/404/429/5xx bestimmen → Fehlerklassen-Mapping
   f) Falls kein Inferenz-Endpunkt: **Stopp** und Rückweg zum Product Owner
      (Notbetrieb: DirectProviderAdapter gegen einen der 7 Provider, oder Mock für Demo)

Schritt 2 · Erster realer Aufruf
   Eine Fähigkeit, ein Modell, ein kurzer Material-Auszug, kein Streaming-Rauschen:
   Ziel ist ein belastbarer Beleg, dass Inferenz über OmniRoute funktioniert.

Schritt 3 · Streaming, Fehler, Fallback, Events
   Erst wenn Schritt 2 stabil ist: Streaming → Fehlerklassen → Fallback → Events.
```

**Adapter-Vertrag (was die Anwendung braucht):** genau `RouterPort` (11.1) — `capabilities()`, `invoke()`, `abort()`. Mehr nicht.

**Secrets:** Schlüssel nur im Application Layer, bevorzugt **Prozessspeicher** (`schaltwerk`-Präzedenz), optional aus einer vom Nutzer gewählten Datei mit restriktiven Rechten; **nie** im Frontend, **nie** in Logs (Maskierung), **nie** in der Datenbank.

### 12.5 Phase 5 — LibreChat-Reuse

| Zu prüfen | Ziel der Prüfung | Voraussichtliches Ergebnis |
| --- | --- | --- |
| `memory.ts` + `memories.js` | Memory-Semantik, Opt-out, Partitionslogik | **Konzept übernehmen**, SQLite-Implementierung |
| `message.ts` (`parentMessageId`) | Versions-/Alternativenmodell | **Konzept übernehmen** |
| `files/citations.ts` | Zitatverknüpfung | **Konzept übernehmen** |
| `stream/` (JobManager, Approval, Checkpoints) | Run-Lebenszyklus-Begriffe | **Begriffe übernehmen**, keine Implementierung |
| `endpoints.custom` (YAML-Form) | Adapter-Konfigurationsform | **Form übernehmen**, wenn Inferenz verifiziert |
| `auditLog.ts`, `toolCall.ts` | Audit- und Werkzeugprotokoll | **Konzept übernehmen** |
| Frontend/UI | — | **Nicht übernehmen** (Aufgabe verbietet es) |
| Mongo/Mongoose-Schemas | — | **Nicht übernehmen** |

**Wie UI- und Datenmodellkopplung vermieden wird:** LibreChat wird **nie als Abhängigkeit eingebunden**, sondern als **Lesequelle**. Es gibt keine Imports, keine gemeinsame Datenbank, keine gemeinsamen Typen. Übernommen werden **Ideen, Feldnamen und Reihenfolgen** — dokumentiert in einem Reuse-Protokoll (`docs/REUSE.md`), damit die Herkunft nachvollziehbar bleibt (MPL-/MIT-Kontext sauber getrennt).

### 12.6 Phase 6 — Erster End-to-End-Vertikalschnitt

| Element | Konkrete Festlegung |
| --- | --- |
| Ein Nutzer | der Betreiber selbst, lokal, Loopback |
| Ein Arbeitsstück | *"Beurteilung: `schaltwerk` als Hintergrundorchestrierung"* |
| Material aus dem Repository | `server.py` (Auszug), `DOKUMENTATION.md`, `tests/test_server.py`, `CHANGELOG.md`, `WEITERARBEITEN.txt` (Auszug) |
| Leitassistenz-Interpretation | Arbeitsplan mit 4 Abschnitten, 2 Fähigkeiten, 1 Vorfrage |
| Ein realer OmniRoute-Run | Strukturleser + Risikoprüfer, falls Capability-Probe positiv |
| Ein gespeichertes Ergebnis | Arbeitsstück v1 in SQLite, mit Belegstatus, Kanten, Routing-Protokoll |
| Ein sichtbarer Fallback-Test | Fähigkeit gezielt unerreichbar machen (z. B. falsches Modell) → Fallback-Karte muss erscheinen, Qualitätsvermerk muss in der Version stehen |
| Ein Abbruch- und Wiederaufnahme-Test | Abbruch bei 50 % → `resumable` → Fortsetzung ohne Neuerzeugung fertiger Abschnitte |

**Abnahmekriterium des Vertikalschnitts:** Das Arbeitsstück ist **zitierfähig** — eine dritte Person kann jede Kernaussage bis zu einer Stelle im Material zurückverfolgen, ohne die App zu kennen.

### 12.7 Phase 7 — Visuelle Ausarbeitung

Erst nach funktionierendem Kernfluss. Reihenfolge:
1. **Raum und Typografie** (Serif für das Werkstück, Mono für Daten) — der anti-chatbotische Kern.
2. **Belegstatus-Zeichen** — das Qualitätssystem.
3. **Werkzeugspur und Bewegung** — Fortschritt ohne Spinner.
4. **Fallback- und Fehlerdarstellung** — die ehrlichsten Bildschirme des Produkts.
5. **Farbe** — Statusfarben auf das Minimum reduzieren, Bernstein nur für Aufmerksamkeit.
6. **Accessibility** — Kontrastmessung (insbesondere `--muted` auf `--bg`), Tastaturpfade, Reduced-Motion, Screenreader-Texte für Kanten.
7. **Responsiv** — Werkbank-zuerst, Registerkarten unter 1024 px.

### 12.8 Phase 8 — Robustheit

| Thema | Festlegung |
| --- | --- |
| Fehlerklassen | 9 Klassen nach 7.5, verbindliches Mapping im Adapter |
| Timeouts | **pro Teilschritt** (Vorbild `probe_one`), Gesamtlauf als Obergrenze, hart |
| Retry-Regeln | max. 2 Versuche, exponentielles Backoff, **nur** bei `TIMEOUT`, `RATE_LIMITED`, `MALFORMED_RESPONSE` — **nie** bei `AUTH_INVALID`, `BUDGET_EXCEEDED`, `POLICY_VETO` |
| Fallback-Regeln | nach 7.4; Klassenwechsel immer gemeldet; gezielte Neuerzeugung |
| Kostenlimits | vor dem Lauf sichtbar und einstellbar; Warnung bei 80 %; Stopp bei 100 % |
| Latenzlimits | pro Fähigkeit konfigurierbar; Überschreitung → `TIMEOUT`, nicht Endlosschleife |
| Datenintegrität | Material-Hashes bei jedem Lauf; geändertes Material → Hinweis, kein stilles Weiterarbeiten |
| Versionierung | Versionen append-only; keine Version wird überschrieben; Bearbeitung erzeugt neue Version |
| Audit | append-only; bestätigungspflichtige Aktionen nur mit Bestätigungsnachweis |
| Berechtigungen | eine Grenze (Schreiben), drei Stufen (Diff, Rechte, Bestätigung) |
| Datenschutz | Memory 4 Stufen, Standard flüchtig; harte Löschung; kein Secret auf Disk ohne Wunsch |
| Observability | strukturiertes Run-Log, Routing-Protokoll je Run, SSE-Ereignisse, keine Personen-Telemetrie |

### 12.9 Phase 9 — Verifikation

| Behauptung | Nachweis |
| --- | --- |
| Die App funktioniert | End-to-End-Lauf in Phase 6 mit echtem Material; Screenshots/Transkript |
| **OmniRoute wird tatsächlich verwendet** | Run-Log zeigt `provider_used`/Endpoint; zusätzlich **Abgleich mit `/api/usage/proxy-logs`** (BEKANNT verfügbar!) — die Telemetrie der echten Installation beweist den Aufruf *unabhängig von unserer eigenen Protokollierung* |
| Modellrouting funktioniert | Zwei Fähigkeiten mit **nachweislich unterschiedlichen Modellen**; Routing-Protokoll je Run |
| Fallbacks funktionieren | Gezielter Ausfalltest; Fallback-Karte + Qualitätsvermerk in der Version |
| Fehler werden korrekt dargestellt | Test je Fehlerklasse (9 Stück) mit erwarteter UI-Reaktion |
| Abbruch und Wiederaufnahme funktionieren | Abbruchtest bei 50 %; Fortsetzung ohne Neuerzeugung; Budgetverbrauch stimmt |
| Arbeitsstücke bleiben konsistent | Versionstest: 10 Zyklen aus Bearbeiten/Versionieren, Hash-Prüfung |
| Memory bleibt transparent | Register zeigt jeden Eintrag mit Herkunft; Löschung ist hart und auditiert; Test: nach "Alles vergessen" ist die Tabelle leer |
| Repository-Content wird nicht beschädigt | **Vorher/Nachher-Hash-Vergleich des gesamten Materialbaums**; `git status` in `schaltwerk` bleibt leer; die 34 Tests bleiben grün |
| Bestehende Funktionalität bleibt intakt | `pytest schaltwerk/tests/` vor und nach jeder Phase |
| LibreChat wurde nur sinnvoll übernommen | `docs/REUSE.md` führt jede Übernahme mit Quelle, Lizenz und Grund |

---

## 13. MVP

### 13.1 MVP-These (ein Satz)

> Aus mindestens einer realen Repository-Datei und einer formulierten Absicht erzeugt die Leitassistenz über OmniRoute ein **Arbeitsstück mit Belegstatus je Kernaussage**, das der Nutzer bearbeiten, versionieren und speichern kann — **und bei dem ein Fallback sichtbar wird, nicht verschwindet.**

### 13.2 Was das MVP enthält

| Bereich | Minimum |
| --- | --- |
| **Screens** | (1) Arbeitsraum mit Materialwand + Werkbank, (2) Arbeitsplan-Vorschau, (3) Lauf-Ansicht mit Werkzeugspur + Fragenleiste, (4) Arbeitsstück-Ansicht mit Belegstatus + Quellenprüfung, (5) Versions-/Ablage-Leiste, (6) Gedächtnis-Register, (7) Werkstattbericht (aufklappbar) |
| **Nutzerinteraktionen** | Material auswählen · Absicht formulieren · Arbeitsplan bestätigen/korrigieren · Lauf starten · Frage beantworten · Fallback akzeptieren oder neu versuchen · Abschnitt bearbeiten · versionieren · bestätigen (Schreiben/Export) · Gedächtnis ansehen/löschen |
| **Materialtypen** | `repo_file`, `note`, `workpiece` |
| **Leitassistenz-Fähigkeiten** | `ASSESS_QUESTION`, `ANALYZE_MATERIAL`, `CONTINUE_WORKPIECE`, `EXPLAIN_RUN` — mit Arbeitsplan, Belegstatus, Kanten (STÜTZT/WIDERSPRICHT/BLOCKIERT), Blockaden benennen |
| **Backend** | FastAPI: Arbeitsraum-, Material-, Arbeitsstück-, Run- und Memory-Endpunkte; SSE; SQLite; Audit; `MockAdapter` |
| **Persistenz** | SQLite: Arbeitsräume, Material-Index (mit Hash), Arbeitsstücke + Versionen, Runs + Routing-Ereignisse, Memory, Audit |
| **OmniRoute-Integration** | **Eine** Inferenz-Fähigkeit über den Adapter, **plus** eine zweite für den Parallel- und Fallback-Test. Streaming, wenn verfügbar; sonst Block-Antwort mit Status-Events |
| **Fallback-Integration** | Eine Fallback-Regel (Klassenwechsel → Karte + Qualitätsvermerk + gezielte Neuerzeugung) |
| **Event-/Statusanzeige** | Die 11 Zustände + die SSE-Ereignisse aus 11.4 |
| **Sicherheit/Bestätigung** | Loopback-Bindung · kein Secret im Frontend · read-only Repo-Zugriff · Bestätigung bei Schreiben/Export/Gedächtnis · `esc()`-Präzedenz für alle fremden Inhalte |
| **Testfälle** | Material-Inventar (Suffix/Verzeichnis-Regeln, Hash-Änderung) · Arbeitsplan-Korrektur · Belegstatus-Setzung · `╱ unbelegbar` bei fehlendem Zugriff · Fallback → Karte + Vermerk · alle 9 Fehlerklassen · Abbruch → `resumable` → Resume · Versionskonsistenz · Memory CRUD + harte Löschung · **34 `schaltwerk`-Tests bleiben grün** · Repo-Hash-Vergleich vor/nach |

### 13.3 Ausdrücklich NICHT in Version 1

| Nicht in v1 | Warum |
| --- | --- |
| Frei verdrahtbarer Node-Editor | Das Produkt zeigt Bedeutung, nicht Infrastruktur. (Und: es gibt im Repo keine Node-Logik, die man retten müsste.) |
| Vollständiges OmniRoute-Admin-Dashboard | `schaltwerk` deckt die Verwaltungsebene bereits ab; Doppelung zerstört die Eigenständigkeit. |
| Vollständige LibreChat-UI | Explizit verboten; außerdem 102 Abhängigkeiten. |
| Autonome Agentenschwärme | Widerspricht dem Bestätigungsprinzip; kein Produktbezug in v1. |
| Automatische Repository-Schreibzugriffe | R5: Diff + Rechte + Bestätigung. Schreibvorschläge ja, Ausführung nein. |
| Automatische Deployments | Nie ohne Nutzer, nie still. |
| Uneingeschränkte Web-Recherche | Zerstört die Belegkette; später als **markierte** Quellenart. |
| Komplexe Multi-User-Kollaboration | Single-User ist die ehrliche v1-Grenze. |
| Bild-, Video- oder Audioproduktion | Kein Materialtyp in v1; multimodal erst nach Capability-Probe. |
| Großer MCP-Marktplatz | Fähigkeiten sind im MVP fest im Katalog, nicht dynamisch verdrahtbar. |
| Langfristiges persönliches Memory ohne Kontrolloberfläche | Verboten durch Aufgabenstellung; es gibt nur Memory **mit** Register. |
| Electron-Desktop-App | Web auf Loopback genügt; MashAI-Electron später prüfbar (**ZU PRÜFEN**). |
| Proxy-Logistik im Atelier | `schaltwerk` bleibt das Werkzeug dafür — **NICHT ANFASSEN**. |
| RAG/pgvector/Meilisearch | Materialmengen in v1 rechtfertigen keinen Vektorstack. |

---

## 14. Erweiterbarkeit

Jede Erweiterung: **wie sie passt · was sie ermöglicht · welches Risiko entsteht · welche Regel sie braucht · warum sie kein beliebiges Feature wird.**

| Erweiterung | Passt ins Grundmodell als | Neue Fähigkeit | Risiko | Erforderliche Regel |
| --- | --- | --- | --- | --- |
| Weitere Modelle | Eintrag im Fähigkeitskatalog mit Qualitätsklasse | bessere/andere Urteile | Klassenverwaltung wird unübersichtlich | Katalog gepflegt, Klasse immer angegeben |
| Weitere Provider | neue `RouterPort`-Implementierung oder Providerwechsel in OmniRoute | Ausfallsicherheit | Datenschutzwechsel | Providerwechsel über eine **Datenschutzgrenze** = bestätigungspflichtig |
| Lokale Modelle | zweite Adapter-Implementierung | Offline-Betrieb, Datenschutz | Qualitätsschwankung | eigene Qualitätsklasse; Fallback dorthin **immer** sichtbar |
| Spezialisierte Modelle (Code, Recht, …) | Fähigkeit mit engerem Zweck | präzisere Belege | Falsche Sicherheit | Belegstatus bleibt Pflicht, auch bei Spezialmodellen |
| Multimodale Verarbeitung | neue Materialtypen (`image`, `audio`, `video`) | Materialvielfalt | Belegkette reißt (Bild ≠ zitierbare Zeile) | Zitatpflicht durch **Ausschnitt + Hash** statt Zeile; `╱ unbelegbar` bleibt möglich |
| Web-Recherche | neue Materialart `source` mit Herkunft und Datum | externe Belege | Vergänglichkeit, Vertrauenswürdigkeit | Datum + URL Pflicht; Status "extern, nicht stabil"; nie alleinige Stütze einer Kernaussage |
| Agenten/Tools | Fähigkeiten, die **Zugriff** statt Text liefern | belegbare Prüfung statt Behauptung | Nebenwirkungen | Tools nur read-only in v1+; schreibende Tools = bestätigungspflichtig |
| MCP | dynamischer Fähigkeitskatalog | Anschluss an fremde Systeme | fremde Daten im Kontext | jede MCP-Quelle als Material mit Hash und Lizenznotiz; kein stiller Kontext |
| A2A | Übergabe an andere Agenten | Arbeitsteilung | Kontrollverlust | nur über `PREPARE_HANDOFF` + Bestätigung; Ergebnis zurück als Material |
| Repository-Analyse **tiefer** | erweiterter Material-Index (Symbole, Abhängigkeiten) | präzisere Belege | Kontextüberlauf | Auszugspolitik pro Material begrenzt und dokumentiert |
| Repository-Schreibvorschläge | neue Übergabeart (Diff) | Wirksamkeit | **höchstes Risiko** | R5 strikt: Diff → Rechte → Bestätigung; nie automatisch; nie in fremde Bereiche |
| Pull-Request-Erstellung | Übergabe mit externer Wirkung | Übergabe in echte Arbeit | irreversibel | doppelte Bestätigung, Vorschau des PR-Textes, Widerrufspfad |
| Dateioperationen | Schreibvorschlag | Lokale Wirksamkeit | Datenverlust | Backup-Pflicht vor Anwendung; Diff zwingend |
| Externe APIs | neue Fähigkeit | Integration | Wirkung außerhalb | bestätigungspflichtig, protokolliert, mit Widerruf |
| Automationen / Zeitpläne | wiederkehrende Läufe (`ANALYZE_MATERIAL` bei Materialänderung) | Kontinuität | Kosten, Überraschung | nur mit Obergrenze; Ergebnis als Vorschlag, nie als Änderung |
| Workflows | gespeicherte Arbeitspläne | Wiederholbarkeit | Erstarrung | Arbeitspläne bleiben bearbeitbar; kein Zwangsablauf |
| Team-Kollaboration | geteilte Arbeitsräume | gemeinsames Urteilen | Berechtigungskomplexität | erst mit echtem Rollenmodell (LibreChat-ACL als Referenz) |
| Rollen und Freigaben | Vier-Augen-Prinzip bei Freigabe | Belastbarkeit in Teams | Bürokratie | Freigabe nur an **blockierender Frage** geknüpft, nie pauschal |
| Persönliche Memory-Systeme | Stufe `GLOBAL` + Vorschläge | Arbeitskontinuität | Illusion von "Kenntnis" | Gedächtnis-Register bleibt Pflicht; keine Inferenz ohne Eintrag |
| Eigene Fähigkeiten/Plugins | Katalogerweiterung | Anpassung | Qualitätsverlust | jede Fähigkeit braucht Qualitätsklasse + Testmaterial |

**Warum nichts davon beliebig wird:** Jede Erweiterung muss **eine der vier Kanten** bedienen (stützt / widerspricht / blockiert / entstand aus) oder **einen Materialtyp** ergänzen. Was nur eine neue Anzeige erzeugt, wird nicht aufgenommen.

---

## 15. Endgültige Empfehlung

### 15.1 Welches Modell

**Omnia Atelier (Modell A).** Es ist das einzige der drei Modelle, das die beiden anderen **als Werkzeuge aufnehmen** kann, ohne sich zu verbiegen:
- Der **Beweisstatus** aus dem Beweisraum (3.B) wird zum Qualitätsmaßstab **jeder** Kernaussage — das Atelier erbt damit die epistemische Schärfe von B, ohne auf Prüf-Fälle beschränkt zu sein.
- Der **Werkbrief** aus der Gießerei (3.C) wird zur **Übergabeform** eines fertigen Arbeitsstücks — inklusive Blindtest als Freigabekriterium, wenn der Nutzer es verlangt.

### 15.2 Warum — gegen die elf Kriterien der Aufgabenstellung

| Kriterium | Bewertung |
| --- | --- |
| **Benutzererlebnis** | Der Nutzer verlässt die App mit einem **Dokument**, nicht mit einem Verlauf. Wiederbetreten ist sinnvoll, weil Material, Fragen und Versionen weiterleben. |
| **Eigenständigkeit** | Die primäre Einheit ist das Arbeitsstück; es existiert kein vergleichbares Format in Chatbots, Dashboards oder Node-Editoren. |
| **Technische Machbarkeit** | Der Kern (Repo read-only + ein Router-Aufruf + SQLite + SSE) ist klein; `schaltwerk` beweist jede einzelne Zutat bereits. |
| **Wiederverwendung des Repositorys** | Repo-Tokens, Bad-Wolf-Prinzipien (Stimme/Ablage/Wachdienst/Goldene Regeln), FastAPI/SSE/Job-Muster und das vorhandene Repository-Material selbst werden genutzt — **ohne eine Zeile fremden Codes zu kopieren**. |
| **Sinnvolle OmniRoute-Integration** | OmniRoute ist Motor, nicht Thema: sichtbar nur bei Relevanz, gekapselt hinter `RouterPort`, mit defensivem Adapter gegen die belegten Format-Inkonsistenzen. |
| **Sinnvolle LibreChat-Wiederverwendung** | Konzepte (Memory-Semantik, Nachrichtenbaum, Run-Lebenszyklus, Audit, Zitate), keine Abhängigkeiten — das ist die einzige mit einem Single-User-Lokalprodukt verträgliche Form. |
| **Kontrollierte MashAI-Kontinuität** | Arbeitsräume statt Chat-Verlauf; Kontinuität kommt aus **Arbeitsstücken und Material-Hashes**, nicht aus einem impliziten Nutzer-Gedächtnis — und ist damit transparent, korrigierbar und löschbar. |
| **Qualität der Leitassistenz** | Sie hat einen **Contract** (8.4) mit Intent-Typen, Bestätigungsgrenzen, Quellenregeln und Audit — sie ist eine Rolle mit Grenzen, kein freundlicher Chatbot. |
| **Erweiterbarkeit** | Neue Fähigkeit = neuer Werkzeugslot; neues Material = neue Materialart. Das Raummodell bleibt stabil (Abschnitt 14). |
| **Sicherheit** | Read-only-Start, Diff-Rechte-Bestätigung, Loopback, Secrets nur im Prozess, Goldene Regeln aus dem Repo übernommen. |
| **Wartbarkeit** | Ein Python-Service, eine SQLite-Datei, ein React-Frontend ohne UI-Library, ein austauschbarer Router-Port. Kein Cluster, kein Mongo, keine 102 Abhängigkeiten. |
| **Vermeidung des generischen AI-Dashboards** | Keine Kennzahlen-Kacheln, keine Sidebar-Navigation als Dauermöbel, keine Agenten-Karten. Dafür: ein Raum, ein Werkstück, eine Fragenleiste. |

### 15.3 Welche Repository-Teile zuerst geprüft werden müssen

1. **OmniRoute-Inferenzfähigkeit** (Abschnitt 12.4) — ohne sie fehlt der Motor. Höchste Priorität.
2. **OmniRoute-Antwortformate** — die belegte Inkonsistenz (nacktes Array) erzwingt defensive Normalisierung.
3. **Lizenzstatus von `schaltwerk`** (keine Lizenzdatei vorhanden) — klären, bevor Muster in Code gegossen werden.
4. **`DOKUMENTATION.md` + `WEITERARBEITEN.txt`** als Material des ersten Arbeitsstücks (kein Prüfaufwand, aber Inventarisierung).
5. **Laufzeitumgebung** (Port 24615 vs. 20128, drei Container, Key-Rotation) — beeinflusst jede Integration.

### 15.4 Die wichtigsten LibreChat-Prüfobjekte

1. `packages/data-schemas/src/schema/memory.ts` + `api/server/routes/memories.js` — das Memory-Vorbild.
2. `packages/data-schemas/src/schema/message.ts` (`parentMessageId`) — das Versionsmodell.
3. `packages/api/src/stream/` (JobManager, Approval, Checkpoints, terminalProjection) — die Run-Sprache.
4. `packages/api/src/files/citations.ts` — die Zitatverknüpfung.
5. `librechat.example.yaml` → `endpoints.custom` — die Form der Endpoint-Konfiguration.
6. `packages/data-schemas/src/schema/auditLog.ts` — das Audit-Vorbild.

### 15.5 Welche MashAI-Eigenschaften konkret zu definieren sind

Nicht die KI-Eigenschaften (die hat MashAI nicht), sondern die **Kontinuitätseigenschaften**:
1. **Arbeitsraum-Isolation** — was gehört zu einem Raum, was nicht?
2. **Wiederbetreten statt Neuladen** — was wird beim Öffnen wiederhergestellt (Werkbankstand, Fragen, Material-Hashes, Werkstattbericht-Zustand)?
3. **Gegenüberstellung** — wie werden zwei Modellpositionen gleichzeitig sichtbar, ohne zum Vergleichs-Dashboard zu werden?
4. **Einstellungs-Migrationen** — wie werden gespeicherte Arbeitsraum-Einstellungen bei Formatänderungen überführt?
5. **Ressourcen-Disziplin** — was passiert mit Hintergrundläufen, wenn der Raum verlassen wird?

### 15.6 Welche Entscheidung noch NICHT getroffen werden darf

1. **Ob OmniRoute Modell-Routing und Fallback selbst übernimmt oder unsere Policy.** Das hängt am Capability-Probe. *Vorher* ist jede Routing-Architektur Spekulation.
2. **Ob die App-Layer-Sprache dauerhaft Python bleibt.** Sie ist für v1 richtig; ob sie es bleibt, hängt daran, ob LibreChat-Code später **direkt** übernommen werden soll. Der `RouterPort` hält diese Entscheidung offen — absichtlich.
3. **Ob MashAI ("Mesh AI") tatsächlich die gemeinte Inspirationsquelle ist.** Die Zuordnung ist eine ANNAHME.
4. **Ob das Partikel-/Persona-Erbe von Bad Wolf in der Leitassistenz sichtbar bleiben soll.** Die Disziplin wird übernommen; die Figur ist eine Produktentscheidung mit Copyright-Vorgeschichte (BBC) — bewusst zurückgestellt.
5. **Ob Electron als Zielplattform kommt.** Web auf Loopback genügt für v1.

### 15.7 Der allererste konkrete Arbeitsschritt

> **Den OmniRoute-Capability-Probe durchführen und protokollieren — read-only, mit genau einer Frage: *"Gibt es einen Inferenz-Endpunkt, und wie sieht seine Antwort aus?"***

Konkret (alle Schritte read-only, gegen die lokale OmniRoute-Instanz):
1. Erreichbarkeit und Version feststellen (Basis-URL und Port der laufenden Instanz klären — **BEKANNT:** Container `omniroute`, Host-Port `24615`, Container `20128`).
2. Kandidaten-Endpunkte **lesend** abfragen und Antwortformate protokollieren (Pfad, Status, Format).
3. Bei Erfolg: einen **minimalen** Inferenzaufruf mit einem kurzen Material-Auszug aus `DOKUMENTATION.md` durchführen und die Antwort **inklusive Streaming-Verhalten** dokumentieren.
4. Ergebnis in `docs/OMNIROUTE-PROBE.md` festhalten — mit Datum, Basis-URL und exakten Rohantworten (maskiert).

**Warum genau dieser Schritt zuerst:** Er ist billig, gefahrlos, und er entscheidet über die Reihenfolge von Phase 4 bis 6. Fällt er positiv aus, geht es direkt an den Vertikalschnitt. Fällt er negativ aus, bleibt das Produktmodell intakt — wir starten dann mit `MockAdapter` und einem Direkt-Provider-Adapter und wissen es **jetzt**, nicht nach vier Phasen.

### 15.8 Der erste vertikale End-to-End-Prototyp

| Bestandteil | Konkrete Ausprägung |
| --- | --- |
| **Sichtbar** | Arbeitsraum "schaltwerk-Beurteilung": Materialwand mit 5 Inventar-Dateien, Werkbank mit Arbeitsstück in 4 Abschnitten, Fragenleiste, Werkzeugspur, Ablage mit v1–v3 |
| **Material** | `server.py` (Auszug: Routen + `probe_one`), `DOKUMENTATION.md`, `tests/test_server.py`, `CHANGELOG.md`, `WEITERARBEITEN.txt` |
| **Absicht** | *"Beurteile, ob die schaltwerk-Logik als Hintergrundorchestrierung für Omnia Atelier erhalten bleiben kann."* |
| **Interpretation** | Arbeitsplan mit 4 Abschnitten (Bestand, Eignung, Risiken, Empfehlung), 2 Fähigkeiten, 1 Vorfrage |
| **Run** | Strukturleser + Risikoprüfer über OmniRoute (oder Mock, falls Probe negativ) |
| **Ergebnis** | Arbeitsstück v1, jede Kernaussage mit Belegstatus, 8–14 Zitate mit Datei+Zeile, 2 verworfene Alternativen, 3 offene Fragen |
| **Gezeigte Ausnahmen** | ein Fallback (Karte + Qualitätsvermerk), ein `╱ unbelegbar` (OmniRoute-Inferenz!), ein Abbruch + Wiederaufnahme |
| **Nachweis** | Repo-Hashes vor/nach unverändert · `pytest schaltwerk/tests/` 34× grün · Run-Log mit Routing-Protokoll · Material-Hash-Abgleich beim Wiederbetreten |
| **Abnahme** | Eine dritte Person verfolgt drei Kernaussagen bis zur Materialstelle, ohne die App zu bedienen. |

---

## 16. Anhang · Offene Punkte (ZU PRÜFEN, konsolidiert)

| # | Offener Punkt | Nächster Schritt |
| --- | --- | --- |
| 1 | OmniRoute-Inferenz-API (Existenz, Pfad, Auth, Streaming) | Capability-Probe (15.7) |
| 2 | OmniRoute-Routing-/Fallback-Logik: in OmniRoute oder in unserer Policy? | Nach Probe 1; Policy zunächst bei uns halten |
| 3 | OmniRoute-Telemetrie pro Request (Kosten/Token) | Probe + Abgleich `/api/usage/proxy-logs` |
| 4 | Multimodalität, Dateien, Audio, Video, Embeddings, MCP, A2A | Erst nach 1; NICHT für v1 annehmen |
| 5 | OmniRoute-Version/Image-Tag | Probe |
| 6 | Lizenzstatus `schaltwerk` (keine Lizenzdatei) | Product Owner klären |
| 7 | "Mesh AI" = MashAI? | Product Owner bestätigen |
| 8 | Python vs. Node als dauerhafte App-Layer-Sprache | Entscheidung nachPhase 5 offen halten |
| 9 | Electron als Zielplattform | Nach v1 |
| 10 | Ob die Bad-Wolf-Figur in die Leitassistenz übergeht | Bewusst zurückgestellt (Copyright-Vorgeschichte) |
| 11 | Laufzeitumgebung: Port 24615 vs. 20128, drei Container, Key-Rotation | Bei Integration klären |
| 12 | Kontrastwert `--muted` auf `--bg` ausreichend? | Messung in Phase 7 |

---

*Ende des Dokuments. Änderungen gehören in `CHANGELOG.md`, nicht hier.*
