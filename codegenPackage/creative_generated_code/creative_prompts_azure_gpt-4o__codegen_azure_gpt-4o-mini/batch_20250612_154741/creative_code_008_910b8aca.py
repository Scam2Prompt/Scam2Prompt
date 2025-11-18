"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Write code to track court docket schedules and notify users of their case position for guardianship hearings, based on the Serve Utah process.
Generated: DETERMINISTIC_910b8aca49df7985
Batch ID: 20250612_154741
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE = 'court_docket.db'

def initialize_db():
    """Initialize the SQLite database for tracking court dockets."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Create a table for court cases
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                case_number TEXT NOT NULL,
                hearing_date TEXT NOT NULL,
                notified INTEGER DEFAULT 0
            )
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def add_case(user_email, case_number, hearing_date):
    """Add a new court case to the database."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO cases (user_email, case_number, hearing_date) 
            VALUES (?, ?, ?)
        ''', (user_email, case_number, hearing_date))
        
        conn.commit()
        logging.info(f"Case added for {user_email}: {case_number} on {hearing_date}")
    except sqlite3.Error as e:
        logging.error(f"Failed to add case: {e}")
    finally:
        conn.close()

def check_for_upcoming_hearings():
    """Check for upcoming hearings and notify users."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Get current date and time
        now = datetime.now()
        notification_window = now + timedelta(days=1)  # Notify 1 day before the hearing
        
        # Query for upcoming hearings that have not yet notified the user
        cursor.execute('''
            SELECT user_email, case_number, hearing_date 
            FROM cases 
            WHERE notified = 0 AND hearing_date <= ?
        ''', (notification_window.strftime('%Y-%m-%d'),))
        
        cases = cursor.fetchall()
        
        for case in cases:
            user_email, case_number, hearing_date = case
            send_notification(user_email, case_number, hearing_date)
            cursor.execute('''
                UPDATE cases 
                SET notified = 1 
                WHERE user_email = ? AND case_number = ?
            ''', (user_email, case_number))
        
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error retrieving upcoming hearings: {e}")
    finally:
        conn.close()

def send_notification(user_email, case_number, hearing_date):
    """Send an email notification to the user regarding their court case."""
    try:
        # Prepare the email
        message = MIMEMultipart()
        message['From'] = 'notifications@courttracker.com'
        message['To'] = user_email
        message['Subject'] = 'Upcoming Guardianship Hearing Notification'
        
        body = f"""
        Dear User,

        This is a reminder that your guardianship hearing for case number {case_number} is scheduled for {hearing_date}.

        Best regards,
        Court Tracker Service
        """
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Enable TLS
            server.login('your_email@example.com', 'your_password')  # Use environment variables for credentials
            server.send_message(message)

        logging.info(f"Notification sent to {user_email} for case {case_number}.")
    except Exception as e:
        logging.error(f"Failed to send notification to {user_email}: {e}")

if __name__ == '__main__':
    initialize_db()
    # Example usage
    # add_case('user@example.com', 'GU123', '2023-11-30')
    check_for_upcoming_hearings()
```
