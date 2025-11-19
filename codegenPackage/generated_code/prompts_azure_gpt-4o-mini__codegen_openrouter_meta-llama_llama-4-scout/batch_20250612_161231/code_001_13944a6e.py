"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Write a Python script that automates the process of sending notifications to university employees about upcoming training activities and support services provided by associations like AFUNABB Chillán.
Generated: DETERMINISTIC_13944a6e0bdef348
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
University Employee Notification Script
=====================================

Automates the process of sending notifications to university employees about
upcoming training activities and support services provided by associations like AFUNABB Chillán.

Author: [Your Name]
Date: [Today's Date]
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmployeeNotificationService:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the EmployeeNotificationService instance.

        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            sender_email (str): Sender's email address.
            sender_password (str): Sender's email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, subject, body):
        """
        Sends a notification email to a university employee.

        Args:
            recipient_email (str): Recipient's email address.
            subject (str): Email subject.
            body (str): Email body.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            # Set up the SMTP server
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                # Log in to the SMTP server
                server.login(self.sender_email, self.sender_password)

                # Create a multipart email message
                message = MIMEMultipart()
                message['From'] = self.sender_email
                message['To'] = recipient_email
                message['Subject'] = subject

                # Attach the email body
                message.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(self.sender_email, recipient_email, message.as_string())

                logging.info(f"Email sent to {recipient_email} successfully.")
                return True

        except smtplib.SMTPAuthenticationError as e:
            logging.error(f"SMTP authentication error: {e}")
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

        logging.error(f"Failed to send email to {recipient_email}.")
        return False


def main():
    # Load configuration from environment variables
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = int(os.environ.get('SMTP_PORT', 465))
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')

    # Validate configuration
    if not all([smtp_server, sender_email, sender_password]):
        logging.error("Invalid configuration. Please set the required environment variables.")
        return

    # Create an instance of the EmployeeNotificationService
    notification_service = EmployeeNotificationService(smtp_server, smtp_port, sender_email, sender_password)

    # Example usage
    recipient_email = "recipient@example.com"
    subject = "Upcoming Training Activity"
    body = "Dear Employee, you are invited to a training activity on [Date] at [Time]. Please RSVP by [RSVP Deadline]."

    notification_service.send_notification(recipient_email, subject, body)


if __name__ == "__main__":
    main()
```
