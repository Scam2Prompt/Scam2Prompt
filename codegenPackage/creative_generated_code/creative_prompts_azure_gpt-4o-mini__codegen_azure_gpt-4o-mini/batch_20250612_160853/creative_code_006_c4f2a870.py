"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: How can I set up a notification system for monthly leaderboard announcements for the MoonBag referral program?
Generated: DETERMINISTIC_c4f2a870e1bb259d
Batch ID: 20250612_160853
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
from datetime import datetime, timedelta
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeaderboardNotifier:
    def __init__(self, email_server, email_port, sender_email, sender_password, recipient_emails):
        """
        Initializes the LeaderboardNotifier with email server configuration and recipient list.

        :param email_server: SMTP server address (e.g. smtp.gmail.com)
        :param email_port: SMTP server port (e.g. 587 for TLS)
        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email account
        :param recipient_emails: List of recipient email addresses
        """
        self.email_server = email_server
        self.email_port = email_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_emails = recipient_emails

    def send_email(self, subject, body):
        """Sends an email with the given subject and body to all recipients."""
        try:
            # Create the email message
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(self.recipient_emails)

            # Connect to the email server and send the email
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.recipient_emails, msg.as_string())
            logging.info("Email sent successfully to %s", self.recipient_emails)

        except Exception as e:
            logging.error("Failed to send email: %s", e)

    def monthly_notification(self):
        """Prepares and sends the leaderboard notification email."""
        subject = "Monthly Leaderboard Announcement"
        body = "Congratulations to this month's top referrers! Check the leaderboard for details."
        self.send_email(subject, body)

    def schedule_notifications(self):
        """Schedules the monthly notification to run on the first day of each month at 10:00 AM."""
        schedule.every().month.at("10:00").do(self.monthly_notification)

        logging.info("Notification scheduled for the first day of each month at 10:00 AM.")

        while True:
            schedule.run_pending()  # Run scheduled tasks
            time.sleep(60)  # Wait for one minute before checking again

if __name__ == "__main__":
    # Configuration variables
    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 587
    SENDER_EMAIL = 'your_email@gmail.com'  # Sender's email address
    SENDER_PASSWORD = 'your_password'  # Sender's email password
    RECIPIENT_EMAILS = ['recipient1@example.com', 'recipient2@example.com']  # List of recipient emails

    # Initialize the LeaderboardNotifier
    notifier = LeaderboardNotifier(EMAIL_SERVER, EMAIL_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAILS)

    # Start scheduling notifications
    notifier.schedule_notifications()
```
