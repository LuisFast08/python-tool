# 🧰 Luis Tool – Multifunktionales CLI-Tool in Python

## Über das Projekt

**Luis Tool** ist eine selbstentwickelte Konsolenanwendung in Python, die mehrere nützliche Werkzeuge in einem Menü vereint. Ziel des Projekts war es, Python Grundlagen zu lernen.

Dieses Tool ist im Rahmen meiner persönlichen Weiterentwicklung entstanden und demonstriert meine Fähigkeiten in den Bereichen:
- Strukturierte Programmierung
- Fehlerbehandlung und Nutzerführung
- API-Integration (OpenWeather, ipinfo.io)
- Kreatives Projektdenken

---

## Funktionen im Überblick

| 🔧 Funktion                     | Beschreibung                                                |
|-------------------------------|-------------------------------------------------------------|
| Barcode-Checker               | Überprüft die Gültigkeit von EAN-13 Barcodes                |
| Timer                         | Ein einfacher Countdown-Timer                               |
| Primzahl-Tester               | Erkennt, ob eine eingegebene Zahl eine Primzahl ist         |
| Summierer                     | Addiert alle Zahlen bis zu einer bestimmten Eingabe         |
| Teiler-Finder                 | Zeigt alle Teiler einer eingegebenen Zahl                   |
| Zahlen-Ratespiel              | Spiel, bei dem man eine zufällige Zahl erraten muss         |
| Wetterabfrage                 | Wetterinformationen per PLZ über die OpenWeatherMap API     |
| BMI-Rechner                   | Berechnet und bewertet den Body-Mass-Index                  |
| IP-Checker                    | Zeigt öffentliche Informationen zu IP-Adressen              |
| To-Do-Liste                   | Temporäre Aufgabenverwaltung im Speicher                    |
| Passwort-Generator            | Generiert sichere, zufällige Passwörter                     |

---

## Technischer Überblick

- **Sprache:** Python 3  
- **Bibliotheken:** `requests`, `random`, `os`, `time`, `string`  
- **Konzepte:** Eingabevalidierung, Modularität, REST API Nutzung, CLI Design

---

## Projekt starten

python tool.py

### Voraussetzungen

- Python 3.x  
- Internetverbindung (für Wetter- und IP-Funktionen)  
- Installation der benötigten Bibliothek:
```bash

pip install requests
