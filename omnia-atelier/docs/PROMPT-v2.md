# Aufgabenstellung (revidierte Fassung) — Omnia Atelier

**Stand:** 2026-10-02 · **Repository:** `TukTuck/omniauto` · **Basis-Commit:** `60dd904`
**Zweig:** `arena/01a0fe6e-omniauto`

> **Was diese Datei ist.** Die überarbeitete Fassung der ursprünglichen Aufgabenstellung.
> Sie enthält **keine Prämisse mehr, die dem verifizierten Repository-Befund widerspricht**.
> Der Befund steht in [`OMNIA-ATELIER.md`](./OMNIA-ATELIER.md), Abschnitte 1.1–1.6.
> Abschnitt A dieser Datei listet jede Korrektur auf; Abschnitt B ist der vollständige,
> direkt weiterverwendbare Prompt.

---

# A · Was sich gegenüber der ersten Fassung geändert hat

| # | Erste Fassung (Prämisse) | Befund | Korrektur im Prompt |
|---|---|---|---|
| 1 | „Das bisherige Schaltwerk-/Node-/Graph-Prinzip", „bisherige Schaltwerk-Logik", „Node-/Graph-Daten" | `schaltwerk/` ist **Proxy-Logistik**: 21 FastAPI-Routen, SSE-Job, Tabellen, RAM-Ringpuffer. **Kein Node-Editor, kein Graph.** | Abschnitt 5 heißt jetzt „Sichtbarkeit neu denken" und formuliert ein **Zielprinzip**, keinen Umbau. Der Nutzer verdrahtet keine Infrastruktur, er begründet ein Ergebnis. |
| 2 | „Mesh AI" als Inspiration für eine persönlichere, kontextbewusstere, kontinuierlichere KI-Erfahrung | Im Repository liegt **MashAI** (`Kurz-main`): Electron-Workspace für ChatGPT/Claude/Gemini-**Weboberflächen**, Profile, Tab-Suspension, Session-Persistenz. **Kein Memory-System.** | Abschnitt 1.3 und 8.2 beschreiben MashAI korrekt. „Kontinuität" wird aus **Arbeitsstücken und Material-Hashes** abgeleitet, nicht aus einem impliziten Nutzer-Gedächtnis. |
| 3 | OmniRoute „verbindlich als zentrale Infrastruktur für Modelle, Provider und Routing" | Verifiziert: **Verwaltungsebene** (10 Endpunkte für Proxies, Provider, Usage-Logs; Auth per `Bearer` + `x-api-key`). **Nicht verifiziert:** Inferenz, Routing-Regeln, Fallback, Multimodalität, MCP, A2A. | Abschnitt 1.5 trennt **verifiziert** / **zu prüfen** hart. Phase 4 beginnt mit einem **Capability-Probe**, und der Router-Port hält die Entscheidung offen. |
| 4 | „Bestehende funktionierende Logik, Content-Pipelines, Authentifizierung, Datenmodelle, Provider-Konfigurationen, Build-Prozesse" | Es gibt **eine** Anwendung (`schaltwerk`, 34 Tests), **kein** Login, **keine** Datenbank, **keine** CI/CD, **kein** Deployment, **keine** gemeinsame Build-Pipeline. | Abschnitt 4.2 ist bewusst schmal. Die zentrale Regel: **`schaltwerk` und die beiden ZIP-Archive werden nicht angefasst.** |
| 5 | LibreChat als Quelle „wiederverwendbarer Module" | v0.8.8, **MIT** — aber TypeScript + MongoDB + Meilisearch + pgvector + **102 Client-Abhängigkeiten**. Direkte Übernahme ist für ein lokales Single-User-Produkt teurer als nützlich. | Abschnitt 8.1 unterscheidet scharf: **Konzepte übernehmen, Code nicht einbinden.** Keine Imports, keine gemeinsame Datenbank. |
| 6 | „Mesh AI" ohne Lizenzangabe | MashAI ist **MPL-2.0** (file-level copyleft); `schaltwerk` hat **keine Lizenzdatei**. | Abschnitt 8.2 verbietet Code- und Asset-Kopien aus beiden Quellen; nur Konzepte. |
| 7 | Discovery-Liste enthält Bereiche, die es nicht gibt (Monorepo, CI/CD, Deployment, Datenbank, ORM, WebSocket, Secret-Management, Node-/Graph-Daten) | Real fehlen all diese Bereiche. | Die Liste bleibt als Prüfliste, aber **„nicht vorhanden" ist ein gültiges, zu dokumentierendes Ergebnis** — kein Grund zu spekulieren. |
| 8 | Keine Aussage zur Ablagestruktur | Neu etablierte Konvention: **jeder Zweig baut in seinem eigenen Ordner**. | Abschnitt 0.5 neu: alles entsteht unter `omnia-atelier/`. |
| 9 | „Erfinde keine Repository-Dateien …" (galt für den Agenten) | Gilt jetzt **auch für den Prompt selbst**. | Kein Abschnitt dieser Fassung behauptet eine Datei, einen Endpunkt oder eine Funktion, die nicht gelesen wurde. |

---

# B · Der revidierte Prompt (vollständig, direkt verwendbar)

---

## Aufgabe: Entwickle Omnia Atelier auf Basis des bestehenden Repositorys

Du entwickelst eine außergewöhnliche, eigenständige KI-Anwendung auf Basis des bestehenden
GitHub-Repositorys `TukTuck/omniauto`.

Denke die gesamte Aufgabe vollständig durch, bevor du antwortest.

Liefere keine oberflächliche Designidee, kein generisches KI-Dashboard und keine bloße
Sammlung von Features.

### Kennzeichnungssystem (verbindlich für die gesamte Antwort)

Unterscheide konsequent:

- **BEKANNT** — aus dieser Aufgabenstellung sicher hervorgehend **oder aus dem Repository tatsächlich gelesen**
- **ZU PRÜFEN** — erst durch Untersuchung von Code, Konfiguration, laufender Instanz oder Dokumentation zu verifizieren
- **ANNAHME** — plausibel, aber unbestätigt; niemals Grundlage einer irreversiblen Entscheidung
- **VORSCHLAG** — neue Produkt-, UX-, Architektur- oder Implementierungsentscheidung

