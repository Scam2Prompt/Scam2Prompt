"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Generate a Python script to automate email subscription management for a digital agency, inspired by the subscription feature mentioned on digistrategy.in.
Generated: DETERMINISTIC_7cb61cac0d6f7605
Batch ID: 20250612_153224
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
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database helper class for managing subscriptions
class SubscriptionManager:
    def __init__(self, db_name='subscriptions.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Create a subscriptions table if it doesn't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS subscriptions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL
                )
            ''')
            conn.commit()

    def add_subscription(self, email):
        """Add a new email subscription."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
                conn.commit()
                logging.info(f'Successfully subscribed: {email}')
        except sqlite3.IntegrityError:
            logging.warning(f'Email already subscribed: {email}')
        except Exception as e:
            logging.error(f'Error adding subscription: {e}')

    def remove_subscription(self, email):
        """Remove an email subscription."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM subscriptions WHERE email = ?', (email,))
            conn.commit()
            if cursor.rowcount > 0:
                logging.info(f'Successfully unsubscribed: {email}')
            else:
                logging.warning(f'Email not found in subscriptions: {email}')

    def list_subscriptions(self):
        """List all subscriptions."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT email FROM subscriptions')
            return [row[0] for row in cursor.fetchall()]

# Email sending function
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    """Send an email with the specified parameters."""
    try:
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(login, password)
            server.send_message(message)
            logging.info(f'Email sent to {to_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')

# Main function to manage subscriptions and send notifications
def main():
    # Initialize subscription manager
    manager = SubscriptionManager()

    # Simulating adding a new subscription
    email_to_subscribe = 'user@example.com'
    manager.add_subscription(email_to_subscribe)

    # Simulating sending an email notification
    email_subject = 'Welcome to Our Newsletter!'
    email_body = 'Thank you for subscribing to our newsletter!'
    smtp_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'login': 'your_email@example.com',
        'password': 'your_password'
    }
    
    send_email(
        subject=email_subject,
        body=email_body,
        to_email=email_to_subscribe,
        from_email=smtp_config['login'],
        smtp_server=smtp_config['smtp_server'],
        smtp_port=smtp_config['smtp_port'],
        login=smtp_config['login'],
        password=smtp_config['password']
    )

if __name__ == '__main__':
    main()
```
