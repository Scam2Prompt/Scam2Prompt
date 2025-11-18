"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Develop a notification system in Python that sends reminders to residents of the City of York about upcoming refuse and recycling collection days.
Generated: DETERMINISTIC_ed92225757acf3f1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Notification System Class
class NotificationSystem:
    def __init__(self, residents_info, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the Notification System.

        :param residents_info: Dictionary containing resident's email and collection days
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Email address to send notifications from
        :param sender_password: Password for the sender email account
        """
        self.residents_info = residents_info
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email notification.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create the email message
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.sender_email, self.sender_password)  # Authenticate
                server.sendmail(self.sender_email, recipient_email, msg.as_string())  # Send email
                logging.info(f'Notification sent to {recipient_email}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}: {e}')

    def schedule_notifications(self):
        """
        Schedule notifications for residents based on collection days.
        """
        scheduler = BlockingScheduler()
        for resident, collection_days in self.residents_info.items():
            for day in collection_days:
                # Schedule the notification one day before collection
                notification_time = day - timedelta(days=1)
                scheduler.add_job(
                    self.send_email,
                    'date',
                    run_date=notification_time,
                    args=[resident['email'], 'Refuse and Recycling Reminder',
                          f'Reminder: Your refuse and recycling will be collected on {day.strftime("%A, %B %d, %Y")}.']
                )
        try:
            logging.info('Starting the notification scheduler...')
            scheduler.start()  # Start the job scheduler
        except (KeyboardInterrupt, SystemExit):
            logging.info('Scheduler stopped.')

# Sample residents' information
residents_info = {
    "John Doe": {
        "email": "john.doe@example.com",
        "collection_days": [datetime(2023, 11, 1), datetime(2023, 11, 15)]
    },
    "Jane Smith": {
        "email": "jane.smith@example.com",
        "collection_days": [datetime(2023, 11, 2), datetime(2023, 11, 16)]
    }
}

# Configuration for the SMTP server
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@example.com'
SENDER_PASSWORD = 'your_password'

if __name__ == "__main__":
    # Initialize and run the notification system
    notification_system = NotificationSystem(residents_info, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    notification_system.schedule_notifications()
```
