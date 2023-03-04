from flask import render_template, url_for, flash, redirect, request
#from opt-out-form import UserInfo
from run import app
#import app

#from email.message import EmailMessage
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import Mail
#from email import message

#import datetime

#@app.route("/main.html")
#@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    #app.logger.info('Info level log')
    return render_template('main.html')


'''
@app.route("/opt-out-form", methods=['GET', 'POST'])
@app.route("/opt-out-form.html", methods=['GET', 'POST'])
def optOut():
    #form = UserInfo()
    #if form.validate_on_submit():
    #    UserInfo(first_name=form.first_name.data, last_name = form.last_name.data, email=form.email.data)
    #return render_template('opt-out-form.html', title='Opt-Out Email Form', form=form)
    pass
'''

'''
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

'''