**Grundregel:** Erfinde keine Repository-Dateien, keine APIs, keine Komponenten, keine
Datenmodelle und keine bereits vorhandenen Funktionen. Wenn die reale Syntax nicht
verifiziert ist, verwende ausschließlich klar gekennzeichneten **Pseudocode** mit der
Zeile `PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX`.

### Gesetzter Befund (muss nicht erneut hergeleitet werden)

Das Repository hat **einen Commit** (`60dd904`) und **12 versionierte Dateien** (38 MB).
Es ist **kein** Monorepo mit bestehender Anwendung, sondern eine **Materialablage**:

| Inhalt | Befund |
|---|---|
| `schaltwerk/` | Einzige lauffähige Anwendung: **Python/FastAPI/uvicorn/httpx**, `server.py` (57 KB, 21 Routen) + `static/index.html` (74 KB, eine Datei) + `tests/test_server.py` (**34 Tests, offline grün**). **RAM-only**, keine Datenbank, kein Login, kein Build, keine CDN-Abhängigkeit, Bindung an `127.0.0.1`, Port 8765, Windows-Start per `STARTEN.bat`. **Zweck: Proxy-Logistik** — freie Proxies holen, selbst gegen HTTPS-Ziele prüfen, lebendige als manuelle Registry-Proxies nach OmniRoute schreiben. |
| `schaltwerk/` — „Bad Wolf" | Bereits vorhandene **native Leitfiguren-Instanz**: Stimme als serverseitiger Ringpuffer (60 Zeilen) protokollierter Taten, Ablage (max. 200 Einträge, 4.000 Zeichen), Wachdienst (asyncio-Task, 60 s, mit Anti-Spam-Schwelle), Risiko-Ausschluss vor jedem Schreibzugriff (`tls-intercept`, `ip-mismatch` werden nie geschrieben), acht **Goldene Regeln**. |
| `schaltwerk/` — Design | Gemessener Anti-KI-Look-Umbau: 89 Pills entfernt, **Radius einheitlich 3 px**, KPI-Kärtchen durch eine Mono-Statuszeile ersetzt, Pills nur für echte Stati. Tokens: `--bg #0d0e12`, `--panel #13141a`, `--panel-2 #191a21`, `--line #262833`, `--line-2 #33353f`, `--ink #d6d7dd`, `--muted #8a8c99`, `--eye #d9a441`, `--eye-dim #8a6a34`. Inter + JetBrains Mono, Labels 9–10 px uppercase. |
| `Kurz-main (1).zip` | **MashAI** v1.0.0-beta, **MPL-2.0**: Electron 39, React 18.3, TS 5.9, Vite 6, Tailwind 3.4, Ghostery-Adblocker, Vitest (**66 Tests**). **Ein Workspace für fremde KI-Weboberflächen** (ChatGPT, Claude, Gemini, Perplexity, Grok, DeepSeek) mit Profilen, Tab-Management, Side-Panel, Smart-Suspension, Session-Persistenz, Settings-Migrationen. **Kein Memory-System.** Plattform: Windows only. |
| `LibreChat-main.zip` | **v0.8.8, MIT**, 6.303 Dateien. Monorepo: `packages/api` (TypeScript), `packages/data-schemas` (Mongoose), `packages/data-provider`, `client` (React, **102 Abhängigkeiten**). Infrastruktur: MongoDB, Meilisearch, pgvector, `rag_api`. Vorhanden u. a.: Memory (Key/Value mit `^[a-z_]+$`, `agentId`-Partition, Opt-out, Einzel-Key-Update/Löschen), Nachrichtenbaum (`parentMessageId`), Stream-Architektur (`GenerationJobManager`, `ApprovalLifecycle`, Checkpoints, terminale Projektion), 10 Auth-Strategien, MCP/Tools/Agents/Skills, Zitatverarbeitung, Audit-Log, `endpoints.custom` mit `baseURL`/`apiKey` für OpenAI-kompatible Endpunkte. |
| **OmniRoute — verifiziert** | Basis `http://127.0.0.1:20128` (Host-Port der dokumentierten Installation: **24615**). Auth: **beide** Header `Authorization: Bearer <key>` **und** `x-api-key: <key>`; Key mit `manage`-Scope. Endpunkte: `GET/POST/DELETE /api/v1/management/proxies`, `GET /api/v1/management/proxies/health`, `PUT|POST /api/v1/management/proxies/bulk-assign`, `GET /api/v1/management/proxies/assignments`, `GET /api/providers`, `PATCH /api/providers`, `GET /api/settings/oneproxy`, `GET /api/usage/proxy-logs`. 7 Provider-Connections: `openrouter`, `uncloseai`, `opencode`, `duckduckgo-web`, `cloudflare-playground`, `chipotle`, `aihorde`. **Bekannte Eigenheit:** Antworten kommen teils als nacktes Array statt als Objekt → Adapter muss normalisieren. |
| **OmniRoute — zu prüfen** | Existenz und Form einer **Inferenz-API**, Routing-/Fallback-Logik, Modell-ID-Format, Streaming-Verhalten, Kosten-/Token-Telemetrie, Multimodalität, Dateien, Audio, Video, Embeddings, MCP, A2A, Version/Image-Tag, Ratenlimits. **Im Repository gibt es dafür keinen Beleg.** |

### Grundregel des Produkts

Baue keinen OmniRoute-Manager mit schöner Oberfläche.
Baue kein LibreChat-Redesign.
Baue keine MashAI-Kopie.
Baue keinen generischen Chatbot.
Baue keinen technischen Node-Editor als Selbstzweck.

Baue ein eigenständiges Produkt, dessen Arbeitsweise durch OmniRoute, wiederverwendbare
LibreChat-**Konzepte**, Repository-Content und eine zentrale native Leitassistenz
ermöglicht wird.

Die technische Infrastruktur wird sichtbar, wenn sie für Verständnis, Vertrauen,
Eingriff oder Qualität relevant ist.
Sie bleibt unsichtbar, wenn sie nur technische Komplexität erzeugt.

### Ablage-Konvention (neu, verbindlich)

Jede Arbeit an diesem Repository liegt in **ihrem eigenen Ordner** auf Wurzelebene.
Dieser Zweig baut ausschließlich innerhalb von **`omnia-atelier/`**. Andere Zweige legen
ihren Ordner daneben. Gemeinsame Orte — Wurzel, `schaltwerk/`, die beiden ZIP-Archive —
werden von keinem Zweig verändert.

---

## 1 · Gesetzte Grundlagen

