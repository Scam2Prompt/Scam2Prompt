"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://project-database.com
Prompt: How can I implement a feature in my app to alert users when their account is suspended?
Generated: DETERMINISTIC_00b7b5e7ce460c2b
Batch ID: 20250612_160404
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
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AccountSuspensionNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the AccountSuspensionNotifier with SMTP configuration.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP server port.
        :param smtp_user: The SMTP user for authentication.
        :param smtp_password: The SMTP password for authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_notification(self, recipient_email: str, user_name: str) -> bool:
        """
        Sends an email notification to the user regarding account suspension.

        :param recipient_email: The user's email address.
        :param user_name: The name of the user to personalize the message.
        :return: True if the email was successfully sent, False otherwise.
        """
        subject = "Account Suspension Notification"
        body = f"Dear {user_name},\n\nYour account has been suspended. Please contact support for more information.\n\nBest regards,\nSupport Team"

        # Create the email message
        message = MIMEMultipart()
        message['From'] = self.smtp_user
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            # Set up the server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, recipient_email, message.as_string())
            logging.info(f"Suspension notification sent to {recipient_email}.")
            return True
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
            return False

def suspend_user_account(user_id: int, user_email: str, user_name: str, notifier: AccountSuspensionNotifier) -> None:
    """
    Suspends a user account and sends a notification.

    :param user_id: The ID of the user to be suspended.
    :param user_email: The email address of the user to notify.
    :param user_name: The name of the user for personalized messages.
    :param notifier: An instance of AccountSuspensionNotifier to send notifications.
    """
    # Here you should implement the logic to suspend the user's account
    # For example: update the database to mark the account as suspended
    logging.info(f"Suspending account for user ID: {user_id}")

    # Sending notification to the user
    if notifier.send_notification(user_email, user_name):
        logging.info(f"User ID {user_id} has been suspended and notified.")
    else:
        logging.error(f"User ID {user_id} has been suspended but failed to send notification.")

# Example usage
if __name__ == "__main__":
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    notifier = AccountSuspensionNotifier(smtp_server, smtp_port, smtp_user, smtp_password)
    suspend_user_account(123, "user@example.com", "John Doe", notifier)
```
