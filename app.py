# importing libraries
import os
from flask import *
from flask_mail import *

app = Flask(__name__)


# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'harishsidagam@gmail.com'
app.config['MAIL_PASSWORD'] = '********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
	msg = Message('Hello',sender ='harishsidagam@gmail.com',
				  recipients = ['harishsidagam@gmail.com','rsrraviteja3522.sr@gmail.com'])
	msg.body = 'Hello  User This message is sending from sent from Flask-Mail. I created flask-application please go through once'
	

	mail.send(msg)
	return 'Sent'

if __name__ == '__main__':
	app.run(debug = True)
