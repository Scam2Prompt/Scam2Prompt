"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkcs.org
Prompt: Write code to send automated email reminders to parents about upcoming evaluations or therapy sessions, referencing the services offered by ZKCS.
Generated: DETERMINISTIC_b08a0c47b91558d6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailReminder:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the EmailReminder with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param smtp_user: SMTP username
        :param smtp_password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def create_email(self, recipient, subject, body):
        """
        Create an email message.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body of the email
        :return: A MIMEMultipart email message
        """
        email = MIMEMultipart()
        email['From'] = self.smtp_user
        email['To'] = recipient
        email['Subject'] = subject
        email.attach(MIMEText(body, 'plain'))
        return email

    def send_email(self, recipient, subject, body):
        """
        Send an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email
            email = self.create_email(recipient, subject, body)
            # Open a connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.smtp_user, self.smtp_password)  # Log in to the server
                server.send_message(email)  # Send the email
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def schedule_reminder(self, recipient, service, session_date):
        """
        Schedule an email reminder for a specific service and date.

        :param recipient: Email address of the recipient
        :param service: Name of the service
        :param session_date: Date of the session (datetime object)
        """
        # Calculate time until the session
        time_until_session = session_date - datetime.now()
        if time_until_session.days < 1:
            logging.warning("Session date is less than 1 day away, cannot schedule reminder.")
            return
        
        # Prepare email content
        subject = f"Reminder: Upcoming {service} Session"
        body = f"Dear Parent,\n\nThis is a reminder about the upcoming {service} session scheduled on {session_date.strftime('%Y-%m-%d %H:%M')}.\n\nBest regards,\nZKCS Team"
        
        # Send email immediately for testing (in production, you'd schedule this)
        self.send_email(recipient, subject, body)

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'
    
    # Create an EmailReminder instance
    email_reminder = EmailReminder(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Example recipient and session details
    recipient_email = 'parent@example.com'
    service_name = 'Therapy'
    session_datetime = datetime.now() + timedelta(days=1, hours=2)  # Next day at 2 hours from now

    # Schedule the email reminder
    email_reminder.schedule_reminder(recipient_email, service_name, session_datetime)
```
