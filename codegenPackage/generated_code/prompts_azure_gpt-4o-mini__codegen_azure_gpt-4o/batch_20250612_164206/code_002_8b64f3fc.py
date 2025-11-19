"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a code snippet that sends a reminder to users for the periodic verification of their gas meters, based on the guidelines provided by ИП Семьянинов Сергей Юрьевич.
Generated: DETERMINISTIC_8b64f3fc24659235
Batch ID: 20250612_164206
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
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Reminder configuration
REMINDER_INTERVAL_DAYS = 365  # Periodic verification interval (e.g., yearly)
REMINDER_SUBJECT = "Gas Meter Verification Reminder"
REMINDER_BODY_TEMPLATE = """
Dear {name},

This is a friendly reminder to verify your gas meter as per the guidelines provided by ИП Семьянинов Сергей Юрьевич.

Last verification date: {last_verification_date}
Next verification due: {next_verification_date}

Please ensure timely verification to avoid any inconvenience.

Best regards,
Your Service Team
"""

# List of users to send reminders to
users = [
    {"name": "John Doe", "email": "john.doe@example.com", "last_verification_date": "2022-10-15"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "last_verification_date": "2022-11-01"},
    # Add more users as needed
]

def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    :param to_email: Recipient's email address
    :param subject: Email subject
    :param body: Email body
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def calculate_next_verification_date(last_verification_date):
    """
    Calculates the next verification date based on the last verification date.

    :param last_verification_date: Date of the last verification (YYYY-MM-DD)
    :return: Next verification date (YYYY-MM-DD)
    """
    try:
        last_date = datetime.strptime(last_verification_date, "%Y-%m-%d")
        next_date = last_date + timedelta(days=REMINDER_INTERVAL_DAYS)
        return next_date.strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Error parsing date {last_verification_date}: {e}")
        return None

def send_reminders():
    """
    Sends periodic verification reminders to all users in the list.
    """
    for user in users:
        name = user.get("name")
        email = user.get("email")
        last_verification_date = user.get("last_verification_date")

        if not name or not email or not last_verification_date:
            print(f"Skipping user due to missing information: {user}")
            continue

        next_verification_date = calculate_next_verification_date(last_verification_date)
        if not next_verification_date:
            print(f"Skipping user due to invalid last verification date: {user}")
            continue

        # Format the email body
        email_body = REMINDER_BODY_TEMPLATE.format(
            name=name,
            last_verification_date=last_verification_date,
            next_verification_date=next_verification_date
        )

        # Send the email
        send_email(email, REMINDER_SUBJECT, email_body)

# Entry point for the script
if __name__ == "__main__":
    send_reminders()
```
