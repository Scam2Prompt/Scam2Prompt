"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Develop a script that triggers a callback request for users who fill out the form, ensuring they are contacted within a month, as described on the Proximus client site.
Generated: DETERMINISTIC_46d8840a69cc8965
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup
DB_NAME = 'proximus.db'

def initialize_database():
    """
    Initializes the database to store form submissions.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create a table for submissions if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS form_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            submission_date TEXT NOT NULL,
            callback_due_date TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def store_submission(name, email, phone):
    """
    Stores the user's form submission in the database.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Calculate callback due date (30 days from today)
    submission_date = datetime.now()
    callback_due_date = submission_date + timedelta(days=30)
    
    cursor.execute('''
        INSERT INTO form_submissions (name, email, phone, submission_date, callback_due_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, phone, submission_date.strftime('%Y-%m-%d'), callback_due_date.strftime('%Y-%m-%d')))
    
    connection.commit()
    connection.close()

def send_callback_email(to_email, name):
    """
    Sends a callback email notification to the user.
    """
    try:
        # Email server configuration
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'your_email@example.com'
        smtp_password = 'your_password'

        # Create email
        message = MIMEMultipart()
        message['From'] = smtp_username
        message['To'] = to_email
        message['Subject'] = 'Callback Scheduled'
        
        email_body = f"Dear {name},\n\nThank you for your submission. " \
                     f"Our team will contact you within the next 30 days.\n\nBest regards,\nProximus Team"
        
        message.attach(MIMEText(email_body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        server.quit()
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def process_form_submission(name, email, phone):
    """
    Processes a form submission: stores the data and sends a callback email.
    """
    try:
        store_submission(name, email, phone)
        send_callback_email(email, name)
    except Exception as e:
        print(f"Error processing form submission: {e}")

# Initialize database
initialize_database()

# Example form submission
process_form_submission('John Doe', 'johndoe@example.com', '123-456-7890')
```
