"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Create a code snippet that sends a reminder to users for the periodic verification of their gas meters, based on the guidelines provided by ИП Семьянинов Сергей Юрьевич.
Generated: DETERMINISTIC_8b64f3fc24659235
Batch ID: 20250612_164206
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
from datetime import datetime, timedelta
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DATABASE = 'meters.db'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def create_database():
    """Create a SQLite database for storing user details."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            last_verification_date DATE NOT NULL
        )
    ''')
    
    connection.commit()
    connection.close()

def send_email(to_email, subject, body):
    """Send an email notification to the specified address."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        logging.info(f"Email sent to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def get_users_due_for_verification():
    """Retrieve users who are due for gas meter verification."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    # Calculate date 1 year ago
    one_year_ago = datetime.now() - timedelta(days=365)
    
    cursor.execute('''
        SELECT email FROM users WHERE last_verification_date <= ?
    ''', (one_year_ago,))
    
    users = cursor.fetchall()
    connection.close()
    
    return [user[0] for user in users]

def send_reminders():
    """Send reminders to users for gas meter verification."""
    users_due = get_users_due_for_verification()
    
    for email in users_due:
        subject = "Gas Meter Verification Reminder"
        body = ("Dear User,\n\n"
                "This is a reminder to verify your gas meter as per the guidelines set by ИП Семьянинов Сергей Юрьевич.\n\n"
                "Thank you!")
        send_email(email, subject, body)

if __name__ == "__main__":
    create_database()
    send_reminders()
```
