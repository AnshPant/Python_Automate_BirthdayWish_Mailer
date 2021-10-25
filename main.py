
from datetime import datetime
import pandas
import random
import smtplib  #simple mail transfer protocol

MY_EMAIL = "your mail @gmail.com"  #create a new gmail and password to test it .
MY_PASSWORD = "password enter"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
#creating a birthday dictionary which will help to
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  #calling a rand letter template from letter_templates folder
    with open(file_path) as letter_file:   #open as well automatically close the path
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:    # smtp.mail.yahoo.com for yahoo mail accounts and similary for hot mails . Please search documentaiton for this
        connection.starttls()  #secures connection by encrypting messages
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"  #before the two new line is subject and after it is the content of mail
                    #its necessary to add subject so that our mail does not go in spam
        )
