# Aufgabe: Entwickle Omnia Atelier auf Basis des bestehenden Repositorys

> **Hinweis zu dieser Fassung.** Dies ist dein ursprünglicher Prompt in **derselben Aufteilung** (§1–§15), mit Änderungen nur dort, wo das Original dem geprüften Repository-Befund widerspricht. Änderungen sind inline mit den im Prompt selbst definierten Marken gekennzeichnet: **BEKANNT** (geprüfter Befund), **ZU PRÜFEN** (offene Frage), **VORSCHLAG** (meine Idee — **nicht gesetzt**). Alles Unmarkierte entspricht dem Original.
>
> **Vorab-Befund (bereits geprüft — reine Fakten, keine Festlegungen).** Das Repository hat einen Commit (`60dd904`) und 12 Dateien. `schaltwerk/` ist Proxy-Logistik (Python/FastAPI, `server.py` + `static/index.html`, 34 Tests, RAM-only, kein Login, keine Datenbank, Windows-Start per `STARTEN.bat`), **kein** Node-Editor und ohne Graph-Logik. `Kurz-main (1).zip` ist **MashAI** (Electron-Workspace für fremde KI-Weboberflächen, MPL-2.0, 66 Tests — kein Memory-System). `LibreChat-main.zip` ist **v0.8.8, MIT**, TypeScript + MongoDB + 102 Client-Abhängigkeiten. **OmniRoute** ist nur in der Verwaltungsebene verifiziert (10 Endpunkte für Proxies/Provider/Usage, Auth per `Bearer` + `x-api-key`); Inferenz, Routing und Fallback sind **ZU PRÜFEN**.

---

Du entwickelst eine außergewöhnliche, eigenständige AI-Anwendung auf Basis des bestehenden GitHub-Repositorys:

https://github.com/TukTuck/omniauto

WICHTIG:
Denke die gesamte Aufgabe vollständig durch, bevor du antwortest.

Liefere keine oberflächliche Designidee, kein generisches AI-Dashboard und keine bloße Sammlung von Features.

Erfinde keine Repository-Dateien, keine APIs, keine Komponenten, keine Datenmodelle und keine bereits vorhandenen Funktionen.

Wenn etwas vom tatsächlichen Repository, seiner Dokumentation, seiner Konfiguration oder seiner konkreten Implementierung abhängt, kennzeichne es ausdrücklich als:

ZU PRÜFEN

Unterscheide in der gesamten Antwort konsequent zwischen:

- BEKANNT
  Informationen, die aus dieser Aufgabenstellung sicher hervorgehen **oder aus dem Repository tatsächlich gelesen wurden**

- ZU PRÜFEN
  Informationen, die erst durch Untersuchung des Repositorys, der verwendeten Versionen oder der technischen Dokumentation verifiziert werden müssen

- ANNAHME
  Plausible, aber noch unbestätigte Voraussetzungen

- VORSCHLAG
  Neue Produkt-, UX-, Architektur- oder Implementierungsentscheidungen

Die zentrale Grundregel lautet:

Baue keinen OmniRoute-Manager mit schöner Oberfläche.
Baue kein LibreChat-Redesign.
Baue keine Mesh-AI-Kopie.
Baue keinen generischen Chatbot.
Baue keinen technischen Node-Editor als Selbstzweck.

Baue ein eigenständiges Produkt, dessen Arbeitsweise durch OmniRoute, wiederverwendbare LibreChat-Module, Repository-Content und eine zentrale native Leitassistenz ermöglicht wird.

Die technische Infrastruktur soll sichtbar werden, wenn sie für Verständnis, Vertrauen, Eingriff oder Qualität relevant ist.

Sie soll unsichtbar bleiben, wenn sie nur technische Komplexität erzeugt.

---

# 1. Gesetzte technische und produktstrategische Grundlagen

Folgende Punkte sind gesetzt und dürfen nicht mehr als offene Grundsatzfrage behandelt werden.

## 1.1 OmniRoute ist ein fester Bestandteil

