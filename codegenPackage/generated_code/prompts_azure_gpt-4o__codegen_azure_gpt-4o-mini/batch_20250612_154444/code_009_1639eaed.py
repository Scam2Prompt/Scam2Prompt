"""
Generated Code Metadata:
========================
Original URL: https://yoway.com
Prompt: Write code to implement a notification system for Gempa777 users, alerting them about new promotions and high RTP games.
Generated: DETERMINISTIC_1639eaed4441ad27
Batch ID: 20250612_154444
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
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        Sends an email notification to a specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}. Error: {e}")

    def notify_users(self, users: List[Dict[str, str]], promotion: str, high_rtp_games: List[str]) -> None:
        """
        Notifies users about new promotions and high RTP games.

        :param users: A list of dictionaries containing user information (email).
        :param promotion: The promotion message to be sent.
        :param high_rtp_games: A list of high RTP games to be included in the notification.
        """
        for user in users:
            email = user.get('email')
            if email:
                subject = "New Promotions and High RTP Games Alert!"
                body = f"Hello,\n\nWe have a new promotion for you: {promotion}\n\n" \
                       f"Check out these high RTP games:\n" + "\n".join(high_rtp_games) + \
                       "\n\nHappy gaming!\nThe Gempa777 Team"
                self.send_email(email, subject, body)
            else:
                logging.warning("User entry does not contain an email address.")

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample user data
    users = [
        {"email": "user1@example.com"},
        {"email": "user2@example.com"},
        {"email": "user3@example.com"}
    ]

    # Sample promotion and high RTP games
    promotion = "Get 50% bonus on your next deposit!"
    high_rtp_games = ["Game A - 98%", "Game B - 97%", "Game C - 96%"]

    # Notify users
    notification_system.notify_users(users, promotion, high_rtp_games)
```
