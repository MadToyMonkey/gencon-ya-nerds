"""
function for sending emails with a text file attachement
"""

# https://pythonroadmap.com/blog/send-email-attachments-with-python
# https://medium.com/@abdullahzulfiqar653/sending-emails-with-attachments-using-python-32b908909d73
# https://realpython.com/python-send-email/
import smtplib
from email.message import EmailMessage

# email account info
email_address = "shitlords21@gmail.com"
email_password = "12ampcurrent"
smtp_server = "smtp.gmail.com"
smtp_port = 587


def task_email():
    """creating the emails to send"""
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = "recipient_email@example.com"
    msg.set_content("Hello Gilfoyle, this is a test email with an attachment. -Dinesh")
    with open("attachment.txt", "rb") as f:
        file_data = f.read()
    msg.add_attachment(
        file_data, maintype="text", subtype="plain", filename="attachment.txt"
    )
