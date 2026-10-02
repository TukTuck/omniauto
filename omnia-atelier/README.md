# omnia-atelier/ — Arbeitsordner des Zweigs `arena/01a0fe6e-omniauto`

Dieser Ordner enthält **alles**, was dieser Zweig baut. Nichts davon liegt auf der
Repository-Wurzel, und nichts davon berührt einen anderen Zweig oder `schaltwerk/`.

## Ordner-Konvention

```
omniauto/                          ← Wurzel: nur gemeinsame, unveränderliche Dinge
├── Kurz-main (1).zip              ← Material (MashAI, MPL-2.0) · NICHT ANFASSEN
├── LibreChat-main.zip             ← Material (LibreChat v0.8.8, MIT) · NICHT ANFASSEN
├── schaltwerk/                    ← bestehendes Werkzeug · NICHT ANFASSEN
├── omnia-atelier/                 ← DIESER ZWEIG
└── <ordner-eines-anderen-zweigs>/ ← ein anderer Zweig, daneben, ohne Berührung
```

Regeln:

1. **Ein Zweig = ein Ordner.** Der Ordnername benennt die Version/das Produkt.
2. **Keine gemeinsamen Dateien.** Wurzeldateien, `schaltwerk/` und die Archive bleiben unangetastet.
3. **Pfade im Dokument** sind ab Repository-Wurzel angegeben, damit sie eindeutig bleiben.
4. **Jeder Ordner ist selbststartfähig:** kein Build, keine CDN-Abhängigkeit, keine
   Abhängigkeit von einem anderen Ordner.

## Inhalt

| Pfad | Zweck |
| --- | --- |
| `docs/OMNIA-ATELIER.md` | Produkt-, UX- und Architekturkonzept (15 Teile) |
| `docs/OMNIROUTE-PROBE.md` | *(folgt)* Protokoll des read-only Capability-Probe |
| `docs/REUSE.md` | *(folgt)* Reuse-Protokoll: was woher übernommen wurde, mit Lizenz |
| `prototype/index.html` | klickbarer Phase-3-Prototyp, simulierte Events |

## Prototyp starten

```bash
python3 -m http.server 8765 --bind 0.0.0.0 --directory omnia-atelier/prototype
# → http://127.0.0.1:8765
```

Eine HTML-Datei, kein Build, keine CDN-Abhängigkeit, kein Netzwerkaufruf.
Alle Ereignisse sind simuliert (MockAdapter).

## Erster Arbeitsschritt

Der OmniRoute-Capability-Probe — read-only, eine Frage:
*Gibt es einen Inferenz-Endpunkt, und wie sieht seine Antwort aus?*
Ergebnis in `docs/OMNIROUTE-PROBE.md` (Konzept Abschnitt 15.7).
