"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Recommend libraries or APIs to build a WhatsApp-based scheduling system for sending reminders and managing consultations, similar to the solution provided by Invicta Cobranças.
Generated: DETERMINISTIC_97f43ff2df70e3b8
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to set up a WhatsApp-based scheduling system for sending reminders
and managing consultations using Twilio's API for WhatsApp. Twilio supports WhatsApp Business
Messaging and allows sending automated messages. Note: Ensure you have a WhatsApp Business Account
and Twilio credentials for this to work.

Dependencies:
1. Twilio Python library (`pip install twilio`)
2. A database library like SQLite or SQLAlchemy for scheduling storage.
"""

from twilio.rest import Client
import sqlite3
import datetime

# Twilio credentials
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio WhatsApp sandbox number or your verified number

# Initialize Twilio Client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Database setup
DB_FILE = 'scheduling.db'

def setup_database():
    """
    Set up SQLite database for storing reminders and consultations.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT NOT NULL,
            message TEXT NOT NULL,
            schedule_time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def schedule_reminder(phone_number, message, schedule_time):
    """
    Store a reminder in the database.
    Args:
        phone_number (str): Recipient's WhatsApp number in the format "whatsapp:+<country_code><number>"
        message (str): Reminder message content
        schedule_time (datetime): Time to send the reminder
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reminders (phone_number, message, schedule_time) VALUES (?, ?, ?)',
                   (phone_number, message, schedule_time.strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def send_reminder(phone_number, message):
    """
    Send a reminder via WhatsApp using Twilio API.
    Args:
        phone_number (str): Recipient's WhatsApp number
        message (str): Reminder message content
    """
    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=phone_number
        )
        print(f"Message sent! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

def check_and_send_reminders():
    """
    Check the database for reminders that are due and send them.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('SELECT id, phone_number, message FROM reminders WHERE schedule_time <= ?', (now,))
    reminders = cursor.fetchall()

    for reminder in reminders:
        reminder_id, phone_number, message = reminder
        send_reminder(phone_number, message)
        # Remove the sent reminder from the database
        cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder_id,))
    
    conn.commit()
    conn.close()

# Initialize the database
setup_database()

# Example usage
if __name__ == "__main__":
    # Schedule a reminder
    phone_number = "whatsapp:+1234567890"  # Replace with recipient's number
    message = "Reminder: Your consultation is scheduled at 3 PM today."
    schedule_time = datetime.datetime.now() + datetime.timedelta(minutes=1)  # 1 minute from now
    schedule_reminder(phone_number, message, schedule_time)

    # Simulate a job that periodically checks for due reminders
    import time
    while True:
        check_and_send_reminders()
        time.sleep(60)  # Wait for 1 minute before checking again
```

### Notes:
1. Replace the Twilio credentials with your actual account SID, auth token, and WhatsApp number.
2. Use a job scheduler like `cron` or a task queue like Celery for periodic execution in production.
3. Ensure that you comply with WhatsApp Business policies and privacy regulations.
