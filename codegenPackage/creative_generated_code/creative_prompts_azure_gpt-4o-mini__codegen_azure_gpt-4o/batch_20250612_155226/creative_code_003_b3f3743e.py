"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Create a code snippet that sends automated reminders to participants of a financial sales training course, reflecting the training structure at Debridge Advisory.
Generated: DETERMINISTIC_b3f3743e6016d1fb
Batch ID: 20250612_155226
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

# Configuration for SMTP server
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"          # Replace with your email password

# Training course structure details
TRAINING_COURSE = {
    "course_name": "Financial Sales Training",
    "trainer_name": "John Doe",
    "duration_days": 5,
    "start_date": datetime(2023, 11, 15),
    "daily_topics": [
        "Introduction to Financial Sales",
        "Understanding Financial Products",
        "Building Rapport with Clients",
        "Negotiation Techniques",
        "Closing Deals Effectively"
    ]
}

# List of participants (replace with actual participant data)
PARTICIPANTS = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]


def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject line.
        body (str): Email message body.
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Reminder sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")


def generate_reminder_message(participant_name, course_details, day):
    """
    Generates the content of the reminder message.

    Args:
        participant_name (str): Name of the participant.
        course_details (dict): Training course details.
        day (int): Day of the training.

    Returns:
        str: Formatted reminder message.
    """
    topic = course_details["daily_topics"][day - 1]
    return (
        f"Dear {participant_name},\n\n"
        f"Reminder: You are enrolled in the '{course_details['course_name']}' course.\n"
        f"Trainer: {course_details['trainer_name']}\n"
        f"Day {day} Topic: {topic}\n\n"
        f"Please make sure to attend the session tomorrow.\n\n"
        f"Best regards,\n"
        f"Debridge Advisory Team"
    )


def send_reminders(course_details, participants):
    """
    Sends daily reminders to participants for the training course.

    Args:
        course_details (dict): Training course details.
        participants (list): List of participants with their details.
    """
    today = datetime.now().date()
    for day in range(1, course_details["duration_days"] + 1):
        reminder_date = course_details["start_date"].date() + timedelta(days=day - 1)
        if reminder_date == today + timedelta(days=1):  # Check if tomorrow is the session
            for participant in participants:
                message = generate_reminder_message(
                    participant["name"], course_details, day
                )
                send_email(participant["email"], f"Reminder: Day {day} of Financial Sales Training", message)


if __name__ == "__main__":
    # Run the reminder sender
    send_reminders(TRAINING_COURSE, PARTICIPANTS)
```
