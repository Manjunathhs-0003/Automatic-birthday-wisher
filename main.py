from datetime import datetime
import pandas
import random
import smtplib, ssl

today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "Your Email (sender mail id)"
MY_PASSWORD = "Password to the above mail id"

data = pandas.read_csv("path to the file containing birthdays")
birthdays_dict = {(data_row.month, data_row.day): [] for (index, data_row) in data.iterrows()}

for index, data_row in data.iterrows():
    birthdays_dict[(data_row.month, data_row.day)].append({"name": data_row["name"], "email": data_row["email"]})

if today_tuple in birthdays_dict:
    birthday_people = birthdays_dict[today_tuple]

    for birthday_person in birthday_people:
        file_path = f"Path to the letter templates_{random.randint(1,3)}.txt"  #here the folder is in the name "letter_templates" the word "templates" is replaced with {random.randint(1,3)} to pick a random letter from the letters in the folder, the range is (1,3) because it has 3 letters, you can add as many letters you want and change the range (should be in .txt format)
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])  # Fix the replace method

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # parameters = mail server hostname and port number
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: HAPPY BIRTHDAY!!!!\n\n{contents}".encode('utf-8'))