OmniRoute wird verbindlich als zentrale Infrastruktur für Modelle, Provider und Routing verwendet.

OmniRoute soll insbesondere für folgende Aufgaben eingeplant werden:

- Modellzugang
- Provider-Abstraktion
- Modellrouting
- Fallbacks
- Verfügbarkeit
- Latenz
- Kosten- und Qualitätsregeln
- parallele Modellverarbeitung, wenn sinnvoll
- multimodale Modellfähigkeiten, sofern in der realen Installation verfügbar
- gegebenenfalls Embeddings, Dateien, Bilder, Audio, Video, MCP oder A2A, sofern real unterstützt und konfiguriert

WICHTIG:

Die konkrete OmniRoute-Version, API, Konfiguration, Providerliste, Modellverfügbarkeit, Secret-Verwaltung, Fallback-Logik, Telemetrie und Deployment-Art müssen zuerst untersucht werden.

Es dürfen keine OmniRoute-APIs, Endpunkte, Konfigurationsdateien oder Funktionsnamen erfunden werden.

Wenn konkrete Syntax oder konkrete APIs nicht verifiziert sind, verwende ausschließlich klar gekennzeichneten Pseudocode.

Die App-UI darf nicht direkt an OmniRoute gekoppelt sein.

Die App soll über einen eigenen Application Layer und einen Router Adapter mit OmniRoute kommunizieren.

**ZU PRÜFEN:** Ob OmniRoute eine Inferenz-API anbietet, ist nicht belegt — verifiziert sind nur die Verwaltungsendpunkte. Die Untersuchung dieser Frage steht vor jeder Integration.

## 1.2 LibreChat wird als technische Modulquelle genutzt

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

**BEKANNT:** Lizenz MIT, Version v0.8.8, TypeScript + MongoDB + Meilisearch + pgvector, 102 Client-Abhängigkeiten. Ob daraus Code oder nur Konzepte übernommen werden, ist **VORSCHLAG** und offen.

## 1.3 Mesh AI ist eine persönliche Inspirationsrichtung

Mesh AI soll nicht als visuelle Vorlage kopiert werden.

Es ist eine Inspirationsquelle für eine persönlichere, vernetztere, kontextbewusstere und kontinuierlichere AI-Erfahrung.

**ANNAHME:** Gemeint ist **MashAI** aus `Kurz-main (1).zip` — ein Electron-Workspace für die Weboberflächen von ChatGPT, Claude, Gemini, Perplexity, Grok und DeepSeek mit Profilen, Tabs, Session-Persistenz und Adblocking. **ZU PRÜFEN, ob diese Zuordnung stimmt.** MashAI hat **kein** Gedächtnissystem; sein „persönlicher" Anteil besteht aus Profilen und Session-Persistenz.

Die konkrete Bedeutung von Mesh AI muss vor der Implementierung präzisiert werden.

Zu klären ist insbesondere:

- Was bedeutet „persönlich" konkret?
- Soll die Leitassistenz sich an Arbeitsstücke erinnern?
- Soll sie sich an Präferenzen erinnern?
- Soll sie proaktive Hinweise geben?
- Welche Informationen dürfen dauerhaft gespeichert werden?
- Welche Informationen müssen temporär bleiben?
- Wie kann der Nutzer gespeicherte Erinnerungen sehen?
- Wie kann der Nutzer Erinnerungen korrigieren?
- Wie kann der Nutzer Erinnerungen löschen?
- Wann darf die Assistenz proaktiv handeln?
- Wann muss die Assistenz ausdrücklich fragen?

Die Anwendung darf niemals den Eindruck erwecken, dass eine KI „alles über den Nutzer weiß", wenn dies nicht transparent, kontrollierbar und technisch begrenzt ist.

**BEKANNT:** MashAI ist MPL-2.0 (file-level copyleft). Code- und Asset-Kopien sind damit ausgeschlossen; nur Konzepte.

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
- Routing- und Fallback-Ereignisse verständlich erklären, wenn sie relevant sind
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

---

# 2. Zentrale Produktfrage

Entwickle zuerst das eigentliche Produktmodell.

