"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Generate a Python script to create a maintenance notification system for a website, similar to the one described on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_ebbbbba2b00bc000
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
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    filename='maintenance_notification.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
MAINTENANCE_START = datetime(2023, 10, 10, 22, 0)  # Maintenance start date and time
MAINTENANCE_DURATION = timedelta(hours=2)  # Maintenance duration
NOTIFICATION_EMAILS = ['admin@example.com']  # List of emails to notify
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

def send_notification(email_list, subject, body):
    """Send maintenance notification email."""
    try:
        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USERNAME
        msg['To'] = ", ".join(email_list)

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to the SMTP server
            server.sendmail(SMTP_USERNAME, email_list, msg.as_string())  # Send the email
        
        logging.info(f'Notification sent to: {email_list}')
    
    except Exception as e:
        logging.error(f'Error sending email notification: {e}')

def generate_notification_body(start_time, duration):
    """Generate the body of the maintenance notification email."""
    end_time = start_time + duration
    body = (
        f"Dear User,\n\n"
        f"We would like to inform you that our website will undergo maintenance "
        f"starting from {start_time.strftime('%Y-%m-%d %H:%M')} to {end_time.strftime('%H:%M')} UTC.\n\n"
        "During this time, the website may be unavailable. We apologize for any inconvenience this may cause.\n\n"
        "Thank you for your understanding.\n\n"
        "Best Regards,\n"
        "The Website Team"
    )
    return body

def main():
    """Main function to execute the notification system."""
    # Check if maintenance is scheduled
    current_time = datetime.now()
    if MAINTENANCE_START <= current_time < (MAINTENANCE_START + MAINTENANCE_DURATION):
        subject = "Scheduled Maintenance Notification"
        body = generate_notification_body(MAINTENANCE_START, MAINTENANCE_DURATION)
        send_notification(NOTIFICATION_EMAILS, subject, body)
    else:
        logging.info("No maintenance notification sent. Current time is outside of maintenance window.")

if __name__ == "__main__":
    main()
```
