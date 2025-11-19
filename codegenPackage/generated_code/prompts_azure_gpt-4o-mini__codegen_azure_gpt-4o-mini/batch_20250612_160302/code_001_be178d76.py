"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Write a Python script that sends an email notification to participants about upcoming Zeybek dance courses starting in October 2020.
Generated: DETERMINISTIC_be178d7693d061e0
Batch ID: 20250612_160302
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
from email.utils import formataddr
from typing import List

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

# Email content
SUBJECT = 'Upcoming Zeybek Dance Courses - October 2020'
BODY_TEMPLATE = """
Dear Participant,

We are excited to announce that our Zeybek dance courses will be starting in October 2020. 
Join us to learn the beautiful art of Zeybek dance!

Best regards,
Zeybek Dance Academy
"""

def send_email(to_email: str) -> None:
    """
    Sends an email notification to the specified recipient.

    :param to_email: The recipient's email address.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Zeybek Dance Academy', USERNAME))
        msg['To'] = to_email
        msg['Subject'] = SUBJECT

        # Attach the email body
        msg.attach(MIMEText(BODY_TEMPLATE, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email

        print(f"Email sent successfully to {to_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email to {to_email}: {e}")

def notify_participants(email_list: List[str]) -> None:
    """
    Notifies all participants by sending an email to each one.

    :param email_list: A list of email addresses to notify.
    """
    for email in email_list:
        send_email(email)

if __name__ == '__main__':
    # List of participants' email addresses
    participants_emails = [
        'participant1@example.com',
        'participant2@example.com',
        'participant3@example.com',
        # Add more email addresses as needed
    ]

    # Notify all participants
    notify_participants(participants_emails)
```
