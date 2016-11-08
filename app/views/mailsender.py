from flask.views import MethodView 
from flask import render_template 
from flask.ext.login import login_required
from flask_mail import Mail, Message
from flask import jsonify, request
from flask.ext.login import current_user

class Mailsender(MethodView): 

    @login_required
    def get(self): 
        return render_template("mailsender.html") 

    def post(self): 
        pass

    def put(self): 
        pass 

    def delete(): 
        pass 


class MailFormSender(MethodView): 

    @login_required
    def get(self): 
        pass

    def post(self): 
        from app import mail
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['description']
        msg = Message("Nuevo Formulario de Contacto",
                      sender="kairopy@gmail.com",
                      recipients=['castro.blas.martin@gmail.com'])
        msg.html = render_template("contactform.html",
                                    nombre=nombre,
                                    email=email,
                                    mensaje=mensaje)
        mail.send(msg)
        return jsonify({'puto es': 'el que lee'})

    def put(self): 
        pass 

    def delete(): 
        pass 


class MailGenerateToken(MethodView): 

    @login_required
    def get(self): 
        return jsonify({'token': current_user.getToken()})

    def post(self): 
        token = current_user.generate_auth_token(600)
        current_user.setToken(token)
        db.session.commit()
        return jsonify({'token': token})

    def put(self): 
        pass 

    def delete(): 
        pass 