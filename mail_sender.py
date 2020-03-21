
import smtplib
from email.message import EmailMessage

def send_mail(mail: str, name: str):
    user = ''
    password = ''
    text="Hello " + name + ", \n your account has been created succesfully"
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = "Confirmation"
    msg['From'] = ""
    msg['To'] = mail
    s = smtplib.SMTP("", 465)
    s.ehlo()
    s.starttls()
    s.login(user, password)

    s.send_message(msg)
    s.close()