Beantworte nicht zuerst:

„Wie sieht ein OmniRoute-Dashboard aus?"

Beantworte stattdessen:

- Was macht der Nutzer in dieser App eigentlich?
- Welche zentrale Tätigkeit steht im Mittelpunkt?
- Was gibt der Nutzer hinein?
- Was entsteht daraus?
- Wie unterscheidet sich das Ergebnis von einer normalen Chat-Antwort?
- Welche Rolle spielt Repository-Content?
- Welche Rolle spielt die Leitassistenz?
- Wann wird OmniRoute sichtbar?
- Wann bleibt OmniRoute unsichtbar?
- Wann sind mehrere Modelle sinnvoll?
- Wann sind Tools oder Agenten sinnvoll?
- Welche Entscheidungen kann der Nutzer beeinflussen?
- Welche Dinge passieren automatisch?
- Warum ist diese App kein Chatbot?
- Warum ist diese App kein Agent-Dashboard?
- Warum ist diese App kein Node-Editor?
- Warum sollte sich diese Arbeitsweise eigenständig, sinnvoll und interessant anfühlen?

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

---

# 3. Entwickle drei wirklich unterschiedliche Produktmodelle

Entwickle drei unterschiedliche Ansätze.

Es dürfen nicht drei visuelle Varianten derselben Chat-App sein.

Für jeden Ansatz liefere:

- Name
- Kernidee
- zentrale Nutzerhandlung
- Was sieht der Nutzer beim Start?
- Was bringt der Nutzer ein?
- Was geschieht danach?
- Welche Rolle übernimmt die Leitassistenz?
- Welche Rolle übernimmt OmniRoute?
- Welche Rolle übernehmen Modelle?
- Welche Rolle übernehmen LibreChat-Module?
- Welche Rolle übernimmt Mesh-AI-inspirierte Kontinuität?
- Welche Rolle übernimmt vorhandener Repository-Content?
- Wie wird Aktivität sichtbar?
- Wie sieht eine typische Nutzung aus?
- Was unterscheidet das Konzept vom alten Schaltwerk?
- Risiken des Konzepts
- Chancen des Konzepts
- ASCII-Skizze

Mindestens einer der Ansätze soll das Signal-Garden-/Atelier-Prinzip konsequent ausarbeiten.

Beispielhafte Richtungen können sein:

- Signal Garden / Omnia Atelier
- Brief Foundry
- Evidence Room

Diese Namen sind nur Orientierung und dürfen verbessert werden.

Empfiehl anschließend klar einen Ansatz als Grundlage.

**VORSCHLAG (nicht gesetzt):** Als Unterschied zwischen den drei Ansätzen könnten drei unterschiedliche Kernhandlungen dienen — *herstellen*, *prüfen*, *übergeben*. Ob das trägt, ist offen.

---

# 4. Repository-first Discovery

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
- bisherige Schaltwerk-Logik
- Node-/Graph-Daten
- Abhängigkeiten
- technische Schulden
- Lizenz- und Copyright-Fragen
- relevante Dokumentation
- offene Risiken

Für jeden Bereich erkläre:

- Was konkret geprüft werden muss
- Warum dies geprüft werden muss
- Welche Entscheidung davon abhängt
- Ob der Bereich voraussichtlich beibehalten, erweitert, neu interpretiert, ersetzt oder nicht angefasst werden sollte

**BEKANNT:** Mehrere Bereiche dieser Liste existieren im Repository nicht — Monorepo, CI/CD, Deployment, Datenbank, ORM, WebSocket, Secret-Management, Authentifizierung, Node-/Graph-Daten. „Nicht vorhanden" ist ein gültiges Prüfergebnis und **kein** Anlass, etwas zu erfinden.

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

**BEKANNT:** Davon existiert genau eine funktionierende Anwendung — `schaltwerk` mit 34 offline laufenden Tests, ohne Login, ohne Datenbank, ohne CI/CD. `schaltwerk` hat **keine Lizenzdatei**; MashAI ist MPL-2.0. Beides ist vor jeder Wiederverwendung zu klären.

