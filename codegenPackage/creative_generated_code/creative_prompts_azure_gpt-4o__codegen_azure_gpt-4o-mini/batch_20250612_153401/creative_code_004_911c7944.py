"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donk-meme.pages.dev
Prompt: Create a script to monitor the countdown timer for the Donk.Meme presale and notify users when the sale ends.
Generated: DETERMINISTIC_911c794493ff9562
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import requests
from datetime import datetime
from threading import Timer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SALE_END_TIMESTAMP = "2023-10-15T15:00:00Z"  # Set the sale end time in UTC
CHECK_INTERVAL = 60  # Check every 60 seconds
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
NOTIFY_EMAIL = "notify_email@example.com"  # Replace with the recipient's email

def send_email_notification():
    """Sends an email notification to notify_user when the presale ends."""
    subject = "Donk.Meme Presale Notification"
    body = "The Donk.Meme presale has ended."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = NOTIFY_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Notification email sent to {NOTIFY_EMAIL}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def countdown_monitor():
    """Monitors the countdown timer for the Donk.Meme presale."""
    sale_end_time = datetime.strptime(SALE_END_TIMESTAMP, "%Y-%m-%dT%H:%M:%SZ")
    
    while True:
        current_time = datetime.utcnow()
        if current_time >= sale_end_time:
            print("The Donk.Meme presale has ended.")
            send_email_notification()
            break
        else:
            time_remaining = (sale_end_time - current_time).seconds
            print(f"Time remaining for the presale: {time_remaining // 60} minutes and {time_remaining % 60} seconds.")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        countdown_monitor()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note**: Replace SMTP server, email addresses, and passwords with actual credentials for the script to run successfully.
