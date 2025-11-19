"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giorgiobarbagelata.eu
Prompt: Write a Python script to handle service maintenance notifications for a web application, similar to the message on the Giorgiobarbagelata website.
Generated: DETERMINISTIC_c12a72330e4d5bf0
Batch ID: 20250612_135538
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
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    filename='maintenance_notifications.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MaintenanceNotification:
    def __init__(self, recipients, smtp_server, smtp_port, username, password):
        """
        Initialize the MaintenanceNotification with the necessary parameters.
        
        :param recipients: List of email addresses to notify
        :param smtp_server: SMTP server for sending emails
        :param smtp_port: SMTP port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.recipients = recipients
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_message(self, subject, body):
        """
        Create an email message object.
        
        :param subject: Subject of the email
        :param body: Body of the email
        :return: A MIMEText email object
        """
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = ', '.join(self.recipients)
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        return message

    def send_email(self, subject, body):
        """
        Send an email notification to the recipients.
        
        :param subject: Subject of the email
        :param body: Body of the email
        """
        message = self.create_message(subject, body)
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.sendmail(self.username, self.recipients, message.as_string())
                logging.info("Maintenance notification sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send email notification: {e}")
            raise

    def notify_maintenance(self, start_time, duration, reason):
        """
        Notify users about maintenance details.
        
        :param start_time: Start time of the maintenance (datetime object)
        :param duration: Duration of the maintenance (str)
        :param reason: Reason for maintenance (str)
        """
        subject = "Service Maintenance Notification"
        body = (f"Dear user,\n\n"
                f"We would like to inform you that our web application will undergo maintenance.\n"
                f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Duration: {duration}\n"
                f"Reason: {reason}\n\n"
                f"Thank you for your understanding.\n\n"
                f"Best regards,\n"
                f"The Team")
        self.send_email(subject, body)

if __name__ == "__main__":
    # Environment variables for sensitive data
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    USERNAME = os.getenv('SMTP_USERNAME')
    PASSWORD = os.getenv('SMTP_PASSWORD')
    
    # List of recipients to notify
    RECIPIENTS = ['user1@example.com', 'user2@example.com']

    # Example usage
    notification = MaintenanceNotification(RECIPIENTS, SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Notify users of maintenance (example parameters)
    try:
        maintenance_start = datetime(2023, 10, 15, 1, 0, 0)  # Example start time
        maintenance_duration = "2 hours"
        maintenance_reason = "Scheduled server upgrade"
        notification.notify_maintenance(maintenance_start, maintenance_duration, maintenance_reason)
    except Exception as e:
        logging.error(f"An error occurred while notifying users: {e}")
```