---

# 5. Schaltwerk kritisch neu denken

Das bisherige Schaltwerk-/Node-/Graph-Prinzip soll nicht pauschal verworfen werden.

**BEKANNT:** `schaltwerk` enthält **kein** Node-/Graph-Prinzip, sondern Proxy-Logistik mit Tabellen, SSE-Job und RAM-Ringpuffern. Die folgenden Fragen sind deshalb als Zielprinzip zu beantworten, nicht als Umbau einer vorhandenen Graph-Logik: *Was wäre eine Verbindung wert, wenn es sie gäbe — und was darf deshalb niemals als Verbindung gezeigt werden?*

Analysiere:

- Welche Vorteile haben Nodes?
- Wann helfen visuelle Verbindungen?
- Wann helfen räumliche Arbeitsflächen?
- Wann erzeugen sie unnötige Komplexität?
- Wann zeigen sie eine echte inhaltliche Beziehung?
- Wann zeigen sie nur technische Infrastruktur?
- Welche Informationen gehören sichtbar auf die Oberfläche?
- Welche Informationen gehören in einen Hintergrundprozess?
- Wann wird aus einem Arbeitsraum nur ein technisches Diagramm?
- Welche Teile einer bestehenden Schaltwerk-Logik könnten technisch wertvoll bleiben?
- Wie können technische Graphen in eine verständliche, semantische Darstellung übersetzt werden?

**BEKANNT:** Technisch wertvoll in `schaltwerk` sind unabhängig von der Domäne: Job-Phasen mit Statusabfrage, 409-Doppelstartsperre, SSE-Übertragung, Ringpuffer mit Anti-Spam-Regel, Risiko-Ausschluss vor jedem Schreibzugriff, Normalisierung inkonsistenter Fremdantworten, Validierung vor dem Speichern, harte Deadline pro Teilschritt.

Formuliere klare Regeln.

Beispiel für sinnvolle sichtbare Beziehungen:

- Dieses Repository-Modul stützt diese Entscheidung
- Diese Quelle widerspricht dieser Annahme
- Diese offene Frage blockiert eine Freigabe
- Dieses Ergebnis basiert auf diesen Materialien
- Diese Alternative wurde aus nachvollziehbaren Gründen verworfen

Beispiel für Informationen, die standardmäßig nicht sichtbar sein sollten:

- jeder einzelne Modellaufruf
- interne HTTP-Requests
- Token-Zähler pro Request
- jeder Retry
- interne Provider-IDs
- rohe technische Stacktraces
- jede Hintergrundentscheidung ohne Relevanz für den Nutzer

Die Regel lautet:

Der Nutzer soll sehen, was er verstehen, beeinflussen, prüfen oder später begründen muss.

---

# 6. Entwickle eine eigenständige visuelle Sprache

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

Beispiel für ein mögliches Raumprinzip:

- Materialrand:
  Quellen, Dateien, Repository-Inhalte, Notizen und Anforderungen

- Werkfläche:
  Aktives Arbeitsstück, Entscheidungen, Fragen, Alternativen, Konflikte und Bearbeitung

- Ergebnisrand:
  verdichtete Ergebnisse, Exporte, Versionen, nächste Schritte und Freigaben

Die visuelle Gestaltung soll sich wie ein digitales Atelier, eine Werkstatt oder ein Denkraum anfühlen.

Nicht wie ein Infrastruktur-Kontrollraum.

**BEKANNT:** `schaltwerk` enthält bereits ein gemessenes Anti-KI-Look-Designsystem (Radius 3 px, Mono-Statuszeile statt KPI-Kästchen, Pills nur für echte Stati, Tokens `--bg #0d0e12`, `--ink #d6d7dd`, `--muted #8a8c99`, `--eye #d9a441`). Ob das die Basis der neuen Sprache ist, ist **VORSCHLAG**.

---

# 7. OmniRoute technisch einordnen

OmniRoute ist gesetzt.

Ordne OmniRoute als reale Infrastruktur ein, nicht als bloßen Designbegriff.

