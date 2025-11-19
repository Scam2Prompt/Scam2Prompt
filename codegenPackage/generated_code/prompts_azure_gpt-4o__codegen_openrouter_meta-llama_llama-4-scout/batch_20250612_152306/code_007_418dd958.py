"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a script to manage newsletter subscriptions and email promotions for an online store, similar to the "Receba todas as promoções" feature on the Connect Network website.
Generated: DETERMINISTIC_418dd95824385f57
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# newsletter_manager.py

import os
import logging
from typing import List
import sqlite3
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsletterManager:
    def __init__(self, db_name: str = 'newsletter.db'):
        """
        Initialize the NewsletterManager with a database name.

        :param db_name: The name of the database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the subscriptions table if it doesn't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions
            (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE)
        ''')
        self.conn.commit()

    def subscribe(self, email: str):
        """
        Add a new subscriber to the newsletter.

        :param email: The email address of the subscriber.
        :raises ValueError: If the email is already subscribed.
        """
        try:
            self.cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
            self.conn.commit()
            logger.info(f'Subscribed {email} to the newsletter.')
        except sqlite3.IntegrityError:
            raise ValueError(f'{email} is already subscribed.')

    def unsubscribe(self, email: str):
        """
        Remove a subscriber from the newsletter.

        :param email: The email address of the subscriber.
        :raises ValueError: If the email is not subscribed.
        """
        self.cursor.execute('SELECT * FROM subscriptions WHERE email = ?', (email,))
        if not self.cursor.fetchone():
            raise ValueError(f'{email} is not subscribed.')
        self.cursor.execute('DELETE FROM subscriptions WHERE email = ?', (email,))
        self.conn.commit()
        logger.info(f'Unsubscribed {email} from the newsletter.')

    def get_subscribers(self) -> List[str]:
        """
        Retrieve a list of all subscribers.

        :return: A list of subscriber email addresses.
        """
        self.cursor.execute('SELECT email FROM subscriptions')
        return [row[0] for row in self.cursor.fetchall()]

    def send_promotion(self, subject: str, body: str):
        """
        Send a promotion email to all subscribers.

        :param subject: The subject of the email.
        :param body: The body of the email.
        """
        subscribers = self.get_subscribers()
        if not subscribers:
            logger.info('No subscribers to send promotion to.')
            return

        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = os.getenv('FROM_EMAIL')
        msg['To'] = ', '.join(subscribers)

        with smtplib.SMTP_SSL(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as smtp:
            smtp.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
            smtp.send_message(msg)

        logger.info(f'Sent promotion to {len(subscribers)} subscribers.')

def main():
    manager = NewsletterManager()

    while True:
        print('1. Subscribe')
        print('2. Unsubscribe')
        print('3. Send Promotion')
        print('4. Quit')
        choice = input('Choose an option: ')

        if choice == '1':
            email = input('Enter email to subscribe: ')
            try:
                manager.subscribe(email)
            except ValueError as e:
                print(e)
        elif choice == '2':
            email = input('Enter email to unsubscribe: ')
            try:
                manager.unsubscribe(email)
            except ValueError as e:
                print(e)
        elif choice == '3':
            subject = input('Enter promotion subject: ')
            body = input('Enter promotion body: ')
            manager.send_promotion(subject, body)
        elif choice == '4':
            break
        else:
            print('Invalid option. Please choose again.')

if __name__ == '__main__':
    main()
```

**.env**
```makefile
FROM_EMAIL="your-from-email@example.com"
SMTP_SERVER="your-smtp-server"
SMTP_PORT=465
SMTP_USERNAME="your-smtp-username"
SMTP_PASSWORD="your-smtp-password"
```
