"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baycarepatientportal.net
Prompt: Write a script that automates the process of sending appointment reminders via email for a healthcare system like BayCare.
Generated: DETERMINISTIC_6d903b96d8697a67
Batch ID: 20250612_162508
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Typical port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Appointment data (In a real scenario, this would be fetched from a database)
appointments = [
    {'patient_name': 'John Doe', 'email': 'john@example.com', 'appointment_date': datetime.now() + timedelta(days=1)},
    {'patient_name': 'Jane Smith', 'email': 'jane@example.com', 'appointment_date': datetime.now() + timedelta(days=2)},
]

def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.
    
    :param to_email: Recipient's email address
    :param subject: Subject line of the email
    :param body: Body of the email
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server using TLS
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {to_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')

def generate_reminder_body(patient_name, appointment_date):
    """
    Generates the body of the reminder email.
    
    :param patient_name: Name of the patient
    :param appointment_date: The date and time of the appointment
    :return: The email body as a string
    """
    return f"Dear {patient_name},\n\nThis is a reminder for your appointment on {appointment_date.strftime('%Y-%m-%d %H:%M')}.\n\nThank you!"

def send_appointment_reminders():
    """
    Iterates through the list of appointments and sends reminders to each patient.
    """
    for appointment in appointments:
        patient_name = appointment['patient_name']
        patient_email = appointment['email']
        appointment_date = appointment['appointment_date']

        # Check if the appointment is within the next 24 hours
        if appointment_date <= datetime.now() + timedelta(days=1):
            subject = 'Appointment Reminder'
            body = generate_reminder_body(patient_name, appointment_date)
            send_email(patient_email, subject, body)
        else:
            logging.info(f"No reminders needed for {patient_name}. Appointment on {appointment_date} is more than 24 hours away.")

if __name__ == "__main__":
    send_appointment_reminders()
```
