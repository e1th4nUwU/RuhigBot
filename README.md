# 🧸 RuhigBot

## 📖 Beschreibung
**RuhigBot** ist eine Webapp-Chatbot 🖥️, der auf dem **Llama 4 Modell** 🦙 basiert.  
Er wurde entwickelt, um eine **benutzerfreundliche Schnittstelle** für die Interaktion mit dem Modell bereitzustellen.  
Der Bot kann auf verschiedene Fragen ❓ und Anfragen 📩 reagieren und bietet eine einfache Möglichkeit, mit dem Modell zu interagieren.

## 🧸 Wie kann RuhigBot ihr helfen ?
- **Fragen beantworten** ❓: RuhigBot kann auf eine Vielzahl von Fragen antworten, die Sie ihm stellen.
- **Unterhaltung führen** 💬: Sie können mit RuhigBot chatten und er wird versuchen, auf Ihre Nachrichten zu reagieren.
- **Spaß haben** 🎉: RuhigBot ist nicht nur informativ, sondern auch unterhaltsam. Sie können mit ihm spielen und experimentieren.

## 📝 Benutzer-Anweisungen
1. **Zugriff auf die Webanwendung** 🌐: Öffnen Sie Ihren Webbrowser und gehen Sie zu `http://localhost:8000` oder `http://<Ihre_IP>:8000`.
2. **Füllen sie die Daten aus** 📝:
- Name 👤
- Alter 🎂
- Woher kommen Sie? 🌍
- Was mir in früheren Therapien geholfen hat 🧸
- Was mich jetzt stört 😔 (*obligatorisch*)

1. **Chatten** 💬: Geben Sie Ihre Fragen oder Nachrichten in das Textfeld ein und klicken Sie auf "Senden" 📤.


## 🛠️ Technologien
- **DJango** 🐍: Ein leistungsstarkes Web-Framework für Python, das die Entwicklung von Webanwendungen erleichtert.
- **OpenRouter API** 🔑: Eine API, die den Zugriff auf das Llama 4 Modell ermöglicht.
- **HTML/CSS** 🎨: Für die Gestaltung der Benutzeroberfläche.
- **Python** 🐍: Die Programmiersprache, in der die Anwendung geschrieben ist.
- **Git** 🔧: Versionskontrollsystem zur Verwaltung des Quellcodes.
- **GitHub** 🐙: Plattform zur Speicherung und Verwaltung des Quellcodes.
- **EC2** ☁️: Amazon Web Services (AWS) Elastic Compute Cloud, um die Anwendung in der Cloud bereitzustellen.

## 🗂️ Projektstruktur und Beschreibung der Komponenten
```
ruhigbot/
├── ruhigbot/
│   ├── static/
│   │   ├── img/
│   │   │   ├── favicon.png
│   │   └── style.css
│   ├── templates/
│   │   ├── chat.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── settings.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ruhigbot_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── db.sqlite3
├── manage.py
├── urls.py
├── venv/
└── .gitignore
```
- `ruhigbot/` 📂: Enthält die Hauptanwendung des Chatbots.
  - `static/` 🎨: Enthält statische Dateien wie CSS und Bilder.
  - `templates/` 🖼️: Enthält HTML-Vorlagen für die Benutzeroberfläche.
  - `__init__.py` 🛠️: Initialisiert das Python-Paket.
  - `admin.py` 🧑‍💼: Konfiguration für das Django-Admin-Interface.
  - `apps.py` 🧩: Konfiguration der Anwendung.
  - `models.py` 🗃️: Datenbankmodelle (derzeit leer).
  - `settings.py` ⚙️: Einstellungen für die Django-Anwendung.
  - `tests.py` 🧪: Tests für die Anwendung (derzeit leer).
  - `urls.py` 🛣️: URL-Routing für die Anwendung.
  - `views.py` 👀: Logik für die Verarbeitung von Anfragen und Antworten.
- `ruhigbot_project/` 🗂️: Enthält die Django-Projektkonfiguration.
- `.env` 🌿: Umgebungsvariablen für die Anwendung.
- `db.sqlite3` 🛢️: SQLite-Datenbankdatei.
- `manage.py` ⚙️: Skript zum Verwalten der Django-Anwendung.
- `venv/` 📦: Virtuelle Umgebung für die Anwendung.
- `.gitignore` 🚫: Ignoriert bestimmte Dateien und Verzeichnisse in Git.
- `requirements.txt` 📋: Liste der Abhängigkeiten für die Anwendung.
- `README.md` 📖: Diese Datei.

## 🛠️ Installation (Linux System)
1. 📥 Installieren Sie Python 3.10 oder höher.
2. 📦 Installieren Sie Python Pip (Paketmanager für Python) und die python3-venv-Bibliothek.
3. 🔧 Installieren Sie Git.
4. 🌐 Besuchen Sie [OpenRouter](https://openrouter.ai/) und erstellen Sie ein Konto.
5. 🔑 Erstellen Sie einen API-Schlüssel bei OpenRouter.
6. 📂 Klonen Sie dieses Repository:
```bash
git clone https://github.com/e1th4nUwU/RuhigBot.git
```
7. 📁 Wechseln Sie in das Verzeichnis des Projekts:
```bash
cd RuhigBot
```
8. 🐍 Erstellen Sie eine virtuelle Umgebung:
```bash
python3 -m venv venv
```
9. ▶️ Aktivieren Sie die virtuelle Umgebung:
```bash
source venv/bin/activate
```
10. 📋 Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```
11. 📝 Erstellen Sie eine `.env`-Datei im `src`-Verzeichnis und fügen Sie Ihren API-Schlüssel hinzu:
```bash
API_KEY = "ihr_api_key"
```
12. 📂 Wechseln Sie in den `src`-Ordner:
```bash
cd src
```
13. 🛠️ Führen Sie die Migrationen durch:
```bash
python manage.py migrate
```
14. 🚀 Starten Sie den Server:
```bash
python manage.py runserver 0.0.0.0:8000
```
15. 🌐 Öffnen Sie Ihren Webbrowser und besuchen Sie `http://localhost:8000` oder `http://<Ihre_IP>:8000`, um RuhigBot zu benutzen!