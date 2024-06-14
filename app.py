from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import venv.config as config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    db.init_app(app)
    migrate = Migrate(app, db)  # Инициализация Flask-Migrate

    with app.app_context():
        from logs.views import register_views
        register_views(app)

    return app

db = SQLAlchemy()
