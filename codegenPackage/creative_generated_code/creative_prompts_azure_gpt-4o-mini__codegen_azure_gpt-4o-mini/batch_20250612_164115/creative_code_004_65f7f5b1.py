"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamusk.app
Prompt: How can I set up a soft launch event notification system in my app, similar to what metamusk.app is planning?
Generated: DETERMINISTIC_65f7f5b171f211c3
Batch ID: 20250612_164115
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
from datetime import datetime
import logging
from apscheduler.schedulers.background import BackgroundScheduler

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SoftLaunchNotifier:
    def __init__(self, email_config, launch_date):
        """
        Initializes the SoftLaunchNotifier.

        Args:
            email_config (dict): Configuration for email notifications.
            launch_date (datetime): The date and time of the soft launch event.
        """
        self.email_config = email_config
        self.launch_date = launch_date
        self.scheduler = BackgroundScheduler()

    def send_email(self, recipient: str, subject: str, body: str):
        """
        Sends an email notification.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Raises:
            Exception: If there's an error in sending the email.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['from_email']
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()  # Use TLS
                server.login(self.email_config['from_email'], self.email_config['password'])
                server.send_message(msg)

            logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise

    def schedule_notification(self, recipient: str):
        """
        Schedules the notification email for the soft launch event.

        Args:
            recipient (str): The recipient's email address.
        """
        notification_time = self.launch_date  # You can adjust this to send reminders before launch
        self.scheduler.add_job(self.send_email, 'date', run_date=notification_time,
                                args=[recipient, "Soft Launch Notification", "The soft launch is happening soon!"])
        self.scheduler.start()
        logging.info(f"Notification scheduled for {recipient} at {notification_time}")

    def shutdown_scheduler(self):
        """Shuts down the scheduler gracefully."""
        self.scheduler.shutdown()

# Example usage
if __name__ == "__main__":
    # Email configuration
    email_config = {
        'from_email': 'your_email@example.com',
        'password': 'your_password',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587
    }

    # Set the soft launch date and time
    launch_date = datetime(2023, 10, 30, 15, 0, 0)  # Example: October 30, 2023, 3:00 PM

    # Create notifier instance
    notifier = SoftLaunchNotifier(email_config=email_config, launch_date=launch_date)

    # Schedule notification for a recipient
    recipient_email = 'recipient@example.com'
    notifier.schedule_notification(recipient_email)

    try:
        # Keep the main thread alive to allow scheduled tasks to run
        while True:
            pass
    except KeyboardInterrupt:
        notifier.shutdown_scheduler()
        logging.info("Scheduler has been shut down.")
```
