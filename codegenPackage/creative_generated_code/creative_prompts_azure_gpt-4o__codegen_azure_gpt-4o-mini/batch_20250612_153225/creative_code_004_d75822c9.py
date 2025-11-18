"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Write a script to automate sending email reminders for polygraph test appointments, using the contact details format provided on the Euro Poligraf Center website.
Generated: DETERMINISTIC_d75822c9808c7f27
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = "smtp.your-email-provider.com"
SMTP_PORT = 587
USERNAME = "your-email@example.com"
PASSWORD = "your-email-password"

# Function to send an email reminder
def send_email_reminder(to_email, appointment_date):
    try:
        # Create the email content
        subject = "Reminder: Your Upcoming Polygraph Test Appointment"
        body = f"Dear Client,\n\nThis is a reminder for your polygraph test appointment scheduled on {appointment_date}.\n\nBest regards,\nEuro Poligraf Center"
        
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email} for appointment on {appointment_date}.")
    
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}. Error: {e}")

# Function to schedule reminders
def schedule_reminders(appointments):
    # Calculate reminder date (1 day before the appointment date)
    for appointment in appointments:
        appointment_date = appointment['date']
        reminder_date = appointment_date - timedelta(days=1)
        current_date = datetime.now().date()
        
        if current_date == reminder_date:
            send_email_reminder(appointment['email'], appointment_date)

# Sample appointment data, typically this would come from a database or an API
appointments = [
    {'email': 'client1@example.com', 'date': datetime(2023, 10, 15).date()},
    {'email': 'client2@example.com', 'date': datetime(2023, 10, 16).date()},
]

# Run the reminder scheduling
schedule_reminders(appointments)
```

Make sure to update the SMTP server configuration with your email provider’s details and credentials before running the script.
