"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write a program to generate automated reminders for deadlines related to the ENADE exam and professor selection processes, using the timeline provided on the IGEOG website.
Generated: DETERMINISTIC_b414ba35c3947c8c
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

# Configuration for email
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Define deadlines for ENADE exam and professor selection processes
DEADLINES = {
    "ENADE Exam": datetime.datetime(2024, 11, 15),
    "Professor Selection": datetime.datetime(2024, 10, 1),
}

def send_email(recipient: str, subject: str, body: str) -> None:
    """
    Sends an email to the specified recipient with the given subject and body.

    :param recipient: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body of the email
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
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {recipient} successfully.")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

def generate_reminders(deadlines: Dict[str, datetime.datetime], days_before: int) -> List[str]:
    """
    Generates reminder messages for upcoming deadlines.

    :param deadlines: A dictionary of deadlines with their descriptions
    :param days_before: Number of days before the deadline to send the reminder
    :return: A list of reminder messages
    """
    reminders = []
    today = datetime.datetime.now()

    for event, deadline in deadlines.items():
        if (deadline - today).days == days_before:
            reminders.append(f"Reminder: The deadline for {event} is on {deadline.strftime('%Y-%m-%d')}.")

    return reminders

def main() -> None:
    """
    Main function to generate reminders and send emails.
    """
    # Generate reminders for deadlines 7 days before
    reminders = generate_reminders(DEADLINES, days_before=7)

    # List of recipients to send reminders to
    recipients = ['recipient1@example.com', 'recipient2@example.com']

    # Send reminders via email
    for reminder in reminders:
        for recipient in recipients:
            send_email(recipient, "Upcoming Deadline Reminder", reminder)

if __name__ == "__main__":
    main()
```
