"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write a script that sends reminders to clients about their upcoming legal consultations, similar to the booking system mentioned on the Juridisk Klinik site.
Generated: DETERMINISTIC_5b81ba097b675fea
Batch ID: 20250612_160853
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
from datetime import datetime, timedelta
import sqlite3

# Database configuration
DB_PATH = 'consultations.db'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
FROM_EMAIL = 'your_email@example.com'
SUBJECT = 'Reminder: Upcoming Legal Consultation'

def create_database():
    """Create a SQLite database for consultations if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consultations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_email TEXT NOT NULL,
                consultation_date TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_upcoming_consultations():
    """Fetch consultations scheduled within the next 3 days."""
    upcoming_date = datetime.now() + timedelta(days=3)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT client_email, consultation_date 
            FROM consultations 
            WHERE consultation_date <= ?
        ''', (upcoming_date.strftime('%Y-%m-%d %H:%M:%S'),))
        return cursor.fetchall()

def send_email(to_email, message):
    """Send an email reminder to the specified address."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = SUBJECT
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print(f'Reminder email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email to {to_email}: {e}')

def send_reminders():
    """Send reminders to clients about their upcoming consultations."""
    consultations = get_upcoming_consultations()
    
    for email, date in consultations:
        message = f'Dear Client,\n\nThis is a reminder for your upcoming legal consultation scheduled on {date}.\n\nBest regards,\nYour Legal Team'
        send_email(email, message)

if __name__ == '__main__':
    create_database()  # Ensure the database is created
    send_reminders()    # Send reminders to clients
```
