from flask import Flask, render_template, url_for
from flask_mail import Mail, Message
from werkzeug.utils import redirect

from forms import ContactForm

app = Flask(__name__)
app.secret_key = "Y\xd5^\xa1{\xf3\n\xf7s\xedz\x945zM\xa0;&'\xd9.\xade"

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'joeracostawebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'joeswebsite'

mail = Mail(app)

@app.route('/')
def home():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods=('GET','POST'))
def contact():
    form = ContactForm()

    if form.validate() == False:
        return 'Error. All fields not filled in'
    else:
        msg = Message("Message from your visitor" + form.name.data,
                      sender='joeracostawebsite@gmail.com',
                      recipients=['joe@joeracosta.com'])
        msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()