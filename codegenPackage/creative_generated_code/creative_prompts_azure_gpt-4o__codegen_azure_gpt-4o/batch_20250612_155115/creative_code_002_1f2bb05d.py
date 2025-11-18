"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.firstmate.xyz
Prompt: Generate code to create a notification system that alerts users every Monday about new NFT drops from the Bankless ecosystem.
Generated: DETERMINISTIC_1f2bb05d22757495
Batch ID: 20250612_155115
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
import time

# Configuration for the notification system
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587                   # Commonly used SMTP port
EMAIL_ADDRESS = "your_email@example.com"  # Sender email address
EMAIL_PASSWORD = "your_password"          # Password for the email account
NOTIFICATION_SUBJECT = "Bankless NFT Drop Alert"
NOTIFICATION_MESSAGE = (
    "Hello,\n\n"
    "Exciting news! There are new NFT drops from the Bankless ecosystem. "
    "Visit the Bankless marketplace to explore.\n\n"
    "Best regards,\nBankless Team"
)

# List of recipient email addresses
RECIPIENT_LIST = [
    "user1@example.com",
    "user2@example.com",
    # Add more email addresses as needed
]

def send_notification_email(subject, message, recipients):
    """
    Sends a notification email to the list of recipients.

    :param subject: The email subject.
    :param message: The email message body.
    :param recipients: List of recipient email addresses.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipients, msg.as_string())
            print(f"Notification email successfully sent to {len(recipients)} recipients.")
    except Exception as e:
        print(f"Error sending email: {e}")

def wait_until_next_monday():
    """
    Calculates the time until the next Monday and waits until then.
    """
    today = datetime.now()
    # Calculate days until Monday (weekday 0)
    days_until_monday = (0 - today.weekday() + 7) % 7
    next_monday = today + timedelta(days=days_until_monday)
    # Set time to 9:00 AM on next Monday
    next_monday = next_monday.replace(hour=9, minute=0, second=0, microsecond=0)
    wait_time_seconds = (next_monday - today).total_seconds()

    print(f"Next notification scheduled for: {next_monday}, waiting {wait_time_seconds} seconds...")
    time.sleep(wait_time_seconds)

def main():
    """
    Main function to run the notification system.
    """
    while True:
        # Wait until the next Monday
        wait_until_next_monday()
        # Send the notification email to all recipients
        send_notification_email(NOTIFICATION_SUBJECT, NOTIFICATION_MESSAGE, RECIPIENT_LIST)

if __name__ == "__main__":
    main()
```
