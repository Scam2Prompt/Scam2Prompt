"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dentistasuzano.com.br
Prompt: Develop a script that sends automated reminders to patients for their dental evaluations at Odontoclinic, incorporating appointment details and contact information.
Generated: DETERMINISTIC_84ab505a322d2aa9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def send_email(to_address, subject, body):
    """Send an email to the specified address."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email sent to {to_address}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_address}: {e}")

def create_reminder(patient_name, appointment_date, contact_info):
    """Create a reminder message for the patient."""
    return (f"Dear {patient_name},\n\n"
            f"This is a friendly reminder for your dental evaluation appointment at Odontoclinic.\n"
            f"Appointment Date: {appointment_date.strftime('%Y-%m-%d %H:%M')}\n\n"
            f"If you have any questions, feel free to contact us at {contact_info}.\n\n"
            f"Best regards,\n"
            f"Odontoclinic Team")

def schedule_reminders(patients):
    """Schedule reminders for each patient in the provided list."""
    for patient in patients:
        patient_name = patient['name']
        appointment_date = patient['appointment_date']
        contact_info = patient['contact_info']
        
        # Calculate the reminder date (2 days before the appointment)
        reminder_date = appointment_date - timedelta(days=2)

        # Send reminder if today is the reminder date
        if datetime.now().date() == reminder_date.date():
            reminder_message = create_reminder(patient_name, appointment_date, contact_info)
            send_email(patient['email'], "Dental Evaluation Reminder", reminder_message)

# Example patient data
patients_info = [
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'appointment_date': datetime(2023, 11, 15, 10, 30),
        'contact_info': 'contact@odontoclinic.com'
    },
    {
        'name': 'Jane Smith',
        'email': 'janesmith@example.com',
        'appointment_date': datetime(2023, 11, 20, 11, 00),
        'contact_info': 'contact@odontoclinic.com'
    }
]

# Schedule reminders
schedule_reminders(patients_info)
```
