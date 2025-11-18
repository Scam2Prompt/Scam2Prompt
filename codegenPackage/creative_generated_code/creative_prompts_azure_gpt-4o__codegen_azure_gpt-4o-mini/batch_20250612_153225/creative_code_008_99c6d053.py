"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Write a script to subscribe users to the Études newsletter, ensuring they receive updates on architectural articles and case studies.
Generated: DETERMINISTIC_99c6d0536c2ba0a6
Batch ID: 20250612_153225
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

# Database configuration
DATABASE = 'newsletter_subscribers.db'

def create_database():
    """Create a SQLite database to store subscribers."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def add_subscriber(email):
    """Add a new subscriber to the database."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        logging.info(f"Subscriber {email} added successfully.")
    except sqlite3.IntegrityError:
        logging.warning(f"Subscriber with email {email} already exists.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def send_confirmation_email(email):
    """Send a confirmation email to the new subscriber."""
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        subject = "Subscription Confirmed"
        body = f"Thank you for subscribing to the Études newsletter, {email}! You will now receive updates on architectural articles and case studies."

        # Set up the email server
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        logging.info(f"Confirmation email sent to {email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {email}: {e}")

def subscribe_user(email):
    """Subscribe a user to the newsletter."""
    if validate_email(email):
        add_subscriber(email)
        send_confirmation_email(email)
    else:
        logging.error(f"Invalid email address: {email}")

def validate_email(email):
    """Validate the email format."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

if __name__ == '__main__':
    create_database()
    user_email = input("Enter your email to subscribe to the Études newsletter: ")
    subscribe_user(user_email)
```
