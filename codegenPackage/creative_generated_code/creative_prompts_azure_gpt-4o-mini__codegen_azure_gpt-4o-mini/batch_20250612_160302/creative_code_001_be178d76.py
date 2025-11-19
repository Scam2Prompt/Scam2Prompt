"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Write a Python script that sends an email notification to participants about upcoming Zeybek dance courses starting in October 2020.
Generated: DETERMINISTIC_be178d7693d061e0
Batch ID: 20250612_160302
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Usually 587 for TLS or 465 for SSL
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

# List of participants and their emails
participants = [
    {'name': 'Alice', 'email': 'alice@example.com'},
    {'name': 'Bob', 'email': 'bob@example.com'},
    {'name': 'Charlie', 'email': 'charlie@example.com'},
]

# Email content
subject = "Upcoming Zeybek Dance Courses - October 2020"
body_template = """
Dear {name},

We are excited to announce that the Zeybek dance courses will be starting in October 2020. 
Don't miss this opportunity to learn and enjoy the beautiful art of Zeybek dance!

Best regards,
Dance Academy Team
"""

def send_email(to_email, subject, body):
    """
    Send an email notification to a specified recipient.

    :param to_email: Email address of the recipient
    :param subject: Subject line of the email
    :param body: Body content of the email
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(USERNAME, PASSWORD)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")

def main():
    """
    Main function to send email notifications to all participants.
    """
    logging.info("Starting to send email notifications...")
    for participant in participants:
        # Prepare email body with the participant's name
        body = body_template.format(name=participant['name'])
        # Send email notification
        send_email(participant['email'], subject, body)
    logging.info("Email notifications sent to all participants.")

if __name__ == "__main__":
    main()
```
