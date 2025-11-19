"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordoflifenw.com
Prompt: Write a Python script that sends automated reminders for church events, inspired by the event management practices at Word of Life Northwest.
Generated: DETERMINISTIC_74f15d7c2861e1b5
Batch ID: 20250612_162203
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

# Constants for email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_SENDER = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'         # Replace with your email password

# Database configuration (SQLite for simplicity)
DB_NAME = 'church_events.db'

# Set up database for event storage
def setup_database():
    """
    Sets up the SQLite database with the required table for events.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Add a new event to the database
def add_event(name, date, time, email):
    """
    Adds a new event to the database.
    :param name: Event name
    :param date: Event date in YYYY-MM-DD format
    :param time: Event time in HH:MM format
    :param email: Recipient email for reminders
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO events (name, date, time, email)
        VALUES (?, ?, ?, ?)
    ''', (name, date, time, email))
    connection.commit()
    connection.close()

# Fetch all events that require reminders
def fetch_upcoming_events():
    """
    Retrieves events happening within the next 24 hours.
    :return: List of event dictionaries
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    now = datetime.now()
    next_24_hours = now + timedelta(hours=24)
    cursor.execute('''
        SELECT name, date, time, email 
        FROM events 
        WHERE datetime(date || ' ' || time) BETWEEN ? AND ?
    ''', (now.strftime('%Y-%m-%d %H:%M:%S'), next_24_hours.strftime('%Y-%m-%d %H:%M:%S')))
    events = cursor.fetchall()
    connection.close()
    return [{'name': e[0], 'date': e[1], 'time': e[2], 'email': e[3]} for e in events]

# Send email reminder
def send_email(recipient, subject, body):
    """
    Sends an email reminder to the specified recipient.
    :param recipient: Recipient email address
    :param subject: Email subject
    :param body: Email body content
    """
    try:
        # Create email message
        message = MIMEMultipart()
        message['From'] = EMAIL_SENDER
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
        print(f"Reminder sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Main function for sending reminders
def send_reminders():
    """
    Sends automated reminders for upcoming church events.
    """
    events = fetch_upcoming_events()
    for event in events:
        subject = f"Reminder: {event['name']} at {event['time']} on {event['date']}"
        body = f"Dear attendee,\n\nThis is a reminder for the upcoming event:\n\nEvent: {event['name']}\nDate: {event['date']}\nTime: {event['time']}\n\nWe look forward to seeing you!\n\nBlessings,\nWord of Life Northwest"
        send_email(event['email'], subject, body)

if __name__ == "__main__":
    # Ensure the database is set up
    setup_database()

    # Add sample events (comment out in production)
    # add_event("Sunday Service", "2023-11-05", "09:00", "attendee1@example.com")
    # add_event("Youth Fellowship", "2023-11-05", "18:00", "attendee2@example.com")

    # Send reminders for upcoming events
    send_reminders()
```

Note: Replace `your_email@example.com` and `your_password` with your actual email credentials for testing. Ensure that your email account has "less secure app access" enabled if using Gmail, or set up OAuth2 for enhanced security in production.
