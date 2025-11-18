"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a script to manage newsletter subscriptions and email promotions for an online store, similar to the "Receba todas as promoções" feature on the Connect Network website.
Generated: DETERMINISTIC_418dd95824385f57
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database setup
DB_NAME = 'subscriptions.db'

def create_database():
    """Create a SQLite database to store newsletter subscriptions."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            subscribed INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

def subscribe(email):
    """Subscribe a user to the newsletter."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
        conn.commit()
        print(f'Successfully subscribed {email}.')
    except sqlite3.IntegrityError:
        print(f'Email {email} is already subscribed.')
    finally:
        conn.close()

def unsubscribe(email):
    """Unsubscribe a user from the newsletter."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE subscriptions SET subscribed = 0 WHERE email = ?', (email,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f'Successfully unsubscribed {email}.')
    else:
        print(f'Email {email} was not found in the subscription list.')
    conn.close()

def send_promotions():
    """Send promotional emails to all subscribed users."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM subscriptions WHERE subscribed = 1')
    subscribers = cursor.fetchall()
    conn.close()

    # Email setup
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    subject = "Exclusive Promotions from Our Online Store"
    body = "Hello! Check out our exclusive promotions just for you!"

    # Initialize SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            for (email,) in subscribers:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server.send_message(msg)
                print(f'Promotional email sent to {email}.')
    except Exception as e:
        print(f'Failed to send email: {e}')

def main():
    """Main function to run the subscription management script."""
    create_database()
    while True:
        action = input("Choose an action: (1) Subscribe (2) Unsubscribe (3) Send Promotions (4) Exit: ")
        if action == '1':
            email = input("Enter your email to subscribe: ")
            subscribe(email)
        elif action == '2':
            email = input("Enter your email to unsubscribe: ")
            unsubscribe(email)
        elif action == '3':
            send_promotions()
        elif action == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Environment Variables
To use this script, ensure you have a `.env` file with the following variables:
```
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_email_password
```

### Requirements
Make sure to install the required libraries:
```
pip install python-dotenv
```
