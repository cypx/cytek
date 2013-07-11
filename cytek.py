#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, abort, render_template
from flask.ext.mail import Mail, Message
import errno
from socket import error as socket_error
import sys

app = Flask(__name__)
app.debug = True
mail = Mail(app)

@app.errorhandler(404)
def page_not_found(e):
    error="Erreur 404, adresse incorrect ou page indisponible"
    return render_template('error.html', error=error.decode("utf-8")), 404

@app.errorhandler(403)
def page_not_allowed(e):
    error="Erreur 403, nous n'êtes pas autorisé à accéder à cette page"
    return render_template('error.html', error=error.decode("utf-8")), 403

@app.errorhandler(401)
def page_not_authorized(e):
    error="Erreur 401, nous n'êtes pas autorisé à accéder à cette page"
    return render_template('error.html', error=error.decode("utf-8")), 401

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        sender=request.form['email']
        recipient=["info@cytek.fr"]
        subject= "[cytek] Message de: "+request.form['name']
        message= request.form['message']+"\n\nTel: "+request.form['phone']+"\n\n Site: "+request.form['url']
        msg = Message(sender=sender,recipients=recipient,body=message,subject=subject)
        try:
                mail.send(msg)
                return render_template('contact.html')
        except socket_error as serr:
                error="Erreur, votre mail n'a pas pu être envoyé, serveur mail indisponible"
                log="from: "+sender+"\n\nSubject: "+subject+"\n\n"+message+"\n\n###############################################\n\n"
                with open('./message.log', 'wb') as dest_file:
                       dest_file.write(log)
                return render_template('error.html', error=error.decode("utf-8"))

if __name__ == '__main__':
    app.run()
