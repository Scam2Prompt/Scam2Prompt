"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Write Python code to automate email reminders for dental appointments, including details like the service type (e.g., root canal, teeth whitening) and clinic location (e.g., Mission, San Juan).
Generated: DETERMINISTIC_e8dab0cf78104640
Batch ID: 20250612_152710
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'    # Replace with your email password

# Function to send email reminders
def send_email_reminder(recipient_email, appointment_date, service_type, clinic_location):
    """
    Sends an email reminder for a dental appointment.
    
    Args:
        recipient_email (str): Patient's email address.
        appointment_date (str): Date and time of the appointment (format: 'YYYY-MM-DD HH:MM').
        service_type (str): Type of dental service (e.g., "Root Canal", "Teeth Whitening").
        clinic_location (str): Clinic location (e.g., "Mission", "San Juan").
    """
    try:
        # Create the email content
        subject = "Dental Appointment Reminder"
        body = f"""
        Dear Patient,

        This is a friendly reminder for your upcoming dental appointment:
        
        Service Type: {service_type}
        Clinic Location: {clinic_location}
        Appointment Date: {appointment_date}
        
        Please arrive 15 minutes early. If you need to reschedule, contact us at least 24 hours in advance.

        Best regards,
        Your Dental Clinic
        """

        # Set up the email message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)

        logging.info(f"Email successfully sent to {recipient_email} for appointment on {appointment_date}.")
    
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Example appointment data
    appointments = [
        {
            'recipient_email': 'patient1@example.com',
            'appointment_date': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d %H:%M'),
            'service_type': 'Root Canal',
            'clinic_location': 'Mission'
        },
        {
            'recipient_email': 'patient2@example.com',
            'appointment_date': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d %H:%M'),
            'service_type': 'Teeth Whitening',
            'clinic_location': 'San Juan'
        }
    ]

    # Send reminders for all appointments
    for appointment in appointments:
        send_email_reminder(
            recipient_email=appointment['recipient_email'],
            appointment_date=appointment['appointment_date'],
            service_type=appointment['service_type'],
            clinic_location=appointment['clinic_location']
        )
```
