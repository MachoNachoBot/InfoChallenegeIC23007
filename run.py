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
@app.route("/main", methods=['GET', 'POST'])
@app.route("/main.html", methods=['GET', 'POST'])
def home():
    #app.logger.info('Info level log')
    return render_template('main.html')

@app.route("/opt-out-form", methods=['GET', 'POST'])
@app.route("/opt-out-form.html", methods=['GET', 'POST'])
def optOut():
    form = OptOutForm()
    return render_template('opt-out-form.html', title='Opt-Out Email Form', form=form)
    

@app.route("/sendemailnow", methods=['GET', 'POST'])
def sendemailnow():
    strFirstName = request.form['first_name']
    strLastName = request.form['last_name']
    
    sendEmail("SuperiorSpiron@gmail.com", "Request to remove Name - " + strFirstName + " " + strLastName, strFirstName)
    return redirect(url_for("home"))

@app.route("/harm.html", methods=['GET', 'POST'])
@app.route("/harm", methods=['GET', 'POST'])
def harmpage():
    return render_template('harm.html')

@app.route("/what.html", methods=['GET', 'POST'])
@app.route("/what", methods=['GET', 'POST'])
def harm():
    return render_template('what.html')

@app.route("/sendemailnow", methods=['GET', 'POST'])
def sendemailnowpage():
    strFirstName = request.form['first_name']
    strLastName = request.form['last_name']
    strEmail = request.form['email']
    strPhone = request.form['phone']
    strFromEmail = "Authorized Agent <AuthorizedAgent@danishnadar.com>"

    strDataBroker = "Acxiom"

    strEmailBody = '''\
Dear {aDataBroker} Team,<br><br>

I am writing to request that you remove my personal information from your database and stop selling or sharing it with third-party companies.<br><br>

Please find below the details you may need to process my request. You may reach out to me anytime if you need more information from me to proceed with my request.<br><br>

Name: {aFirstName} {aLastName}<br>
Email Address: {aEmail}<br>
Phone Number: {aPhone}<br><br>

I would like to emphasize that I did not give you permission to collect or share my information, and I do not wish to receive any further communications from your company.<br><br>

As per my rights under the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA), I request that you delete my information from your database within 30 days of receiving this email.<br><br>

Thank you for your prompt attention to this matter. I look forward to receiving confirmation from you that my information has been removed.<br><br>

Sincerely,<br><br>

{aFirstName} {aLastName}<br><br>

    '''.format(aDataBroker=strDataBroker, aFirstName=strFirstName, aLastName=strLastName, aEmail=strEmail, aPhone=strPhone)

    
    sendEmail("superiorspiron@gmail.com", "Request to Remove - " + strFirstName + " " + strLastName + " from " + strDataBroker, strEmailBody,strFromEmail)
    return redirect(url_for("home"))
    