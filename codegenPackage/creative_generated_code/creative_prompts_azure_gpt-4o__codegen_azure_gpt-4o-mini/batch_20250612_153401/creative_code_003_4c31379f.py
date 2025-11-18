"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Suggest tools or frameworks to develop a subscription-based notification system for exam preparation updates, as highlighted in Educar Comitán's "Suscríbete" section.
Generated: DETERMINISTIC_4c31379f99dd4371
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_service.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from sqlite3 import Error

class SubscriptionService:
    """
    A class to handle the subscription management and notification system
    for exam preparation updates.
    """

    def __init__(self, db_file: str):
        """Initialize the SubscriptionService with a database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def subscribe_user(self, email: str) -> bool:
        """Subscribe a user by adding their email to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
            self.connection.commit()
            print(f"User {email} subscribed successfully.")
            return True
        except Error as e:
            print(f"Error subscribing user: {e}")
            return False

    def unsubscribe_user(self, email: str) -> bool:
        """Unsubscribe a user by removing their email from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
            self.connection.commit()
            print(f"User {email} unsubscribed successfully.")
            return True
        except Error as e:
            print(f"Error unsubscribing user: {e}")
            return False

    def send_notification(self, subject: str, message: str) -> None:
        """Send notification to all subscribed users."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT email FROM subscribers")
        subscribers = cursor.fetchall()

        for subscriber in subscribers:
            email = subscriber[0]
            self.send_email(email, subject, message)

    def send_email(self, to_email: str, subject: str, message: str) -> None:
        """Send an email to a specified address."""
        from_email = "your_email@example.com"
        password = "your_email_password"

        try:
            # Set up the email server
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login(from_email, password)

            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send the email
            server.send_message(msg)
            print(f"Notification sent to {to_email}")
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")
        finally:
            server.quit()

# Example Usage
if __name__ == "__main__":
    db_path = "subscriptions.db"
    
    # Create table if it doesn't exist
    conn = sqlite3.connect(db_path)
    conn.execute('''CREATE TABLE IF NOT EXISTS subscribers (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE);''')
    conn.close()

    service = SubscriptionService(db_path)

    # Subscribe a user
    service.subscribe_user("test_user@example.com")

    # Send a notification
    service.send_notification("Exam Update", "New exam preparation resources are available!")
```
