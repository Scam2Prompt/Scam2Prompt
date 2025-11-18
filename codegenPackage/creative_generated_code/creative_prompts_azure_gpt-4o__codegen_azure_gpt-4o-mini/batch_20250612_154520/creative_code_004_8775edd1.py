"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Create a script to send automated email reminders to plasma donors about upcoming donation appointments using the contact information provided during registration.
Generated: DETERMINISTIC_8775edd15cfdf7fc
Batch ID: 20250612_154520
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

# Database configuration
DB_PATH = 'donors.db'

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Set your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
FROM_EMAIL = 'your_email@example.com'

def get_upcoming_appointments():
    """
    Fetch upcoming donation appointments from the database.
    
    Returns a list of tuples containing donor contact information
    and appointment details.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Get all appointments that are within the next 3 days
        query = """
        SELECT name, email, appointment_date
        FROM donors
        WHERE appointment_date BETWEEN ? AND ?
        """
        today = datetime.now()
        upcoming_date = today + timedelta(days=3)
        cursor.execute(query, (today, upcoming_date))
        appointments = cursor.fetchall()
        logging.info(f"Fetched {len(appointments)} upcoming appointments.")
        return appointments
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def send_email(to_email, donor_name, appointment_date):
    """
    Send an email reminder to the donor about their upcoming appointment.
    
    :param to_email: Recipient email address
    :param donor_name: Name of the donor
    :param appointment_date: Date of the appointment
    """
    try:
        # Set up the email content
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = 'Reminder: Upcoming Plasma Donation Appointment'
        
        body = f"Dear {donor_name},\n\nThis is a reminder for your upcoming plasma donation appointment on {appointment_date}.\n\nThank you for your contribution!"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {donor_name} at {to_email}.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def main():
    """
    Main function to fetch appointments and send reminders.
    """
    appointments = get_upcoming_appointments()
    for name, email, appointment_date in appointments:
        send_email(email, name, appointment_date)

if __name__ == "__main__":
    main()
```
