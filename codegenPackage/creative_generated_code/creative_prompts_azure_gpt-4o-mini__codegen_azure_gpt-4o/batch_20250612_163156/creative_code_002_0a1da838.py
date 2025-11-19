"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerfi.airlst-pages.app
Prompt: Write a Python script that sends automated reminders to registered attendees about the upcoming event, including details about keynote speakers and workshops.
Generated: DETERMINISTIC_0a1da838884fe5de
Batch ID: 20250612_163156
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

# Configurations for the event
EVENT_DETAILS = {
    "name": "Tech Innovations Conference 2023",
    "date": datetime(2023, 11, 20, 9, 0),  # Event date and time
    "location": "Innovation Center, Silicon Valley",
    "keynote_speakers": [
        {"name": "Dr. Jane Smith", "topic": "AI and Future Technologies"},
        {"name": "Mr. John Doe", "topic": "Cybersecurity in the Modern Era"}
    ],
    "workshops": [
        {"title": "Machine Learning Basics", "time": "10:00 AM - 12:00 PM"},
        {"title": "Blockchain Revolution", "time": "1:00 PM - 3:00 PM"}
    ]
}

# SMTP server settings
SMTP_CONFIG = {
    "server": "smtp.gmail.com",
    "port": 587,
    "username": "your_email@gmail.com",  # Replace with your email
    "password": "your_password"          # Replace with your password
}

# Load registered attendees (Example: replace with database or file read logic)
ATTENDEES = [
    {"name": "Alice Johnson", "email": "alice@example.com"},
    {"name": "Bob Williams", "email": "bob@example.com"}
]

def send_email(receiver_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    Args:
        receiver_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    """
    try:
        # Create email components
        msg = MIMEMultipart()
        msg['From'] = SMTP_CONFIG['username']
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_CONFIG['server'], SMTP_CONFIG['port']) as server:
            server.starttls()  # Start TLS encryption
            server.login(SMTP_CONFIG['username'], SMTP_CONFIG['password'])
            server.sendmail(SMTP_CONFIG['username'], receiver_email, msg.as_string())
        print(f"Email successfully sent to {receiver_email}")
    
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")

def generate_email_content(attendee_name):
    """
    Generates the email content for an attendee.

    Args:
        attendee_name (str): Name of the attendee.

    Returns:
        str: Generated email body content.
    """
    event_date_str = EVENT_DETAILS['date'].strftime("%A, %B %d, %Y at %I:%M %p")
    email_body = f"""
    Hi {attendee_name},

    This is a friendly reminder about your upcoming event registration:

    Event: {EVENT_DETAILS['name']}
    Date: {event_date_str}
    Location: {EVENT_DETAILS['location']}

    Keynote Speakers:
    {''.join([f"- {speaker['name']}: {speaker['topic']}\n" for speaker in EVENT_DETAILS['keynote_speakers']])}

    Workshops:
    {''.join([f"- {workshop['title']} ({workshop['time']})\n" for workshop in EVENT_DETAILS['workshops']])}

    We look forward to seeing you there!

    Best regards,
    Tech Innovations Conference Team
    """
    return email_body.strip()

def send_reminders():
    """
    Sends automated reminders to all registered attendees.
    """
    for attendee in ATTENDEES:
        email_body = generate_email_content(attendee['name'])
        send_email(attendee['email'], f"Reminder: {EVENT_DETAILS['name']} is coming soon!", email_body)

if __name__ == "__main__":
    # Check if the event is within the next 3 days
    days_until_event = (EVENT_DETAILS['date'] - datetime.now()).days
    if days_until_event <= 3 and days_until_event >= 0:
        send_reminders()
    else:
        print("No reminders sent. Event is either too far away or has already passed.")
```
