"""
Generated Code Metadata:
========================
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Create a Python script that sends notifications about limited-time offers for best friends when they log in to the website.
Generated: DETERMINISTIC_3c80bb6326b63a7f
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notification_service.py

import logging
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationService:
    def __init__(self, db_name, smtp_server, smtp_port, from_email, password):
        """
        Initialize the notification service.

        Args:
        - db_name (str): Name of the SQLite database file.
        - smtp_server (str): SMTP server address.
        - smtp_port (int): SMTP server port.
        - from_email (str): Email address of the sender.
        - password (str): Password of the sender's email account.
        """
        self.db_name = db_name
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def _connect_to_db(self):
        """
        Establish a connection to the SQLite database.

        Returns:
        - conn (sqlite3.Connection): Connection object.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            logger.error(f"Failed to connect to database: {e}")
            return None

    def _get_best_friends(self):
        """
        Retrieve best friends from the database.

        Returns:
        - best_friends (list): List of best friends' email addresses.
        """
        conn = self._connect_to_db()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM users WHERE is_best_friend = 1")
            best_friends = [row[0] for row in cursor.fetchall()]
            conn.close()
            return best_friends
        except sqlite3.Error as e:
            logger.error(f"Failed to retrieve best friends: {e}")
            conn.close()
            return []

    def _send_notification(self, to_email, subject, body):
        """
        Send a notification email.

        Args:
        - to_email (str): Email address of the recipient.
        - subject (str): Subject of the email.
        - body (str): Body of the email.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send notification: {e}")

    def send_limited_time_offer_notifications(self):
        """
        Send notifications about limited-time offers to best friends.
        """
        best_friends = self._get_best_friends()
        subject = "Limited Time Offer: Exclusive Deal for Best Friends"

        # Assuming the offer is valid for 24 hours
        offer_valid_until = datetime.now() + timedelta(hours=24)
        body = f"Dear Best Friend,\n\nWe have an exclusive deal for you! This offer is valid until {offer_valid_until.strftime('%Y-%m-%d %H:%M:%S')}.\n\nPlease log in to our website to redeem your offer.\n\nBest regards,"

        for best_friend in best_friends:
            self._send_notification(best_friend, subject, body)


if __name__ == "__main__":
    db_name = "users.db"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "your-email@gmail.com"
    password = "your-password"

    notification_service = NotificationService(db_name, smtp_server, smtp_port, from_email, password)
    notification_service.send_limited_time_offer_notifications()
```
