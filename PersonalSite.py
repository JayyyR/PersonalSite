from flask import Flask, render_template

import smtplib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact', methods=['GET','POST'])
def email():
    sender = 'flatpita92@gmail.com'
    receivers = ['joe@joeracosta.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('localhost', 5000)
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"
    return

if __name__ == '__main__':
    app.run(host='localhost')
