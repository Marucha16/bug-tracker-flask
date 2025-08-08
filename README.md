# 🐞bug-tracker-flask
- A web application for managing bug reports and editing their detailed data. Created in Python using the Flask framework. It allows easy tracking and updating of bug statuses within a project.
## Project Structure
- bug-tracker-flask/
- │
- ├── app/
- │ ├── init.py # Flask app initialization
- │ ├── extensions.py # Extensions initialization (SQLAlchemy)
- │ ├── forms.py # WTForms forms
- │ ├── models.py # SQLAlchemy models
- │ ├── routes.py # Flask routes
- │ ├── static/ # Static files (CSS)
- │ └── templates/ # HTML templates
- │
- ├── run.py # Application entry point
- └── requirements.txt # Python dependencies list
## ⚙️ Installation and running
 ```bash   
# 1️⃣ Clone the repository
git clone https://github.com/twoj-login/bug-tracker-flask.git

# 2️⃣ Enter the project directory
cd bug-tracker-flask

# 3️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 4️⃣ Install required packages
pip install -r requirements.txt

# 5️⃣ Run the database migrations to create the database schema(add account)
flask db upgrade

# 6️⃣  Run the application
python run.py
```
## 🛠 Technologies
The project uses the following technologies and libraries:

- **Python** — main programming language
- **Flask** — lightweight web framework
- **Flask-Login** — user session and login management
- **Flask-Migrate** — database migrations (based on Alembic) 
- **Flask-SQLAlchemy** — ORM for database interactions
- **Flask-WTF** — form handling and validation (WTForms)
- **Alembic** — database migration tool
- **SQLAlchemy** — Python ORM library
- **WTForms** — library for creating and validating forms
- **Jinja2** — HTML template engine
- **Werkzeug** — WSGI library used by Flask
## 📸 Screenshots

### Main page - not log in
![Ekran główny](screenshots/ekran_brzlogowania.png)

### Registration
![Ekran rejestracji](screenshots/rejestracja.png)

### Login
![Ekran logowania](screenshots/logowanie.png)

### Main page - logged in
![Ekran główny](screenshots/ekran_glowny.png)

### Report submission form
![Ekran zgłaszania](screenshots/zglaszanie.png)

### Reports page
![Ekran zgłaszania](screenshots/reports.png)
