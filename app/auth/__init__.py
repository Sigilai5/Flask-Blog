from flask import Blueprint
from flask_login import LoginManager
from . import views,forms

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


auth = Blueprint('auth',__name__)

from . import views