"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a Python script that sends reminders for training sessions and events to members of a running club, inspired by the communication style of Thompson Estate Athletics.
Generated: DETERMINISTIC_846cedf2d28cdaf7
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Configuration for the email server
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"          # Replace with your email password

# List of members with their email addresses
members = [
    {"name": "John Doe", "email": "john.doe@example.com"},
    {"name": "Jane Smith", "email": "jane.smith@example.com"},
    {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
]

# List of upcoming events and training sessions
events = [
    {"title": "Interval Training", "date": datetime(2023, 10, 15, 18, 0)},
    {"title": "Long Run", "date": datetime(2023, 10, 17, 7, 0)},
    {"title": "Club Meeting", "date": datetime(2023, 10, 20, 19, 0)},
]

def send_email(recipient_email, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def generate_reminder(event, member):
    """
    Generates a reminder message for a specific event and member.

    Args:
        event (dict): The event details (title and date).
        member (dict): The member details (name and email).

    Returns:
        str: The reminder message.
    """
    return (
        f"Hi {member['name']},\n\n"
        f"Just a friendly reminder about the upcoming event:\n\n"
        f"Event: {event['title']}\n"
        f"Date: {event['date'].strftime('%A, %d %B %Y at %I:%M %p')}\n\n"
        f"We hope to see you there!\n\n"
        f"Best regards,\n"
        f"Thompson Estate Athletics"
    )

def send_reminders():
    """
    Sends reminders for upcoming events to all members.
    """
    now = datetime.now()
    for event in events:
        # Only send reminders for events happening within the next 7 days
        if now <= event['date'] <= now + timedelta(days=7):
            for member in members:
                # Generate the reminder message
                reminder_message = generate_reminder(event, member)
                # Send the email
                send_email(member['email'], f"Reminder: {event['title']}", reminder_message)

if __name__ == "__main__":
    # Run the reminder script
    send_reminders()
```

**Note:** Replace `your_email@example.com` and `your_password` with valid credentials for the email account you want to use for sending reminders. Ensure you follow security best practices, such as using environment variables or a secure secrets manager for sensitive information.
