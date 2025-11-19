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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReminderSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the ReminderSender with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port to connect to the SMTP server.
        :param sender_email: The email address to send reminders from.
        :param sender_password: The password for the sender email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to a specified recipient.

        :param recipient_email: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email} successfully.")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def schedule_reminders(self, members, class_info):
        """
        Schedules reminders for the new makeup classes and live sessions.

        :param members: A list of tuples containing member names and their email addresses.
        :param class_info: A dictionary containing class details (title, date, time).
        """
        subject = f"Reminder: New Makeup Class - {class_info['title']}"
        body_template = f"Dear {{name}},\n\nThis is a reminder for the upcoming makeup class:\n\n" \
                        f"Title: {class_info['title']}\nDate: {class_info['date']}\nTime: {class_info['time']}\n\n" \
                        f"Looking forward to seeing you there!\n\nBest,\nJu Ensina Team"

        for name, email in members:
            body = body_template.format(name=name)
            self.send_email(email, subject, body)

if __name__ == "__main__":
    # SMTP configurations
    SMTP_SERVER = 'smtp.example.com'  # Replace with actual SMTP server
    SMTP_PORT = 587                   # Common port for TLS
    SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
    SENDER_PASSWORD = 'your_password'        # Replace with your email password

    # Sample members list
    members = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com')
    ]

    # Example class information
    class_info = {
        'title': 'Advanced Makeup Techniques',
        'date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),  # Schedule for 3 days from now
        'time': '10:00 AM'
    }

    # Create an instance of ReminderSender and schedule reminders
    reminder_sender = ReminderSender(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    reminder_sender.schedule_reminders(members, class_info)
```
