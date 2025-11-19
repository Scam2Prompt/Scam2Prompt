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
# notification_system.py

import logging
from typing import List, Dict
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    def __init__(self, id: int, email: str, preferences: Dict[str, bool]):
        """
        Initialize a User object.

        Args:
        id (int): Unique user ID.
        email (str): User's email address.
        preferences (Dict[str, bool]): User's notification preferences.
        """
        self.id = id
        self.email = email
        self.preferences = preferences

class Notification:
    def __init__(self, id: int, title: str, content: str, promotion: bool = False, high_rtp_game: bool = False):
        """
        Initialize a Notification object.

        Args:
        id (int): Unique notification ID.
        title (str): Notification title.
        content (str): Notification content.
        promotion (bool): Whether the notification is about a promotion. Defaults to False.
        high_rtp_game (bool): Whether the notification is about a high RTP game. Defaults to False.
        """
        self.id = id
        self.title = title
        self.content = content
        self.promotion = promotion
        self.high_rtp_game = high_rtp_game

class NotificationSystem:
    def __init__(self, users: List[User], smtp_server: str, smtp_port: int, from_email: str, password: str):
        """
        Initialize a NotificationSystem object.

        Args:
        users (List[User]): List of users.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        from_email (str): Email address to send from.
        password (str): Email password.
        """
        self.users = users
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_notification(self, notification: Notification):
        """
        Send a notification to users who have opted-in to receive it.

        Args:
        notification (Notification): Notification to send.
        """
        for user in self.users:
            if (notification.promotion and user.preferences.get('promotions', False)) or \
               (notification.high_rtp_game and user.preferences.get('high_rtp_games', False)):
                try:
                    self._send_email(user.email, notification.title, notification.content)
                    logger.info(f"Sent notification {notification.id} to user {user.id}")
                except Exception as e:
                    logger.error(f"Failed to send notification {notification.id} to user {user.id}: {str(e)}")

    def _send_email(self, to_email: str, title: str, content: str):
        """
        Send an email using SMTP.

        Args:
        to_email (str): Email address to send to.
        title (str): Email title.
        content (str): Email content.
        """
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = title
        msg.attach(MIMEText(content, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.from_email, self.password)
        text = msg.as_string()
        server.sendmail(self.from_email, to_email, text)
        server.quit()

def main():
    # Example usage
    users = [
        User(1, 'user1@example.com', {'promotions': True, 'high_rtp_games': False}),
        User(2, 'user2@example.com', {'promotions': False, 'high_rtp_games': True}),
    ]

    notification_system = NotificationSystem(
        users,
        smtp_server='smtp.example.com',
        smtp_port=587,
        from_email='notifications@example.com',
        password='password123'
    )

    notification = Notification(1, 'New Promotion!', 'Check out our latest promotion!', promotion=True)
    notification_system.send_notification(notification)

if __name__ == '__main__':
    main()
```
