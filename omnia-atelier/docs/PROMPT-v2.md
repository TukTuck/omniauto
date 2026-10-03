# Aufgabenstellung (revidierte Fassung) — Omnia Atelier

**Stand:** 2026-10-02 · **Repository:** `TukTuck/omniauto` · **Basis-Commit:** `60dd904`
**Zweig:** `arena/01a0fe6e-omniauto`

> **Was diese Datei ist.** Die **vollständige** Fassung deines ursprünglichen Prompts —
> in voller Länge, mit allen Aufzählungen, selbsttragend und ohne Verweis auf andere
> Dokumente. Jede Änderung gegenüber dem Original steht **direkt im Text** und ist mit
> `⟨†N⟩` markiert; die Erklärung dazu findet sich in Teil A, Zeile N.
>
> Alles, was nicht mit `⟨†N⟩` markiert ist, entspricht **wortgleich dem Original**.
>
> Diese Datei ist allein verwendbar: Sie kann ohne Kenntnis von
> [`OMNIA-ATELIER.md`](./OMNIA-ATELIER.md) in eine neue Sitzung gegeben werden.

---

# A · Korrekturen gegenüber der ersten Fassung

| # | Erste Fassung (Prämisse) | Befund | Korrektur |
|---|---|---|---|
| †1 | „Das bisherige Schaltwerk-/Node-/Graph-Prinzip", „bisherige Schaltwerk-Logik", „Node-/Graph-Daten" | `schaltwerk/` ist **Proxy-Logistik**: 21 FastAPI-Routen, SSE-Job, Tabellen, RAM-Ringpuffer. **Kein Node-Editor, kein Graph.** | §5 heißt „Sichtbarkeit neu denken" und formuliert ein **Zielprinzip**, keinen Umbau. |
| †2 | „Mesh AI" als Inspiration für eine persönlichere, kontextbewusstere, kontinuierlichere KI-Erfahrung | Im Repository liegt **MashAI** (`Kurz-main`): Electron-Workspace für ChatGPT/Claude/Gemini-**Weboberflächen**, Profile, Tab-Suspension, Session-Persistenz, 66 Tests, **MPL-2.0**. **Kein Memory-System.** | §1.3 und §8.2/§8.3 beschreiben MashAI korrekt. Kontinuität kommt aus **Arbeitsstücken und Material-Hashes**. |
| †3 | OmniRoute „verbindlich als zentrale Infrastruktur für Modelle, Provider und Routing" | Verifiziert: **Verwaltungsebene** (10 Endpunkte, Auth per `Bearer` + `x-api-key`). **Nicht verifiziert:** Inferenz, Routing-Regeln, Fallback, Multimodalität, MCP, A2A. | §1.1/§7 trennen **verifiziert / zu prüfen** hart. Phase 4 beginnt mit einem **Capability-Probe**; der Router-Port hält die Entscheidung offen. |
| †4 | „Bestehende funktionierende Logik, Content-Pipelines, Authentifizierung, Datenmodelle, Provider-Konfigurationen, Build-Prozesse" | Es gibt **eine** Anwendung (`schaltwerk`, 34 Tests). **Kein** Login, **keine** Datenbank, **keine** CI/CD, **kein** Deployment, **keine** gemeinsame Build-Pipeline. | §4 ist bewusst schmal. „Nicht vorhanden" ist ein gültiges Prüfergebnis. Kernregel: **`schaltwerk` und die ZIP-Archive werden nicht angefasst.** |
| †5 | LibreChat als Quelle „wiederverwendbarer Module" | v0.8.8, **MIT** — aber TypeScript + MongoDB + Meilisearch + pgvector + **102 Client-Abhängigkeiten**. | §8.1: **Konzepte übernehmen, Code nicht einbinden.** Keine Imports, keine gemeinsame Datenbank. |
| †6 | „Mesh AI" ohne Lizenzangabe | MashAI ist **MPL-2.0** (file-level copyleft); `schaltwerk` hat **keine Lizenzdatei**. | §8.2 verbietet Code- und Asset-Kopien aus beiden Quellen. |
| †7 | Discovery-Liste enthält Bereiche, die es nicht gibt | Real fehlen Monorepo, CI/CD, Deployment, Datenbank, ORM, WebSocket, Secret-Management, Authentifizierung, Node-/Graph-Daten. | Die Liste bleibt vollständig erhalten, aber **„nicht vorhanden" ist ein zu dokumentierendes Ergebnis**, kein Anlass zu Spekulation. |
| †8 | Keine Aussage zur Ablagestruktur | Neu etablierte Konvention: **jeder Zweig baut in seinem eigenen Ordner**. | Neuer Abschnitt **0.5** vor §1. |
| †9 | Kein verifizierter Befund im Prompt | — | Neuer Block **„Gesetzter Befund"** vor §1, damit nichts erneut hergeleitet oder erfunden wird. |
| †10 | — | — | Neuer Abschnitt **§16 Nachweis**: was am Ende bewiesen sein muss. |

---

# B · Der vollständige Prompt

---

# Aufgabe: Entwickle Omnia Atelier auf Basis des bestehenden Repositorys

Du entwickelst eine außergewöhnliche, eigenständige AI-Anwendung auf Basis des bestehenden GitHub-Repositorys:

`https://github.com/TukTuck/omniauto`

WICHTIG:
Denke die gesamte Aufgabe vollständig durch, bevor du antwortest.

Liefere keine oberflächliche Designidee, kein generisches AI-Dashboard und keine bloße Sammlung von Features.

Erfinde keine Repository-Dateien, keine APIs, keine Komponenten, keine Datenmodelle und keine bereits vorhandenen Funktionen.

Wenn etwas vom tatsächlichen Repository, seiner Dokumentation, seiner Konfiguration oder seiner konkreten Implementierung abhängt, kennzeichne es ausdrücklich als:

**ZU PRÜFEN**

Unterscheide in der gesamten Antwort konsequent zwischen:

- **BEKANNT**
  Informationen, die aus dieser Aufgabenstellung sicher hervorgehen **oder aus dem Repository tatsächlich gelesen wurden** ⟨†9⟩

- **ZU PRÜFEN**
  Informationen, die erst durch Untersuchung des Repositorys, der verwendeten Versionen oder der technischen Dokumentation verifiziert werden müssen

- **ANNAHME**
  Plausible, aber noch unbestätigte Voraussetzungen. **Dürfen niemals Grundlage einer irreversiblen Entscheidung sein.** ⟨†9⟩

- **VORSCHLAG**
  Neue Produkt-, UX-, Architektur- oder Implementierungsentscheidungen

Die zentrale Grundregel lautet:

Baue keinen OmniRoute-Manager mit schöner Oberfläche.
Baue kein LibreChat-Redesign.
Baue keine Mesh-AI-Kopie. ⟨†2⟩
Baue keinen generischen Chatbot.
Baue keinen technischen Node-Editor als Selbstzweck.

Baue ein eigenständiges Produkt, dessen Arbeitsweise durch OmniRoute, wiederverwendbare LibreChat-Module, Repository-Content und eine zentrale native Leitassistenz ermöglicht wird. ⟨†5⟩

Die technische Infrastruktur soll sichtbar werden, wenn sie für Verständnis, Vertrauen, Eingriff oder Qualität relevant ist.

Sie soll unsichtbar bleiben, wenn sie nur technische Komplexität erzeugt.

---

## 0.1 · Gesetzter Befund — muss nicht erneut hergeleitet werden ⟨†9⟩

**BEKANNT.** Das Repository hat **einen Commit** (`60dd904`) und **12 versionierte Dateien** (38 MB). Es ist **kein** Monorepo mit bestehender Anwendung, sondern eine **Materialablage** aus drei Teilen:

