from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'twoj-sekretny-klucz'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugtracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes  # tutaj później dodasz widoki
        db.create_all()

    return app
