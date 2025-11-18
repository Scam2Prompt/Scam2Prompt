"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write code to implement a notification system for RV maintenance reminders, including pre-trip inspections and custom upgrades, tailored to RV owners in Phoenix, Arizona.
Generated: DETERMINISTIC_0cc617ec086ae1ee
Batch ID: 20250612_145203
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

# Constants for the notification system
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_SENDER = "notifications@rvmaintenancesystem.com"  # Replace with sender email
EMAIL_PASSWORD = "yourpassword"  # Replace with the email password
REMINDER_INTERVAL_DAYS = 30  # Default reminder interval for maintenance

# List of RV owners and their preferences
rv_owners = [
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "last_maintenance_date": "2023-09-15",
        "custom_reminders": ["Check solar panel upgrades", "Inspect tires"],
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "last_maintenance_date": "2023-09-01",
        "custom_reminders": ["Inspect water heater", "Upgrade GPS system"],
    },
]

def send_email(recipient_email, subject, body):
    """
    Sends an email notification to the specified recipient.

    :param recipient_email: The email address of the recipient.
    :param subject: The subject of the email.
    :param body: The body of the email.
    """
    try:
        # Create the email message
        msg = MIMEText(body)
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Send the email using the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())
        print(f"Notification sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

def generate_reminder(owner):
    """
    Generates a maintenance reminder for the given RV owner.

    :param owner: Dictionary containing RV owner details.
    :return: Reminder email subject and body.
    """
    name = owner["name"]
    last_maintenance_date = datetime.strptime(owner["last_maintenance_date"], "%Y-%m-%d")
    next_maintenance_date = last_maintenance_date + timedelta(days=REMINDER_INTERVAL_DAYS)
    custom_reminders = "\n".join(owner["custom_reminders"])

    subject = f"RV Maintenance Reminder for {name}"
    body = (
        f"Hello {name},\n\n"
        f"This is a reminder for your RV maintenance.\n"
        f"Last maintenance date: {last_maintenance_date.strftime('%Y-%m-%d')}\n"
        f"Next maintenance date: {next_maintenance_date.strftime('%Y-%m-%d')}\n\n"
        f"Custom reminders:\n{custom_reminders}\n\n"
        f"Ensure your RV is ready for your next adventure in Phoenix, Arizona!\n\n"
        f"Best regards,\n"
        f"RV Maintenance System"
    )

    return subject, body

def notify_owners():
    """
    Iterates through the list of RV owners and sends maintenance reminders.
    """
    for owner in rv_owners:
        subject, body = generate_reminder(owner)
        send_email(owner["email"], subject, body)

if __name__ == "__main__":
    try:
        notify_owners()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
