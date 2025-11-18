"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-merlinstartercom.pages.dev
Prompt: Generate a Python script to track the start and end times of the MerlinStarter Launchpad event for $MP tokens and send notifications when the event goes live or ends.
Generated: DETERMINISTIC_3ebad8ba2284afc6
Batch ID: 20250612_153648
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
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
EVENT_START_TIME = datetime(2023, 10, 1, 12, 0)  # Replace with the actual start time
EVENT_END_TIME = datetime(2023, 10, 1, 14, 0)    # Replace with the actual end time
EMAIL_ADDRESS = 'your_email@example.com'            # Sender email address
EMAIL_PASSWORD = 'your_password'                     # Sender email password
RECIPIENT_EMAIL = 'recipient_email@example.com'     # Recipient email address

def send_email_notification(subject, body):
    """Sends an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with the actual SMTP server
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        logging.info('Email sent: %s', subject)
    except Exception as e:
        logging.error('Failed to send email: %s', e)

def track_event():
    """Tracks the event start and end times, sending notifications as appropriate."""
    logging.info('Tracking event start and end times...')
    
    while True:
        current_time = datetime.now()

        if current_time >= EVENT_START_TIME and current_time < EVENT_END_TIME:
            send_email_notification('Event Started', 'The MerlinStarter Launchpad event for $MP tokens has started.')
            logging.info('Event is live.')
            break  # Exit the loop after sending the start notification

        if current_time >= EVENT_END_TIME:
            send_email_notification('Event Ended', 'The MerlinStarter Launchpad event for $MP tokens has ended.')
            logging.info('Event has ended.')
            break  # Exit the loop after sending the end notification
        
        # Sleep for a minute before checking again
        time.sleep(60)

if __name__ == "__main__":
    try:
        track_event()
    except Exception as e:
        logging.error('An error occurred while tracking the event: %s', e)
```
