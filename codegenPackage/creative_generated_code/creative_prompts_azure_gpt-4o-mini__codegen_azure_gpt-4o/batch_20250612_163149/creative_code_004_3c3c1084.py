"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-buildon.online
Prompt: How can I create a notification system for participants to remind them to vote within the first 24 hours for priority allocation?
Generated: DETERMINISTIC_3c3c108400027476
Batch ID: 20250612_163149
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

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration for email server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

# Notification system class
class NotificationSystem:
    def __init__(self):
        self.participants = []  # List to store participant data

    def add_participant(self, email, signup_time):
        """
        Add a participant to the notification system.

        :param email: Participant's email address.
        :param signup_time: Timestamp of signup (datetime object).
        """
        self.participants.append({"email": email, "signup_time": signup_time})

    def send_email(self, recipient_email):
        """
        Send a reminder email to the participant.

        :param recipient_email: Email address of the recipient.
        :raises: Exception if email sending fails.
        """
        try:
            # Create the email content
            subject = "Reminder to Vote for Priority Allocation"
            body = (
                "Dear participant,\n\n"
                "This is a reminder to vote within the first 24 hours for priority allocation.\n"
                "Please make sure to cast your vote as soon as possible.\n\n"
                "Best regards,\nThe Team"
            )

            # Construct email
            message = MIMEMultipart()
            message["From"] = EMAIL_ADDRESS
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, recipient_email, message.as_string())

            logging.info(f"Reminder email successfully sent to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
            raise

    def check_and_notify(self):
        """
        Check for participants who signed up within the last 24 hours and send reminders.
        """
        now = datetime.now()
        for participant in self.participants:
            signup_time = participant["signup_time"]
            email = participant["email"]

            # Check if signup time falls within the first 24 hours
            if now - signup_time <= timedelta(hours=24):
                try:
                    self.send_email(email)
                except Exception as e:
                    logging.error(f"Error while sending notification to {email}: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the notification system
    notification_system = NotificationSystem()

    # Add participants (replace with actual data)
    notification_system.add_participant("participant1@example.com", datetime.now() - timedelta(hours=23))
    notification_system.add_participant("participant2@example.com", datetime.now() - timedelta(hours=25))

    # Check and notify participants
    notification_system.check_and_notify()
```
