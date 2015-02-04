from flask import Flask, render_template, request, url_for
from flask.ext.mail import Message, Mail
from os import environ

####### CONFIG
TO_EMAIL = environ.get('TO_EMAIL')
MAIL_SERVER = environ.get('MAIL_SERVER')
MAIL_PORT = environ.get('MAIL_PORT')
MAIL_USERNAME = environ.get('MAIL_USERNAME')
MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = True
####### END CONFIG

####### INIT
app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)
####### END INIT

####### VIEWS
@app.route('/')
@app.route('/index')
def index():
    """Home page"""
    return render_template('index.html',
                           to_email=TO_EMAIL,
                           from_email=MAIL_USERNAME,
                           target_url=url_for('wt_feed', _external=True))

@app.route("/wt_feed", methods=['POST'])
def wt_feed():
    """Webhook receiver for WattTime data"""
    data = request.get_json()
    msg = Message('WattTime data update',
                  sender=MAIL_USERNAME,
                  recipients=[TO_EMAIL])
    msg.body = render_template('email.txt', **data['data'])
    mail.send(msg)
    return 'ok'
####### END VIEWS

####### MAIN
if __name__ == '__main__':
    app.run(debug=True)
####### END MAIN