| Inhalt | Befund |
|---|---|
| `schaltwerk/` | Einzige lauffähige Anwendung. **Python / FastAPI / uvicorn / httpx[socks]**. `server.py` (57 KB, 21 Routen) + `static/index.html` (74 KB, eine Datei, kein Build, keine CDN-Abhängigkeit) + `tests/test_server.py` (**34 Tests, offline grün**). **RAM-only**, keine Datenbank, kein Login, kein CI/CD. Bindung an `127.0.0.1`, Port 8765 (`HOST=`/`PORT=` überschreibbar). Windows-Start per `STARTEN.bat`. **Zweck: Proxy-Logistik** — freie Proxies aus 10 Quellen holen, selbst gegen echte HTTPS-Ziele prüfen, tote eigene Einträge entfernen, lebendige als **manuelle** Registry-Proxies nach OmniRoute schreiben, nie in die kostenpflichtige 1proxy-/Free-Kategorie. |
| `schaltwerk/` — „Bad Wolf" | Bereits vorhandene **native Leitfiguren-Instanz**: **Stimme** als serverseitiger Ringpuffer (`bw_log`, 60 Zeilen, RAM-only) protokollierter Taten; **Ablage** (`/api/tray`, max. 200 Einträge, Kürzung auf 4.000 Zeichen) mit Selbstprüfung (`/api/tray/check`); **Wachdienst** (asyncio-Task im Lifespan, 60 s, Anti-Spam-Regel: Fehler sofort, laufender Traffic max. 1 Meldung / 10 min); **Risiko-Ausschluss vor jedem Schreibzugriff** (`tls-intercept`, `ip-mismatch` werden konsequent nie geschrieben); **acht Goldene Regeln** (u. a. nie in die 1proxy-Kategorie schreiben, `HARVEST_TAG = "proxy-exchange"` nicht umbenennen, Typ nie pauschal erzwingen, `STARTEN.bat` mit CRLF). |
| `schaltwerk/` — Design | Gemessener Anti-KI-Look-Umbau („De-Scale-Pass"): Ausgangslage 89 Pills, 22 Kästchen, Blaustich, vier Radius-Stufen → **Radius einheitlich 3 px**, keine Gradient-Karten, KPI-Kärtchen ersetzt durch eine dichte **Mono-Statuszeile**, Pills **nur für echte Stati**. Tokens (wörtlich in `static/index.html`): `--bg #0d0e12`, `--panel #13141a`, `--panel-2 #191a21`, `--line #262833`, `--line-2 #33353f`, `--ink #d6d7dd`, `--muted #8a8c99`, `--eye #d9a441`, `--eye-dim #8a6a34`. Typografie: Inter/system-ui für Text, JetBrains Mono für Daten, Labels 9–10 px uppercase. |
| `Kurz-main (1).zip` | **MashAI** v1.0.0-beta, **MPL-2.0**, `github.com/Avaxerrr/MashAI`. Electron **39.2**, React **18.3**, TypeScript **5.9**, Vite **6**, Tailwind **3.4**, Ghostery-Adblocker, Vitest (**66 Tests**, Branch `arena/01a0e39c-kurz`, Commit `9e6d88e`). Claim: *„Your Unified AI Workspace — Stop losing work in browser tabs."* Es ist ein **Electron-Browser für die Web-Oberflächen von ChatGPT, Claude, Gemini, Perplexity, Grok und DeepSeek** plus Organisationsschichten: Profile (eigene Session/Cookies/LocalStorage, vollständige Isolation), Tab-Management, **Smart Tab Suspension** (1–120 min, media-aware), **Side Panel** (zwei Assistenten gleichzeitig, Ziehteiler), Quick Search (`Ctrl+K`), Open Tab Search (`Ctrl+Shift+K`, Ranking exakt > Präfix > Wortanfang > Teilstring), **Session Persistence** (Tabs, Fensterposition, Profilzustand), SettingsManager mit Defaults/Merge/**Migrationen**. Plattform: **Windows only**. Roadmap offen: Bring Your Own Keys, Local AI, Unified Chat Interface. **Es ist kein System mit Gedächtnis.** |
| `LibreChat-main.zip` | **v0.8.8, MIT** (`LICENSE`, "Copyright (c) 2026 LibreChat"); Workspace-Pakete teils `ISC` (`@librechat/api` 1.7.52, `librechat-data-provider` 0.8.527), `@librechat/data-schemas` 0.0.74 `MIT`. **6.303 Dateien**, 66,8 MB entpackt. Monorepo (turbo): `api/` (legacy Express), `packages/api` (TypeScript, neues Backend), `packages/data-schemas` (Mongoose), `packages/data-provider`, `client/` (React, **102 Abhängigkeiten**: recoil + jotai, framer-motion, Radix, Ariakit, react-router 7). Infrastruktur: MongoDB 8.0.20, Meilisearch v1.35.1, pgvector 0.8.0-pg15, `rag_api`. **Verifiziert vorhanden:** Memory (`memory.ts`: Key/Value, `key` validiert durch `^[a-z_]+$`, `agentId`-Partition, `tokenCount`, `charLimit` 10.000, `tokenLimit`; Routen `GET/POST/DELETE /memories`, `PATCH /:key`, `PATCH /preferences` mit `checkMemoryOptOut`) · Nachrichtenbaum (`parentMessageId`) · Stream-Architektur (`GenerationJobManager`, `ApprovalLifecycle`, `SteeringLifecycle`, `checkpoints`, `terminalProjection`, `abortContent`) · 10 Auth-Strategien (local, jwt, google, github, discord, facebook, apple, openid, saml, ldap) · MCP/Tools/Agents/Skills/Code-Environments · Datei- und Zitatverarbeitung (`files/`, `citations.ts`) · `auditLog.ts` · `endpoints.custom` mit `baseURL` + `apiKey` für OpenAI-kompatible Endpunkte. |
| **OmniRoute — verifiziert** | Basis-URL konfigurierbar, Standard `http://127.0.0.1:20128`; dokumentierte Installation: Docker-Container `omniroute`, **Host-Port 24615 → Container 20128**. Auth: **beide** Header werden gesetzt — `Authorization: Bearer <key>` **und** `x-api-key: <key>`. Key mit **`manage`-Scope**. Verifizierte Endpunkte: `GET/POST/DELETE /api/v1/management/proxies`, `GET /api/v1/management/proxies/health`, `PUT|POST /api/v1/management/proxies/bulk-assign`, `GET /api/v1/management/proxies/assignments`, `GET /api/providers`, `PATCH /api/providers`, `GET /api/settings/oneproxy`, `GET /api/usage/proxy-logs`. **7 Provider-Connections:** `openrouter`, `uncloseai`, `opencode`, `duckduckgo-web`, `cloudflare-playground`, `chipotle`, `aihorde`. **Bekannte Eigenheit:** `/api/usage/proxy-logs` liefert teils ein **nacktes Array** statt eines Objekts → der Adapter muss defensiv normalisieren. |
| **OmniRoute — zu prüfen** | Existenz und Form einer **Inferenz-API** · Routing-/Fallback-Logik · Modell-ID-Format · Streaming-Verhalten · Kosten-/Token-Telemetrie · Multimodalität · Dateien · Audio · Video · Embeddings · MCP · A2A · Version/Image-Tag · Ratenlimits. **Im Repository gibt es dafür keinen Beleg** (Suche nach `chat/completions`, `/v1/models`, `embeddings` in `schaltwerk`: kein Treffer). |

## 0.5 · Ablage-Konvention ⟨†8⟩

**BEKANNT / verbindlich.** Jede Arbeit an diesem Repository liegt in **ihrem eigenen Ordner** auf Wurzelebene. Dieser Zweig baut ausschließlich innerhalb von **`omnia-atelier/`**. Andere Zweige legen ihren Ordner daneben. Gemeinsame Orte — Wurzel, `schaltwerk/`, die beiden ZIP-Archive — werden von keinem Zweig verändert.

```
omniauto/
├── Kurz-main (1).zip        ← Material · NICHT ANFASSEN
├── LibreChat-main.zip       ← Material · NICHT ANFASSEN
├── schaltwerk/              ← bestehendes Werkzeug · NICHT ANFASSEN
├── omnia-atelier/           ← DIESER ZWEIG
└── <ordner-andere-zweige>/  ← daneben, ohne Berührung
```

---

# 1 · Gesetzte technische und produktstrategische Grundlagen

Folgende Punkte sind gesetzt und dürfen nicht mehr als offene Grundsatzfrage behandelt werden.

## 1.1 OmniRoute ist ein fester Bestandteil — mit offener Fähigkeitsfrage ⟨†3⟩

OmniRoute wird verbindlich als zentrale Infrastruktur für Modelle, Provider und Routing verwendet — **jeweils nur so weit, wie die reale Installation es hergibt.**

OmniRoute soll insbesondere für folgende Aufgaben eingeplant werden:

- Modellzugang
- Provider-Abstraktion
- Modellrouting
- Fallbacks
- Verfügbarkeit
- Latenz
- Kosten- und Qualitätsregeln
- parallele Modellverarbeitung, wenn sinnvoll
- multimodale Modellfähigkeiten, **sofern in der realen Installation verfügbar**
- gegebenenfalls Embeddings, Dateien, Bilder, Audio, Video, MCP oder A2A, **sofern real unterstützt und konfiguriert**

WICHTIG:

Die konkrete OmniRoute-Version, API, Konfiguration, Providerliste, Modellverfügbarkeit, Secret-Verwaltung, Fallback-Logik, Telemetrie und Deployment-Art müssen zuerst untersucht werden.

Es dürfen keine OmniRoute-APIs, Endpunkte, Konfigurationsdateien oder Funktionsnamen erfunden werden.

Wenn konkrete Syntax oder konkrete APIs nicht verifiziert sind, verwende ausschließlich klar gekennzeichneten Pseudocode mit der Zeile:

`PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX`

Die App-UI darf nicht direkt an OmniRoute gekoppelt sein.

Die App soll über einen eigenen Application Layer und einen Router Adapter mit OmniRoute kommunizieren.

⟨†3⟩ **Der Router Adapter sitzt hinter einem Port (Interface)** mit mindestens `capabilities()`, `invoke()`, `abort()`. Grund: Ein negativer Fähigkeitsbefund darf das Produktmodell nicht zerstören. Es muss drei Implementierungen geben können: OmniRoute-Adapter, Direkt-Provider-Adapter (Notbetrieb) und Mock-Adapter (Tests, offline — Präzedenz: die 34 `schaltwerk`-Tests laufen ohne Netz und ohne OmniRoute).

## 1.2 LibreChat wird als technische Modulquelle genutzt ⟨†5⟩

LibreChat soll nicht als UI-Referenz dienen.

Die neue Anwendung darf nicht wie LibreChat aussehen und darf nicht einfach auf eine Chat-Oberfläche reduziert werden.

LibreChat wird als potenzielle Quelle für bereits erprobte technische Bausteine untersucht.

Zu prüfen sind insbesondere mögliche Wiederverwendungs- oder Adaptionskandidaten:

- Authentifizierung
- Nutzer- und Session-Management
- Thread- oder Verlaufssysteme
- Streaming
- Datei- und Kontextverarbeitung
- Tool-Integration
- Agenten-/Fähigkeiten-Integration
- Presets oder Rollenlogik
- OpenAI-kompatible Endpoint-Anbindung
- Berechtigungen
- Datenbank- und Persistenzmuster
- Fehlerbehandlung
- Sicherheitsmechanismen

Für jeden untersuchten LibreChat-Bereich soll entschieden werden:

- BEIBEHALTEN
- ADAPTIERT ÜBERNEHMEN
- NUR ALS REFERENZ NUTZEN
- NICHT ÜBERNEHMEN

WICHTIG:

LibreChat darf nicht als Gesamtprodukt eingebettet werden, wenn dadurch dessen UI, Datenmodell, Architekturzwänge oder Produktlogik die neue Anwendung dominieren würden.

⟨†5⟩ **Bewertungsmaßstab:** LibreChat wird **nie als Abhängigkeit eingebunden**. Es gibt keine Imports, keine gemeinsame Datenbank, keine gemeinsamen Typen. Übernommen werden **Ideen, Feldnamen und Reihenfolgen**, dokumentiert in `omnia-atelier/docs/REUSE.md` mit Quelle und Lizenz. Begründung: MIT-Lizenz ist freizügig, aber MongoDB + Meilisearch + pgvector + Express-Legacy + 102 Client-Abhängigkeiten sind für ein lokales Single-User-Produkt teurer als nützlich.

## 1.3 Mesh AI ist eine persönliche Inspirationsrichtung — präzise, nicht romantisch ⟨†2⟩

⟨†2⟩ **Klarstellung:** Im Repository liegt **MashAI** (`Kurz-main (1).zip`, MPL-2.0). **ANNAHME: mit „Mesh AI" ist MashAI gemeint — ZU PRÜFEN.** MashAI ist **kein intelligentes System mit Gedächtnis**, sondern ein **Workspace für fremde KI-Weboberflächen**: Profile, Tabs, Session-Persistenz, Side-Panel, Adblocking.

MashAI soll nicht als visuelle Vorlage kopiert werden. ⟨†6⟩ **Wegen MPL-2.0 (file-level copyleft) gilt: keine Code-Kopie, keine Assets.**

Es ist eine Inspirationsquelle für eine persönlichere, vernetztere, kontextbewusstere und kontinuierlichere AI-Erfahrung.

Die konkrete Bedeutung von Mesh AI muss vor der Implementierung präzisiert werden.

Zu klären ist insbesondere:

- Was bedeutet „persönlich" konkret?
  → **arbeitsbezogen, nicht personenbezogen.** Erinnert werden Arbeitsräume, Entscheidungen, verworfene Alternativen und Arbeitseinstellungen — keine biografischen Merkmale, keine Stimmungsprofile.
- Soll die Leitassistenz sich an Arbeitsstücke erinnern?
  → **Ja.** Versionen, Verlauf, offene Fragen, verworfene Alternativen. Vollständig einsehbar und löschbar.
- Soll sie sich an Präferenzen erinnern?
  → **Ja, aber nur an explizit gesetzte Arbeitseinstellungen:** Standard-Fähigkeiten, Budgetgrenzen, Schreibverbote, Materialquellen, Ausgabeformate.
- Soll sie proaktive Hinweise geben?
  → **Ja, mit Schwellen:** eine Blockade entsteht · Material hat sich seit dem letzten Lauf geändert · eine frühere Entscheidung wird durch neues Material berührt. **Nie ohne Bezug zu einem konkreten Objekt.**
- Welche Informationen dürfen dauerhaft gespeichert werden?
  → Arbeitsstücke, Versionen, Runs, Material-Hashes, Routing-Protokolle, **explizit bestätigte** Arbeitseinstellungen, Audit-Einträge.
- Welche Informationen müssen temporär bleiben?
  → Alles, was nur für einen Lauf gilt: Zwischenergebnisse, Kandidaten, Kontextfenster, nicht bestätigte Vorschläge.
- Wie kann der Nutzer gespeicherte Erinnerungen sehen?
  → Ein eigenes Register **„Gedächtnis"** im Arbeitsraum: Schlüssel, Wert, Herkunft („gesetzt von dir" / „vorgeschlagen am …"), Datum, Verwendung.
- Wie kann der Nutzer Erinnerungen korrigieren?
  → Jeder Eintrag einzeln bearbeitbar, mit Zeitstempel der Änderung.
- Wie kann der Nutzer Erinnerungen löschen?
  → Einzeln oder als Sammellöschung („Alles vergessen"); Löschung ist **hart** (kein Soft-Delete) und wird im Audit vermerkt.
- Wann darf die Assistenz proaktiv handeln?
  → Bei reinen Lese- und Analysehandlungen innerhalb eines bestätigten Arbeitsplans.
- Wann muss die Assistenz ausdrücklich fragen?
  → Bei jeder Schreibhandlung, jeder externen Wirkung, jedem Qualitätsklassenwechsel, jedem Datenschutzwechsel, jedem Speichervorschlag für Gedächtnis.

Die Anwendung darf niemals den Eindruck erwecken, dass eine KI „alles über den Nutzer weiß", wenn dies nicht transparent, kontrollierbar und technisch begrenzt ist.

⟨†2⟩ **Anti-Illusions-Regel:** Es gibt keine Formulierung wie „Du bevorzugst normalerweise…", es sei denn, die Quelle ist ein sichtbarer Gedächtnis-Eintrag mit Datum und Bearbeiten-Knopf.

## 1.4 Zentrale native Leitassistenz

Die Anwendung erhält eine zentrale Leitassistenz.

Diese Leitassistenz ist kein austauschbarer Chatbot in einer Sidebar.

Sie ist die verbindende Intelligenz des gesamten Produkts.

Sie soll:

- den aktuellen Arbeitskontext verstehen
- Material einordnen
- Arbeitsabsichten erkennen
- offene Fragen sichtbar machen
- relevante Fähigkeiten oder Modelle anfordern
- Ergebnisse zusammenführen
- Routing- und Fallback-Ereignisse verständlich erklären, **wenn sie relevant sind**
- Arbeitsstücke versionieren und fortsetzen helfen
- den Nutzer auf Widersprüche, Risiken, fehlende Quellen oder blockierte Entscheidungen hinweisen
- Vorschläge machen, ohne die Kontrolle des Nutzers zu übernehmen

Die Leitassistenz ist eine Anwendungsrolle und nicht zwingend ein einzelnes Modell.

Sie kann unterschiedliche Modelle, Tools oder spezialisierte Fähigkeiten über OmniRoute verwenden.

Die Leitassistenz darf nicht:

- stillschweigend Repository-Dateien verändern
- stillschweigend deployen
- stillschweigend externe Aktionen ausführen
- Modellwechsel bei kritischen Ergebnissen verbergen
- persönliche Daten oder Memory ohne transparente Regeln speichern
- behaupten, Repository-Inhalte oder Quellen geprüft zu haben, wenn kein Zugriff bestand
- technische Agentenaktivität nur zur Dekoration darstellen

Irreversible oder externe Aktionen müssen durch den Nutzer bestätigt werden.

⟨†1⟩ **Weiterentwicklung aus dem Bestand:** Die vorhandene Bad-Wolf-Instanz in `schaltwerk` (Stimme als protokollierte Tat, Ablage, Wachdienst mit Anti-Spam-Schwelle, Goldene Regeln) ist die Keimzelle dieses Contracts. Die **Disziplin** wird übernommen, nicht die Figur.

---

# 2 · Zentrale Produktfrage

Entwickle zuerst das eigentliche Produktmodell.

Beantworte nicht zuerst:

„Wie sieht ein OmniRoute-Dashboard aus?"

Beantworte stattdessen:

⟨†9⟩ **Und beantworte zuallererst: „Was entsteht hier, das es ohne diese App nicht gäbe?"**

- Was macht der Nutzer in dieser App eigentlich?
- Welche zentrale Tätigkeit steht im Mittelpunkt?
  → **Urteilen, nicht Fragenstellen.**
- Was gibt der Nutzer hinein?
- Was entsteht daraus?
- Wie unterscheidet sich das Ergebnis von einer normalen Chat-Antwort?
  → Eine Chat-Antwort ist eine **Äußerung ohne Haftung**. Ein Arbeitsstück ist ein **Objekt mit Struktur, Herkunft, Version und Status** — zitier-, kritisier-, versionier- und übergebbar, ohne dass die Entstehung neu verhandelt werden muss.
- Welche Rolle spielt Repository-Content?
  → **Material ersten Ranges**: prüfbar, versioniert, real.
- Welche Rolle spielt die Leitassistenz?
- Wann wird OmniRoute sichtbar?
  → wenn eine Routing-Entscheidung **Qualität, Kosten, Latenz, Datenschutz oder Fähigkeiten** des Ergebnisses beeinflusst.
- Wann bleibt OmniRoute unsichtbar?
  → wenn der Nutzer nur wissen muss, **was** herauskam, nicht **wo** es herkam. Ein gerader Lauf ohne Anomalie erzeugt **keine** Router-Meldung.
- Wann sind mehrere Modelle sinnvoll?
  → bei **Urteilen mit Konfliktpotenzial**; nicht bei faktischen Extraktionen.
- Wann sind Tools oder Agenten sinnvoll?
  → wenn eine Behauptung nur durch **Zugriff** belegbar ist (Datei lesen, Code suchen, Version vergleichen); nicht, um Beschäftigung zu demonstrieren.
- Welche Entscheidungen kann der Nutzer beeinflussen?
  → Materialauswahl, Absicht, Arbeitsplan, Fähigkeiten/Modelle, Budgetgrenzen, Bestätigung aller externen oder schreibenden Aktionen, Inhalt des Arbeitsstücks, Versionierung, Memory.
- Welche Dinge passieren automatisch?
  → Material-Indexierung, Arbeitsplan-Vorschlag, Fähigkeitsauswahl innerhalb der Policy, Routing, Fallback innerhalb der Policy, Quellenverknüpfung, Status- und Eventprotokoll, Versionierung.
- Warum ist diese App kein Chatbot?
  → weil die primäre Einheit nicht die Nachricht ist, sondern das **Arbeitsstück**.
- Warum ist diese App kein Agent-Dashboard?
  → weil Aktivität nicht zum Selbstzweck angezeigt wird. Keine Agenten-Karten, sondern **Spuren am Arbeitsstück**.
- Warum ist diese App kein Node-Editor?
  → weil die Verbindungen, die hier zählen, **semantisch** sind (stützt / widerspricht / blockiert), nicht technisch.
- Warum sollte sich diese Arbeitsweise eigenständig, sinnvoll und interessant anfühlen?
  → weil drei Dinge zusammenkommen, die es so nicht gibt: **prüfbares Material**, **haftendes Ergebnis**, **eine Instanz, die den Überblick behält** — bei austauschbarer Infrastruktur darunter.

Die bevorzugte Richtung ist:

Signal Garden / Omnia Atelier

Ein digitaler Arbeitsraum, in dem aus Material belastbare Arbeitsstücke entstehen.

Material kann beispielsweise sein:

- Repository-Inhalte
- Code
- Komponenten
- Dokumentation
- Notizen
- Ideen
- Aufgaben
- Dateien
- Anforderungen
- Entscheidungen
- frühere Ergebnisse
- Quellen
- Medien, falls später unterstützt

Arbeitsstücke können beispielsweise sein:

- technische Entscheidungen
- Produktkonzepte
- Architekturpläne
- Spezifikationen
- Content-Systeme
- Research-Ergebnisse
- Strategiepapiere
- Roadmaps
- Code-Änderungsvorschläge
- Briefings
- überprüfbare Hypothesen
- Umsetzungspläne

Der Nutzer arbeitet nicht mit vielen separaten AI-Tools.

Er arbeitet mit einer intelligenten Werkstatt.

Die Leitassistenz verbindet Material, Kontext, Modelle, Tools, Ergebnisse und Verlauf.

⟨†9⟩ **Regel:** Ohne Material gibt es kein Arbeitsstück. Die Leitassistenz darf eine Absicht **nicht** in einen Lauf überführen, wenn kein Material benannt ist — sie muss nach Material fragen oder eines vorschlagen. Das verhindert, dass das Atelier zum Chatbot degeneriert.

---

# 3 · Entwickle drei wirklich unterschiedliche Produktmodelle

Entwickle drei unterschiedliche Ansätze.

Es dürfen nicht drei visuelle Varianten derselben Chat-App sein.

⟨†9⟩ Sie müssen drei **unterschiedliche Kernhandlungen** haben: **herstellen · prüfen · übergeben.**

Für jeden Ansatz liefere:

1. Name
2. Kernidee
3. zentrale Nutzerhandlung
4. Was sieht der Nutzer beim Start?
5. Was bringt der Nutzer ein?
6. Was geschieht danach?
7. Welche Rolle übernimmt die Leitassistenz?
8. Welche Rolle übernimmt OmniRoute?
9. Welche Rolle übernehmen Modelle?
10. Welche Rolle übernehmen LibreChat-Module?
11. Welche Rolle übernimmt Mesh-AI-inspirierte Kontinuität?
12. Welche Rolle übernimmt vorhandener Repository-Content?
13. Wie wird Aktivität sichtbar?
14. Wie sieht eine typische Nutzung aus?
15. Was unterscheidet das Konzept vom alten Schaltwerk? ⟨†1⟩
16. Risiken des Konzepts
17. Chancen des Konzepts
18. **ASCII-Skizze**

⟨†1⟩ Zu Punkt 15: „altes Schaltwerk" ist **kein** Node-Editor, sondern Proxy-Logistik mit Tabellen, SSE-Job und RAM-Ringpuffern. Der Unterschied ist also: **Arbeit als Objekt** vs. **Infrastruktur als Tabelle**.

Mindestens einer der Ansätze soll das Signal-Garden-/Atelier-Prinzip konsequent ausarbeiten.

Beispielhafte Richtungen können sein:

- Signal Garden / Omnia Atelier — Kernhandlung *herstellen*
- Brief Foundry / Werkbrief-Gießerei — Kernhandlung *übergeben*
- Evidence Room / Beweisraum — Kernhandlung *prüfen*

Diese Namen sind nur Orientierung und dürfen verbessert werden.

Empfiehl anschließend klar einen Ansatz als Grundlage.

⟨†9⟩ **Maßgabe:** Die Stärken der beiden nicht gewählten Modelle müssen **als Werkzeuge im Gewinner-Modell erhalten** bleiben (der Beweisstatus wird zum Qualitätsmaßstab jeder Kernaussage; der Werkbrief zur Übergabeform).

---

# 4 · Repository-first Discovery ⟨†4⟩

Bevor endgültige technische oder gestalterische Entscheidungen getroffen werden, muss das Repository untersucht werden.

Erstelle einen konkreten Discovery-Plan.

Untersuche mindestens:

- Verzeichnisstruktur
- Root-Dateien
- Monorepo- oder Single-App-Struktur
- Build- und Startprozess
- lokale Entwicklungsumgebung
- Deployment
- CI/CD
- Frontend
- Backend
- Frameworks
- Routen
- Komponenten
- Styling
- UI-Bibliotheken
- Design Tokens
- Zustandverwaltung
- Datenmodelle
- Datenbank
- ORM
- API-Struktur
- Authentifizierung
- Berechtigungen
- Persistenz
- Caching
- Hintergrundjobs
- Streaming
- WebSocket oder SSE
- Logging
- Monitoring
- Error Handling
- Tests
- Sicherheitsmechanismen
- Umgebungsvariablen
- Secret-Verwaltung
- bestehende Provider-Anbindungen
- bestehende OmniRoute-Anbindung
- OmniRoute-Version und Konfiguration
- bestehende LibreChat-Anteile oder Integrationen
- bestehende Agenten-, Tool- oder MCP-Logik
- vorhandener Custom Content
- Wissensquellen
- Dateien
- Assets
- bestehende UI
- bestehende Workflows
- bisherige Schaltwerk-Logik ⟨†1⟩
- Node-/Graph-Daten ⟨†1⟩
- Abhängigkeiten
- technische Schulden
- Lizenz- und Copyright-Fragen ⟨†6⟩
- relevante Dokumentation
- offene Risiken

Für jeden Bereich erkläre:

- Was konkret geprüft werden muss
- Warum dies geprüft werden muss
- Welche Entscheidung davon abhängt
- Ob der Bereich voraussichtlich beibehalten, erweitert, neu interpretiert, ersetzt oder nicht angefasst werden sollte

⟨†7⟩ **Wichtig für diese Prüfliste:** Mehrere dieser Bereiche existieren im Repository **nicht** (Monorepo, CI/CD, Deployment, Datenbank, ORM, WebSocket, Secret-Management, Authentifizierung, Node-/Graph-Daten). „**Nicht vorhanden**" ist ein gültiges, zu dokumentierendes Prüfergebnis — **kein** Anlass zu Spekulation und **kein** Anlass, etwas zu erfinden.

Erstelle anschließend einen Preservation Contract.

Der Preservation Contract muss klar unterscheiden:

- BEIBEHALTEN
- ERWEITERN
- NEU INTERPRETIEREN
- ERSETZEN
- NICHT ANFASSEN

WICHTIG:

Es darf nichts pauschal ersetzt werden, nur weil eine neue UX entsteht.

Bestehende funktionierende Logik, Content-Pipelines, Authentifizierung, Datenmodelle, Provider-Konfigurationen, Build-Prozesse oder getestete Komponenten müssen zuerst verstanden werden.

⟨†4⟩ **Realität:** Von all dem existiert genau **eine** funktionierende Anwendung (`schaltwerk`, 34 Tests) — ohne Login, ohne Datenbank, ohne CI/CD, ohne Deployment. Der Preservation Contract ist deshalb schmal und besteht im Kern aus vier Regeln:

- **NICHT ANFASSEN:** die beiden ZIP-Archive (kein Entpacken ins Repo, keine Code-Kopie, keine Assets — MPL-2.0 bei MashAI, **keine Lizenzdatei** bei `schaltwerk`), OmniRoute selbst, die laufende `schaltwerk`-Instanz, das Windows-zuerst-Prinzip von `schaltwerk`, die 8 dokumentierten offenen Punkte von `schaltwerk`.
- **BEIBEHALTEN:** `schaltwerk` als Ganzes (inkl. `HARVEST_TAG`, `px-`-Präfix, 1proxy-Schreibverbot, RAM-only-Key-Disziplin, Loopback-Bindung, `STARTEN.bat` mit CRLF), die acht Goldenen Regeln, die Design-Tokens und Anti-KI-Look-Regeln, der Dokumentationsstandard (`DOKUMENTATION.md` als Wahrheit, `CHANGELOG.md` als Historie), die 34 Tests als Regressionnetz.
- **NEU INTERPRETIEREN:** Bad Wolf → Leitassistenz · Ablage → Materialwand · Hub-Gedanke → Arbeitsräume · Wachdienst → Proaktivität mit Relevanzschwelle.
- **ERSETZEN:** RAM-only-Zustand → SQLite (Arbeitsstücke müssen wiederbetretbar sein); Tabellen-UI → Raum-UI. **Ausnahme:** die RAM-Disziplin für **Secrets** bleibt bestehen.

---

# 5 · Schaltwerk kritisch neu denken → **Sichtbarkeit neu denken** ⟨†1⟩

⟨†1⟩ **Korrektur der Prämisse:** Das bisherige Schaltwerk-Prinzip ist **kein** Node-/Graph-Prinzip. `schaltwerk` enthält keine Nodes, keine Kanten, keine visuellen Verbindungen. Es ist Proxy-Logistik. Die nachfolgende Analyse wird deshalb als **Zielprinzip** beantwortet, nicht als Umbau: *Was wäre eine Verbindung wert, wenn es sie gäbe — und was darf deshalb niemals als Verbindung gezeigt werden?*

Analysiere:

- Welche Vorteile haben Nodes?
  → Zeigen Datenfluss (**hier: nein** — Datenfluss ist Infrastruktur, nicht Arbeit) · Abhängigkeit (**teils** — nur wenn die Abhängigkeit eine Aussage betrifft) · direkte Manipulation (**nein** — der Nutzer will kein System bauen) · Übersicht über Komplexität (**nein** — verlagert sie nur) · Parallelität sichtbar machen (**teils** — aber Parallelität ist hier ein Zustand) · räumliche Arbeitsfläche (**ja** — als Atelier, nicht als Graph).
- Wann helfen visuelle Verbindungen?
  → Nur wenn sie eine **inhaltliche Beziehung** zeigen.
- Wann helfen räumliche Arbeitsflächen?
  → Wenn sie Material, Bearbeitung und Ergebnis **gleichzeitig** halten.
- Wann erzeugen sie unnötige Komplexität?
  → Sobald sie **Infrastruktur** beschreiben.
- Wann zeigen sie eine echte inhaltliche Beziehung?
  → Wenn die Kante eine Aussage stützt, widerlegt, blockiert oder herleitet.
- Wann zeigen sie nur technische Infrastruktur?
  → Sobald sie Rechenschritte statt Bedeutung darstellen.
- Welche Informationen gehören sichtbar auf die Oberfläche?
- Welche Informationen gehören in einen Hintergrundprozess?
- Wann wird aus einem Arbeitsraum nur ein technisches Diagramm?
  → Wenn die sichtbaren Verbindungen Rechenschritte statt Bedeutung darstellen.
- Welche Teile einer bestehenden Schaltwerk-Logik könnten technisch wertvoll bleiben?
  → **Job-Phasen mit Statusabfrage** (`/api/job-status`, 5-s-Polling, reload-verlustfrei) · **409-Doppelstartsperre** (synchron im Handler geprüft) · **SSE-Übertragung** (`StreamingResponse`) · **Ringpuffer mit Anti-Spam-Regel** (60 Zeilen) · **Risiko-Ausschluss vor dem Schreiben** · **Normalisierung inkonsistenter Fremdantworten** (`unwrap_list`) · **Validierung vor dem Speichern** · **harte Deadline pro Teilschritt** (`probe_one`).
- Wie können technische Graphen in eine verständliche, semantische Darstellung übersetzt werden?
  → **Übersetzungsregel:** Statt „Node A → Node B" heißt es: „Diese Aussage stützt sich auf diese drei Quellen; diese Quelle widerspricht; diese Prüfung steht noch aus." Die Topologie verschwindet, die **Begründung** bleibt.

Formuliere klare Regeln.

**Beispiel für sinnvolle sichtbare Beziehungen** (⟨†1⟩: ausschließlich diese vier, ausschließlich zwischen Inhaltsobjekten):

| Kante | Frage, die sie beantwortet |
|---|---|
| **STÜTZT** | Dieses Repository-Modul stützt diese Entscheidung. → *Warum soll ich das glauben?* |
| **WIDERSPRICHT** | Diese Quelle widerspricht dieser Annahme. → *Was spricht dagegen?* |
| **BLOCKIERT** | Diese offene Frage blockiert eine Freigabe. → *Was fehlt noch?* |
| **ENTSTAND AUS** | Dieses Ergebnis basiert auf diesen Materialien. → *Wo kommt das her?* |

**Beispiel für Informationen, die standardmäßig nicht sichtbar sein sollten:**

- jeder einzelne Modellaufruf
- interne HTTP-Requests
- Token-Zähler pro Request
- jeder Retry
- interne Provider-IDs
- rohe technische Stacktraces
- jede Hintergrundentscheidung ohne Relevanz für den Nutzer

Die Regel lautet:

**Der Nutzer soll sehen, was er verstehen, beeinflussen, prüfen oder später begründen muss.**

⟨†9⟩ Alles andere existiert — aber im Run-Log, nicht auf der Fläche.

---

# 6 · Entwickle eine eigenständige visuelle Sprache

Die App darf modern und außergewöhnlich wirken.

Sie darf aber nicht einfach auf folgende Muster zurückfallen:

- Standard-Dashboard
- permanente Sidebar
- Kartenraster
- generische Nodes
- sterile Admin-Oberfläche
- austauschbares AI-Chatfenster
- Cyberpunk
- Neon
- Glassmorphism
- Glow ohne Bedeutung
- Partikel ohne Funktion
- übertriebene Animation
- dekorative Schalter ohne echte Wirkung

⟨†9⟩ **Zusatz:** Die visuelle Sprache wird aus den **vorhandenen Repo-Tokens** entwickelt (Abschnitt 0.1), nicht neu erfunden. Und: das vorhandene Partikel-Porträt in `schaltwerk` wird **nicht** übernommen — seine *Disziplin* schon (`prefers-reduced-motion` → Standbild, Pause bei `document.hidden`, Performance gemessen statt geschätzt).

Entwickle stattdessen eine visuelle Sprache aus der Funktion des Produkts.

Beschreibe konkret:

- räumliche Struktur
- Materialbereiche
- Arbeitsfläche
- Ergebnisbereiche
- Verlauf
- Quellen
- offene Fragen
- Spannungen und Konflikte
- Entscheidungen
- Farben
- Typografie
- Bewegungsprinzipien
- Zustände
- Interaktionen
- Übergänge
- Informationshierarchie
- visuelles Feedback
- Fehlerdarstellung
- Fallbackdarstellung
- Fortschrittsdarstellung
- Accessibility
- responsive Verhalten

Jedes visuelle Element muss eine Funktion erfüllen.

**Beispiel für ein mögliches Raumprinzip** (⟨†9⟩: als Vorschlag ausformuliert):

- **Materialrand** (links, schmal): Quellen, Dateien, Repository-Inhalte, Notizen und Anforderungen — als **Objekte mit Herkunft und Prüfstatus** (Bogen = Datei, Zettel = Notiz, Mappe = früheres Arbeitsstück), nicht als Dateibaum.
- **Werkfläche** (Mitte, dominant, ~60 %): Aktives Arbeitsstück, Entscheidungen, Fragen, Alternativen, Konflikte und Bearbeitung — als **zusammenhängendes Dokument**, nicht als Kacheln.
- **Ergebnisrand** (rechts, schmal): verdichtete Ergebnisse, Exporte, Versionen, nächste Schritte und Freigaben — der einzige Ort mit bestätigungspflichtigen Knöpfen.
- **Fragenleiste** (unten, persistent): offene Fragen und Spannungen. Persistent sichtbar, weil Blockaden die Arbeit steuern.
- **Stimme** (oben, **eine Zeile**): die Leitassistenz. Kein Chatfenster.

⟨†9⟩ **Beispiel für eine funktionale Gestaltungsentscheidung:** Das Arbeitsstück wird in einer **Serifenschrift** gesetzt. Funktion: Der Text soll sich wie ein **Werkstück** lesen, nicht wie eine Chatnachricht. Das ist der stärkste einzelne anti-chatbotische Eingriff im gesamten Design.

⟨†9⟩ **Belegstatus als durchgehendes Qualitätsmaß:** `● belegt · ◐ teilweise · ? offen · ✗ widersprochen · ╱ unbelegbar`. Immer als **Zeichen + Text**, nie Farbe allein. `╱ unbelegbar` ist **kein Fehler**, sondern Ehrlichkeit; Freigabe ist bei `✗` und ungelöstem `?` gesperrt, bei `╱` erlaubt.

⟨†9⟩ **Bewegungsprinzip:** Bewegung trägt Zustand, sonst nichts. Werkzeugspur füllt sich = Fortschritt · Abschnitt setzt sich = Ergebnis erzeugt · Bernstein-Puls = neue Blockade · Kante zeichnet sich ein = neue Beziehung erkannt. Sonst: **nichts.**

Die visuelle Gestaltung soll sich wie ein digitales Atelier, eine Werkstatt oder ein Denkraum anfühlen.

Nicht wie ein Infrastruktur-Kontrollraum.

---

# 7 · OmniRoute technisch einordnen

OmniRoute ist gesetzt.

⟨†3⟩ **Aber:** Ordne OmniRoute als reale Infrastruktur mit **offener Fähigkeitsfrage** ein, nicht als bloßen Designbegriff und nicht als gesicherte Modellebene.

Beschreibe einen Ziel-Datenfluss:

```
Nutzer
  ↓
Omnia Atelier UI
  ↓
Application Layer
  ↓
Leitassistenz / Intent- und Kontextlogik
  ↓
Orchestrierungs-Policy
  ↓
Router-Port  ──►  OmniRoute Adapter        ⟨†3⟩
  ↓
OmniRoute
  ↓
Provider / Modelle / Fähigkeiten
  ↓
Ergebnisse / Events / Telemetrie
  ↓
Application Layer
  ↓
UI
  ↓
Nutzer
```

Entwickle mindestens einen konkreten End-to-End-Workflow.

Beispiel:

Nutzer möchte beurteilen, ob die bestehende Schaltwerk-Logik als Hintergrundorchestrierung erhalten bleiben kann. ⟨†1⟩

```
Aufgabe
  ↓
Material- und Repository-Analyse
  ↓
Leitassistenz erstellt Arbeitsplan
  ↓
Nutzer bestätigt oder korrigiert
  ↓
Orchestrierungs-Policy bestimmt benötigte Fähigkeiten
  ↓
OmniRoute routet die Analyse
  ↓
Modell A analysiert Struktur und Abhängigkeiten
Modell B prüft Risiken und Gegenargumente
  ↓
Synthese
  ↓
Qualitätsprüfung
  ↓
Arbeitsstück:
Entscheidung, Begründung, Quellen, Risiken, offene Prüfungen
  ↓
Gespeicherte Version und Verlauf
```

Erkläre dabei:

- Warum welches Modell oder welche Fähigkeit verwendet wird
- Wann ein einzelnes Modell genügt
  → Extraktion (Struktur lesen, Inventar) und Formulierung: **ein** Modell, kein Zweitmodell.
- Wann mehrere Modelle sinnvoll sind
  → **Urteil mit Konfliktpotenzial**: zwei Modelle **parallel**. **Beweisprüfung**: zwei Modelle mit **unterschiedlichen Rollen** (Belegsucher / Gegenprüfer) — gleichartige Modelle bestätigen sich sonst gegenseitig.
- Wann Parallelisierung sinnvoll ist
- Wann sie unnötig ist
  → bei Extraktion, bei Abhängigkeiten zwischen Teilaufgaben, unterhalb der Budgetschwelle, bei vom Nutzer festgelegter Fähigkeit.
- Wie Fallbacks funktionieren sollen
  → **Klassenmodell** (⟨†3⟩): Wechsel **innerhalb** einer Qualitätsklasse läuft automatisch und steht nur im Run-Log. Wechsel **zwischen** Klassen wird immer am betroffenen Abschnitt gemeldet und dauerhaft in der Version vermerkt. Wechsel über eine **Datenschutzgrenze** ⇒ Rückfrage. Fähigkeit unavailable ⇒ Abschnitt bleibt `offen`, kein künstlicher Abschluss. Budgetgrenze ⇒ kontrollierter Stopp.
- Welche Fehlerarten unterschieden werden müssen
  → mindestens: `UNAVAILABLE`, `TIMEOUT`, `RATE_LIMITED`, `AUTH_INVALID`, `BUDGET_EXCEEDED`, `MALFORMED_RESPONSE`, `CAPABILITY_MISSING`, `MATERIAL_UNREADABLE`, `POLICY_VETO`. Regel: **kein** Fallback bei `AUTH_INVALID`, `BUDGET_EXCEEDED`, `POLICY_VETO`.
- Wie Abbruch funktioniert
  → jederzeit, nie destruktiv; bereits erzeugte Abschnitte bleiben als Version erhalten.
- Wie Wiederaufnahme funktioniert
  → am letzten **abgeschlossenen Abschnitt**, nicht am letzten Token; gespeichert werden Material-Hashes, Abschnittsstände, verbrauchte Fähigkeiten, Budgetverbrauch, Routing-Ereignisse.
- Wie Kosten- und Latenzgrenzen behandelt werden
  → **vor** dem Lauf sichtbar und einstellbar; Warnung bei 80 %; kontrollierter Stopp bei 100 %. Zeitlimits **pro Teilschritt** (Präzedenz `probe_one`), nicht nur pro Gesamtlauf.
- Wie Routing-Entscheidungen dokumentiert werden
  → Routing-Protokoll je Run (Fähigkeit → Modell → Grund → Dauer → Ereignisse), Teil des Arbeitsstücks, damit zitierfähig.
- Welche Informationen die UI zeigen soll
  → Belegstatus je Kernaussage · Fallback mit Auswirkung · blockierende Fragen · Kosten **pro Run** · Routing als Zusammenfassung · Fähigkeitsnamen in Klartext.
- Welche Informationen verborgen bleiben sollen
  → interner Request-Verlauf · erfolgreiche Einzel-Retries · interne Provider-IDs · Token-Zähler pro Request · vollständige Header · Hintergrundentscheidungen ohne Relevanz.
- Wie verhindert wird, dass ein Fallback die Ergebnisqualität unbemerkt verändert
  → (1) jede Fähigkeit hat eine Qualitätsklasse in der Policy, Klassenwechsel ist meldepflichtig; (2) jeder Abschnitt speichert unveränderlich, welche Fähigkeit und welches Modell ihn erzeugt hat; (3) das Arbeitsstück trägt einen Klassen-Vermerk; (4) der Nutzer kann jeden betroffenen Abschnitt gezielt neu erzeugen, nicht das ganze Werk.

Es dürfen keine erfundenen OmniRoute-Aufrufe als echte Syntax dargestellt werden.

Nicht verifizierte Beispiele müssen als PSEUDOCODE markiert werden mit der Zeile:

`PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX`

---

# 8 · LibreChat und Mesh AI technisch sinnvoll einarbeiten

Entwickle eine Reuse-Matrix.

Für LibreChat unterscheide:

- direkt wiederverwendbar, falls kompatibel
- adaptiert wiederverwendbar
- nur als Architektur- oder Implementierungsreferenz
- nicht übernehmen

Berücksichtige:

- Lizenz **⟨†5⟩: MIT — freizügig**
- Sicherheit
- Datenmodell-Kompatibilität **⟨†5⟩: Mongo-Dokumente vs. relationale Arbeitsstück-Versionen ⇒ ungünstig**
- Abhängigkeitsrisiken **⟨†5⟩: hoch — 102 Client-Deps, Cluster-Infrastruktur**
- UI-Abhängigkeiten **⟨†5⟩: hoch — und ausdrücklich nicht gewünscht**
- Migrationsaufwand **⟨†5⟩: hoch**
- Testbarkeit **⟨†5⟩: schwer — Cluster nötig**
- langfristige Wartbarkeit

⟨†5⟩ **Erwartete Richtung (zu begründen, nicht blind zu übernehmen):**
**adaptiert übernehmen** = Memory-Semantik (Key/Value + Opt-out + Partitionen), Nachrichtenbaum als Versionsmodell, Stream-Begriffe (Approval, Checkpoint, terminale Projektion, Abbruch), Zitatverarbeitung, Audit-Log, `endpoints.custom`-Form.
**nur als Referenz** = Run-/Stream-Implementierung, Authentifizierung (10 Strategien), ACL/Rollen, Datei-/RAG-Verarbeitung, Agenten/Tools/MCP/Skills, Presets, Projekte, Schedules/Subagenten.
**nicht übernehmen** = Frontend/UI, Mongo/Mongoose-Schemas, Express-Legacy.

Für Mesh-AI-inspirierte Funktionen entwickle ein kontrolliertes Konzept für: ⟨†2⟩

- Arbeitskontinuität
- kontextbezogene Hinweise
- persönliche Präferenzen
- Memory
- proaktive Assistenz
- Datenschutz
- Einsicht
- Korrektur
- Löschung
- Deaktivierung
- Berechtigung
- Auditierbarkeit

⟨†2⟩ **Vier Memory-Stufen, Standard ist die flüchtigste:** `SESSION` (nur dieser Lauf) → `WORKSPACE` (dieser Arbeitsraum, sichtbar im Register) → `GLOBAL` (nur nach ausdrücklicher Bestätigung) → `NEVER` (abschaltbar). Schlüssel nur `^[a-z_]+$` (LibreChat-Präzedenz), Wertlänge begrenzt, **Herkunft und Zeitstempel obligatorisch**, keine Inferenz über nicht abgelegte Inhalte.

MashAI liefert dabei nicht die Intelligenz, sondern drei übernehmbare Ideen: **Profile → Arbeitsräume** · **Side Panel → Gegenüberstellung** · **Session-Persistence + Settings-Migrationen → Wiederbetreten statt Neuladen**. ⟨†2⟩

Die Leitassistenz darf keine unklare Blackbox sein.

Definiere einen Leitassistenz-Contract.

Der Contract soll mindestens enthalten:

- unterstützte Intent-Typen
- erlaubte Aktionen ohne Bestätigung
  → Material lesen/indexieren/hashen · Arbeitspläne vorschlagen · Fähigkeiten innerhalb der Policy aufrufen · Fallback innerhalb derselben Qualitätsklasse · Abschnitte erzeugen, Belegstatus setzen, Versionen anlegen · Blockaden benennen.
- bestätigungspflichtige Aktionen
  → jeder Schreibzugriff · jede externe Wirkung · jeder Gedächtnis-Eintrag · jede Übergabe · jeder Fallback in eine niedrigere Qualitätsklasse oder über eine Datenschutzgrenze · jedes Überschreiten einer Nutzergrenze · jede Änderung an Goldenen Regeln.
- Memory-Regeln
- Kontextregeln
  → Kontext = Material + Arbeitsstück + Arbeitsplan + Laufstand + bestätigte Einstellungen. Kein Kontext aus Dateien, die nicht an der Werkbank liegen. Kontextfenster begrenzt **und dokumentiert**.
- Quellenregeln
  → **Jede Kernaussage braucht einen Belegstatus. Ohne Beleg ist sie `offen`, nicht wahr.** Es ist **verboten** zu behaupten, Material geprüft zu haben, wenn kein Zugriff stattfand — dann `╱ unbelegbar`, und die Leitassistenz sagt das ausdrücklich. Zitate mit **Datei + Zeile/Hash**, nie „laut Dokumentation".
- Modell-/Routing-Transparenz
  → auf Nachfrage vollständig; unaufgefordert nur bei qualitäts-, kosten-, latenz- oder datenschutzrelevanten Abweichungen; Modellwechsel zwischen Versionen immer vermerkt.
- Fehlerregeln
  → Klartext + Handlungsoption, kein Stacktrace in der Produktoberfläche, kein „Weitermachen als ob".
- Fallback-Regeln
- Audit-Regeln
  → protokolliert werden alle Runs, Routing-Ereignisse, bestätigungspflichtigen Aktionen mit Bestätigungsnachweis, Gedächtnis-Operationen, Materialzugriffe mit Hash. Append-only, nur lesbar, exportierbar.
- Rechte- und Sicherheitsgrenzen

---

# 9 · Vollständiger Benutzerablauf

Beschreibe einen vollständigen Nutzerablauf.

Nicht nur einzelne Buttons.

Beschreibe:

- Leerer Zustand
- erster Einstieg
- Material hinzufügen
- Repository-Content auswählen
- Arbeitsabsicht formulieren
- Interpretation durch die Leitassistenz
- Korrektur durch den Nutzer
- Start eines Runs
- parallele Verarbeitung
- verständliche Aktivitätsanzeige
- Fallback
- Fehler
- Abbruch
- Wiederaufnahme
- Ergebnis
- Quellenprüfung
- Eingriff in das Ergebnis
  → der Abschnitt verliert seinen Belegstatus und wird `offen`; die Version vermerkt „von dir bearbeitet".
- Versionierung
- Speichern
- Verlauf
- erneute Nutzung eines früheren Arbeitsstücks
  → Material-Hashes werden geprüft; geändertes Material wird markiert.
- kontrollierte Memory-Nutzung
- mögliche spätere Übergabe in eine Code-Änderung oder einen Pull-Request-Vorschlag
  → **als Diff zur Bestätigung, nie als ausgeführte Änderung.**

Berücksichtige mindestens diese Zustände:

- leer
- vorbereitet
- laufend
- wartet auf Nutzereingabe
- erfolgreich
- mit Einschränkung erfolgreich
- Fallback aktiv
- fehlgeschlagen
- abgebrochen
- wiederaufnehmbar
- archiviert

⟨†9⟩ **Invarianten der Zustandsmaschine:** kein Zustand verliert bereits erzeugte Abschnitte · `Fallback aktiv` ist **kein** Endzustand · Nutzerende heißt immer `abgebrochen`, nie `fehlgeschlagen` · `archiviert` bleibt zitierfähig, aber nicht fortsetzbar.

⟨†9⟩ **Proaktivität mit Schwelle** (abgeleitet vom vorhandenen Wachdienst): Meldung bei Laufabschluss, neuer Blockade, Fallback mit Klassenwechsel, geändertem Material beim Wiederbetreten (maximal ein Hinweis pro Arbeitsraum und Tag), berührter früherer Entscheidung. **Keine** Meldung bei laufendem Fortschritt ohne Besonderheit, erfolgreichen Retries, Routing-Entscheidungen ohne Relevanz.

---

# 10 · Technische Zielarchitektur

Entwickle eine technisch belastbare Zielarchitektur.

Trenne klar:

- Frontend
- UI State
- Application Layer
- Leitassistenz
- Intent-Erkennung
- Kontextmanagement
- Orchestrierungs-Policy
- **Router-Port** ⟨†3⟩
- OmniRoute Adapter
- OmniRoute
- Provider
- Modelle
- Tools
- Repository-/Content-Layer
- LibreChat-Module, falls übernommen
- Persistenz
- Memory
- Authentifizierung
- Berechtigungen
- Konfiguration
- Secrets
- Monitoring
- Logging
- Audit
- Eventing
- Streaming
- Fehlerbehandlung
- Teststrategie
- Deployment

Zeige die Architektur als ASCII-Diagramm.

Formuliere Architekturprinzipien:

- Das Frontend kennt keine Provider-Secrets.
- Das Frontend ruft OmniRoute nicht direkt auf.
- Die Leitassistenz ist nicht identisch mit einem einzelnen Modell.
- Repository-Zugriffe starten read-only.
- Schreibzugriffe erfordern Diff, Rechteprüfung und Bestätigung **— in dieser Reihenfolge.** ⟨†9⟩
- Jeder Run ist nachvollziehbar.
- Fallbacks müssen erkennbar sein, wenn sie Ergebnisqualität, Kosten, Datenschutz oder Fähigkeiten beeinflussen.
- Memory ist transparent und kontrollierbar.
- Provider- und Routerdetails sind austauschbar, ohne das Produktmodell zu zerstören. ⟨†3⟩
- Bestehende Repository-Funktionalität wird nur mit Schutztests verändert.

⟨†9⟩ **Ergänzende Prinzipien:**

- Externe Antworten werden **niemals ungeprüft** in die Oberfläche geschrieben (`esc()`-Präzedenz aus `schaltwerk`).
- Ein Lauf endet **nie** mit einer Behauptung, die nicht belegt, als offen markiert oder als unbelegbar gekennzeichnet ist.
- Kein Secret verlässt den Prozessspeicher in eine Datei, solange es nicht ausdrücklich gewünscht ist (`schaltwerk`-Präzedenz).
- Die Anwendung bindet in v1 an Loopback.

---

# 11 · Entwicklungsstrategie

Erstelle eine konkrete Reihenfolge.

## Phase 1 – Repository Discovery

Definiere:

- welche Dateien, Bereiche und Konfigurationen untersucht werden
- welche Befunde dokumentiert werden
- welche Risiken sichtbar werden müssen
- wie ein Preservation Contract entsteht
- welche bestehenden Funktionen durch Regressionstests geschützt werden

⟨†9⟩ **Regression:** `cd schaltwerk && pip install -r requirements-dev.txt && pytest tests/` — **34 Tests, offline**, vor und nach jeder Phase.

⟨†9⟩ **Bereits dokumentierte Risiken:** (1) OmniRoute-Inferenz unbelegt · (2) inkonsistente OmniRoute-Antwortformate (nacktes Array belegt) · (3) `schaltwerk` ohne Lizenzdatei · (4) MashAI MPL-2.0 · (5) drei OmniRoute-Container, einer mit Port-Mapping, Key-Rotation nach Neustart · (6) dokumentierte Umgebung Windows-zentriert.

## Phase 2 – Produktdefinition

Definiere:

- die erste Zielgruppe → **Technik-Entscheider mit eigenem KI-Setup, Single-User, lokal**
- die wichtigste Nutzerhandlung → **Beurteilen**
- das erste Arbeitsstück → *„Kann `schaltwerk` als Hintergrundorchestrierung dienen?"* (Material ist real und vollständig im Repo vorhanden)
- die ersten Materialtypen → `repo_file`, `note`, `workpiece`
- die ersten Intent-Typen → `ASSESS_QUESTION`, `ANALYZE_MATERIAL`, `CONTINUE_WORKPIECE`, `EXPLAIN_RUN`
- die Grenzen der Leitassistenz
- die Datenschutz- und Memory-Regeln
- die Zustandsmaschine eines Runs

## Phase 3 – UX-Prototyp

Definiere:

- was zunächst mit simulierten Events getestet wird → **alle SSE-Ereignisse aus einem MockAdapter, kein Netz, keine OmniRoute**
- welche Screens und Zustände klickbar sein müssen → leerer Raum · Material an die Werkbank · Arbeitsplan korrigieren · Lauf mit Werkzeugspur · Fallback-Karte · blockierende Frage · Abbruch und Wiederaufnahme · Quellenprüfung · Eingriff in einen Abschnitt · Gedächtnis-Register
- wie geprüft wird, ob der Arbeitsraum verständlich ist → **fünf Fragen:** (1) Steht **ein zusammenhängendes Dokument** im Zentrum? (2) Erscheinen Zahlen **im Satz** statt in Kästchen? (3) Ist die **Fragenleiste** wichtiger als jede Kennzahl? (4) Lässt sich jede Aussage **bis zur Quelle** zurückverfolgen? (5) Sieht man **keine** Infrastruktur, solange sie nicht relevant ist?
- wie verhindert wird, dass der Prototyp wieder wie ein Dashboard wirkt

## Phase 4 – OmniRoute-Integration

Definiere:

- welche reale OmniRoute-Funktion zuerst angebunden wird → **die Fähigkeitsfeststellung, nicht das Routing.** Read-only Probe: (a) welche Endpunkte antworten, (b) ist ein Inferenz-Endpunkt erreichbar, (c) Antwortformat und Streaming-Verhalten, (d) Authentifizierung, (e) Fehlerverhalten bei 401/404/429/5xx, (f) **bei negativem Befund: Stopp und Rückweg** — Direkt-Provider-Adapter gegen einen der 7 bekannten Provider, oder Mock für die Demo.
- welchen Adapter-Vertrag die Anwendung benötigt → `capabilities()`, `invoke()`, `abort()` — mehr nicht
- wie Streaming, Fehler, Fallbacks und Events behandelt werden
- wie Secrets und Provider-Informationen geschützt werden → nur im Application Layer, bevorzugt nur im Prozessspeicher, nie im Frontend, nie in Logs, nie in der Datenbank

## Phase 5 – LibreChat-Reuse

Definiere:

- welche LibreChat-Module geprüft werden → `memory.ts` + `memories.js`, `message.ts` (`parentMessageId`), `packages/api/src/stream/`, `files/citations.ts`, `librechat.example.yaml → endpoints.custom`, `auditLog.ts`
- welche Bausteine tatsächlich übernommen werden
- welche nur als Referenz dienen
- wie UI- und Datenmodellkopplung vermieden wird → **keine Imports, keine gemeinsame Datenbank, keine gemeinsamen Typen**; Protokoll in `omnia-atelier/docs/REUSE.md` mit Quelle und Lizenz

## Phase 6 – erster End-to-End-Vertikalschnitt

Definiere:

- einen Nutzer
- ein Arbeitsstück
- Material aus dem Repository → `server.py` (Auszug), `DOKUMENTATION.md`, `tests/test_server.py`, `CHANGELOG.md`, `WEITERARBEITEN.txt` (Auszug)
- eine Leitassistenz-Interpretation
- einen realen OmniRoute-Run
- ein gespeichertes Ergebnis
- einen sichtbaren Fallback-Test → Fähigkeit gezielt unerreichbar machen; Fallback-Karte muss erscheinen, Qualitätsvermerk muss in der Version stehen
- einen Abbruch- und Wiederaufnahme-Test → Abbruch bei 50 %; Fortsetzung ohne Neuerzeugung fertiger Abschnitte

⟨†9⟩ **Abnahmekriterium:** Das Arbeitsstück ist **zitierfähig** — eine dritte Person verfolgt jede Kernaussage bis zu einer Stelle im Material, ohne die App zu kennen.

## Phase 7 – visuelle Ausarbeitung

Definiere:

- welche visuellen Regeln erst nach funktionierendem Kernfluss verfeinert werden → Reihenfolge: Raum und Typografie → Belegstatus-Zeichen → Werkzeugspur und Bewegung → Fallback-/Fehlerdarstellung → Farbe → Accessibility → Responsivität
- wie Typografie, Farben, Bewegung und Interaktion funktional eingesetzt werden
- wie Accessibility und Responsivität sichergestellt werden → Kontrastmessung (insbesondere `--muted` auf `--bg`), Tastaturpfade, Reduced-Motion, Screenreader-Texte für Kanten, „Werkbank zuerst" unter 1024 px

## Phase 8 – Robustheit

Definiere:

- Fehlerklassen → die neun aus §7
- Timeouts → **pro Teilschritt**, Gesamtlauf als Obergrenze, hart
- Retry-Regeln → max. 2 Versuche, exponentielles Backoff, **nur** bei `TIMEOUT`, `RATE_LIMITED`, `MALFORMED_RESPONSE`; **nie** bei `AUTH_INVALID`, `BUDGET_EXCEEDED`, `POLICY_VETO`
- Fallback-Regeln
- Kostenlimits
- Latenzlimits
- Datenintegrität → Material-Hashes bei jedem Lauf; geändertes Material ⇒ Hinweis, kein stilles Weiterarbeiten
- Versionierung → append-only, keine Version wird überschrieben, Bearbeitung erzeugt eine neue
- Audit → append-only; bestätigungspflichtige Aktionen nur mit Bestätigungsnachweis
- Berechtigungen → eine Grenze (Schreiben), drei Stufen (Diff, Rechte, Bestätigung)
- Datenschutz → Memory in vier Stufen, Standard flüchtig, harte Löschung
- Observability → strukturiertes Run-Log, Routing-Protokoll je Run, SSE-Ereignisse, keine Personen-Telemetrie

## Phase 9 – Verifikation

Zeige, wie bewiesen wird, dass: ⟨†10⟩

- die App funktioniert → End-to-End-Lauf mit echtem Material
- **OmniRoute tatsächlich verwendet wird** → Run-Log **plus unabhängiger Abgleich mit `/api/usage/proxy-logs`** (die Telemetrie der echten Installation beweist den Aufruf unabhängig von unserer eigenen Protokollierung)
- Modellrouting funktioniert → zwei Fähigkeiten mit nachweislich unterschiedlichen Modellen, Routing-Protokoll je Run
- Fallbacks funktionieren → gezielter Ausfalltest, Karte + Qualitätsvermerk in der Version
- Fehler korrekt dargestellt werden → Test je Fehlerklasse mit erwarteter UI-Reaktion
- Abbruch und Wiederaufnahme funktionieren → Abbruchtest bei 50 %, Budgetverbrauch stimmt
- gespeicherte Arbeitsstücke konsistent bleiben → Versionstest über 10 Zyklen mit Hash-Prüfung
- Memory transparent und kontrollierbar bleibt → Register zeigt Herkunft; nach „Alles vergessen" ist die Tabelle leer
- Repository-Content nicht unbeabsichtigt beschädigt wird → **Hash-Vergleich des gesamten Materialbaums vor/nach**, `git status` in `schaltwerk` bleibt leer
- bestehende Funktionalität nicht durch die neue UX zerstört wird → `pytest schaltwerk/tests/` vor und nach jeder Phase
- LibreChat-Komponenten nur dort übernommen wurden, wo sie wirklich Mehrwert liefern → `docs/REUSE.md` führt jede Übernahme mit Quelle, Lizenz und Grund

---

# 12 · MVP

Definiere ein realistisches MVP.

Das MVP soll nicht möglichst viele AI-Features enthalten.

Es soll die zentrale Produktidee beweisen.

Das MVP soll mindestens beweisen:

**Aus ausgewähltem Repository-Material und einer klaren Nutzerabsicht kann die Leitassistenz über OmniRoute ein nachvollziehbares, bearbeitbares und speicherbares Arbeitsstück erzeugen.**

⟨†9⟩ **Und:** ein Fallback wird **sichtbar**, statt zu verschwinden.

Definiere:

- minimale Screens → Arbeitsraum mit Materialwand + Werkbank · Arbeitsplan-Vorschau · Lauf-Ansicht mit Werkzeugspur und Fragenleiste · Arbeitsstück-Ansicht mit Belegstatus und Quellenprüfung · Versions-/Ablage-Leiste · Gedächtnis-Register · Werkstattbericht (aufklappbar)
- minimale Nutzerinteraktionen → Material auswählen · Absicht formulieren · Arbeitsplan bestätigen/korrigieren · Lauf starten · Frage beantworten · Fallback akzeptieren oder neu versuchen · Abschnitt bearbeiten · versionieren · bestätigen (Schreiben/Export) · Gedächtnis ansehen/löschen
- minimale Materialtypen → `repo_file`, `note`, `workpiece`
- minimale Leitassistenz-Fähigkeiten → die vier Intent-Typen aus Phase 2, plus Arbeitsplan, Belegstatus, Kanten, Blockaden benennen
- minimale Backend-Funktionen → FastAPI: Arbeitsraum, Material, Arbeitsstück, Run, Memory; SSE; SQLite; Audit; MockAdapter
- minimale Persistenz → SQLite: Arbeitsräume, Material-Index mit Hash, Arbeitsstücke + Versionen, Runs + Routing-Ereignisse, Memory, Audit
- minimale OmniRoute-Integration → **eine** Inferenz-Fähigkeit über den Adapter, plus eine zweite für Parallel- und Fallback-Test
- minimale Fallback-Integration → eine Regel: Klassenwechsel ⇒ Karte + Qualitätsvermerk + gezielte Neuerzeugung
- minimale Event- und Statusanzeige → die elf Zustände plus die SSE-Ereignisse
- minimale Sicherheits- und Bestätigungslogik → Loopback-Bindung · kein Secret im Frontend · read-only Repo-Zugriff · Bestätigung bei Schreiben/Export/Gedächtnis · `esc()`-Präzedenz für alle fremden Inhalte
- minimale Testfälle → Material-Inventar · Arbeitsplan-Korrektur · Belegstatus-Setzung · `╱ unbelegbar` bei fehlendem Zugriff · Fallback ⇒ Karte + Vermerk · alle neun Fehlerklassen · Abbruch ⇒ Wiederaufnahme · Versionskonsistenz · Memory CRUD + harte Löschung · **34 `schaltwerk`-Tests bleiben grün** · Repo-Hash-Vergleich vor/nach

Definiere ebenso klar:

Was gehört ausdrücklich NICHT in Version 1?

- frei verdrahtbarer Node-Editor ⟨†1⟩ — das Produkt zeigt Bedeutung, nicht Infrastruktur; im Repo gibt es zudem keine Node-Logik, die man retten müsste
- vollständiges OmniRoute-Admin-Dashboard — `schaltwerk` deckt die Verwaltungsebene bereits ab
- vollständige LibreChat-UI — ausdrücklich verboten, außerdem 102 Abhängigkeiten
- autonome Agentenschwärme — widerspricht dem Bestätigungsprinzip
- automatische Repository-Schreibzugriffe — Schreibvorschläge ja, Ausführung nein
- automatische Deployments
- uneingeschränkte Web-Recherche — zerstört die Belegkette
- komplexe Multi-User-Kollaboration — Single-User ist die ehrliche v1-Grenze
- Bild-, Video- oder Audioproduktion — kein Materialtyp in v1
- großer MCP-Marktplatz — Fähigkeiten im MVP fest im Katalog
- langfristiges persönliches Memory ohne klare Kontrolloberfläche — es gibt nur Memory **mit** Register
- ⟨†9⟩ **Electron-Desktop-App** — Web auf Loopback genügt; MashAI-Electron später prüfbar (**ZU PRÜFEN**)
- ⟨†9⟩ **Proxy-Logistik im Atelier** — `schaltwerk` bleibt das Werkzeug dafür, **NICHT ANFASSEN**
- ⟨†9⟩ **RAG / pgvector / Meilisearch** — Materialmengen in v1 rechtfertigen keinen Vektorstack

---

# 13 · Erweiterbarkeit

Zeige, wie das System später erweitert werden kann, ohne die zentrale Produktidee zu verlieren.

Berücksichtige:

- weitere Modelle
- weitere Provider
- lokale Modelle
- spezialisierte Modelle
- multimodale Verarbeitung
- Web-Recherche
- Agenten
- Tools
- MCP
- A2A
- Repository-Analyse
- Repository-Schreibvorschläge
- Pull-Request-Erstellung
- Dateioperationen
- externe APIs
- Automationen
- Workflows
- Team-Kollaboration
- Rollen und Freigaben
- persönliche Memory-Systeme
- Bild-, Audio- und Video-Material
- eigene Fähigkeiten oder Plugins

Für jede Erweiterung erkläre:

- wie sie in das Grundmodell passt
- welche neue Fähigkeit sie ermöglicht
- welches Risiko entsteht
- welche Sicherheits- oder UX-Regeln erforderlich sind
- warum sie nicht zu einem beliebigen Feature ohne Produktbezug wird

⟨†9⟩ **Aufnahmekriterium (verbindlich):** Eine Erweiterung muss eine der vier Kanten bedienen (stützt / widerspricht / blockiert / entstand aus) **oder** einen Materialtyp ergänzen. Was nur eine neue Anzeige erzeugt, wird **nicht** aufgenommen.

⟨†9⟩ **Risikohinweise:** Repository-Schreibvorschläge und PR-Erstellung tragen das höchste Risiko (irreversibel, extern) ⇒ Diff + Rechte + Bestätigung + Widerrufspfad. Multimodale Verarbeitung reißt die Belegkette (Bild ≠ zitierbare Zeile) ⇒ Zitatpflicht über Ausschnitt + Hash, `╱ unbelegbar` bleibt möglich. MCP/A2A bringen fremde Daten in den Kontext ⇒ jede Quelle als Material mit Hash und Lizenznotiz, kein stiller Kontext. Automationen ⇒ nur mit Kostenobergrenze, Ergebnis als Vorschlag, nie als Änderung.

---

# 14 · Technische Beispiele

Erst nachdem Produktmodell, UX, Discovery-Plan und Architektur feststehen, darfst du kleine technische Beispiele verwenden.

Mögliche Beispiele:

- Router-Port-Interface ⟨†3⟩
- OmniRoute-Adapter als Pseudocode
- Datenmodell für Arbeitsstücke
- Datenmodell für Materialreferenzen
- Datenmodell für Runs
- Event-/Statusmodell
- Fallback-Event
- Frontend-State
- Leitassistenz-Intent
- API-Struktur
- Berechtigungsprüfung
- Repository-Read-only-Zugriff
- gespeicherte Ergebnisversion

WICHTIG:

Keine erfundene OmniRoute-Syntax als reale API darstellen.

Wenn die reale Syntax nicht durch das Repository oder die Dokumentation verifiziert wurde, klar markieren:

`PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX`

⟨†9⟩ **Ergänzung zu den Datenmodellen:** Ein `MaterialRef` trägt zwingend `content_hash` (SHA-256) und `read_state` — nur dadurch ist Änderungserkennung beim Wiederbetreten möglich. Ein `Section` trägt `produced_by` (Fähigkeit, Modell, Qualitätsklasse, Run-ID) und `edited_by_user`. Ein `Run` trägt `material_hashes`, `routing_events`, `budget_used` und `resume_point`.

---

# 15 · Endgültige Empfehlung

Schließe mit einer klaren, konkreten Empfehlung ab.

Beantworte:

- Welche der drei Produktideen sollte weiterverfolgt werden?
- Warum ist sie die beste Wahl?
  → ⟨†9⟩ **Maßgabe:** die Stärken der anderen beiden müssen als Werkzeuge im Gewinner-Modell erhalten bleiben.
- Wie verbindet sie OmniRoute, LibreChat, Mesh-AI-inspirierte Prinzipien und das bestehende Repository?
- Welche Teile des Repositorys müssen zuerst geprüft werden?
  → (1) OmniRoute-Inferenzfähigkeit · (2) OmniRoute-Antwortformate · (3) Lizenzstatus `schaltwerk` · (4) `DOKUMENTATION.md` + `WEITERARBEITEN.txt` als Material · (5) Laufzeitumgebung
- Welche LibreChat-Module sind die wahrscheinlich wichtigsten Prüfobjekte?
  → `memory.ts` + `memories.js` · `message.ts` (`parentMessageId`) · `packages/api/src/stream/` · `files/citations.ts` · `endpoints.custom` · `auditLog.ts`
- Welche Eigenschaften aus Mesh AI sollten konkret definiert werden?
  → ⟨†2⟩ nicht KI-Eigenschaften (die hat MashAI nicht), sondern **Kontinuitätseigenschaften**: Arbeitsraum-Isolation · Wiederbetreten statt Neuladen · Gegenüberstellung · Einstellungs-Migrationen · Ressourcen-Disziplin
- **Welche Entscheidung darf noch NICHT getroffen werden?** ⟨†9⟩
  → (1) ob OmniRoute Routing und Fallback selbst übernimmt oder unsere Policy · (2) ob die App-Layer-Sprache dauerhaft Python bleibt · (3) ob „Mesh AI" tatsächlich MashAI meint · (4) ob die Bad-Wolf-Figur übergeht (Copyright-Vorgeschichte BBC) · (5) ob Electron als Zielplattform kommt
- Was ist der allererste konkrete nächste Arbeitsschritt?
  → **Der OmniRoute-Capability-Probe — read-only, eine Frage: „Gibt es einen Inferenz-Endpunkt, und wie sieht seine Antwort aus?"** Ergebnis in `omnia-atelier/docs/OMNIROUTE-PROBE.md` mit Datum, Basis-URL und maskierten Rohantworten.
- Wie sieht der erste vertikale End-to-End-Prototyp aus?

Die Empfehlung darf nicht auf Ästhetik allein beruhen.

Sie muss begründet werden durch:

- Benutzererlebnis
- Eigenständigkeit
- technische Machbarkeit
- Wiederverwendung des bestehenden Repositorys
- sinnvolle OmniRoute-Integration
- sinnvolle LibreChat-Wiederverwendung
- kontrollierte Mesh-AI-inspirierte Kontinuität
- Qualität der Leitassistenz
- Erweiterbarkeit
- Sicherheit
- Wartbarkeit
- Vermeidung eines generischen AI-Dashboards

Die wichtigste Grundregel lautet abschließend:

Die App ist kein Modell- oder Provider-Manager.

Die App ist ein persönliches, intelligentes Atelier.

OmniRoute ist die Werkstattlogik darunter — ⟨†3⟩ **sofern und so weit die reale Installation es hergibt.**
LibreChat liefert gegebenenfalls bewährte technische Bausteine — ⟨†5⟩ **als Konzepte, nicht als Abhängigkeit.**
Mesh-AI-inspirierte Prinzipien liefern Kontinuität und persönliche Relevanz — ⟨†2⟩ **aus Arbeitsstücken, nicht aus einem Nutzer-Gedächtnis.**
Die Leitassistenz verbindet alles nativ.

Der Nutzer soll nicht das Gefühl haben, mehrere AI-Systeme zu bedienen.

Er soll das Gefühl haben, in einem einzigen, verständlichen und eigenständigen Arbeitsraum bessere Entscheidungen und wertvolle Ergebnisse zu erzeugen.

---

# 16 · Nachweis — was am Ende vorliegen muss ⟨†10⟩

Die Antwort auf diesen Prompt gilt nur dann als vollständig, wenn sie diese Artefakte enthält:

1. **Produktmodell** mit beantworteter Zentralfrage (§2) — in einem Satz.
2. **Drei Modelle**, jedes mit allen 18 Feldern inklusive ASCII-Skizze (§3).
3. **Discovery-Plan** mit allen 48 Prüfbereichen, je vier Angaben (§4), plus **Preservation Contract** mit fünf Haltungen.
4. **Visuelle Sprache**, in der jedes beschriebene Element eine benannte Funktion hat (§6).
5. **OmniRoute-Datenfluss und End-to-End-Workflow**, mit allen 15 Erklärpunkten (§7).
6. **Zwei Reuse-Matrizen** (LibreChat, MashAI) mit Lizenzbewertung, plus **Leitassistenz-Contract** mit allen 11 Teilen (§8).
7. **Zustandsmaschine** mit elf Zuständen und Invarianten (§9).
8. **Architekturdiagramm (ASCII)** und Architekturprinzipien (§10).
9. **MVP** mit Negativliste (§12).
10. **Erweiterbarkeitstabelle** mit Aufnahmekriterium (§13).
11. **Technische Beispiele**, OmniRoute-Blöcke als Pseudocode markiert (§14).
12. **Empfehlung** mit den sechs offenen Nicht-Entscheidungen und dem ersten Arbeitsschritt (§15).

Jede Aussage über das Repository trägt eines der vier Labels: **BEKANNT · ZU PRÜFEN · ANNAHME · VORSCHLAG**.

---

*Änderungen an dieser Aufgabenstellung gehören in diese Datei, nicht in ein neues Dokument.*
