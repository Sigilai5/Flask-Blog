from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



db = SQLAlchemy()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    # Initializing Application
    app = Flask(__name__)

    #Initializing Flask Extensions
    login_manager.init_app(app)


    bootstrap.init_app(app)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].__init__(app)

    # Registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # CONFIGURE UPLOADSET
    configure_uploads(app,photos)



    db.init_app(app)





    return app
