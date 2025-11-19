"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Illustrate how to use a library to send automated emails to parents for school announcements, similar to those from the Colegio Panamericano e Instituto Libertadores.
Generated: DETERMINISTIC_47c98e99f5f49cd3
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from typing import List, Dict

# Constants for email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_NAME = "Your School Name"
SENDER_PASSWORD = "your_email_password"

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Sends an email to a specified recipient.

    :param to_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body content of the email
    :raises Exception: Raises an exception if sending fails
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login with credentials
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())  # Send the email

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

def send_bulk_emails(recipients: List[Dict[str, str]], subject: str, message: str) -> None:
    """
    Sends bulk emails to a list of recipients.

    :param recipients: List of dictionaries containing recipient information (name and email)
    :param subject: Subject of the email
    :param message: Body content of the email
    """
    for recipient in recipients:
        name = recipient.get('name')
        email = recipient.get('email')
        personalized_message = f"Dear {name},\n\n{message}"  # Personalize the message
        send_email(email, subject, personalized_message)

if __name__ == "__main__":
    # Example list of recipients
    recipients_list = [
        {'name': 'Juan Pérez', 'email': 'juan.perez@example.com'},
        {'name': 'María García', 'email': 'maria.garcia@example.com'}
    ]

    # Email subject and message
    subject = "School Announcement: Important Update"
    message = "We would like to inform you about the upcoming events at our school."

    # Send bulk emails
    send_bulk_emails(recipients_list, subject, message)
```

**Important Note**: Please ensure to replace `your_email@gmail.com` and `your_email_password` with valid credentials. It's recommended to use environment variables or a configuration file for sensitive information in production code.