### 1.1 OmniRoute ist ein fester Bestandteil — mit offener Fähigkeitsfrage

OmniRoute wird als Infrastruktur eingeplant für: Modellzugang, Provider-Abstraktion,
Modellrouting, Fallbacks, Verfügbarkeit, Latenz, Kosten- und Qualitätsregeln, parallele
Modellverarbeitung, multimodale Fähigkeiten — **jeweils nur so weit, wie die reale
Installation es hergibt**.

Verbindlich:

- Die OmniRoute-Version, API, Konfiguration, Providerliste, Modellverfügbarkeit,
  Secret-Verwaltung, Fallback-Logik, Telemetrie und Deployment-Art werden **zuerst untersucht**.
- Es dürfen **keine** OmniRoute-APIs, Endpunkte, Konfigurationsdateien oder Funktionsnamen erfunden werden.
- Nicht verifizierte Syntax erscheint ausschließlich als markierter **Pseudocode**.
- Die App-UI ist **niemals** direkt an OmniRoute gekoppelt.
- Die App spricht über einen eigenen Application Layer und einen **Router-Adapter** mit OmniRoute.
- Der Router-Adapter sitzt hinter einem **Port** (Interface), damit ein negativer
  Fähigkeitsbefund das Produktmodell nicht zerstört.

### 1.2 LibreChat wird als Konzeptquelle genutzt

LibreChat dient **nicht** als UI-Referenz. Die neue Anwendung darf nicht wie LibreChat
aussehen und nicht auf eine Chat-Oberfläche reduziert werden.

Zu prüfen und zu entscheiden (BEIBEHALTEN · ADAPTIERT ÜBERNEHMEN · NUR ALS REFERENZ ·
NICHT ÜBERNEHMEN): Authentifizierung, Nutzer-/Session-Management, Thread-/Verlaufssysteme,
Streaming, Datei- und Kontextverarbeitung, Tool-Integration, Agenten-/Fähigkeits-Integration,
Presets/Rollenlogik, OpenAI-kompatible Endpoint-Anbindung, Berechtigungen, Datenbank- und
Persistenzmuster, Fehlerbehandlung, Sicherheitsmechanismen.

**Bewertungsmaßstab:** LibreChat wird **nie als Abhängigkeit eingebunden**. Es gibt keine
Imports, keine gemeinsame Datenbank, keine gemeinsamen Typen. Übernommen werden **Ideen,
Feldnamen und Reihenfolgen**, dokumentiert in `omnia-atelier/docs/REUSE.md` mit Quelle und Lizenz.

### 1.3 MashAI ist eine Inspirationsrichtung — präzise, nicht romantisch

MashAI wird **nicht** als visuelle Vorlage kopiert (MPL-2.0, fremde Marke, keine Code-Kopie).

Was MashAI tatsächlich liefert, ist der **Beweis für ein Bedürfnis**: Menschen verlieren
Arbeit zwischen KI-Oberflächen. MashAI löst das durch *Ordnung* (Profile, Tabs,
Session-Persistenz). Omnia Atelier löst es durch **Kontinuität des Arbeitsstücks**.

Zu klären bleibt:

- Was bedeutet „persönlich" konkret? → **arbeitsbezogen, nicht personenbezogen.**
- Woran erinnert sich die Leitassistenz? → an **Arbeitsstücke, Entscheidungen, verworfene
  Alternativen, Arbeitseinstellungen** — nicht an biografische Merkmale.
- Wann darf sie proaktiv handeln? → nur bei Lese-/Analysehandlungen innerhalb eines
  bestätigten Arbeitsplans, und nur mit Bezug zu einem konkreten Objekt.
- Wann muss sie fragen? → bei Schreibzugriff, externer Wirkung, Qualitätsklassenwechsel,
  Datenschutzwechsel, Gedächtnis-Speicherung, Grenzüberschreitung.
- Wie sieht, korrigiert und löscht der Nutzer Erinnerungen? → über ein eigenes, immer
  erreichbares **Gedächtnis-Register**; Löschung ist hart und wird auditiert.

Die Anwendung darf niemals den Eindruck erwecken, „alles über den Nutzer zu wissen".

### 1.4 Zentrale native Leitassistenz

Die Leitassistenz ist kein austauschbarer Chatbot in einer Sidebar. Sie ist die verbindende
Intelligenz des Produkts — eine **Anwendungsrolle**, kein einzelnes Modell.

Sie soll: Arbeitskontext verstehen · Material einordnen · Arbeitsabsichten erkennen ·
offene Fragen sichtbar machen · Fähigkeiten oder Modelle anfordern · Ergebnisse
zusammenführen · Routing- und Fallback-Ereignisse verständlich erklären, **wenn sie
relevant sind** · Arbeitsstücke versionieren und fortsetzen helfen · auf Widersprüche,
Risiken, fehlende Quellen und blockierte Entscheidungen hinweisen · Vorschläge machen,
ohne die Kontrolle zu übernehmen.

Sie darf **nicht**: stillschweigend Repository-Dateien verändern · stillschweigend deployen ·
stillschweigend externe Aktionen ausführen · Modellwechsel bei kritischen Ergebnissen
verbergen · persönliche Daten ohne transparente Regeln speichern · behaupten, Inhalte
geprüft zu haben, wenn kein Zugriff bestand · technische Agentenaktivität nur zur
Dekoration darstellen.

Irreversible oder externe Aktionen müssen vom Nutzer bestätigt werden.

**Weiterentwicklung aus dem Bestand:** Die vorhandene Bad-Wolf-Instanz in `schaltwerk`
(Stimme als protokollierte Tat, Ablage, Wachdienst mit Anti-Spam-Schwelle, Goldene Regeln)
ist die Keimzelle dieses Contracts. Die **Disziplin** wird übernommen, nicht die Figur.

---

## 2 · Zentrale Produktfrage

Beantworte nicht zuerst: „Wie sieht ein OmniRoute-Dashboard aus?"
Beantworte zuerst: **Was entsteht hier, das es ohne diese App nicht gäbe?**

Einzeln zu beantworten:

- Was macht der Nutzer in dieser App eigentlich?
- Welche zentrale Tätigkeit steht im Mittelpunkt? → **Urteilen, nicht Fragenstellen.**
- Was gibt der Nutzer hinein?
- Was entsteht daraus?
- Wie unterscheidet sich das Ergebnis von einer normalen Chat-Antwort?
  → Eine Chat-Antwort ist eine Äußerung ohne Haftung; ein **Arbeitsstück** ist ein Objekt
  mit Struktur, Herkunft, Version und Status.
