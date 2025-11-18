"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Write code to send automated reminders for medical appointments, tailored to Grupo Clínico IDET's operating hours and patient contact methods.
Generated: DETERMINISTIC_1c34294cfdeede21
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for Grupo Clínico IDET operating hours
OPERATING_HOURS_START = 9  # 9:00 AM
OPERATING_HOURS_END = 18  # 6:00 PM

# SMTP server configuration (example, replace with actual data)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_password"

# Function to check if the reminder falls within operating hours
def is_within_operating_hours(reminder_time):
    return OPERATING_HOURS_START <= reminder_time.hour < OPERATING_HOURS_END

# Function to send email reminders
def send_email_reminder(patient_email, patient_name, appointment_time):
    try:
        # Set up the email content
        subject = "Reminder: Upcoming Medical Appointment"
        body = f"Dear {patient_name},\n\nThis is a reminder for your medical appointment scheduled on {appointment_time.strftime('%A, %d %B %Y at %I:%M %p')}.\n\nThank you,\nGrupo Clínico IDET"
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = patient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Initiate connection to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure connection
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, patient_email, msg.as_string())
        server.quit()
        
        print(f"Reminder email sent successfully to {patient_email}")
    except Exception as e:
        print(f"Error sending email to {patient_email}: {e}")

# Function to send reminders based on patient data
def send_reminders(patient_data):
    """
    patient_data format:
    [
        {"name": "John Doe", "email": "johndoe@example.com", "appointment_time": datetime_object},
        ...
    ]
    """
    for patient in patient_data:
        appointment_time = patient['appointment_time']
        reminder_time = appointment_time - timedelta(hours=24)  # Send reminder 24 hours before the appointment
        
        # Check if reminder time is within operating hours
        if is_within_operating_hours(reminder_time):
            # Send the email reminder
            send_email_reminder(patient['email'], patient['name'], appointment_time)
        else:
            print(f"Reminder for {patient['name']} falls outside operating hours and was not sent.")

# Example patient data
patient_data = [
    {"name": "Alice Smith", "email": "alice@example.com", "appointment_time": datetime(2023, 11, 22, 10, 0)},
    {"name": "Bob Johnson", "email": "bob@example.com", "appointment_time": datetime(2023, 11, 22, 17, 0)},
]

# Send reminders
send_reminders(patient_data)
```
