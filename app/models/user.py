from manage import app, db 
from sqlalchemy import ForeignKey
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.orm import relationship 
import datetime

class User(db.Model): 

    __tablename__ = "user" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(32))
    password = db.Column('password' , db.String(64))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    token = db.Column(db.String(128), default='')
 
    def __init__(self , username ,password , email):
        self.username = username
        self.hash_password(password)
        self.email = email
        self.registered_on = datetime.datetime.utcnow()

    def get_name(self):
        return self.username

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def setToken(self, token):
        self.token = token

    def getToken(self):
        try:
            print self.token
            return unicode(self.token)  # python 2
        except NameError:
            print self.token
            return str(self.token)  # python 3

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        return '<name {}'.format(self.username)