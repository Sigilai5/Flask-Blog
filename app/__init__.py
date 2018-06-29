from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from config import config_options
from  flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()

def create_app(config_name):
    # Initializing Application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].__init__(app)

    # Registering main blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    db.init_app(app)





    return app
