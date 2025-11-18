"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Write code to schedule and send reminders for upcoming events (e.g., Easter Eve programs) via email and SMS, using Twilio or SendGrid APIs.
Generated: DETERMINISTIC_d56e5f584d0a57c8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import schedule
import time
import smtplib
from twilio.rest import Client
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up Twilio client
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# Email configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_email(to_email, subject, body):
    """Send an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_sms(to_phone, message):
    """Send an SMS notification."""
    try:
        twilio_client.messages.create(
            body=message,
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            to=to_phone
        )
        print(f"SMS sent to {to_phone}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def schedule_reminder(event_name, event_time, email_recipients, sms_recipients):
    """Schedule a reminder for an upcoming event."""
    def reminder():
        subject = f"Reminder: {event_name} is happening soon!"
        body = f"Don't forget about the upcoming event: {event_name} at {event_time}."
        for email in email_recipients:
            send_email(email, subject, body)
        for phone in sms_recipients:
            send_sms(phone, body)

    # Schedule the reminder to be sent 1 hour before the event
    reminder_time = event_time - timedelta(hours=1)
    schedule.every().day.at(reminder_time.strftime("%H:%M")).do(reminder)

def run_scheduler():
    """Run the scheduled tasks in the background."""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait a minute before checking again

if __name__ == "__main__":
    # Example event details
    event_name = "Easter Eve Program"
    event_time = datetime(2023, 4, 8, 18, 0)  # Example: April 8, 2023, at 18:00
    email_recipients = ["example@example.com"]
    sms_recipients = ["+12345678901"]

    # Schedule the reminder for the event
    schedule_reminder(event_name, event_time, email_recipients, sms_recipients)

    # Start the scheduler
    run_scheduler()
```
