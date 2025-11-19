"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Develop a notification system for homeowner associations to alert residents about upcoming maintenance or cleaning tasks, inspired by BlocPrest's services.
Generated: DETERMINISTIC_6383ca81bf7de2c8
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the NotificationSystem with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email notification to a resident.

        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def schedule_notifications(self, residents, task_details, notify_days_before=3):
        """
        Schedule notifications for upcoming maintenance tasks.

        :param residents: List of resident email addresses
        :param task_details: Dictionary containing task details with 'date' and 'description'
        :param notify_days_before: Number of days before the task to send the notification
        """
        task_date = datetime.strptime(task_details['date'], '%Y-%m-%d')
        notify_date = task_date - timedelta(days=notify_days_before)

        if datetime.now() >= notify_date:
            subject = f"Upcoming Maintenance Notification: {task_details['description']}"
            body = f"Dear Resident,\n\nThis is a reminder that the following maintenance task is scheduled:\n\n" \
                   f"Task: {task_details['description']}\nDate: {task_details['date']}\n\nThank you,\nHomeowner Association"

            for resident in residents:
                self.send_email(resident, subject, body)

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of resident email addresses
    residents = ['resident1@example.com', 'resident2@example.com']

    # Task details
    task_details = {
        'date': '2023-10-15',  # Date of the maintenance task
        'description': 'Building exterior cleaning'
    }

    # Schedule notifications
    notification_system.schedule_notifications(residents, task_details)
```
