"""Functions used to send task emails to players of the GenCon Versus game."""

import csv
import random
import smtplib
from email.message import EmailMessage

# email account info
EMAIL_ADDRESS = "dungeonmasterBU@hotmail.com"
EMAIL_PASSWORD = "12ampcurrent"
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587
EMAIL = """
    Hello {name},
    You are on team {team}.
    
    Here are your tasks:
        {task_list}

    The rules and pointing are simple. The tasks are in order -> 1, 1, 3, 5 points each.
    A task is completed by posting a photo that encapsulates the completed task in #gencon-versus. Please include the task name as well.
    You may challenge someone who has completed THE EXACT SAME TASK you have listed above. 
    Once the task is completed by anyone, it cannot be completed again during this day.

    Have a nice day!
    ~ Task Master

    """


def task_email(r_email, name, task, team, mext):
    """creating the emails to send"""
    msg = EmailMessage()
    msg["Subject"] = "GENCON TASKS - SHAUN DOES THIS MAKE SENSE"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = r_email
    newline = "\n\n\t"  # escapes not allowed in f-strings
    task_list = newline.join(f"{i[0]}-> {i[1]}" for i in task)
    msg.set_content(mext.format(name=name, team=team, task_list=task_list))

    # Send email message
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


# import player list
with open("src/players.csv", mode="r") as file:
    players = list(csv.reader(file))
# print(players)

# import task lists
with open("src/easy.csv", mode="r") as file:
    easy = list(csv.reader(file, delimiter=";"))
with open("src/medium.csv", mode="r") as file:
    medium = list(csv.reader(file, delimiter=";"))
with open("src/hard.csv", mode="r") as file:
    hard = list(csv.reader(file, delimiter=";"))
# print(easy, medium, hard)

# randomize task and assign to player
random.shuffle(players)
COUNT = 0
for i in players:
    if COUNT < len(players) // 2:
        TEAM = "RED"
    else:
        TEAM = "BLUE"
    random.shuffle(easy)
    random.shuffle(medium)
    random.shuffle(hard)
    todo = easy[:][:2] + medium[:][:1] + hard[:][:1]
    task_email(i[1], i[0], todo, TEAM, EMAIL)
    # print(todo)
    i.append(TEAM)
    COUNT += 1
print("Done")
print(players)
