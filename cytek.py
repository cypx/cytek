#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, abort, render_template
from flask.ext.mail import Mail



app = Flask(__name__)
app.debug = False
mail = Mail(app)

@app.errorhandler(404)
def page_not_found(e):
    error="Erreur 404, adresse incorrect ou page indisponible"
    return render_template('error.html', error=error), 404

@app.errorhandler(403)
def page_not_allowed(e):
    error="Erreur 403, nous n'êtes pas autorisé à accéder à cette page"
    return render_template('error.html', error=error), 403

@app.errorhandler(401)
def page_not_authorized(e):
    error="Erreur 401, nous n'êtes pas autorisé à accéder à cette page"
    return render_template('error.html', error=error), 401

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['POST'])
def contact():
    sender=request.form['email']
    recipient=["info@cytek.fr"]
    subject= "[cytek] Message de: "+request.form['name']
    message= request.form['message']+"\n\nTel: "+request.form['phone']+"\n\n Site: "+request.form['url']
    msg = Message(sender=sender,recipients=body,recipient=message,subject=subject)
    conn.send(msg)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
