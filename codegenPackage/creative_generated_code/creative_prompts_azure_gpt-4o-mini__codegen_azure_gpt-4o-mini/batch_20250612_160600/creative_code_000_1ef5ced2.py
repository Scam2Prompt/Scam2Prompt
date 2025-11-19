"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joinnow.info
Prompt: Generate a code snippet for a marketing system that automates follow-ups for referrals in a residual income program similar to Money Order Freedom.
Generated: DETERMINISTIC_1ef5ced251222b2c
Batch ID: 20250612_160600
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

# Database setup
def initialize_database():
    """Create a SQLite database to store referral data."""
    conn = sqlite3.connect('referrals.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            referral_date TEXT NOT NULL,
            follow_up_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a referral
def add_referral(name, email):
    """Insert a new referral into the database."""
    follow_up_date = datetime.now() + timedelta(days=7)  # Follow up in 7 days
    conn = sqlite3.connect('referrals.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO referrals (name, email, referral_date, follow_up_date)
        VALUES (?, ?, ?, ?)
    ''', (name, email, datetime.now().isoformat(), follow_up_date.isoformat()))
    conn.commit()
    conn.close()

# Function to send follow-up emails
def send_follow_up_email(referral):
    """Send a follow-up email to the referral."""
    try:
        msg = MIMEText(f"Hello {referral[1]}, just wanted to follow up on your referral!")
        msg['Subject'] = 'Follow-Up on Your Referral'
        msg['From'] = 'noreply@example.com'
        msg['To'] = referral[2]

        with smtplib.SMTP('smtp.example.com', 587) as server:  # Update SMTP server details
            server.starttls()
            server.login('your_email@example.com', 'password')  # Update login credentials
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email to {referral[2]}: {e}")

# Function to check and send follow-ups
def check_and_send_follow_ups():
    """Check for referrals due for follow-up and send emails."""
    conn = sqlite3.connect('referrals.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM referrals WHERE follow_up_date <= ?', (datetime.now().isoformat(),))
    referrals_due = cursor.fetchall()
    
    for referral in referrals_due:
        send_follow_up_email(referral)
        # Optionally, update follow_up_date or remove the record after sending
        # cursor.execute('DELETE FROM referrals WHERE id = ?', (referral[0],))
    
    conn.commit()
    conn.close()

# Initialize database
initialize_database()

# Example usage
# add_referral('John Doe', 'johndoe@example.com')
# check_and_send_follow_ups()
```
