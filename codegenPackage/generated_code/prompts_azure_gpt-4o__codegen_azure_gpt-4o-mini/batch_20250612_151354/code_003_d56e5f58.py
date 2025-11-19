"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Write code to schedule and send reminders for upcoming events (e.g., Easter Eve programs) via email and SMS, using Twilio or SendGrid APIs.
Generated: DETERMINISTIC_d56e5f584d0a57c8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from twilio.rest import Client
from datetime import datetime, timedelta
import schedule
import time

# Load environment variables for sensitive information
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_SENDER_EMAIL = os.getenv('SENDGRID_SENDER_EMAIL')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_phone_number, message):
    """Send an SMS message using Twilio API."""
    try:
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"SMS sent to {to_phone_number}: {message}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def send_email(to_email, subject, message):
    """Send an email using SendGrid API."""
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        email = Mail(
            from_email=SENDGRID_SENDER_EMAIL,
            to_emails=to_email,
            subject=subject,
            plain_text_content=message
        )
        response = sg.send(email)
        print(f"Email sent to {to_email}: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_reminder(event_name, event_time, phone_number, email):
    """Schedule a reminder for an upcoming event."""
    # Calculate the time to send the reminder (1 day before the event)
    reminder_time = event_time - timedelta(days=1)

    # Schedule the SMS reminder
    schedule.every().day.at(reminder_time.strftime("%H:%M")).do(
        send_sms, to_phone_number=phone_number, message=f"Reminder: {event_name} is tomorrow!"
    )

    # Schedule the email reminder
    schedule.every().day.at(reminder_time.strftime("%H:%M")).do(
        send_email, to_email=email, subject=f"Reminder: {event_name}", message=f"Don't forget about {event_name} tomorrow!"
    )

def run_scheduler():
    """Run the scheduler to check for pending tasks."""
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Example usage
    event_name = "Easter Eve Program"
    event_time = datetime(2023, 4, 8, 18, 0)  # Example event time
    phone_number = "+1234567890"  # Replace with the recipient's phone number
    email = "recipient@example.com"  # Replace with the recipient's email

    # Schedule the reminder
    schedule_reminder(event_name, event_time, phone_number, email)

    # Start the scheduler
    run_scheduler()
```

Make sure to set the environment variables for Twilio and SendGrid credentials before running the code.
