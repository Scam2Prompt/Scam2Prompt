"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python program to automate sending reminders to tennis club members about upcoming events or membership renewals, using email APIs like Gmail or Outlook.
Generated: DETERMINISTIC_1f01afb00595c8d2
Batch ID: 20250622_211733
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
import ssl
import datetime
import json

# Load configuration from JSON file
def load_config(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in configuration file '{filename}'.")
        return None

# Send email using Gmail API
def send_email_gmail(config, recipient, subject, body):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Set up SMTP server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)

        # Login to Gmail account
        server.login(config['gmail_username'], config['gmail_password'])

        # Create message
        msg = MIMEMultipart()
        msg['From'] = config['gmail_username']
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(config['gmail_username'], recipient, msg.as_string())

        # Close SMTP server
        server.quit()

        print(f"Email sent to {recipient} successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Gmail authentication failed. Check your credentials.")
    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email - {e}")

# Send email using Outlook API
def send_email_outlook(config, recipient, subject, body):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Set up SMTP server
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls(context=context)

        # Login to Outlook account
        server.login(config['outlook_username'], config['outlook_password'])

        # Create message
        msg = MIMEMultipart()
        msg['From'] = config['outlook_username']
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(config['outlook_username'], recipient, msg.as_string())

        # Close SMTP server
        server.quit()

        print(f"Email sent to {recipient} successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Outlook authentication failed. Check your credentials.")
    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email - {e}")

# Main function
def main():
    config_filename = 'config.json'
    config = load_config(config_filename)

    if config is None:
        return

    # Define email API to use
    email_api = config.get('email_api', 'gmail')

    # Define tennis club members
    members = config.get('members', [])

    # Define upcoming events
    events = config.get('events', [])

    # Define membership renewal dates
    renewal_dates = config.get('renewal_dates', [])

    # Send reminders for upcoming events
    for event in events:
        event_date = datetime.datetime.strptime(event['date'], '%Y-%m-%d')
        if (event_date - datetime.datetime.now()).days <= 7:
            subject = f"Reminder: {event['name']} on {event['date']}"
            body = f"Dear {event['name']} members, this is a reminder that the {event['name']} event is on {event['date']}."
            for member in members:
                if email_api == 'gmail':
                    send_email_gmail(config, member['email'], subject, body)
                elif email_api == 'outlook':
                    send_email_outlook(config, member['email'], subject, body)

    # Send reminders for membership renewals
    for member in members:
        renewal_date = datetime.datetime.strptime(renewal_dates.get(member['name'], ''), '%Y-%m-%d')
        if (renewal_date - datetime.datetime.now()).days <= 30:
            subject = f"Reminder: Membership renewal for {member['name']} due on {renewal_dates[member['name']]}"
            body = f"Dear {member['name']}, this is a reminder that your membership renewal is due on {renewal_dates[member['name']]}."
            if email_api == 'gmail':
                send_email_gmail(config, member['email'], subject, body)
            elif email_api == 'outlook':
                send_email_outlook(config, member['email'], subject, body)

if __name__ == "__main__":
    main()
```

**config.json**
```json
{
    "email_api": "gmail",
    "gmail_username": "your-gmail-username@gmail.com",
    "gmail_password": "your-gmail-password",
    "outlook_username": "your-outlook-username@outlook.com",
    "outlook_password": "your-outlook-password",
    "members": [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Doe", "email": "jane.doe@example.com"}
    ],
    "events": [
        {"name": "Tennis Tournament", "date": "2024-09-20"}
    ],
    "renewal_dates": {
        "John Doe": "2024-10-01",
        "Jane Doe": "2024-11-01"
    }
}
```
