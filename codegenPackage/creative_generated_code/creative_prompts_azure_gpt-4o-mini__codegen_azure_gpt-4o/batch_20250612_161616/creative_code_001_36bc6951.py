"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jualessandraensina.com
Prompt: Write a Python script that automates the process of sending reminders for new makeup classes and live sessions to members of a beauty school like Ju Ensina.
Generated: DETERMINISTIC_36bc695179243eac
Batch ID: 20250612_161616
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("reminder_log.log"),
        logging.StreamHandler()
    ]
)

class ReminderSender:
    def __init__(self, smtp_server, smtp_port, email, password):
        """
        Initializes the ReminderSender with SMTP server details and sender credentials.

        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            email (str): Sender email address.
            password (str): Sender email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        Sends an email to the specified recipient.

        Args:
            recipient (str): Recipient email address.
            subject (str): Email subject.
            body (str): Email body.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
                logging.info(f"Reminder email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def get_upcoming_events():
    """
    Retrieves a list of upcoming events.

    Returns:
        list of dict: A list of events, each represented as a dictionary.
    """
    # Mock list of events for demonstration purposes
    return [
        {"name": "Makeup Masterclass", "date": datetime.now() + timedelta(days=2)},
        {"name": "Live Q&A Session", "date": datetime.now() + timedelta(days=5)}
    ]

def get_member_list():
    """
    Retrieves the list of members to send reminders to.

    Returns:
        list of dict: A list of members, each represented as a dictionary.
    """
    # Mock list of members for demonstration purposes
    return [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]

def format_email_body(member_name, event_name, event_date):
    """
    Formats the email body for a reminder.

    Args:
        member_name (str): Name of the member.
        event_name (str): Name of the event.
        event_date (datetime): Date of the event.

    Returns:
        str: Formatted email body.
    """
    return (
        f"Dear {member_name},\n\n"
        f"We are excited to remind you about the upcoming event:\n\n"
        f"Event: {event_name}\n"
        f"Date: {event_date.strftime('%A, %d %B %Y at %I:%M %p')}\n\n"
        f"Don't miss it!\n\n"
        f"Best regards,\n"
        f"The Ju Ensina Team"
    )

def send_reminders():
    """
    Sends reminders for upcoming events to all members.
    """
    # Configuration for email sender
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Initialize the ReminderSender
    reminder_sender = ReminderSender(smtp_server, smtp_port, sender_email, sender_password)

    # Get the upcoming events and member list
    events = get_upcoming_events()
    members = get_member_list()

    # Iterate over each event and send reminders to members
    for event in events:
        for member in members:
            email_body = format_email_body(member['name'], event['name'], event['date'])
            reminder_sender.send_email(member['email'], f"Reminder: {event['name']}", email_body)

if __name__ == "__main__":
    # Execute the reminder sending process
    try:
        logging.info("Starting the reminder sending process.")
        send_reminders()
        logging.info("Reminder sending process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
