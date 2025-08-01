# 🐞bug-tracker-flask
## Struktura projektu
- bug-tracker-flask/
- │
- ├── app/
- │ ├── init.py # Inicjalizacja aplikacji Flask
- │ ├── extensions.py # Inicjalizacja rozszerzeń (SQLAlchemy)
- │ ├── forms.py # Formularze WTForms
- │ ├── models.py # Modele SQLAlchemy
- │ ├── routes.py # Trasy (flask)
- │ ├── static/ # Pliki statyczne (CSS)
- │ └── templates/ # Szablony HTML 
- │
- ├── run.py # Plik startowy aplikacji
- └── requirements.txt # Lista zależności Pythona
## ⚙️ Instalacja i uruchomienie
 ```bash   
# 1️⃣ Sklonuj repozytorium
git clone https://github.com/twoj-login/bug-tracker-flask.git

# 2️⃣ Wejdź do katalogu projektu
cd bug-tracker-flask

# 3️⃣ Utwórz i aktywuj wirtualne środowisko
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 4️⃣ Zainstaluj wymagane paczki
pip install -r requirements.txt

# 5️⃣ Uruchom aplikację
python run.py
```
## 🛠 Technologie
Projekt korzysta z następujących technologii i bibliotek:

- **Python** — główny język programowania  
- **Flask** — lekki framework webowy  
- **Flask-Login** — zarządzanie sesjami i logowaniem użytkowników  
- **Flask-Migrate** — migracje bazy danych (oparte na Alembic)  
- **Flask-SQLAlchemy** — ORM do pracy z bazą danych  
- **Flask-WTF** — obsługa formularzy i walidacja (WTForms)  
- **Alembic** — narzędzie do migracji baz danych  
- **SQLAlchemy** — biblioteka ORM dla Pythona  
- **WTForms** — biblioteka do tworzenia i walidacji formularzy  
- **Jinja2** — silnik szablonów HTML  
- **Werkzeug** — biblioteka WSGI wykorzystywana przez Flask  
- **Mako** — alternatywny silnik szablonów (może być wykorzystywany)  
- **email_validator** — walidacja adresów email  
- **dnspython**, **idna** — obsługa DNS i IDN, wspierające inne pakiety  
- **click** — narzędzie do tworzenia interfejsów CLI (wykorzystywane przez Flask)  
- **blinker** — system sygnałów i zdarzeń  
- **itsdangerous** — bezpieczne podpisywanie danych (np. do sesji)  
- **greenlet** — wykorzystywany przez SQLAlchemy do współbieżności  
- **typing_extensions** — rozszerzenia typów dla Pythona
