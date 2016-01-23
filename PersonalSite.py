from flask import Flask, render_template
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'YourSuperSecreteKey'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'joeracostawebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'joeswebsite'

mail = Mail(app)

@app.route('/')
def hello_world():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods=('GET','POST'))
def contact():
    form = ContactForm()

    if form.validate() == False:
        return 'Please fill in all fields <p><a href="/contact">Try Again!!!</a></p>'
    else:
        msg = Message("Message from your visitor" + form.name.data,
                      sender='YourUser@NameHere',
                      recipients=['joe@joeracosta.com'])
        msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return "Successfully  sent message!"


if __name__ == '__main__':
    app.run(host='localhost')