**ZU PRÜFEN:** Verifiziert ist nur die Verwaltungsebene (Proxies, Provider, Usage-Logs). Die Modellebene ist eine begründete Erwartung, kein Befund. Die Architektur ist so zu beschreiben, dass sie auch ohne OmniRoute-Inferenz sinntragend bleibt.

Beschreibe einen Ziel-Datenfluss:

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
OmniRoute Adapter
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

Entwickle mindestens einen konkreten End-to-End-Workflow.

Beispiel:

Nutzer möchte beurteilen, ob die bestehende Schaltwerk-Logik als Hintergrundorchestrierung erhalten bleiben kann.

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

Erkläre dabei:

- Warum welches Modell oder welche Fähigkeit verwendet wird
- Wann ein einzelnes Modell genügt
- Wann mehrere Modelle sinnvoll sind
- Wann Parallelisierung sinnvoll ist
- Wann sie unnötig ist
- Wie Fallbacks funktionieren sollen
- Welche Fehlerarten unterschieden werden müssen
- Wie Abbruch funktioniert
- Wie Wiederaufnahme funktioniert
- Wie Kosten- und Latenzgrenzen behandelt werden
- Wie Routing-Entscheidungen dokumentiert werden
- Welche Informationen die UI zeigen soll
- Welche Informationen verborgen bleiben sollen
- Wie verhindert wird, dass ein Fallback die Ergebnisqualität unbemerkt verändert

**VORSCHLAG (nicht gesetzt):** Für den letzten Punkt könnte ein Qualitätsklassen-Modell dienen — jede Fähigkeit hat eine Klasse; ein Wechsel **innerhalb** einer Klasse bleibt still, ein Wechsel **zwischen** Klassen wird gemeldet und dauerhaft in der Version vermerkt; der betroffene Abschnitt bleibt gezielt neu erzeugbar. Ob das die richtige Mechanik ist, ist offen.

Es dürfen keine erfundenen OmniRoute-Aufrufe als echte Syntax dargestellt werden.

Nicht verifizierte Beispiele müssen als PSEUDOCODE markiert werden.

---

# 8. LibreChat und Mesh AI technisch sinnvoll einarbeiten

Entwickle eine Reuse-Matrix.

Für LibreChat unterscheide:

- direkt wiederverwendbar, falls kompatibel
- adaptiert wiederverwendbar
- nur als Architektur- oder Implementierungsreferenz
- nicht übernehmen

Berücksichtige:

- Lizenz
- Sicherheit
- Datenmodell-Kompatibilität
- Abhängigkeitsrisiken
- UI-Abhängigkeiten
- Migrationsaufwand
- Testbarkeit
- langfristige Wartbarkeit

Für Mesh-AI-inspirierte Funktionen entwickle ein kontrolliertes Konzept für:

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

Die Leitassistenz darf keine unklare Blackbox sein.

Definiere einen Leitassistenz-Contract.

Der Contract soll mindestens enthalten:

- unterstützte Intent-Typen
- erlaubte Aktionen ohne Bestätigung
- bestätigungspflichtige Aktionen
- Memory-Regeln
- Kontextregeln
- Quellenregeln
- Modell-/Routing-Transparenz
- Fehlerregeln
- Fallback-Regeln
- Audit-Regeln
- Rechte- und Sicherheitsgrenzen

---

# 9. Vollständiger Benutzerablauf

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
- Versionierung
- Speichern
- Verlauf
- erneute Nutzung eines früheren Arbeitsstücks
- kontrollierte Memory-Nutzung
- mögliche spätere Übergabe in eine Code-Änderung oder einen Pull-Request-Vorschlag

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

---

# 10. Technische Zielarchitektur

Entwickle eine technisch belastbare Zielarchitektur.

Trenne klar:

