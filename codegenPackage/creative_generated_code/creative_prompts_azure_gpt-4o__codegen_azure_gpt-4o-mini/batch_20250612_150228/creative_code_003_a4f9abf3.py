"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3l7e667ujuarffoatjdcaaydxgnjde2rbbwwt6zmewgsgowh4sm.ipfs.dweb.link
Prompt: Create a script to monitor the BasedAI sign-up deadline and send alerts when the 48-hour registration window is about to close.
Generated: DETERMINISTIC_a4f9abf3816130a8
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
REGISTRATION_DEADLINE = datetime(2023, 10, 31, 23, 59)  # Set the registration deadline
ALERT_WINDOW = timedelta(hours=48)  # Alert 48 hours before the deadline
CHECK_INTERVAL = 3600  # Check every hour (3600 seconds)
EMAIL_SENDER = 'your_email@example.com'
EMAIL_RECEIVER = 'recipient_email@example.com'
EMAIL_SUBJECT = 'BasedAI Registration Alert'
EMAIL_SMTP_SERVER = 'smtp.example.com'
EMAIL_SMTP_PORT = 587
EMAIL_PASSWORD = 'your_email_password'

def send_email_alert():
    """Send an email alert about the upcoming registration deadline."""
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = EMAIL_SUBJECT
        body = f"The registration deadline for BasedAI is approaching. You have less than 48 hours left to sign up!"
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Authenticate
            server.send_message(msg)  # Send email

        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_registration_deadline():
    """Continuously monitor the registration deadline and send alerts when within the alert window."""
    while True:
        now = datetime.now()
        time_remaining = REGISTRATION_DEADLINE - now

        if time_remaining <= ALERT_WINDOW and time_remaining > timedelta(0):
            send_email_alert()
            break  # Exit after sending the alert

        if time_remaining <= timedelta(0):
            print("The registration deadline has passed.")
            break  # Exit if the deadline has passed

        # Wait for the specified interval before checking again
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_registration_deadline()
```
