from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendmail', methods=['POST'])
def sendmail():
    name = request.form['name']
    email = request.form['email']
    description = request.form['description']

    YOUR_EMAIL = 'tucorreo@ejemplo.com'
    YOUR_PASSWORD = 'tucontraseña'

    message = f'''\
Subject: Nuevo mensaje de contacto: {name}
From: {email}
To: {YOUR_EMAIL}

Nombre: {name}
Correo electrónico: {email}

Descripción del proyecto:
{description}
'''

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        server.sendmail(email, YOUR_EMAIL, message)
        server.quit()
        return redirect(url_for('index', success=1))
    except Exception as e:
        print(e)
        return redirect(url_for('index', error=1))

if __name__ == '__main__':
    app.run(debug=True)
