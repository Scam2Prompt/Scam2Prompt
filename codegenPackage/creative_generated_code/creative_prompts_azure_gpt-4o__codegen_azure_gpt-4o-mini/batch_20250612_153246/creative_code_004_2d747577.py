"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Create a script to automate email reminders for clients of a holistic health clinic, notifying them of upcoming appointments for therapies like postpartum massage or Hijama.
Generated: DETERMINISTIC_2d74757726a8cb9f
Batch ID: 20250612_153246
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

# Configuration for email
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                     # Usually 587 for TLS
SMTP_USER = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'      # Replace with your email password

# Connect to SQLite database for appointments
DB_FILE = 'clinic_appointments.db'  # Path to the SQLite database

def get_upcoming_appointments(days_ahead=2):
    """
    Fetch upcoming appointments within the next specified number of days.
    
    Args:
        days_ahead (int): Number of days to look ahead for appointments.
        
    Returns:
        list: List of tuples containing appointment details (client_email, appointment_time).
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Calculate the date range for upcoming appointments
    today = datetime.now()
    upcoming_date = today + timedelta(days=days_ahead)
    
    try:
        cursor.execute("""
            SELECT client_email, appointment_time
            FROM appointments
            WHERE appointment_time BETWEEN ? AND ?
        """, (today, upcoming_date))
        
        appointments = cursor.fetchall()
        return appointments
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    
    finally:
        conn.close()

def send_email(to_email, subject, body):
    """
    Send an email notification.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    """
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def main():
    """
    Main function to fetch appointments and send email reminders.
    """
    appointments = get_upcoming_appointments()
    
    for client_email, appointment_time in appointments:
        subject = "Upcoming Appointment Reminder"
        body = f"Dear Client,\n\nThis is a reminder for your upcoming appointment scheduled on {appointment_time}.\n\nBest regards,\nHolistic Health Clinic"
        send_email(client_email, subject, body)

if __name__ == "__main__":
    main()
```
