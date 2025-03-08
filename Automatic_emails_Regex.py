import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re


x = True
while x:
  pattern = re.compile(r'^[A-Za-z ]+')
  text = input("Enter Name: ")
  matches = pattern.fullmatch(text)
  if matches:
    name = matches.group()
    x = False
  else:
    print("Enter Name in correct format")
    
x = True
while x:
  pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
  dob1 = input("Enter Date of Birth: ")
  matches = pattern.fullmatch(dob1)
  if matches:
    dob = matches.group()
    x = False
  else:
    print("Enter DOB in correct format")

x = True
while x:
  pattern = re.compile(r'\d{3}\d{3}\d{4}')
  phone1 = input("Enter Mobile Number: ")
  matches = pattern.fullmatch(phone1)
  if matches:
    phone = matches.group()
    x = False
  else:
    print("Enter Mobile in correct format")

insta = input("Enter Insta Id: ")

x = True
while x:
  pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
  email1 = input("Enter Email: ")
  matches = pattern.fullmatch(email1)
  if matches:
    email = matches.group()
    x = False
  else:
    print("Enter Email in correct format")

def send_email(name, dob, phone, insta, email):
    sender_email = "kprathyusha.799@gmail.com"  
    sender_password = "ihqh wsve sgur tlyk"  

    subject = "Your Collected Details"
    body = f"""Hello {name},

Here are the details you provided:

1. Name: {name}
2. Date of Birth: {dob}
3. Mobile: {phone}
4. Instagram ID: {insta}
5. Email: {email}

Do let me know if any details need to be updated.

Best Regards,  
Admin 
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print("\nYour details have been emailed successfully!")
    except Exception as e:
        print(f"\n Error sending email: {e}")

send_email(name, dob, phone, insta, email)
