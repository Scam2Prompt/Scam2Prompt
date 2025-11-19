"""
Generated Code Metadata:
========================
Original URL: https://pomrajufm.edu.bd
Prompt: Construct a code snippet that sends email notifications for important dates like admission deadlines from the Pomra Jameul Ulum Fazil Madrasha's calendar.
Generated: DETERMINISTIC_5b2761366a5d05c4
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Configuration for email server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# List of important dates (replace with actual dates from the calendar)
important_dates = [
    {"event": "Admission Deadline", "date": "2023-12-15"},
    {"event": "Exam Registration Deadline", "date": "2023-11-30"},
]

# List of recipients (replace with actual email addresses)
recipients = [
    "recipient1@example.com",
    "recipient2@example.com",
]

def send_email(subject, body, recipient):
    """
    Sends an email notification.
    
    :param subject: Subject of the email
    :param body: Body of the email
    :param recipient: Recipient's email address
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {recipient} successfully.")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

def check_and_notify():
    """
    Checks for upcoming important dates and sends email notifications.
    """
    today = datetime.now().date()
    for event in important_dates:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
        days_until_event = (event_date - today).days

        # Notify if the event is within 7 days
        if 0 <= days_until_event <= 7:
            subject = f"Reminder: {event['event']} is on {event_date}"
            body = f"Dear recipient,\n\nThis is a reminder that the {event['event']} is scheduled for {event_date}. Please take necessary actions.\n\nBest regards,\nPomra Jameul Ulum Fazil Madrasha"
            for recipient in recipients:
                send_email(subject, body, recipient)

if __name__ == "__main__":
    # Run the notification system
    check_and_notify()
```
