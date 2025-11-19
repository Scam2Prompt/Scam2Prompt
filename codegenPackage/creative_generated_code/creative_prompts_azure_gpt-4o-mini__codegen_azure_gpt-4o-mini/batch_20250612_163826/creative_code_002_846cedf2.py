"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a Python script that sends reminders for training sessions and events to members of a running club, inspired by the communication style of Thompson Estate Athletics.
Generated: DETERMINISTIC_846cedf2d28cdaf7
Batch ID: 20250612_163826
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

# Database setup (SQLite in this example)
DATABASE = 'running_club.db'

def setup_database():
    """Sets up the database for storing member information and events."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      email TEXT NOT NULL UNIQUE)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                      id INTEGER PRIMARY KEY,
                      event_name TEXT NOT NULL,
                      event_date TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def send_email(to_email, subject, body):
    """Sends an email to the specified address with a given subject and body."""
    try:
        sender_email = "your_email@example.com"
        sender_password = "your_password"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        logging.info(f"Email sent to {to_email} with subject: {subject}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}. Error: {str(e)}")

def fetch_upcoming_events():
    """Fetches upcoming events from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT event_name, event_date FROM events WHERE event_date >= ?", (datetime.now().isoformat(),))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_members():
    """Fetches all members from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM members")
    members = cursor.fetchall()
    conn.close()
    return members

def send_reminders():
    """Sends reminders for upcoming events to all club members."""
    upcoming_events = fetch_upcoming_events()
    members = fetch_members()

    for event_name, event_date in upcoming_events:
        for member_name, member_email in members:
            subject = f"Reminder: Upcoming Event - {event_name}"
            body = f"Dear {member_name},\n\nThis is a friendly reminder for the upcoming event: {event_name} on {event_date}.\n\nSee you there!\n\nBest,\nThompson Estate Athletics"
            send_email(member_email, subject, body)

if __name__ == "__main__":
    # Set up the database if it is not already set up
    setup_database()
    
    # Send reminders for upcoming events
    send_reminders()
```
