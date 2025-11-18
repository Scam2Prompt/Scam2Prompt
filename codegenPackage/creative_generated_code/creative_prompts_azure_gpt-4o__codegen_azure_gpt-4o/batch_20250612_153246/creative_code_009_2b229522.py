"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Write code to implement a notification system for tracking money transfers, inspired by the features of Dadih Online Exchange's services.
Generated: DETERMINISTIC_2b229522824fed8b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Logging configuration for tracking errors and activity
logging.basicConfig(
    filename="notification_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MoneyTransferNotificationSystem:
    """
    A class to implement a notification system for tracking money transfers.
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

    def send_email_notification(self, recipient_email, subject, message):
        """
        Send an email notification for a money transfer.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email notification
        :param message: Message content to be sent in the email
        """
        try:
            # Set up the email MIME structure
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # Establish connection with the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure the connection
            server.login(self.email, self.password)

            # Send the email
            server.send_message(msg)
            server.quit()

            # Log successful email sending
            logging.info(f"Email sent successfully to {recipient_email}. Subject: {subject}")

        except smtplib.SMTPException as e:
            # Log any errors during email sending
            logging.error(f"Failed to send email to {recipient_email}. Error: {e}")
            raise Exception(f"Failed to send email notification: {str(e)}")

    def notify_transfer(self, recipient_email, sender_name, recipient_name, amount, currency):
        """
        Notify the recipient of a money transfer.

        :param recipient_email: Recipient's email address
        :param sender_name: Name of the sender
        :param recipient_name: Name of the recipient
        :param amount: Amount transferred
        :param currency: Currency of the transferred amount
        """
        try:
            subject = f"Money Transfer Notification"
            message = (
                f"Dear {recipient_name},\n\n"
                f"You've received a money transfer of {amount} {currency} from {sender_name}.\n"
                f"If you have any questions, please contact our support.\n\n"
                f"Best regards,\nYour Notification System"
            )

            # Send the notification via email
            self.send_email_notification(recipient_email, subject, message)

        except Exception as e:
            # Log any errors during notification handling
            logging.error(f"Failed to notify transfer for recipient {recipient_email}. Error: {e}")
            raise Exception(f"Failed to notify transfer: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize the notification system with SMTP server details
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"

    notification_system = MoneyTransferNotificationSystem(
        smtp_server, smtp_port, sender_email, sender_password
    )

    # Perform a money transfer notification
    try:
        notification_system.notify_transfer(
            recipient_email="recipient@example.com",
            sender_name="Alice",
            recipient_name="Bob",
            amount=100,
            currency="USD"
        )
        print("Notification sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
