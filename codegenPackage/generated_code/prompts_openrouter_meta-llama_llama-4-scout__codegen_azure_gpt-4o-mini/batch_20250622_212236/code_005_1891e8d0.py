"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Create a simple notification system for sending updates on promotions, game statuses, and loyalty program rewards to users of an online casino platform like Treasury Brisbane Casino.
Generated: DETERMINISTIC_1891e8d019a2e4ce
Batch ID: 20250622_212236
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
from typing import List, Dict, Any

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If there is an error sending the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent successfully to {recipient}")

        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")

    def notify_users(self, users: List[Dict[str, Any]], notification_type: str) -> None:
        """
        Sends notifications to a list of users based on the notification type.

        :param users: A list of dictionaries containing user information (email and name).
        :param notification_type: The type of notification (promotions, game status, loyalty rewards).
        """
        for user in users:
            email = user.get('email')
            name = user.get('name')

            if email:
                subject = f"Update on {notification_type.capitalize()}"
                body = self.create_notification_body(name, notification_type)
                self.send_email(email, subject, body)

    def create_notification_body(self, name: str, notification_type: str) -> str:
        """
        Creates the body of the notification email based on the type.

        :param name: The name of the user.
        :param notification_type: The type of notification.
        :return: The body of the email.
        """
        if notification_type == "promotions":
            return f"Hello {name},\n\nCheck out our latest promotions and offers!\n\nBest regards,\nTreasury Brisbane Casino"
        elif notification_type == "game status":
            return f"Hello {name},\n\nHere are the latest updates on your favorite games!\n\nBest regards,\nTreasury Brisbane Casino"
        elif notification_type == "loyalty rewards":
            return f"Hello {name},\n\nYou have new loyalty rewards waiting for you!\n\nBest regards,\nTreasury Brisbane Casino"
        else:
            return f"Hello {name},\n\nWe have some updates for you!\n\nBest regards,\nTreasury Brisbane Casino"

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample user data
    users = [
        {"email": "user1@example.com", "name": "Alice"},
        {"email": "user2@example.com", "name": "Bob"},
    ]

    # Send notifications
    notification_system.notify_users(users, "promotions")
```
