"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: How can I implement a notification system for updates on SST regulations and best practices, similar to the collaborative efforts of the AFCO regional coordinators?
Generated: DETERMINISTIC_a03cd86c46ba1d01
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notification_system.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from typing import List

class NotificationSystem:
    def __init__(self, db_name: str, smtp_server: str, smtp_port: int, from_email: str, password: str):
        """
        Initialize the notification system.

        Args:
        - db_name (str): The name of the SQLite database file.
        - smtp_server (str): The SMTP server to use for sending emails.
        - smtp_port (int): The port to use for the SMTP server.
        - from_email (str): The email address to use as the sender.
        - password (str): The password for the sender's email account.
        """
        self.db_name = db_name
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the subscribers table if it doesn't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers
            (id INTEGER PRIMARY KEY, email TEXT UNIQUE)
        ''')
        self.conn.commit()

    def add_subscriber(self, email: str):
        """
        Add a new subscriber to the notification system.

        Args:
        - email (str): The email address of the subscriber.
        """
        try:
            self.cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Subscriber {email} already exists.")

    def remove_subscriber(self, email: str):
        """
        Remove a subscriber from the notification system.

        Args:
        - email (str): The email address of the subscriber.
        """
        self.cursor.execute('DELETE FROM subscribers WHERE email = ?', (email,))
        self.conn.commit()

    def send_notification(self, subject: str, message: str):
        """
        Send a notification to all subscribers.

        Args:
        - subject (str): The subject of the email.
        - message (str): The body of the email.
        """
        self.cursor.execute('SELECT email FROM subscribers')
        subscribers: List[str] = [row[0] for row in self.cursor.fetchall()]
        
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.from_email, self.password)

        for subscriber in subscribers:
            msg['To'] = subscriber
            text = msg.as_string()
            server.sendmail(self.from_email, subscriber, text)

        server.quit()

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db_name = 'notification.db'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your-email@gmail.com'
    password = 'your-password'

    notification_system = NotificationSystem(db_name, smtp_server, smtp_port, from_email, password)

    while True:
        print("\n1. Add subscriber")
        print("2. Remove subscriber")
        print("3. Send notification")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            email = input("Enter subscriber's email: ")
            notification_system.add_subscriber(email)
        elif choice == '2':
            email = input("Enter subscriber's email: ")
            notification_system.remove_subscriber(email)
        elif choice == '3':
            subject = input("Enter notification subject: ")
            message = input("Enter notification message: ")
            notification_system.send_notification(subject, message)
        elif choice == '4':
            notification_system.close_connection()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
