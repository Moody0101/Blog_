

# Importing EmailMessage, to make the Message that will be sent.
from email.message import EmailMessage
# Importing the os lib to get the password, email from the env var.
from os import environ
# import the smtplib which the built-in lib in python to send the email.
import smtplib


HOST = 'smtp.gmail.com'

PORT = 465

PASSWORD = os.getenviron("MYPASSWORD")
EMAIL = os.getenviron("MYEMAIL")

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL
msg['To'] = 'example@gmail.com'
msg.set_content(content)

with smtplib.SMTP_SSL(HOST , PORT) as S:
	S.login(ADDRESS, PASSWORD)
	S.send_message(msg)
	print(f"The message was sent to {msg['to']}")


