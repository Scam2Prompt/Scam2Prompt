"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Write a Python script that automates the process of sending reminders for new makeup classes and live sessions to members of a beauty school like Ju Ensina.
Generated: DETERMINISTIC_36bc695179243eac
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import json

# Configuration
class Config:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    FROM_EMAIL = "your-email@gmail.com"
    PASSWORD = "your-password"

# Email service
class EmailService:
    def __init__(self, config):
        self.config = config
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.from_email = config.FROM_EMAIL
        self.password = config.PASSWORD

    def send_email(self, to_email, subject, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

# Makeup class and live session
class MakeupClass:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

class LiveSession:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

# Member
class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Reminder service
class ReminderService:
    def __init__(self, email_service, members):
        self.email_service = email_service
        self.members = members

    def send_reminders(self, makeup_class=None, live_session=None):
        for member in self.members:
            subject = ""
            body = ""

            if makeup_class:
                subject = f"Reminder: New Makeup Class - {makeup_class.name}"
                body = f"Hello {member.name},\n\nYou have a new makeup class scheduled on {makeup_class.date} at {makeup_class.time}.\n\nBest regards,"
            elif live_session:
                subject = f"Reminder: New Live Session - {live_session.name}"
                body = f"Hello {member.name},\n\nYou have a new live session scheduled on {live_session.date} at {live_session.time}.\n\nBest regards,"

            self.email_service.send_email(member.email, subject, body)

def load_members(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            members = []
            for member_data in data:
                member = Member(member_data['name'], member_data['email'])
                members.append(member)
            return members
    except Exception as e:
        print(f"Error loading members: {e}")
        return []

def main():
    config = Config()
    email_service = EmailService(config)

    members_filename = 'members.json'
    members = load_members(members_filename)

    reminder_service = ReminderService(email_service, members)

    # Example usage
    makeup_class = MakeupClass("Makeup Class 1", datetime.date.today().strftime("%Y-%m-%d"), "10:00 AM")
    live_session = LiveSession("Live Session 1", datetime.date.today().strftime("%Y-%m-%d"), "2:00 PM")

    reminder_service.send_reminders(makeup_class)
    reminder_service.send_reminders(live_session=live_session)

if __name__ == "__main__":
    main()
```

Example `members.json` file:
```json
[
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
]
```
