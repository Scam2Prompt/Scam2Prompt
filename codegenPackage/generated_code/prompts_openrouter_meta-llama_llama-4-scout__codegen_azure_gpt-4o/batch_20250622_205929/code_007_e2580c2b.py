"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Develop a notification system for stakers when rewards are distributed or when there are updates to their staking positions.
Generated: DETERMINISTIC_e2580c2b7b6ba5e5
Batch ID: 20250622_205929
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    """
    A notification system for stakers to receive updates about rewards distribution
    or changes to their staking positions.
    """

    def __init__(self, smtp_server, smtp_port, email, password):
        """
        Initialize the notification system with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param email: Sender email address
        :param password: Sender email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_email(self, recipient_email, subject, message):
        """
        Send an email notification to the recipient.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param message: Body of the email
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email, self.password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_reward_distribution(self, recipient_email, reward_amount):
        """
        Notify the staker about reward distribution.

        :param recipient_email: Recipient's email address
        :param reward_amount: Amount of rewards distributed
        """
        subject = "Reward Distribution Notification"
        message = f"Dear Staker,\n\nYou have received a reward of {reward_amount} tokens.\n\nThank you for staking with us!"
        self.send_email(recipient_email, subject, message)

    def notify_staking_update(self, recipient_email, staking_position):
        """
        Notify the staker about updates to their staking position.

        :param recipient_email: Recipient's email address
        :param staking_position: Updated staking position details
        """
        subject = "Staking Position Update"
        message = f"Dear Staker,\n\nYour staking position has been updated:\n{staking_position}\n\nThank you for staking with us!"
        self.send_email(recipient_email, subject, message)


# Example usage
if __name__ == "__main__":
    # SMTP server configuration (replace with actual credentials)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"

    # Initialize the notification system
    notifier = NotificationSystem(SMTP_SERVER, SMTP_PORT, EMAIL, PASSWORD)

    # Example notifications
    recipient = "staker@example.com"
    notifier.notify_reward_distribution(recipient, 100)
    notifier.notify_staking_update(recipient, "New staking position: 500 tokens")
```