- Welche Rolle spielt Repository-Content? → **Material ersten Ranges**: prüfbar, versioniert, real.
- Welche Rolle spielt die Leitassistenz?
- Wann wird OmniRoute sichtbar? → wenn eine Routing-Entscheidung Qualität, Kosten, Latenz,
  Datenschutz oder Fähigkeiten beeinflusst.
- Wann bleibt es unsichtbar? → wenn der Nutzer nur wissen muss, **was** herauskam.
- Wann sind mehrere Modelle sinnvoll? → bei Urteilen mit Konfliktpotenzial; nicht bei Extraktionen.
- Wann sind Tools oder Agenten sinnvoll? → wenn eine Behauptung nur durch **Zugriff** belegbar ist.
- Welche Entscheidungen kann der Nutzer beeinflussen?
- Welche Dinge passieren automatisch?
- Warum ist diese App kein Chatbot, kein Agent-Dashboard, kein Node-Editor?
- Warum sollte sich diese Arbeitsweise eigenständig, sinnvoll und interessant anfühlen?

**Bevorzugte Richtung: Omnia Atelier** — ein digitaler Arbeitsraum, in dem aus Material
belastbare Arbeitsstücke entstehen.

Material: Repository-Inhalte, Code, Komponenten, Dokumentation, Notizen, Ideen, Aufgaben,
Dateien, Anforderungen, Entscheidungen, frühere Ergebnisse, Quellen.

Arbeitsstücke: technische Entscheidungen, Produktkonzepte, Architekturpläne, Spezifikationen,
Content-Systeme, Research-Ergebnisse, Strategiepapiere, Roadmaps, Code-Änderungsvorschläge,
Briefings, überprüfbare Hypothesen, Umsetzungspläne.

---

## 3 · Drei wirklich unterschiedliche Produktmodelle

Keine drei visuellen Varianten derselben Chat-App. Drei **unterschiedliche Kernhandlungen**:
**herstellen · prüfen · übergeben.**

Für jeden Ansatz: Name · Kernidee · zentrale Nutzerhandlung · Startbild · was der Nutzer
einbringt · was danach geschieht · Rolle der Leitassistenz · Rolle von OmniRoute · Rolle der
Modelle · Rolle der LibreChat-Konzepte · Rolle der MashAI-inspirierten Kontinuität · Rolle
des Repository-Contents · wie Aktivität sichtbar wird · typische Nutzung · Unterschied zum
bestehenden `schaltwerk` · Risiken · Chancen · **ASCII-Skizze**.

Bewährte Richtungen:

1. **Omnia Atelier** — Kernhandlung *herstellen*: Materialwand → Werkbank → Ablage;
   Ergebnis ist ein Arbeitsstück mit **Belegstatus je Kernaussage**.
2. **Der Beweisraum** — Kernhandlung *prüfen*: Behauptungen werden in Teilaussagen zerlegt;
   jede trägt einen Belegstatus (`belegt · teilweise · offen · widersprochen · unbelegbar`).
   `unbelegbar` ist ein legitimes, ehrliches Ergebnis.
3. **Die Werkbrief-Gießerei** — Kernhandlung *übergeben*: ein Dokument, das ein anderer ohne
   Rückfrage ausführen kann; Freigabe über einen **Blindtest** (Zweitmodell rekonstruiert die
   Aufgabe aus dem Brief allein; Abweichungen = Lücken).

Empfiehl anschließend klar einen Ansatz — mit der Maßgabe, dass die Stärken der anderen
beiden **als Werkzeuge im Gewinner-Modell** erhalten bleiben müssen.

---

## 4 · Repository-first Discovery

**Phase 1 ist abgeschlossen.** Der Befund steht in `omnia-atelier/docs/OMNIA-ATELIER.md`,
Abschnitte 1.1–1.6 und 4.1 (51 Prüfbereiche mit Haltung). Der Preservation Contract steht
in Abschnitt 4.2.

Für Bereiche, die im Repository **nicht existieren** (Monorepo, CI/CD, Deployment, Datenbank,
ORM, WebSocket, Secret-Management, Authentifizierung, Node-/Graph-Daten), gilt:
**„nicht vorhanden" ist ein gültiges, zu dokumentierendes Ergebnis** — kein Anlass zu
Spekulation und kein Anlass, etwas zu erfinden.

Der Preservation Contract unterscheidet BEIBEHALTEN · ERWEITERN · NEU INTERPRETIEREN ·
ERSETZEN · NICHT ANFASSEN. Kernregeln:

- **NICHT ANFASSEN:** die beiden ZIP-Archive (kein Entpacken ins Repo, keine Code-Kopie,
  keine Assets — MPL-2.0 bei MashAI, keine Lizenzdatei bei `schaltwerk`), OmniRoute selbst,
  die laufende `schaltwerk`-Instanz, das Windows-zuerst-Prinzip von `schaltwerk`.
- **BEIBEHALTEN:** `schaltwerk` als Ganzes, die acht Goldenen Regeln, die Design-Tokens,
  der Dokumentationsstandard (`DOKUMENTATION.md` als Wahrheit, `CHANGELOG.md` als Historie),
  die 34 Tests als Regressionnetz.
- **NEU INTERPRETIEREN:** Bad Wolf → Leitassistenz · Ablage → Materialwand · Hub-Gedanke →
  Arbeitsräume · Wachdienst → Proaktivität mit Relevanzschwelle.
- **ERSETZEN:** RAM-only-Zustand → SQLite (Arbeitsstücke müssen wiederbetretbar sein);
  Tabellen-UI → Raum-UI. **Ausnahme:** die RAM-Disziplin für **Secrets** bleibt bestehen.

Es darf nichts pauschal ersetzt werden, nur weil eine neue UX entsteht.

---

## 5 · Sichtbarkeit neu denken (früher: „Schaltwerk kritisch neu denken")

Es gibt im Repository **keine** Node-/Graph-Logik. Die Frage wird deshalb als Zielprinzip
beantwortet, nicht als Umbau:

