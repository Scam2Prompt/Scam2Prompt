"""
Generated Code Metadata:
========================
Original URL: https://tojsat.net
Prompt: Illustrate how to implement a notification system for authors when their articles are published in an online journal, inspired by the practices of TOJSAT.
Generated: DETERMINISTIC_5fe352331b3ec49d
Batch ID: 20250612_161514
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
    A notification system to inform authors when their articles are published.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the notification system with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, author_name, article_title):
        """
        Send a notification email to the author.

        :param recipient_email: Author's email address
        :param author_name: Author's name
        :param article_title: Title of the published article
        """
        try:
            # Create the email content
            subject = "Your Article Has Been Published!"
            body = f"Dear {author_name},\n\n" \
                   f"We are pleased to inform you that your article titled \"{article_title}\" " \
                   f"has been successfully published in our journal.\n\n" \
                   f"Thank you for your contribution.\n\n" \
                   f"Best regards,\nThe Editorial Team"

            # Create the email message
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            logging.info(f"Notification sent successfully to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send notification to {recipient_email}: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration (use a valid SMTP server and credentials)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Send a notification to an author
    AUTHOR_EMAIL = "author_email@example.com"
    AUTHOR_NAME = "John Doe"
    ARTICLE_TITLE = "Innovative Research in AI"

    notification_system.send_notification(AUTHOR_EMAIL, AUTHOR_NAME, ARTICLE_TITLE)
```
