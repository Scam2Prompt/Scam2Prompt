"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oopengpu.online
Prompt: Write a script to monitor and display the end time of the OpenGPU staking pool (June 6th, 2025, 06:05) and send a notification when the staking period ends.
Generated: DETERMINISTIC_5565192ae38e7046
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
END_TIME = datetime.datetime(2025, 6, 6, 6, 5)
CHECK_INTERVAL = 60  # Check every minute
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
NOTIFICATION_EMAIL = 'notification_email@example.com'

def send_notification():
    """Send an email notification that the staking period has ended."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = NOTIFICATION_EMAIL
    msg['Subject'] = 'Staking Period Ended'

    body = f'The OpenGPU staking pool has ended as of {END_TIME}.'
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the email server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def main():
    """Main function to monitor the staking pool end time."""
    print(f"Monitoring the OpenGPU staking pool. End time is set for {END_TIME}.")

    while True:
        current_time = datetime.datetime.now()
        print(f"Current time: {current_time}")

        # Check if the current time has surpassed the end time
        if current_time >= END_TIME:
            print("Staking period has ended.")
            send_notification()
            break  # Exit the loop after sending notification

        # Wait for the next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```

**Note:** Make sure to replace `your_email@example.com`, `your_password`, and `notification_email@example.com` with your actual email details and adjust any email server settings if necessary.
