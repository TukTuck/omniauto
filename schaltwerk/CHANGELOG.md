# Changelog

Alle wesentlichen Änderungen an diesem Projekt werden hier mit
Versionsnummern dokumentiert. Format orientiert sich an
[Keep a Changelog](https://keepachangelog.com/de/1.1.0/), Versionierung
nach [SemVer](https://semver.org/lang/de/).

Versionierung:
- **Patch** (1.0.1): Fixes, die nichts kaputt machen können
- **Minor** (1.1.0): neue Funktionen, abwärtskompatibel
- **Major** (2.0.0): Verhalten ändert sich / Endpunkte brechen

Neue Änderungen gehören in den Block `[Unreleased]` und werden beim
nächsten Stand nach unten in eine Versionsnummer verschoben.

## [Unreleased]

### Hinzugefügt

- **Bad Wolf wird wach:** Wachdienst beim Serverstart (Bereitschaftsmeldung
  mit Pool-/Register-Stand, bzw. „aber blind" ohne Key), Begrüßung nach dem
  ersten erfolgreichen Connect, und ein Beobachter, der alle 60 s den
  Proxy-Traffic prüft und Auffälligkeiten meldet (fehlgeschlagene
  Proxy-Requests, laufender Traffic — max. eine Traffic-Meldung pro 10 min).
- **Bad Wolf versteht ihre Ablage** (`POST /api/tray/check`): Proxy-Einträge
  im Ablagefeld haben einen Knopf „Prüfen & übernehmen" — Bad Wolf prüft
  selbst (Ziel-HTTPS, Risikobefund) und schreibt bei Bestehen direkt ins
  Register; Risiko-/Tot-Fälle werden gemeldet und verworfen.

### Geändert

- **Porträt v2 (menschlicher):** Brauen und Nase als Partikel-Strukturen,
  Wangen über Dichte-Skulptur modelliert, volleres Haar (breitere Masse,
  mehr Ströme), weicher Goldschleier als Glow-Grundierung hinter der Figur.
- **Austausch-Parameter im UI:** Timeout, Parallelität, Listen-Limit und
  Schreib-Limit über ein Parameter-Menü neben „Austausch starten"
  einstellbar (statt hartcodiert).
- **Hologramm-Feinschliff:** Partikel deutlich feiner und zahlreicher
  (~7.000 statt ~1.300), Gesicht als flimmernder Staub, die Haar- und
  Randpartikel entweichen als feine goldene Schlieren seitlich und
  formieren sich neu — Energie statt Punktbild. Die Augen leuchten als
  pulsierende Sterne stärker als alles andere.
- **Bad Wolf ist jetzt ein Hologramm** (nach neuen Referenzen des PO):
  ihr Porträt besteht aus ~1.300 goldenen Partikeln (Canvas), die sanft
  driften und funkeln, an den Rändern ins Nichts zerstäuben — dazu fest
  leuchtende Augen als Sterne und Tränen-Ströme, die als funkelnde
  Sterne weiterfallen. Das Gold ist bewusst Träger: sie ist reine
  Energie/Zeit. Automatische Standbild-Fallbacks bei
  `prefers-reduced-motion` und im Hintergrund-Tab.
- **Marken-Figur überarbeitet:** aus dem Wolf-Glyph wurde Bad Wolf selbst —
  schemenhafte Frauenfigur (Sidebar-breit, ~¼ der Höhe) mit blass
  leuchtendem Gesicht, langen Haaren, glühenden Bernstein-Augen und
  Tränen, die zu fallenden Sternen werden (Starry-Night-Motiv). Gold
  weiterhin nur für Augen und Tränen. Alle Benennungen von „Die Wölfin"
  auf „Bad Wolf" gestellt. Vorlage: die Referenzbilder des PO.

- **Marken-Theme „Die Wölfin in der Sternennacht"** (Bad-Wolf-Hommage,
  schematisch wegen BBC-Copyright, plus van-Gogh-Nachtblau, gemeinfrei):
  gezeichnetes Wolf-Glyph mit leuchtenden Bernstein-Augen in der Sidebar,
  verstreutes „BAD WOLF"-Stencil, dezenter Sternenstaub, Nachtblau-Palette.
- **Die Wölfin — Ablage der Hub-KI** (`GET/POST/DELETE /api/tray` +
  Wolf-Glyph in der Sidebar): nimmt Proxies (Drag & Drop aus der
  Kandidaten-Tabelle), Text, Links und Datei-Inhalte auf; Panel mit
  Badge-Zähler, Einzeln-löschen, Leeren. Läuft bewusst nur im RAM.
- Doppel-Ablage-Bug behoben: beim Proxy-Drag wurde der Drag-Stempel-Text
  („N Proxy/Proxies") zusätzlich als Text-Item gesammelt.

### Geändert

- **Design-Audit + De-Scale-Pass** (Taste-Methodik: messen → Muster → Eingriff):
  Das vorherige Theme hatte 89 Pills, 22 Kästchen-Elemente, Blaustich in
  Grundfarben und vier Radius-Stufen — die typische KI-Dashboard-Signatur.
  Ersetzt durch eine entsättigte Graphit-Palette ohne Blau-Akzent
  (aktiv = helles Ink + Balken, Primär-Button = heller Kasten), Radius
  einheitlich 3 px, gedämpfte Statusfarben nur semantisch, KPI-Kärtchen
  durch eine dichte Mono-Statuszeile ersetzt, Pills nur noch für echte
  Stati. Alle Interaktionen und Endpunkte unverändert.

### Hinzugefügt

- **Hub-Übersicht** (`GET /api/hub-summary` + Tab „Übersicht", neue
  Startseite): Live-KPIs — OmniRoute-Verbindung, aktive Provider,
  Proxy-Pool, Proxy-Requests/Fehler, Job-Status — plus Live-Aktivität und
  Schnellzugriffe. Pollt alle 5 s.
- **Provider-Seite:** listet alle installierten Provider-Connections und
  erlaubt Aktivieren/Deaktivieren per Schalter
  (`POST /api/omni/provider-status`, mit Bestätigungsdialog).
- **Schadensprüfung für Proxies:** jeder HTTPS-Check testet jetzt auch,
  ob der Proxy TLS abfängt (Zertifikatsprüfung schlägt fehl = Intercept —
  kann Provider-API-Keys mitlesen) und ob die Exit-IP zwischen zwei
  Echo-Diensten wechselt (Manipulation/Rotation). Befund als `risk`
  markiert, im UI als Pill angezeigt und konsequent vom Schreiben
  ausgeschlossen (Austausch und manuelles Übernehmen).
- **Drag & Drop rechts→links:** Kandidaten-Zeilen lassen sich in den
  OmniRoute-Bestand ziehen (Mehrfachauswahl wird mitgenommen) und werden
  dort übernommen — visuelle Drop-Zone, Risikofälle werden serverseitig
  übersprungen.
- **Traffic-Filter:** Freitextfilter (Host/Provider/Ziel) und Schalter
  „nur echter Proxy-Traffic" (blendet Direkt-Traffic aus).

### Behoben

- openrouter-Connection-Toggle via PATCH /api/providers live verifiziert
  (an→aus→an, Zustand wiederhergestellt).

## [1.1.0] – 2026-09-08

Sprint „Stabilität + Hub-Vorbereitung": UI-Erneuerung, Sicherheitsfixes,
geplanter Austausch, Live-Traffic, manuelle Übernahme.

### Hinzugefügt

- **Geplanter Austausch** (`GET/POST /api/schedule` + UI-Tab „Zeitplan"):
  Hintergrund-Task führt regelmäßig denselben Austausch-Ablauf aus
  (Intervall 5–1440 min, nutzt dieselbe Doppelstart-Sperre). Status zeigt
  nächsten/letzten Lauf und Fehler.
- **Manuelles Übernehmen** (`POST /api/push-selected` + Button
  „Ausgewählte übernehmen"): Kandidaten-Tabelle hat Checkboxen; nur
  HTTPS-geprüfte werden als manuelle Proxies geschrieben, Rest wird
  übersprungen und gemeldet.
- **Live-Traffic** (`GET /api/omni/proxy-logs` + UI-Tab „Traffic"):
  liest alle 5 s die letzten Proxy-Requests aus OmniRoute
  (`/api/usage/proxy-logs`) und zeigt, ob und wo gerade etwas läuft.
- **Quellenauswahl im UI**: „Quellen"-Menü mit Checkboxen je Quelle
  (aus `GET /api/meta`), fließt in Harvest und Austausch ein.
- **Hub-Sidebar**: Navigation Austausch/Traffic/Zeitplan plus deaktivierte
  Hub-Platzhalter (Übersicht/Provider/Einstellungen) — Vorbereitung für die
  spätere Dashboard-Zusammenführung.
- **Tests** (`tests/test_server.py`, 25 Stück): Parser, Dedupe,
  OmniRoute-Hilfen, Connect-Validierung, Schedule-Validierung,
  Push-Selected-Grenzen, 409-Doppelstart-Sperre. Läuft ohne Netz:
  `pip install -r requirements-dev.txt && pytest tests/`

### Geändert

- **Komplette UI-Erneuerung:** kompaktes Dark-Theme (Graphit/Blau, keine
  Gradient-Flächen), Tabs statt Endlos-Scroll, dichte Tabellen, echte
  Empty-States, Lade-/Disabled-Zustände, Fehlerbehandlung für jeden Fetch.
- **XSS behoben:** exit_ip/error/country aus unverifizierten Proxy-Antworten
  wurden ungefiltert per innerHTML eingesetzt — jetzt HTML-Escaping aller
  dynamischen Felder.
- **Doppelstart-Sperre:** POST /api/exchange antwortet mit 409, wenn schon
  ein Lauf aktiv ist (synchron im Handler geprüft); UI-Button deaktiviert
  sich während des Laufs.
- **Job-Status robust:** Status wird beim Seitenladen geholt und alle 5 s
  gepollt — ein Reload während eines Laufs verliert den Zustand nicht mehr;
  abgeschlossene Läufe werden nachgetragen.
- **`/api/connect`:** URL wird vor dem Speichern validiert; ein leerer
  Key-Feld löscht den gespeicherten Key nicht mehr (Page-Reload/Auto-Connect
  ist damit harmlos). Die Oberfläche verbindet sich beim Laden selbstständig.
- Windows-Event-Loop-Policy nur noch unter Python <3.14 setzen (Deprecation).
- SOCKS4-Einträge aus der 1proxy-Quelle werden verworfen statt als SOCKS5
  weitergeprüft zu werden.

## [1.0.0] – 2026-08-12

Erster dokumentierter Stand nach dem Umbau „Austausch + Zuordnung“.

### Hinzugefügt

- **„Provider zuordnen“** (`POST /api/assign-providers` + Button):
  ordnet die besten lebendigen `px-*`-Proxies allen installierten
  Providern zu (scope=provider, Scope-ID = Provider-ID aus
  `GET /api/providers`). Prüft zur Laufzeit, ob mehrere Proxies pro
  Scope (Pool) via API möglich sind; sonst gilt 1 Proxy pro Provider
  (Replace-Semantik). OmniRoute nutzt einen Proxy erst nach der
  Scope-Zuordnung — vorher füllte das Tool nur das Register.
- **Verifikation nach dem Zuordnen:** `/api/assign-providers` liest
  die tatsächlichen Zuweisungen aus OmniRoute zurück und loggt sie
  (Nachweis, dass die Proxies wirklich bei den Providern hängen).
- **`GET /api/job-status`:** Phase/Zähler/Fehler des letzten oder
  laufenden Austausch-Jobs (Diagnose).
- **Laufzeit-Logging:** jeder Austausch schreibt `[job]`-Zeilen mit
  Zeitstempel in die Server-Konsole.
- **UI-Reconnect:** reißt die SSE-Verbindung ab (z. B. Reload), holt
  die Oberfläche den Job-Status nach und zeigt, ob der Lauf
  weiterläuft, statt still zu warten.
- **Harte Deadline pro Einzel-Check** (max. 15 s bzw. 7×Timeout),
  damit kein hängender Proxy den Austausch blockiert.

### Behoben

- **`POST /api/exchange` ignorierte die Typ-Auswahl:** Harvest fiel
  immer auf `["http","https"]` zurück, die Kandidaten wurden nicht und
  der Upload nur unzureichend nach Typ gefiltert — auch wenn z. B. nur
  SOCKS5 angekreuzt war, wurden HTTP/HTTPS-Proxies geholt und
  geschrieben. Jetzt fließt die Auswahl durch Harvest, Kandidaten-Filter
  und Upload; „nur angekreuzte Typen holen, prüfen und hochladen“ gilt
  wirklich.
