import smtplib
import ssl
from random import randint
import pandas as pd
import datetime as dt


def create_letters(names):
    letters = []
    for name in names:
        letter_directory = fr".\letter_templates\letter_{randint(1, 3)}.txt"
        with open(letter_directory) as file:
            letters.append(file.read().replace("[NAME]", name))
    print(letters)
    return letters


def send_mails(names, mails):
    letters = create_letters(names)
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls(context=context)
        connection.login(user=YOUR_EMAIL, password=GMAIL_APP_PASSWORD")
        for i in range(len(names)):
            msg = "Subject: Happy Birthday\n\n"+letters[i]
            print(msg)
            connection.sendmail(from_addr=YOUR_EMAIL, to_addrs=mails[i],
                                msg=msg)


file_directory = ".\birthdays.csv"
birthday = pd.read_csv(file_directory)
today = dt.datetime.now()
persons = birthday[(birthday["month"] == today.month) &
                   (birthday["day"] == today.day)]
send_mails(list(persons["name"]), list(persons["email"]))
