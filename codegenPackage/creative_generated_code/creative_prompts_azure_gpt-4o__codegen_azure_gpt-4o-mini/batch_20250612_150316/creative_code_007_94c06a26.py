"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Write a script to automate the process of watching Big Time on Twitch to gain an access key for the Preseason, including functionality to track eligibility and notify the user.
Generated: DETERMINISTIC_94c06a26398b82f0
Batch ID: 20250612_150316
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
from twitchAPI.twitch import Twitch
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration
TWITCH_CLIENT_ID = 'your_twitch_client_id'
TWITCH_CLIENT_SECRET = 'your_twitch_client_secret'
TWITCH_CHANNEL = 'BigTime'
USER_EMAIL = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
NOTIFICATION_INTERVAL = 60  # in seconds
TRACK_TIME_LIMIT = 3600  # time limit in seconds to track eligibility

# Initialize Twitch API
twitch = Twitch(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
twitch.authenticate_app([])

def send_notification(message):
    """Send a notification email to the user."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'Big Time Twitch Notification'
        msg['From'] = USER_EMAIL
        msg['To'] = USER_EMAIL
        
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(USER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(USER_EMAIL, USER_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Failed to send notification email: {e}")

def check_stream_status(channel_name):
    """Check if the channel is currently live."""
    try:
        user = twitch.get_users(logins=[channel_name])
        if user['data']:
            user_id = user['data'][0]['id']
            streams = twitch.get_streams(user_ids=[user_id])
            return len(streams['data']) > 0
    except Exception as e:
        print(f"Error checking stream status: {e}")
    return False

def main():
    """Main function to watch the Twitch stream for an access key."""
    start_time = time.time()
    eligibility_status = False

    while True:
        # Check eligibility every NOTIFICATION_INTERVAL seconds
        if time.time() - start_time > TRACK_TIME_LIMIT:
            print("Time limit exceeded. Stopping the eligibility tracking.")
            break

        if check_stream_status(TWITCH_CHANNEL):
            if not eligibility_status:
                eligibility_status = True
                send_notification(f"{TWITCH_CHANNEL} is now live! Start watching to gain access key!")

            print(f"{TWITCH_CHANNEL} is live! Keep watching...")
        else:
            if eligibility_status:
                eligibility_status = False
                send_notification(f"{TWITCH_CHANNEL} has gone offline. You may miss the key!")

        time.sleep(NOTIFICATION_INTERVAL)

if __name__ == "__main__":
    main()
```

**Note:** Make sure to replace the placeholders for `TWITCH_CLIENT_ID`, `TWITCH_CLIENT_SECRET`, `USER_EMAIL`, and `EMAIL_PASSWORD` with actual values before running the code. Additionally, ensure your email provider allows SMTP access and the necessary permissions for sending emails.
