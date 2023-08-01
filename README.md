## Automated Birthday Greeting Sender

This Python program checks if today's date matches any birthdays listed in the `birthdays.csv` file. If a match is found, it generates a random birthday letter from a set of letter templates and sends it as an email to the person celebrating their birthday.

### Features:
- Reads birthday data from `birthdays.csv` file.
- Matches today's date with birthdays in the CSV.
- Selects a random birthday letter template and customizes it with the celebrant's name.
- Sends the personalized birthday letter as an email to the person's email address.

### Requirements:
- Python 3.x
- pandas library
- smtplib library
- datetime library

### Usage:
1. Ensure that the `birthdays.csv` file contains the necessary birthday data with columns 'name', 'month', 'day', and 'email'.
2. Prepare letter templates in the `letter_templates` directory with placeholders `[NAME]` for the name.
3. Configure the `my_email` and `password` variables with the sender's Gmail credentials.
4. Run the script, and it will automatically send birthday greetings when a match is found.
