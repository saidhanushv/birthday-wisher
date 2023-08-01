import pandas as pd
import smtplib
import datetime as dt
import random

# 1. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

data = pd.read_csv("birthdays.csv")
birthday_df = pd.DataFrame(data)

for index, row in birthday_df.iterrows():
    if month == row["month"] and day == row["day"]:
        print(f"MATCH FOUND! {row['name']}")

        # 2. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        random_letter = f"letter_{random.randint(1, 3)}.txt"
        print(random_letter)
        with open(f"letter_templates/{random_letter}", "r") as birthday_letter:
            content = birthday_letter.read()
            content = content.replace("[NAME]", row['name'])

        # 3. Send the letter generated in step 3 to that person's email address.
        my_email = "codersinfinite@gmail.com"
        password = "ugcoflqnywkxjysf"

        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=60) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday To You!\n\n{content}"
            )
