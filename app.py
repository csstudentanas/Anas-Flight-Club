from flask import Flask, render_template, request, redirect
import requests
import smtplib
from email.message import EmailMessage
import os


MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = os.environ.get('PASSWORD')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        send_mail(email)
        return render_template('email_sent.html')
    else:
        return render_template("index.html")


@app.route('/features')
def features():
    return render_template('features.html')


with open('templates/email_content.html', encoding='UTF-8') as file:
    html = file.read()


def send_mail(email):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    msg = EmailMessage()
    msg['Subject'] = "Anas's Flight Club"
    msg['From'] = MY_EMAIL
    msg['To'] = email
    msg.add_alternative(html, subtype='html')
    connection.send_message(msg)
    connection.quit()


if __name__ == '__main__':
    app.run(debug=True)
