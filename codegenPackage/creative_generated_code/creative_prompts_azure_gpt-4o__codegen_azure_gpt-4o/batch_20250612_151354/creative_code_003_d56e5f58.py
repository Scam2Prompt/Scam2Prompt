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
import smtplib
import ssl
from email.message import EmailMessage
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Configuration constants
SENDGRID_SMTP_SERVER = "smtp.sendgrid.net"
SENDGRID_PORT = 587
SENDGRID_USERNAME = "your_sendgrid_username"
SENDGRID_PASSWORD = "your_sendgrid_password"
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"  # Replace with Twilio-provided phone number

# Event Structure
EVENTS = [
    {
        "name": "Easter Eve Program",
        "date": "2023-04-08T18:00:00",  # ISO 8601 format
        "email_recipients": ["recipient1@example.com", "recipient2@example.com"],
        "sms_recipients": ["+19876543210", "+12345678901"],
        "reminder_hours": [24, 1]  # Send reminders 24 hours and 1 hour before event
    }
]

def send_email(subject, body, recipients):
    """
    Sends an email using SendGrid SMTP server.

    :param subject: The subject of the email
    :param body: The body of the email
    :param recipients: List of recipient email addresses
    """
    try:
        msg = EmailMessage()
        msg["From"] = SENDGRID_USERNAME
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP(SENDGRID_SMTP_SERVER, SENDGRID_PORT) as server:
            server.starttls(context=context)
            server.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to: {recipients}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def send_sms(body, recipients):
    """
    Sends an SMS using Twilio API.

    :param body: The content of the SMS
    :param recipients: List of recipient phone numbers
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        for recipient in recipients:
            message = client.messages.create(
                body=body,
                from_=TWILIO_PHONE_NUMBER,
                to=recipient
            )
        print(f"SMS sent successfully to: {recipients}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")


def schedule_reminders(events):
    """
    Schedules and sends reminders for upcoming events.

    :param events: List of event dictionaries
    """
    while True:
        now = datetime.now()
        for event in events:
            event_datetime = datetime.fromisoformat(event["date"])
            for hours in event["reminder_hours"]:
                reminder_time = event_datetime - timedelta(hours=hours)
                if now >= reminder_time and now < reminder_time + timedelta(minutes=1):
                    # Send Email Reminder
                    email_subject = f"Reminder: {event['name']} is happening soon!"
                    email_body = f"Dear Participant,\n\nThis is a reminder that the event '{event['name']}' is scheduled for {event_datetime.strftime('%Y-%m-%d %H:%M:%S')}.\n\nBest regards,\nEvent Organizer"
                    send_email(email_subject, email_body, event["email_recipients"])

                    # Send SMS Reminder
                    sms_body = f"Reminder: '{event['name']}' is happening on {event_datetime.strftime('%Y-%m-%d %H:%M:%S')}."
                    send_sms(sms_body, event["sms_recipients"])

        time.sleep(60)  # Check events every minute


if __name__ == "__main__":
    try:
        print("Starting reminder scheduler...")
        schedule_reminders(EVENTS)
    except KeyboardInterrupt:
        print("Scheduler stopped manually.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
