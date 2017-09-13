import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':

    me = "xxxxxxxxxxx@gmail.com"
    passwd = "xxxxxxxxxx"

    you = "xxxxxxxxxxxx@gmail.com"

    title = "test"

    body = "hello!\nthis mail is test"

    msg = MIMEText(body)
    msg['Subject'] = title
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me,passwd)
    s.send_message(msg)
    s.close()
