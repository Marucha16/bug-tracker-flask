#🐞bug-tracker-flask
##Struktura projektu
bug-tracker-flask/
│
├── app/
│ ├── init.py # Inicjalizacja aplikacji Flask
│ ├── extensions.py # Inicjalizacja rozszerzeń (SQLAlchemy)
│ ├── forms.py # Formularze WTForms
│ ├── models.py # Modele SQLAlchemy
│ ├── routes.py # Trasy (flask)
│ ├── static/ # Pliki statyczne (CSS)
│ └── templates/ # Szablony HTML 
│
├── run.py # Plik startowy aplikacji
└── requirements.txt # Lista zależności Pythona
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
