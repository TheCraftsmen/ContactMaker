from config import *
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.via import Via
from flask_mail import Mail, Message

app = Flask(__name__ )
app.config.update(
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'nombre@email.com',
    MAIL_PASSWORD = 'password'
)

mail = Mail(app)
app.config['VIA_ROUTES_MODULE'] = 'config.routes'
db = SQLAlchemy(app)
from app.models import *


via = Via()
via.init_app(app, routes_name='urls')

#app.config.from_object('config.BaseConfig')
app.config.from_object('config.DevelopmentConfig')
#


from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
