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
import datetime
import sqlite3

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS, or 465 for SSL
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
DATABASE_PATH = "appointments.db"  # Path to SQLite database

def send_email(to_email, client_name, appointment_date, therapy_type):
    """
    Sends an email reminder to the client about their upcoming appointment.

    Args:
        to_email (str): Recipient email address.
        client_name (str): Name of the client.
        appointment_date (datetime.date): Appointment date.
        therapy_type (str): Type of therapy the appointment is for.
    """
    try:
        # Create the email content
        subject = "Upcoming Appointment Reminder"
        body = (f"Dear {client_name},\n\n"
                f"This is a reminder for your upcoming appointment:\n\n"
                f"Therapy Type: {therapy_type}\n"
                f"Date: {appointment_date.strftime('%A, %B %d, %Y')}\n\n"
                f"We look forward to seeing you!\n\n"
                f"Best regards,\nHolistic Health Clinic")

        # Construct email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email successfully sent to {to_email}.")
    
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

def get_upcoming_appointments():
    """
    Retrieves appointments from the database that are scheduled for the next day.

    Returns:
        list of dict: A list of upcoming appointments with client details.
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

        # SQL query to retrieve appointments for the next day
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        query = """
        SELECT client_name, email, appointment_date, therapy_type
        FROM appointments
        WHERE appointment_date = ?;
        """
        cursor.execute(query, (tomorrow,))
        appointments = cursor.fetchall()

        # Convert query results to a list of dictionaries
        result = []
        for row in appointments:
            result.append({
                "client_name": row[0],
                "email": row[1],
                "appointment_date": datetime.datetime.strptime(row[2], '%Y-%m-%d').date(),
                "therapy_type": row[3]
            })

        return result
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        if connection:
            connection.close()

def main():
    """
    Main function to send email reminders for upcoming appointments.
    """
    print("Fetching upcoming appointments...")
    appointments = get_upcoming_appointments()

    if not appointments:
        print("No upcoming appointments found.")
        return

    print(f"Found {len(appointments)} upcoming appointment(s). Sending email reminders...")
    for appointment in appointments:
        send_email(
            to_email=appointment['email'],
            client_name=appointment['client_name'],
            appointment_date=appointment['appointment_date'],
            therapy_type=appointment['therapy_type']
        )

if __name__ == "__main__":
    main()
```

**Note:** Replace the placeholder values (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `SMTP_SERVER`, etc.) with actual production credentials and ensure environment security practices are followed when handling sensitive information like email credentials.
