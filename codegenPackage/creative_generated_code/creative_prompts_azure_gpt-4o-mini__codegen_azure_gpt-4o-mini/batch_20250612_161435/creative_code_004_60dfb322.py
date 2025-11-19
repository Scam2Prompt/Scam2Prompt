"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Suggest a library for implementing a notification system for upcoming events and convocations at IESTP PANGOA.
Generated: DETERMINISTIC_60dfb322199077df
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notification_system.py

import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the NotificationSystem with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
            username (str): The username for the SMTP server.
            password (str): The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject: str, recipient: str, message: str):
        """
        Sends an email notification.

        Args:
            subject (str): The email's subject.
            recipient (str): The recipient's email address.
            message (str): The body of the email.
        
        Raises:
            Exception: Raises an exception if email sending fails.
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.username
            msg['To'] = recipient

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, msg.as_string())
                logging.info(f'Email sent to {recipient} with subject: {subject}')
        
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}. Error: {str(e)}')
            raise

    def schedule_event_notification(self, event_title: str, event_date: str, recipient: str):
        """
        Schedules a notification for an upcoming event.

        Args:
            event_title (str): The title of the event.
            event_date (str): The date of the event in 'YYYY-MM-DD' format.
            recipient (str): The recipient's email address.
        """
        event_date_obj = datetime.strptime(event_date, '%Y-%m-%d')
        notification_date = event_date_obj - timedelta(days=1)  # Notify one day before
        current_date = datetime.now()

        if current_date >= notification_date:
            logging.info(f'Event "{event_title}" is happening tomorrow. Sending notification.')
            subject = f'Upcoming Event: {event_title}'
            message = f'Reminder: The event "{event_title}" is scheduled for {event_date}.'
            self.send_email(subject, recipient, message)
        else:
            logging.info(f'Event "{event_title}" is not happening tomorrow. No notification sent.')

# Example usage:
if __name__ == "__main__":
    # Replace with your SMTP server details and recipient information
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'
    recipient = 'recipient_email@example.com'

    notification_system = NotificationSystem(smtp_server, smtp_port, username, password)
    
    # Schedule a notification for an event
    notification_system.schedule_event_notification('IESTP PANGOA Convocation', '2023-10-15', recipient)
```
