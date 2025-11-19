"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Write a Python script to manage bookings and appointments for a beauty services company like Style & Makeup Effect, including sending automated reminders and notifications.
Generated: DETERMINISTIC_c3bc2c6098248f7a
Batch ID: 20250622_205548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import sqlite3

# Database setup
DB_NAME = "appointments.db"

def setup_database():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            service TEXT NOT NULL,
            appointment_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Email setup
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"          # Replace with your email password

def send_email(to_email, subject, message):
    """Send an email notification."""
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Appointment management
def add_appointment(customer_name, customer_email, service, appointment_date):
    """Add a new appointment to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (customer_name, customer_email, service, appointment_date)
            VALUES (?, ?, ?, ?)
        """, (customer_name, customer_email, service, appointment_date))
        conn.commit()
        conn.close()
        print("Appointment added successfully.")
    except Exception as e:
        print(f"Error adding appointment: {e}")

def get_upcoming_appointments():
    """Retrieve all upcoming appointments."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT customer_name, customer_email, service, appointment_date
            FROM appointments
            WHERE appointment_date >= ?
        """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))
        appointments = cursor.fetchall()
        conn.close()
        return appointments
    except Exception as e:
        print(f"Error retrieving appointments: {e}")
        return []

def send_reminders():
    """Send reminders for upcoming appointments."""
    appointments = get_upcoming_appointments()
    for appointment in appointments:
        customer_name, customer_email, service, appointment_date = appointment
        appointment_datetime = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M:%S")
        if appointment_datetime - datetime.now() <= timedelta(days=1):  # Reminder for appointments within 24 hours
            subject = "Appointment Reminder"
            message = f"Dear {customer_name},\n\nThis is a reminder for your upcoming {service} appointment on {appointment_date}.\n\nThank you!"
            send_email(customer_email, subject, message)

# Main script
if __name__ == "__main__":
    setup_database()

    # Example usage
    add_appointment("Alice Johnson", "alice@example.com", "Makeup", "2023-10-15 14:00:00")
    add_appointment("Bob Smith", "bob@example.com", "Hair Styling", "2023-10-16 10:00:00")

    print("Upcoming appointments:")
    for appointment in get_upcoming_appointments():
        print(appointment)

    print("Sending reminders...")
    send_reminders()
```
