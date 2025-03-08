# Automatic_Emails_Regex


Overview

This project collects user details such as Name, Date of Birth, Mobile Number, Instagram ID, and Email, validates them using regular expressions, and sends an email with the collected details using Gmail SMTP.

Features

User Input Validation: Ensures correct formatting for name, date of birth, phone number, and email.

Email Notification: Sends a summary of collected details to the user via email.

Regex-Based Validation: Uses Python's re module to enforce correct input formats.

Technologies Used

Python

smtplib (for sending emails)

email.mime (for email formatting)

re (for input validation using regular expressions)

Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/user-details-email.git

Navigate to the project directory:

cd user-details-email

Install dependencies (if required):

pip install smtplib email re

(Note: smtplib and re are built-in Python modules, so installation is usually not needed.)

Update the sender email credentials in the send_email() function:

sender_email = "your-email@gmail.com"
sender_password = "your-app-password"

Enable Less Secure Apps or use an App Password for Gmail authentication.

Usage

Run the script using:

python user_details_email.py

Follow the prompts to enter details, and an email will be sent upon successful validation.

Example Workflow

User enters their Name, DOB, Mobile Number, Instagram ID, and Email.

Script validates each field using regex.

Once all details are correctly entered, an email is sent with the collected information.

Contributing

Feel free to submit issues and pull requests to improve the system!
