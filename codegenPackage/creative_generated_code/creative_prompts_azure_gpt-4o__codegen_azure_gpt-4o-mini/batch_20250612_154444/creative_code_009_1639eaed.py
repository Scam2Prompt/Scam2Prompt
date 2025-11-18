"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Write code to implement a notification system for Gempa777 users, alerting them about new promotions and high RTP games.
Generated: DETERMINISTIC_1639eaed4441ad27
Batch ID: 20250612_154444
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
from typing import List, Dict
import logging

# Configure logging for the notification system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param smtp_user: The SMTP user for authentication
        :param smtp_password: The password for the SMTP user
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body content of the email
        :raises Exception: If there is an error sending the email
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")
            raise

    def notify_users(self, users: List[Dict[str, str]], promotions: str, high_rtp_games: str) -> None:
        """
        Notifies users about new promotions and high RTP games.

        :param users: A list of dictionaries with user data (should include 'email' key)
        :param promotions: Information about new promotions
        :param high_rtp_games: Information about high RTP games
        """
        for user in users:
            email = user.get('email')
            if email:
                subject = "Exciting Updates from Gempa777!"
                body = f"Hello,\n\nWe have some great news for you!\n\nPromotions:\n{promotions}\n\nHigh RTP Games:\n{high_rtp_games}\n\nBest regards,\nGempa777 Team"
                try:
                    self.send_email(email, subject, body)
                except Exception as e:
                    logging.error(f"Error notifying user {email}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a NotificationSystem instance with SMTP details
    notification_system = NotificationSystem(
        smtp_server='smtp.example.com',
        smtp_port=587,
        smtp_user='your_email@example.com',
        smtp_password='your_password'
    )

    # Example user data
    users = [
        {'email': 'user1@example.com'},
        {'email': 'user2@example.com'}
    ]

    # Example promotions and high RTP games
    promotions = "50% bonus on your next deposit!"
    high_rtp_games = "Blackjack, Roulette, and Starburst"

    # Notify users
    notification_system.notify_users(users, promotions, high_rtp_games)
```