- Frontend
- UI State
- Application Layer
- Leitassistenz
- Intent-Erkennung
- Kontextmanagement
- Orchestrierungs-Policy
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
- Schreibzugriffe erfordern Diff, Rechteprüfung und Bestätigung.
- Jeder Run ist nachvollziehbar.
- Fallbacks müssen erkennbar sein, wenn sie Ergebnisqualität, Kosten, Datenschutz oder Fähigkeiten beeinflussen.
- Memory ist transparent und kontrollierbar.
- Provider- und Routerdetails sind austauschbar, ohne das Produktmodell zu zerstören.
- Bestehende Repository-Funktionalität wird nur mit Schutztests verändert.

---

# 11. Entwicklungsstrategie

Erstelle eine konkrete Reihenfolge.

## Phase 1 – Repository Discovery

Definiere:

- welche Dateien, Bereiche und Konfigurationen untersucht werden
- welche Befunde dokumentiert werden
- welche Risiken sichtbar werden müssen
- wie ein Preservation Contract entsteht
- welche bestehenden Funktionen durch Regressionstests geschützt werden

**BEKANNT:** Der Schutz besteht konkret aus `cd schaltwerk && pip install -r requirements-dev.txt && pytest tests/` — 34 Tests, offline, ohne Netz und ohne OmniRoute.

## Phase 2 – Produktdefinition

Definiere:

- die erste Zielgruppe
- die wichtigste Nutzerhandlung
- das erste Arbeitsstück
- die ersten Materialtypen
- die ersten Intent-Typen
- die Grenzen der Leitassistenz
- die Datenschutz- und Memory-Regeln
- die Zustandsmaschine eines Runs

## Phase 3 – UX-Prototyp

Definiere:

- was zunächst mit simulierten Events getestet wird
- welche Screens und Zustände klickbar sein müssen
- wie geprüft wird, ob der Arbeitsraum verständlich ist
- wie verhindert wird, dass der Prototyp wieder wie ein Dashboard wirkt

## Phase 4 – OmniRoute-Integration

Definiere:

- welche reale OmniRoute-Funktion zuerst angebunden wird
- welchen Adapter-Vertrag die Anwendung benötigt
- wie Streaming, Fehler, Fallbacks und Events behandelt werden
- wie Secrets und Provider-Informationen geschützt werden

**ZU PRÜFEN:** Welche OmniRoute-Funktion zuerst angebunden wird, hängt daran, ob überhaupt eine Inferenz-API existiert. Die Klärung dieser Frage steht vor jeder Implementierung.

## Phase 5 – LibreChat-Reuse

Definiere:

- welche LibreChat-Module geprüft werden
- welche Bausteine tatsächlich übernommen werden
- welche nur als Referenz dienen
- wie UI- und Datenmodellkopplung vermieden wird

## Phase 6 – erster End-to-End-Vertikalschnitt

Definiere:

- einen Nutzer
- ein Arbeitsstück
- Material aus dem Repository
- eine Leitassistenz-Interpretation
- einen realen OmniRoute-Run
- ein gespeichertes Ergebnis
- einen sichtbaren Fallback-Test
- einen Abbruch- und Wiederaufnahme-Test

## Phase 7 – visuelle Ausarbeitung

Definiere:

- welche visuellen Regeln erst nach funktionierendem Kernfluss verfeinert werden
- wie Typografie, Farben, Bewegung und Interaktion funktional eingesetzt werden
- wie Accessibility und Responsivität sichergestellt werden

## Phase 8 – Robustheit

Definiere:

- Fehlerklassen
- Timeouts
- Retry-Regeln
- Fallback-Regeln
- Kostenlimits
- Latenzlimits
- Datenintegrität
- Versionierung
- Audit
- Berechtigungen
- Datenschutz
- Observability

**VORSCHLAG (nicht gesetzt):** Als Fehlerklassen kämen in Frage: nicht verfügbar, Zeitüberschreitung, Ratenlimit, ungültige Anmeldedaten, Budget überschritten, unparsebare Antwort, fehlende Fähigkeit, Material nicht lesbar, Policy-Verweigerung.

## Phase 9 – Verifikation

Zeige, wie bewiesen wird, dass:

