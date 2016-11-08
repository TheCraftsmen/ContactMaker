from flask.ext.via.routers import default
from app.views import *

urls = [
    # url, clase y nombre de la vista
    default.Pluggable('/', Index, 'index'),
    default.Pluggable('/about', About, 'about'),
    default.Pluggable('/mailsender', Mailsender, 'mailsender')
]
#

user_url = [default.Pluggable('/register',UserRegister,'register'),
    default.Pluggable('/login',UserLogin,'login'),
    default.Pluggable('/logout', UserLogout,'logout')]
urls = urls + user_url