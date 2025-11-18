"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-share.pages.dev
Prompt: Create a program to track the remaining program duration (24.1 days) and send notifications when the duration is about to expire.
Generated: DETERMINISTIC_aae3e95bb0117240
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for email notifications
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
NOTIFICATION_RECIPIENT = "recipient@example.com"

# Duration to track (in days)
DURATION_DAYS = 24.1

# Calculate the end time based on the current time and the duration
end_time = datetime.now() + timedelta(days=DURATION_DAYS)

# Function to send email notifications
def send_notification():
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = NOTIFICATION_RECIPIENT
        msg['Subject'] = "Duration Expiration Notification"
        body = f"The tracking duration of {DURATION_DAYS} days is about to expire."
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Notification sent successfully.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

# Function to check the remaining time and send a notification if needed
def track_duration():
    while True:
        # Calculate the remaining time
        remaining_time = end_time - datetime.now()
        remaining_days = remaining_time.total_seconds() / (24 * 3600)  # Convert to days
        
        # Check if the remaining time is less than or equal to 1 day
        if remaining_days <= 1:
            send_notification()
            break  # Exit the loop after sending the notification
            
        # Sleep for an hour before checking again
        time.sleep(3600)

# Starting the duration tracking in a separate thread
if __name__ == "__main__":
    print(f"Tracking duration of {DURATION_DAYS} days. Ends on {end_time}.")
    duration_thread = threading.Thread(target=track_duration)
    duration_thread.start()
```

Make sure to replace the email configuration values with your actual credentials. This example uses Gmail's SMTP server; ensure that "Allow less secure apps" is enabled for the sender email account or use an app password if two-step verification is enabled.