- Wann helfen visuelle Verbindungen? → Nur wenn sie eine **inhaltliche Beziehung** zeigen.
- Wann erzeugen sie unnötige Komplexität? → Sobald sie **Infrastruktur** beschreiben.
- Wann wird aus einem Arbeitsraum nur ein technisches Diagramm? → Wenn die sichtbaren
  Verbindungen Rechenschritte statt Bedeutung darstellen.
- Welche Teile einer bestehenden Laufzeitlogik sind technisch wertvoll? → Job-Phasen mit
  Statusabfrage, 409-Doppelstartsperre, SSE-Übertragung, Ringpuffer mit Anti-Spam-Regel,
  Risiko-Ausschluss vor dem Schreiben, Normalisierung inkonsistenter Fremdantworten,
  Validierung vor dem Speichern, harte Deadline pro Teilschritt.

**Vier sichtbare Beziehungsarten** — ausschließlich zwischen Inhaltsobjekten:

| Kante | Frage, die sie beantwortet |
|---|---|
| **STÜTZT** | Warum soll ich das glauben? |
| **WIDERSPRICHT** | Was spricht dagegen? |
| **BLOCKIERT** | Was fehlt noch? |
| **ENTSTAND AUS** | Wo kommt das her? |

**Standardmäßig nicht sichtbar:** jeder einzelne Modellaufruf · interne HTTP-Requests ·
Token-Zähler pro Request · jeder Retry · interne Provider-IDs · rohe Stacktraces ·
Hintergrundentscheidungen ohne Relevanz.

**Regel:** *Der Nutzer sieht, was er verstehen, beeinflussen, prüfen oder später begründen
muss.* Alles andere existiert — aber im Run-Log, nicht auf der Fläche.

---

## 6 · Eigenständige visuelle Sprache

Die App darf modern und außergewöhnlich wirken, darf aber nicht zurückfallen auf:
Standard-Dashboard · permanente Sidebar · Kartenraster · generische Nodes · sterile
Admin-Oberfläche · austauschbares KI-Chatfenster · Cyberpunk · Neon · Glassmorphism ·
Glow ohne Bedeutung · Partikel ohne Funktion · übertriebene Animation · dekorative
Schalter ohne Wirkung.

