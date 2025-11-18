"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Write a script to send automated reminders to customers about upcoming cleaning appointments, allowing customization for areas like Falmouth or King George.
Generated: DETERMINISTIC_eda4a38ed5dd2d37
Batch ID: 20250612_153225
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

# Database connection setup
DATABASE = 'appointments.db'

def create_connection():
    """Create a database connection to the SQLite database specified by DATABASE."""
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)
        logging.info("Connection to database established.")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
    return connection

def fetch_upcoming_appointments(connection, days_ahead=3):
    """Fetch upcoming appointments within the next specified number of days."""
    today = datetime.now()
    end_date = today + timedelta(days=days_ahead)
    query = """
    SELECT customer_email, appointment_date, customer_name FROM appointments
    WHERE appointment_date BETWEEN ? AND ?
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (today, end_date))
        return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error fetching upcoming appointments: {e}")
        return []

def send_email(to_email, customer_name, appointment_date):
    """Send an email reminder to the customer about their upcoming appointment."""
    subject = "Reminder: Upcoming Cleaning Appointment"
    body = f"Dear {customer_name},\n\nThis is a reminder for your upcoming cleaning appointment on {appointment_date}.\n\nThank you!"
    
    # Setup the email server and the sender's email configuration
    sender_email = "your_email@example.com"  # Change to your sender email
    sender_password = "your_password"  # Change to your email password
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Change to your SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {to_email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def main():
    """Main function to execute the script logic."""
    connection = create_connection()
    if connection:
        appointments = fetch_upcoming_appointments(connection)
        for email, appointment_date, name in appointments:
            send_email(email, name, appointment_date)
        connection.close()

if __name__ == "__main__":
    main()
```

### Note:
- Be sure to replace placeholders like `your_email@example.com`, `your_password`, and `smtp.example.com` with your actual email configurations.
- Ensure that the database `appointments.db` and the table structure matches the query being executed.
