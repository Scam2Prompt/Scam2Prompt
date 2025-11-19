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
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime, timedelta

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_USER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Constants for referral follow-up
FOLLOW_UP_INTERVAL_DAYS = 3  # Number of days between follow-ups

def send_email(to_email, subject, message):
    """
    Sends an email to the specified recipient.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message (str): Email body content.

    Raises:
        Exception: If email sending fails.
    """
    try:
        # Create email object
        email = MIMEMultipart()
        email['From'] = EMAIL_USER
        email['To'] = to_email
        email['Subject'] = subject

        # Attach the message content
        email.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(email)

        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def get_pending_followups():
    """
    Retrieves pending follow-ups from the database.

    Returns:
        list: List of referrals needing follow-up.
    """
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('referrals.db')
        cursor = conn.cursor()

        # Query referrals needing follow-up
        query = """
        SELECT id, name, email, last_followup_date
        FROM referrals
        WHERE datetime(last_followup_date) <= datetime('now', '-{interval} days')
        """.format(interval=FOLLOW_UP_INTERVAL_DAYS)
        cursor.execute(query)
        
        # Fetch results
        referrals = cursor.fetchall()
        conn.close()

        return referrals
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def update_followup_date(referral_id):
    """
    Updates the last follow-up date for a referral.

    Args:
        referral_id (int): ID of the referral to update.
    """
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('referrals.db')
        cursor = conn.cursor()

        # Update last follow-up date
        query = "UPDATE referrals SET last_followup_date = ? WHERE id = ?"
        cursor.execute(query, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), referral_id))
        conn.commit()
        conn.close()

        print(f"Follow-up date updated for referral ID: {referral_id}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def automate_followups():
    """
    Automates the follow-up process for referrals.
    """
    referrals = get_pending_followups()

    for referral in referrals:
        referral_id, name, email, last_followup_date = referral

        # Generate follow-up message
        subject = "Follow-Up: Residual Income Opportunity"
        message = f"Hi {name},\n\nWe hope you're making progress! Let us know if you have any questions.\n\nBest regards,\nMarketing Team"

        # Send email and update the database
        send_email(email, subject, message)
        update_followup_date(referral_id)

if __name__ == '__main__':
    # Automate the process
    automate_followups()
```

**Dependencies:**
- Ensure the `sqlite3` database (`referrals.db`) has a table named `referrals` with columns: `id`, `name`, `email`, and `last_followup_date`.
- Install Python's `smtplib` for email functionality.