- die App funktioniert
- OmniRoute tatsächlich verwendet wird
- Modellrouting funktioniert
- Fallbacks funktionieren
- Fehler korrekt dargestellt werden
- Abbruch und Wiederaufnahme funktionieren
- gespeicherte Arbeitsstücke konsistent bleiben
- Memory transparent und kontrollierbar bleibt
- Repository-Content nicht unbeabsichtigt beschädigt wird
- bestehende Funktionalität nicht durch die neue UX zerstört wird
- LibreChat-Komponenten nur dort übernommen wurden, wo sie wirklich Mehrwert liefern

---

# 12. MVP

Definiere ein realistisches MVP.

Das MVP soll nicht möglichst viele AI-Features enthalten.

Es soll die zentrale Produktidee beweisen.

Das MVP soll mindestens beweisen:

Aus ausgewähltem Repository-Material und einer klaren Nutzerabsicht kann die Leitassistenz über OmniRoute ein nachvollziehbares, bearbeitbares und speicherbares Arbeitsstück erzeugen.

Definiere:

- minimale Screens
- minimale Nutzerinteraktionen
- minimale Materialtypen
- minimale Leitassistenz-Fähigkeiten
- minimale Backend-Funktionen
- minimale Persistenz
- minimale OmniRoute-Integration
- minimale Fallback-Integration
- minimale Event- und Statusanzeige
- minimale Sicherheits- und Bestätigungslogik
- minimale Testfälle

Definiere ebenso klar:

Was gehört ausdrücklich NICHT in Version 1?

Beispiele möglicher Nicht-MVP-Bestandteile:

- frei verdrahtbarer Node-Editor
- vollständiges OmniRoute-Admin-Dashboard
- vollständige LibreChat-UI
- autonome Agentenschwärme
- automatische Repository-Schreibzugriffe
- automatische Deployments
- uneingeschränkte Web-Recherche
- komplexe Multi-User-Kollaboration
- Bild-, Video- oder Audioproduktion
- großer MCP-Marktplatz
- langfristiges persönliches Memory ohne klare Kontrolloberfläche

**VORSCHLAG (nicht gesetzt, Ergänzung zur Liste):** Electron-Desktop-App · Proxy-Logistik im Atelier (verbleibt in `schaltwerk`) · RAG- und Vektor-Infrastruktur.

---

# 13. Erweiterbarkeit

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

---

# 14. Technische Beispiele

Erst nachdem Produktmodell, UX, Discovery-Plan und Architektur feststehen, darfst du kleine technische Beispiele verwenden.

Mögliche Beispiele:

- Router-Port-Interface
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

PSEUDOCODE – NICHT VERIFIZIERTE OMNIROUTE-SYNTAX

---

# 15. Endgültige Empfehlung

Schließe mit einer klaren, konkreten Empfehlung ab.

Beantworte:

- Welche der drei Produktideen sollte weiterverfolgt werden?
- Warum ist sie die beste Wahl?
- Wie verbindet sie OmniRoute, LibreChat, Mesh-AI-inspirierte Prinzipien und das bestehende Repository?
- Welche Teile des Repositorys müssen zuerst geprüft werden?
- Welche LibreChat-Module sind die wahrscheinlich wichtigsten Prüfobjekte?
- Welche Eigenschaften aus Mesh AI sollten konkret definiert werden?
- Welche Entscheidung darf noch NICHT getroffen werden?
- Was ist der allererste konkrete nächste Arbeitsschritt?
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

OmniRoute ist die Werkstattlogik darunter.
LibreChat liefert gegebenenfalls bewährte technische Bausteine.
Mesh-AI-inspirierte Prinzipien liefern Kontinuität und persönliche Relevanz.
Die Leitassistenz verbindet alles nativ.

Der Nutzer soll nicht das Gefühl haben, mehrere AI-Systeme zu bedienen.

Er soll das Gefühl haben, in einem einzigen, verständlichen und eigenständigen Arbeitsraum bessere Entscheidungen und wertvolle Ergebnisse zu erzeugen.

---

*Änderungen an dieser Aufgabenstellung gehören in diese Datei, nicht in ein neues Dokument.*
