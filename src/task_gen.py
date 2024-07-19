import csv
import random
import os.path
import smtplib
from email.message import EmailMessage

# email account info
email_address = "dungeonmasterBU@hotmail.com"
email_password = "12ampcurrent"
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587


def task_email(r_email, name, tasks):
    """creating the emails to send"""
    msg = EmailMessage()
    msg["Subject"] = "GENCON TASKS"
    msg["From"] = email_address
    msg["To"] = r_email
    msg.set_content(
        f"Hello {name}, here are your tasks for the day.\n {tasks}\n\n Have a nice day!"
    )
    # with open("attachment.txt", "rb") as f:
    #    file_data = f.read()
    # msg.add_attachment(
    #    file_data, maintype="text", subtype="plain", filename="attachment.txt"
    # )
    # Send email message
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)


# import player lists
with open("src/players.csv", mode="r") as file:
    players = list(csv.reader(file))
print(players)

# import task lists
with open("src/tasks.csv", mode="r") as file:
    tasks = list(csv.reader(file))
print(tasks)

# randomize task and assign to player
for i in players:
    random.shuffle(tasks)
    todo = tasks
    task_email(i[1], i[0], todo)
print("Done")
