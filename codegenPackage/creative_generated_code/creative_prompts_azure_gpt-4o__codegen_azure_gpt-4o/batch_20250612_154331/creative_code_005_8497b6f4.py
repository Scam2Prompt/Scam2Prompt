"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frag999.com
Prompt: Design an automated notification system that alerts users when the Fragment premium number claim limit of 5000 is nearing completion.
Generated: DETERMINISTIC_8497b6f474e732f2
Batch ID: 20250612_154331
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the notification system with email server details.

        :param smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        :param smtp_port: SMTP server port (e.g., 587)
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, message):
        """
        Sends an email notification.

        :param recipient_email: Recipient's email address
        :param subject: Email subject
        :param message: Email message content
        """
        try:
            # Create the email
            email = MIMEMultipart()
            email['From'] = self.sender_email
            email['To'] = recipient_email
            email['Subject'] = subject
            email.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(email)

            logging.info(f"Notification sent to {recipient_email}.")
        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

def monitor_fragment_claims(limit, current_claims, notification_system, user_emails):
    """
    Monitors the Fragment premium claim limit and sends alerts if necessary.

    :param limit: The maximum number of claims allowed (e.g., 5000)
    :param current_claims: The current number of claims
    :param notification_system: Instance of NotificationSystem
    :param user_emails: List of user email addresses to notify
    """
    try:
        # Calculate the remaining claims
        remaining_claims = limit - current_claims

        # Check if the remaining claims are below the threshold (10%)
        if remaining_claims <= limit * 0.1:
            # Prepare the notification
            subject = "Fragment Premium Claim Limit Alert"
            message = (
                f"Dear User,\n\n"
                f"The Fragment premium claim limit of {limit} is nearing completion.\n"
                f"Currently, there are only {remaining_claims} claims remaining.\n\n"
                f"Please take necessary action.\n\n"
                f"Best regards,\nNotification System"
            )
            # Send notifications to all users
            for email in user_emails:
                notification_system.send_email(email, subject, message)
    except Exception as e:
        logging.error(f"Error in monitoring claims: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP Configuration
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'your_email@example.com'
    SENDER_PASSWORD = 'your_password'

    # Initialize the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Fragment claim parameters
    PREMIUM_CLAIM_LIMIT = 5000
    current_premium_claims = 4501  # Example current claims

    # User email list
    user_emails = ['user1@example.com', 'user2@example.com']

    # Monitor and alert if necessary
    monitor_fragment_claims(PREMIUM_CLAIM_LIMIT, current_premium_claims, notification_system, user_emails)
```

Note: 
1. Replace `your_email@example.com` and `your_password` with valid credentials.
2. Ensure to use environment variables or a secure vault for sensitive information in production systems.