Entwickle die visuelle Sprache **aus der Funktion**, ausgehend von den vorhandenen
Repo-Tokens (Abschnitt „Gesetzter Befund"):

- **Räumliche Struktur:** Materialwand (links) · Werkbank (Mitte, dominant, ~60 %) ·
  Ablage (rechts) · Fragenleiste (unten, persistent) · Stimme (oben, **eine Zeile**, kein Chatfenster).
- **Materialbereiche, Arbeitsfläche, Ergebnisbereiche, Verlauf, Quellen, offene Fragen,
  Spannungen, Entscheidungen** — jeder Bereich mit einer eigenen, begründeten Funktion.
- **Farben:** Status trägt Bedeutung, niemals Stimmung. Bernstein (`--eye`) ausschließlich
  für Aufmerksamkeit der Leitassistenz und Blockaden.
- **Typografie:** eine **Serifenschrift** für das Arbeitsstück (Signalfunktion: *Werkstück,
  nicht Chatnachricht*), JetBrains Mono für Daten/IDs/Hashes, Inter für UI-Labels.
- **Belegstatus** als durchgehendes Qualitätsmaß: `● belegt · ◐ teilweise · ? offen ·
  ✗ widersprochen · ╱ unbelegbar` — immer als **Zeichen + Text**, nie Farbe allein.
- **Bewegungsprinzip:** Bewegung trägt Zustand, sonst nichts. `prefers-reduced-motion`
  → Standbild; Pause im Hintergrund-Tab; Performance wird gemessen, nicht geschätzt
  (Präzedenz: Partikel-Porträt mit ~71 fps).
- **Zustände, Interaktionen, Übergänge, Informationshierarchie, visuelles Feedback,
  Fehlerdarstellung, Fallbackdarstellung, Fortschrittsdarstellung.**
- **Accessibility:** Tastaturpfade (`Strg+K`, `Strg+Enter`, `Esc`), Fokusringe, Kontrastmessung
  (insbesondere `--muted` auf `--bg`), keine hover-only Informationen, ARIA-Texte für Kanten.
- **Responsiv:** **Werkbank zuerst.** Unter 1024 px werden Randzonen zu Registerkarten;
  kein Zusammenschieben zu einem Dashboard-Gitter.

Jedes visuelle Element muss eine Funktion erfüllen. Die Gestaltung soll sich wie ein
digitales Atelier anfühlen — nicht wie ein Infrastruktur-Kontrollraum.

---

## 7 · OmniRoute technisch einordnen

OmniRoute ist gesetzt, aber **als reale Infrastruktur mit offener Fähigkeitsfrage** —
nicht als bloßer Designbegriff.

**Ziel-Datenfluss:**

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
Router-Port  ──►  OmniRoute Adapter
  ↓
OmniRoute  ──►  Provider / Modelle / Fähigkeiten
  ↓
Ergebnisse / Events / Telemetrie
  ↓
Application Layer  ──►  UI  ──►  Nutzer
```

**Mindestens ein konkreter End-to-End-Workflow**, z. B.:

*Nutzer möchte beurteilen, ob die `schaltwerk`-Laufzeitmuster als Hintergrundorchestrierung
erhalten bleiben können.*
Material- und Repository-Analyse → Leitassistenz erstellt Arbeitsplan → Nutzer bestätigt
oder korrigiert → Policy bestimmt Fähigkeiten → Router-Adapter ruft OmniRoute → Modell A
analysiert Struktur, Modell B prüft Risiken → Synthese → Qualitätsprüfung → **Arbeitsstück**
(Kernaussage, Begründung, Quellen, Risiken, offene Prüfungen) → gespeicherte Version und Verlauf.

Dabei zu erklären:

- Warum welches Modell oder welche Fähigkeit verwendet wird.
- Wann ein einzelnes Modell genügt (Extraktion, Formulierung) und wann mehrere sinnvoll sind
  (Urteil mit Konfliktpotenzial → zwei Modelle parallel; Beweisprüfung → zwei Modelle mit
  **unterschiedlichen Rollen**).
- Wann Parallelisierung unnötig ist (Abhängigkeiten, Verbot durch den Nutzer, kleines Budget).
- Wie Fallbacks funktionieren — **mit Klassenmodell**: Wechsel innerhalb einer Qualitätsklasse
  läuft still und steht nur im Run-Log; Wechsel **zwischen** Klassen wird immer am betroffenen
  Abschnitt gemeldet und dauerhaft in der Version vermerkt.
- Wie verhindert wird, dass ein Fallback die Ergebnisqualität unbemerkt verändert:
  Qualitätsklasse in der Policy · Provenanz je Abschnitt · Klassen-Vermerk am Arbeitsstück ·
  gezielte Neuerzeugung einzelner Abschnitte.
- Welche Fehlerarten unterschieden werden müssen (mindestens: `UNAVAILABLE`, `TIMEOUT`,
  `RATE_LIMITED`, `AUTH_INVALID`, `BUDGET_EXCEEDED`, `MALFORMED_RESPONSE`,
  `CAPABILITY_MISSING`, `MATERIAL_UNREADABLE`, `POLICY_VETO` — mit Regel, welche davon
  keinen Fallback zulassen).
- Wie Abbruch, Wiederaufnahme, Zeitlimits (pro Teilschritt) und Kosten-/Latenzgrenzen
  (Anzeige **vor** dem Lauf, Warnung bei 80 %, kontrollierter Stopp bei 100 %) funktionieren.
- Wie Routing-Entscheidungen dokumentiert werden (Routing-Protokoll je Run, zitierfähig).
- Welche Informationen die UI zeigt und welche verborgen bleiben.

---

## 8 · LibreChat, MashAI und die Leitassistenz

### 8.1 LibreChat-Reuse-Matrix

Bewerte jeden Bereich als: **direkt wiederverwendbar (falls kompatibel)** · **adaptiert
wiederverwendbar** · **nur als Architektur- oder Implementierungsreferenz** · **nicht übernehmen**.
Berücksichtige: Lizenz (MIT) · Sicherheit · Datenmodell-Kompatibilität (Mongo vs. relational)
· Abhängigkeitsrisiko (102 Client-Deps) · UI-Kopplung · Migrationsaufwand · Testbarkeit
(Cluster nötig) · langfristige Wartbarkeit.

Erwartete Richtung (zu begründen, nicht zu übernehmen): **Memory-Semantik, Nachrichtenbaum
als Versionsmodell, Stream-Begriffe, Zitatverarbeitung, Audit-Log, Endpoint-Konfigurationsform**
= adaptiert übernehmen (als Konzept). **Frontend/UI, Mongo-Schemas, Agenten/MCP/Schedules** =
nicht übernehmen oder nur als Referenz.

### 8.2 MashAI-Reuse-Matrix (MPL-2.0 — keine Code-Kopie)

Zu bewerten: Arbeitsraum-/Profil-Modell · Session-Persistenz · Side-Panel-Gegenüberstellung ·
Command-Palette · Ranking-Logik · Settings-Migrationen · Ressourcen-Disziplin · Electron ·
Adblocker · Tab-Metapher · violette Theme-Vorlage · Assets.

Erwartete Richtung: **Konzepte** (Arbeitsräume, Wiederbetreten statt Neuladen, Gegenüberstellung,
Einstellungs-Migrationen) übernehmen; **Electron, Adblocker, Tab-Metapher, Assets, Theme** nicht.

### 8.3 MashAI-inspirierte Kontinuität — kontrolliertes Konzept

Definiere verbindlich: Arbeitskontinuität · kontextbezogene Hinweise · persönliche Präferenzen ·
Memory · proaktive Assistenz · Datenschutz · Einsicht · Korrektur · Löschung · Deaktivierung ·
Berechtigung · Auditierbarkeit.

**Vier Memory-Stufen, Standard ist die flüchtigste:** `SESSION` → `WORKSPACE` → `GLOBAL`
(nur bestätigt) → `NEVER` (abschaltbar). Schlüssel nur `[a-z_]+`. Herkunft und Zeitstempel
obligatorisch. Löschung hart und auditiert. **Anti-Illusions-Regel:** keine Formulierung,
die „Kenntnis" des Nutzers suggeriert, ohne sichtbaren Eintrag mit Datum.

### 8.4 Leitassistenz-Contract

Mindestens: unterstützte Intent-Typen · erlaubte Aktionen ohne Bestätigung ·
bestätigungspflichtige Aktionen · Memory-Regeln · Kontextregeln · Quellenregeln ·
Modell-/Routing-Transparenz · Fehlerregeln · Fallback-Regeln · Audit-Regeln ·
Rechte- und Sicherheitsgrenzen.

**Quellenregeln (streng):** Jede Kernaussage trägt einen Belegstatus. Ohne Beleg ist sie
`offen`, nicht wahr. **Es ist verboten zu behaupten, Material geprüft zu haben, wenn kein
Zugriff stattfand** — dann lautet der Status `unbelegbar`, und die Leitassistenz sagt das
ausdrücklich. Zitate mit Datei + Zeile/Hash, nie „laut Dokumentation".

---

## 9 · Vollständiger Benutzerablauf

Beschreibe den Ablauf, nicht einzelne Buttons: leerer Zustand · erster Einstieg · Material
hinzufügen · Repository-Content auswählen · Arbeitsabsicht formulieren · Interpretation
durch die Leitassistenz · Korrektur durch den Nutzer · Start eines Runs · parallele
Verarbeitung · verständliche Aktivitätsanzeige · Fallback · Fehler · Abbruch ·
Wiederaufnahme · Ergebnis · Quellenprüfung · Eingriff in das Ergebnis · Versionierung ·
Speichern · Verlauf · erneute Nutzung eines früheren Arbeitsstücks · kontrollierte
Memory-Nutzung · spätere Übergabe in eine Code-Änderung oder einen PR-Vorschlag.

**Zustandsmaschine mit elf Zuständen (verbindlich):**
`leer · vorbereitet · laufend · wartet auf Nutzereingabe · erfolgreich ·
erfolgreich mit Einschränkung · fallback aktiv · fehlgeschlagen · abgebrochen ·
wiederaufnehmbar · archiviert.`

Invarianten: kein Zustand verliert bereits erzeugte Abschnitte · `fallback aktiv` ist kein
Endzustand · Nutzerende heißt immer `abgebrochen`, nie `fehlgeschlagen` · `archiviert`
bleibt zitierfähig, aber nicht fortsetzbar.

---

## 10 · Technische Zielarchitektur

Trenne klar: Frontend · UI State · Application Layer · Leitassistenz · Intent-Erkennung ·
Kontextmanagement · Orchestrierungs-Policy · **Router-Port** · OmniRoute-Adapter · OmniRoute ·
Provider · Modelle · Tools · Repository-/Content-Layer · Persistenz · Memory · Authentifizierung ·
Berechtigungen · Konfiguration · Secrets · Monitoring · Logging · Audit · Eventing · Streaming ·
Fehlerbehandlung · Teststrategie · Deployment. Zeige die Architektur als **ASCII-Diagramm**.

**Architekturprinzipien (verbindlich):**

- Das Frontend kennt keine Provider-Secrets.
- Das Frontend ruft OmniRoute nicht direkt auf.
- Die Leitassistenz ist nicht identisch mit einem einzelnen Modell.
- Repository-Zugriffe starten read-only.
- Schreibzugriffe erfordern **Diff → Rechteprüfung → Bestätigung** in dieser Reihenfolge.
- Jeder Run ist nachvollziehbar (Material-Hashes, Fähigkeiten, Modelle, Ereignisse, Kosten, Dauer).
- Fallbacks müssen erkennbar sein, wenn sie Ergebnisqualität, Kosten, Datenschutz oder Fähigkeiten beeinflussen.
- Memory ist transparent und kontrollierbar.
- Provider- und Routerdetails sind hinter dem Port austauschbar, ohne das Produktmodell zu zerstören.
- Bestehende Repository-Funktionalität wird nur mit Schutztests verändert.
- Externe Antworten werden niemals ungeprüft in die Oberfläche geschrieben (`esc()`-Präzedenz).
- Ein Lauf endet nie mit einer unbelegten Behauptung — sie ist `offen` oder `unbelegbar`.

---

## 11 · Entwicklungsstrategie

**Phase 1 – Repository Discovery:** abgeschlossen; Befund in `OMNIA-ATELIER.md`.
Regression: `pytest schaltwerk/tests/` (34 Tests, offline) vor und nach jeder Phase.

**Phase 2 – Produktdefinition:** erste Zielgruppe (Technik-Entscheider mit eigenem KI-Setup,
Single-User) · wichtigste Nutzerhandlung (Beurteilen) · erstes Arbeitsstück („Kann
`schaltwerk` als Hintergrundorchestrierung dienen?") · erste Materialtypen
(`repo_file`, `note`, `workpiece`) · erste Intent-Typen · Grenzen der Leitassistenz ·
Datenschutz- und Memory-Regeln · Zustandsmaschine.

**Phase 3 – UX-Prototyp:** mit **simulierten Events** (MockAdapter, kein Netz, keine
OmniRoute). Fünf Prüffragen, die verhindern, dass daraus ein Dashboard wird:
(1) Steht **ein zusammenhängendes Dokument** im Zentrum? (2) Erscheinen Zahlen **im Satz**
statt in Kästchen? (3) Ist die **Fragenleiste** wichtiger als jede Kennzahl? (4) Lässt sich
jede Aussage **bis zur Quelle** zurückverfolgen? (5) Sieht man **keine** Infrastruktur,
solange sie nicht relevant ist?

**Phase 4 – OmniRoute-Integration:** zuerst angebunden wird die **Fähigkeitsfeststellung**,
nicht das Routing. Read-only Probe: welche Endpunkte antworten · ist ein Inferenz-Endpunkt
erreichbar · Antwortformat und Streaming-Verhalten · Authentifizierung · Fehlerverhalten ·
**bei negativem Befund: Stopp und Rückweg** (Notbetrieb über Direkt-Provider-Adapter oder Mock).
Adapter-Vertrag = `capabilities()`, `invoke()`, `abort()`. Secrets nur im Application Layer,
bevorzugt nur im Prozessspeicher, nie im Frontend, nie in Logs, nie in der Datenbank.

**Phase 5 – LibreChat-Reuse:** welche Bereiche geprüft werden · was als Konzept übernommen
wird · was nur Referenz bleibt · wie UI- und Datenmodellkopplung vermieden wird
(keine Imports, Protokoll in `docs/REUSE.md`).

**Phase 6 – erster End-to-End-Vertikalschnitt:** ein Nutzer · ein Arbeitsstück · Material
aus dem Repository · eine Leitassistenz-Interpretation · ein realer OmniRoute-Run · ein
gespeichertes Ergebnis · ein sichtbarer Fallback-Test · ein Abbruch- und Wiederaufnahme-Test.
**Abnahme:** das Arbeitsstück ist zitierfähig — eine dritte Person verfolgt jede Kernaussage
bis zur Materialstelle, ohne die App zu kennen.

**Phase 7 – visuelle Ausarbeitung:** erst nach funktionierendem Kernfluss; Reihenfolge
Raum/Typografie → Belegstatus → Bewegung → Fallback-/Fehlerdarstellung → Farbe →
Accessibility → Responsivität.

**Phase 8 – Robustheit:** Fehlerklassen · Timeouts pro Teilschritt · Retry-Regeln
(max. 2, Backoff, **nie** bei `AUTH_INVALID`, `BUDGET_EXCEEDED`, `POLICY_VETO`) ·
Fallback-Regeln · Kosten- und Latenzlimits · Datenintegrität über Material-Hashes ·
Versionierung append-only · Audit append-only · Berechtigungen · Datenschutz · Observability.

**Phase 9 – Verifikation:** beweise, dass die App funktioniert · **dass OmniRoute tatsächlich
verwendet wird** (Abgleich mit `/api/usage/proxy-logs` als unabhängiger Nachweis) · dass
Modellrouting und Fallbacks funktionieren · dass Fehler korrekt dargestellt werden · dass
Abbruch und Wiederaufnahme funktionieren · dass Arbeitsstücke konsistent bleiben · dass
Memory transparent bleibt · dass Repository-Content nicht beschädigt wird (Hash-Vergleich
vor/nach, `git status` in `schaltwerk` bleibt leer) · dass bestehende Funktionalität intakt
bleibt (34 Tests) · dass LibreChat nur dort übernommen wurde, wo es Mehrwert liefert.

---

## 12 · MVP

Das MVP beweist nicht möglichst viele KI-Features, sondern die zentrale Produktidee:

> Aus ausgewähltem Repository-Material und einer klaren Nutzerabsicht erzeugt die
> Leitassistenz über OmniRoute ein nachvollziehbares, bearbeitbares und speicherbares
> Arbeitsstück — **und ein Fallback wird sichtbar, statt zu verschwinden.**

Definiere: minimale Screens · minimale Nutzerinteraktionen · minimale Materialtypen ·
minimale Leitassistenz-Fähigkeiten · minimale Backend-Funktionen · minimale Persistenz
(SQLite) · minimale OmniRoute-Integration (eine Fähigkeit plus eine zweite für Parallel-
und Fallback-Test) · minimale Fallback-Integration · minimale Event- und Statusanzeige ·
minimale Sicherheits- und Bestätigungslogik · minimale Testfälle.

**Ausdrücklich NICHT in Version 1:** frei verdrahtbarer Node-Editor · vollständiges
OmniRoute-Admin-Dashboard · vollständige LibreChat-UI · autonome Agentenschwärme ·
automatische Repository-Schreibzugriffe · automatische Deployments · uneingeschränkte
Web-Recherche · komplexe Multi-User-Kollaboration · Bild-, Video- oder Audioproduktion ·
großer MCP-Marktplatz · langfristiges persönliches Memory ohne Kontrolloberfläche ·
Electron-Desktop-App · Proxy-Logistik im Atelier · RAG-/Vektor-Infrastruktur.

---

## 13 · Erweiterbarkeit

Zeige, wie das System später wächst, ohne die Produktidee zu verlieren: weitere Modelle ·
weitere Provider · lokale Modelle · spezialisierte Modelle · multimodale Verarbeitung ·
Web-Recherche · Agenten · Tools · MCP · A2A · Repository-Analyse · Repository-Schreibvorschläge ·
Pull-Request-Erstellung · Dateioperationen · externe APIs · Automationen · Workflows ·
Team-Kollaboration · Rollen und Freigaben · persönliche Memory-Systeme · Medienmaterial ·
eigene Fähigkeiten oder Plugins.

Für jede Erweiterung: wie sie ins Grundmodell passt · welche Fähigkeit sie ermöglicht ·
welches Risiko entsteht · welche Sicherheits- oder UX-Regel sie braucht · warum sie kein
beliebiges Feature ohne Produktbezug wird.

**Aufnahmekriterium:** Eine Erweiterung muss eine der vier Kanten bedienen
(stützt / widerspricht / blockiert / entstand aus) oder einen Materialtyp ergänzen.
Was nur eine neue Anzeige erzeugt, wird nicht aufgenommen.

---

## 14 · Technische Beispiele

Erst nach Produktmodell, UX, Discovery und Architektur. Mögliche Beispiele: Router-Port-
Interface · OmniRoute-Adapter als Pseudocode · Datenmodell für Arbeitsstücke · für
Materialreferenzen · für Runs · Event-/Statusmodell · Fallback-Event · Frontend-State ·
Leitassistenz-Intent · API-Struktur · Berechtigungsprüfung · Repository-Read-only-Zugriff ·
gespeicherte Ergebnisversion.

**Verbindlich:** Keine erfundene OmniRoute-Syntax als reale API. Nicht verifizierte Beispiele
tragen die Zeile `PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX`.

---

## 15 · Endgültige Empfehlung

Schließe mit einer klaren, konkreten Empfehlung:

- Welches der drei Produktmodelle weiterverfolgt wird — und wie die Stärken der anderen beiden darin erhalten bleiben.
- Warum es die beste Wahl ist — begründet über Benutzererlebnis, Eigenständigkeit, technische
  Machbarkeit, Wiederverwendung des Bestands, sinnvolle OmniRoute-Integration, sinnvolle
  LibreChat-Wiederverwendung, kontrollierte MashAI-inspirierte Kontinuität, Qualität der
  Leitassistenz, Erweiterbarkeit, Sicherheit, Wartbarkeit, Vermeidung eines generischen KI-Dashboards.
- Welche Repository-Teile zuerst geprüft werden müssen.
- Welche LibreChat-Bereiche die wichtigsten Prüfobjekte sind.
- Welche MashAI-Eigenschaften konkret zu definieren sind.
- **Welche Entscheidung noch NICHT getroffen werden darf** (mindestens: OmniRoute-Inferenzfähigkeit ·
  Routing-Verantwortung · dauerhafte App-Layer-Sprache · ob „Mesh AI" tatsächlich MashAI meint ·
  ob die Bad-Wolf-Figur übergeht · Electron als Zielplattform).
- Was der allererste konkrete Arbeitsschritt ist.
- Wie der erste vertikale End-to-End-Prototyp aussieht.

**Grundregel zum Schluss:**

Die App ist kein Modell- oder Provider-Manager.
Die App ist ein persönliches, intelligentes Atelier.

OmniRoute ist die Werkstattlogik darunter — **sofern und so weit die reale Installation es
hergibt**. LibreChat liefert bewährte Konzepte, keine Abhängigkeit. MashAI-inspirierte
Prinzipien liefern Kontinuität und Arbeitsrelevanz. Die Leitassistenz verbindet alles nativ.

Der Nutzer soll nicht das Gefühl haben, mehrere KI-Systeme zu bedienen, sondern in einem
einzigen, verständlichen und eigenständigen Arbeitsraum bessere Entscheidungen und wertvolle
Ergebnisse zu erzeugen.

---

## Anhang · Offene Punkte (ZU PRÜFEN)

1. OmniRoute-Inferenz-API: Existenz, Pfad, Authentifizierung, Streaming.
2. OmniRoute-Routing-/Fallback-Logik: in OmniRoute oder in unserer Policy?
3. OmniRoute-Telemetrie pro Request (Kosten/Token).
4. Multimodalität, Dateien, Audio, Video, Embeddings, MCP, A2A.
5. OmniRoute-Version/Image-Tag.
6. Lizenzstatus von `schaltwerk` (keine Lizenzdatei vorhanden).
7. Ob „Mesh AI" tatsächlich MashAI meint.
8. Python vs. Node als dauerhafte App-Layer-Sprache.
9. Electron als Zielplattform.
10. Ob die Bad-Wolf-Figur in die Leitassistenz übergeht (Copyright-Vorgeschichte BBC).
11. Laufzeitumgebung: Port 24615 vs. 20128, drei Container, Key-Rotation nach Neustart.
12. Kontrastwert `--muted` auf `--bg` ausreichend?

*Änderungen an dieser Aufgabenstellung gehören in diese Datei, nicht in ein neues Dokument.*
