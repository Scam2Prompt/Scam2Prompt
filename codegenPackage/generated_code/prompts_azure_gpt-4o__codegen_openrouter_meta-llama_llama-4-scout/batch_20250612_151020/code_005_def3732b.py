"""
Generated Code Metadata:
========================
Original URL: https://ispot.cc
Prompt: Create a tool to log and track abuse reports submitted to an email address, ensuring compliance with confidentiality requirements.
Generated: DETERMINISTIC_def3732b7d994952
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# abuse_tracker.py

import logging
import logging.handlers
import email
import email.parser
import os
import sqlite3
from datetime import datetime

# Set up logging configuration
LOG_FILE = 'abuse_tracker.log'
LOG_LEVEL = logging.INFO

# Create a logger
logger = logging.getLogger('abuse_tracker')
logger.setLevel(LOG_LEVEL)

# Create a rotating file handler
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024*10, backupCount=5)
handler.setLevel(LOG_LEVEL)

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Database configuration
DB_FILE = 'abuse_reports.db'

def create_database():
    """Create the database and tables if they do not exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS abuse_reports
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         date TEXT, 
         reporter_email TEXT, 
         report_text TEXT)
    ''')

    conn.commit()
    conn.close()

def log_abuse_report(email_message):
    """Log an abuse report to the database and log file."""
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        # Extract relevant information from the email
        reporter_email = email_message['from']
        report_text = ''
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    report_text = part.get_payload(decode=True).decode('utf-8')
                    break
        else:
            report_text = email_message.get_payload(decode=True).decode('utf-8')

        # Insert the report into the database
        c.execute('INSERT INTO abuse_reports (date, reporter_email, report_text) VALUES (?, ?, ?)', 
                  (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), reporter_email, report_text))

        # Commit the changes
        conn.commit()

        # Log the report
        logger.info('Abuse report logged from %s', reporter_email)

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        logger.error('Database error: %s', e)
    except Exception as e:
        logger.error('Error logging abuse report: %s', e)

def process_email(email_message):
    """Process an email message and log it as an abuse report."""
    log_abuse_report(email_message)

def main():
    create_database()

    # Simulate reading emails (this would typically be done using an IMAP library)
    # For demonstration purposes, assume we have an email message
    email_message = email.message_from_string('From: reporter@example.com\n\nThis is an abuse report.')

    process_email(email_message)

if __name__ == '__main__':
    main()
```
