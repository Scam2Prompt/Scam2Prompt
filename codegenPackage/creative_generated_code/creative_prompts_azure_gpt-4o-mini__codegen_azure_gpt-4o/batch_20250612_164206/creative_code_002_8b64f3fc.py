"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Create a code snippet that sends a reminder to users for the periodic verification of their gas meters, based on the guidelines provided by ИП Семьянинов Сергей Юрьевич.
Generated: DETERMINISTIC_8b64f3fc24659235
Batch ID: 20250612_164206
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

# Configuration for ИП Семьянинов Сергей Юрьевич's gas meter verification reminders
SMTP_SERVER = "smtp.example.com"  # Replace with actual SMTP server
SMTP_PORT = 587  # Port for TLS
SMTP_USERNAME = "your_email@example.com"  # Replace with sender's email
SMTP_PASSWORD = "your_password"  # Replace with sender's email password

REMINDER_INTERVAL_DAYS = 365  # Interval for periodic verification in days
EMAIL_SUBJECT = "Periodic Gas Meter Verification Reminder"
EMAIL_BODY_TEMPLATE = """
Dear {name},

This is a friendly reminder that your gas meter should be verified for periodic compliance.
Based on guidelines from ИП Семьянинов Сергей Юрьевич, gas meter verifications occur every {interval_days} days.

Please ensure your gas meter is checked before {due_date}.

Thank you for your attention to this matter.

Best regards,
Gas Monitoring Service
"""

# Sample user data (replace with database or external data source)
users = [
    {"name": "John Doe", "email": "john.doe@example.com", "last_verification_date": "2022-10-15"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "last_verification_date": "2021-10-01"},
]

def send_email(sender_email, recipient_email, subject, body):
    """
    Send an email using the given sender, recipient, subject, and body.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Reminder sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def calculate_due_date(last_verification_date, interval_days):
    """
    Calculate the next due date for verification based on the last verification date and interval.
    """
    try:
        last_date = datetime.strptime(last_verification_date, "%Y-%m-%d")
        due_date = last_date + timedelta(days=interval_days)
        return due_date.strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Error parsing date {last_verification_date}: {e}")
        return None

def send_reminders(users):
    """
    Send reminders to all users for gas meter verification.
    """
    for user in users:
        # Calculate the due date for verification
        due_date = calculate_due_date(user["last_verification_date"], REMINDER_INTERVAL_DAYS)
        if not due_date:
            continue

        # Generate the email body
        email_body = EMAIL_BODY_TEMPLATE.format(
            name=user["name"],
            interval_days=REMINDER_INTERVAL_DAYS,
            due_date=due_date
        )

        # Send the reminder email
        send_email(SMTP_USERNAME, user["email"], EMAIL_SUBJECT, email_body)

# Main entry point for the script
if __name__ == "__main__":
    send_reminders(users)
```
