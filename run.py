from flask import Flask
from flask import render_template, url_for, flash, redirect, request
#from Flask.Flask_WTF import FlaskForm
from flask_wtf import FlaskForm
from forms import OptOutForm

from email.message import EmailMessage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from email import message


#import logging
#from app import routes
#import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cda2564d2b56a1f70d6714c017ce32d5'


#logging.basicConfig(filename='flasklog.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 

if __name__ == '__name__': 
    app.run(debug=True)   #), host='127.0.0.1', port=9001, threaded=True)
    app.app_context().push()


def sendEmail(receiver, subject_line, email_content):
    message = Mail(
    from_email='collegeapp@thangakumar.com',
    to_emails=receiver,
    subject=subject_line,
    html_content=email_content)
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

    return


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/home.html", methods=['GET', 'POST'])
def home():
    #app.logger.info('Info level log')
    return render_template('main.html')


@app.route("/opt-out-form", methods=['GET', 'POST'])
@app.route("/opt-out-form.html", methods=['GET', 'POST'])
def optOut():
    form = OptOutForm()
    #flash(form.Firstname.data, 'danger')
    #printf(form.first_name.data)
    #    UserInfo(first_name=form.first_name.data, last_name = form.last_name.data, email=form.email.data)
    #return render_template('opt-out-form.html', title='Opt-Out Email Form', form=form)
    #sendEmail("reachthangs@gmail.com", "Request to remove Name " + form.Firstname.data , form.email.data)
    return render_template('opt-out-form.html', title='Opt-Out Email Form', form=form)
    
