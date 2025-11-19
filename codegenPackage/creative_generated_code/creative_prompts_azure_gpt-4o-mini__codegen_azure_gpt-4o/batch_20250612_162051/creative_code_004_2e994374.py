"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Construct a code snippet that sends notifications to volunteers about upcoming environmental campaigns, based on the volunteer engagement strategies outlined by "Čuvari Šare."
Generated: DETERMINISTIC_2e99437424ca83b4
Batch ID: 20250612_162051
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
from datetime import datetime, timedelta

# Configure logging for error handling and debugging
logging.basicConfig(
    filename='volunteer_notifications.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class VolunteerNotificationSystem:
    def __init__(self, email_host, email_port, email_user, email_password):
        """
        Initialize the notification system.

        :param email_host: SMTP host for email sending
        :param email_port: SMTP port for email sending
        :param email_user: Sender email address
        :param email_password: Sender email password
        """
        self.email_host = email_host
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password

    def send_notification(self, recipient_email, subject, message):
        """
        Sends an email notification to a volunteer.

        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param message: Content of the email
        """
        try:
            # Create email message
            email = MIMEMultipart()
            email['From'] = self.email_user
            email['To'] = recipient_email
            email['Subject'] = subject
            email.attach(MIMEText(message, 'plain'))

            # Send email using SMTP
            with smtplib.SMTP(self.email_host, self.email_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_user, self.email_password)
                server.send_message(email)

            logging.info(f"Notification sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send notification to {recipient_email}: {e}")

    def schedule_notifications(self, volunteers, campaign_date, days_prior=3):
        """
        Schedule notifications for volunteers about an upcoming campaign.

        :param volunteers: List of volunteer emails
        :param campaign_date: Date of the campaign (YYYY-MM-DD)
        :param days_prior: Number of days before the campaign to send notifications
        """
        try:
            campaign_datetime = datetime.strptime(campaign_date, '%Y-%m-%d')
            notification_date = campaign_datetime - timedelta(days=days_prior)
            current_date = datetime.now()

            # Check if it's time to send notifications
            if current_date >= notification_date:
                subject = "Upcoming Environmental Campaign"
                message = (
                    f"Dear Volunteer,\n\nWe are excited to remind you about the upcoming environmental campaign "
                    f"organized by Čuvari Šare on {campaign_date}. Your participation is vital to our mission!\n\n"
                    f"Thank you for your continued support.\n\nBest regards,\nČuvari Šare Team"
                )

                for volunteer in volunteers:
                    self.send_notification(volunteer, subject, message)
            else:
                logging.info("Not time to send notifications yet.")
        except ValueError as ve:
            logging.error(f"Invalid date format provided: {ve}")
        except Exception as e:
            logging.error(f"Error in scheduling notifications: {e}")


# Example usage:
if __name__ == '__main__':
    # Email server configuration
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USER = 'your-email@example.com'
    EMAIL_PASSWORD = 'your-email-password'

    # List of volunteers' email addresses
    volunteers_emails = [
        'volunteer1@example.com',
        'volunteer2@example.com',
        'volunteer3@example.com'
    ]

    # Campaign date
    campaign_date = '2023-12-25'

    # Initialize the notification system
    notifier = VolunteerNotificationSystem(EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD)

    # Schedule notifications
    notifier.schedule_notifications(volunteers_emails, campaign_date)
```
