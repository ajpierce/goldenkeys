import os
import smtplib
import yaml
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

class Mailer(object):
    def __init__(self):
        # Get the sendmail credentials
        try:
            #stream = file('config/sendmail.yaml', 'r')
            stream = file('config/real_sendmail.yaml', 'r')
            self.credentials = yaml.load(stream)
        except Exception as ex:
            raise Exception("Failed to load gmail credentails: %s" % ex)

        # Get the mailing list
        try:
            stream = file('config/listserv.yaml', 'r')
            #stream = file('config/real_listserv.yaml', 'r')
            self.listserv = yaml.load(stream)
        except Exception as ex:
            raise Exception("Failed to load mailing list: %s" % ex)

    def mail(self, subject, text):
        email = MIMEMultipart()
        username = self.credentials['user_name']
        password = self.credentials['password']

        email['From'] = username
        email['To'] = str(self.listserv)
        email['Subject'] = subject
        email.attach(MIMEText(text))

        mailServer = smtplib.SMTP(
            self.credentials['address'],
            self.credentials['port']
        )

        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, self.listserv, email.as_string())
        mailServer.close()
