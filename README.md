# Automated Birthday Wisher

## Overview
Birthday Wisher is a Python script that sends automated birthday wishes to your friends, family, or colleagues via email. The script reads the names and birthdays from a CSV file, creates personalized birthday letters from a set of letter templates, and sends them to the corresponding email addresses using a Gmail account.

## Features
Sends personalized birthday wishes via email automatically.
Uses pre-written letter templates that can be customized.
Reads names and birthdays from a CSV file.
Uses Gmail SMTP to send emails.

## Installation and Setup
Clone this repository to your local machine.
Create a Mail account to send emails from.

Make sure you've got the correct smtp address for your email provider:
- Gmail: smtp.gmail.com 
- Hotmail: smtp.live.com 
- Outlook: outlook.office365.com
- Yahoo: smtp.mail.yahoo.com

Customize the letter templates in the letter_templates folder as desired.
Add the names and birthdays of your contacts to the birthdays.csv file.
Update the email and password fields in the send_mails function in the birthday_wisher.py file with your Gmail account details.
Run the birthday_wisher.py file.

## Future Improvements
The script can be modified to include additional letter templates or customized messages, making it a versatile tool for any occasion.
Add support for different email providers.
Improve error handling and logging.
