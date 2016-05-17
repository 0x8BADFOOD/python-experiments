#!/usr/bin/python

import smtplib
import base64
import datetime
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recepients_list =[
    "your_mail1@gmail.com"
    "your_mail2@gmail.com",
]

CURR_TIME = time.ctime()

def get_next_sunday():
    today = datetime.date.today()
    sunday = today + datetime.timedelta( (6-today.weekday()) % 7 )
    return sunday

def get_day_and_time():
    day = get_next_sunday()
    return str(day .strftime('%b %d at ' + CURR_TIME))

COMMASPACE = ', '

recepients = recepients_list


EMAIL_TO          = COMMASPACE.join(recepients)
EMAIL_SUBJECT     = 'Current date and time: ' + get_day_and_time()
EMAIL_MIME        = "alternative"
EMAIL_FROM        = "USER.NAME@gmail.com"
EMAIL_LOGIN       = "USER.NAME"
#encoded in base 64:
#base64.b64encode("Your password")
EMAIL_PASSWORD    = "WW91ciBwYXNzd29yZA=="
EMAIL_SMTP_SSL_SERVER = "smtp.gmail.com"
EMAIL_SMTP_PORT   = 465
EMAIL_TEXT        = """
Hi All!

This is test mail from my script """ + get_day_and_time() + """


Thanks.
"""
EMAIL_HTML= """\
<html>
  <head></head>
  <body>
    <p>Hi All!</p>
        This is test mail from my script  <b>""" + get_day_and_time() + """</b><br>
        Source could be found here:<br>
        <a href="https://github.com/0x8BADFOOD/python-experiments">
            0x8BADFOOD/python-experiments </a><br>
        Thanks.
    </p>
  </body>
</html>
"""
def send_email():
    # Message container
    msg = MIMEMultipart(EMAIL_MIME)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From']    = EMAIL_FROM
    msg['To']      = EMAIL_TO

    # MIME types for text/plain and text/html.
    plain_section = MIMEText(EMAIL_TEXT, 'plain')
    html_section  = MIMEText(EMAIL_HTML, 'html')

    # Attach
    msg.attach(plain_section)
    msg.attach(html_section)

    # Send the message via SMTP server.
    mail = smtplib.SMTP_SSL(EMAIL_SMTP_SSL_SERVER , EMAIL_SMTP_PORT)
    try:
        mail.ehlo()
        mail.login(EMAIL_LOGIN, base64.b64decode(EMAIL_PASSWORD))
        mail.sendmail(EMAIL_FROM, recepients, msg.as_string())
        print 'OK: mail has been sent'
    except Exception as e:
        print "FAIL: " + str(e)
    #mail.close()
    mail.quit()

if __name__ == "__main__":
    send_email()
