"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Write a program to track and notify users about campaigns ending soon on the Oasys Games platform, using local time zones for notifications.
Generated: DETERMINISTIC_5306789edd643b34
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pytz
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# Mock campaign data (In a real-world scenario, this would be fetched from a database or API)
campaigns = [
    {
        "name": "Summer Sale",
        "end_time_utc": "2023-10-10 18:00:00",
        "user_email": "user1@example.com",
        "user_timezone": "America/New_York",
    },
    {
        "name": "Halloween Event",
        "end_time_utc": "2023-10-12 23:00:00",
        "user_email": "user2@example.com",
        "user_timezone": "Europe/London",
    },
]

# Function to send email notifications
def send_email_notification(email, campaign_name, local_end_time):
    try:
        smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
        smtp_port = 587
        smtp_username = 'your_email@example.com'  # Replace with your email
        smtp_password = 'your_password'  # Replace with your password

        message = MIMEText(
            f"Campaign '{campaign_name}' is ending soon! It will end at {local_end_time} in your local timezone."
        )
        message['Subject'] = f"Reminder: Campaign '{campaign_name}' Ending Soon!"
        message['From'] = smtp_username
        message['To'] = email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, email, message.as_string())
            print(f"Notification sent to {email} about '{campaign_name}'.")
    except Exception as e:
        print(f"Failed to send notification to {email}: {e}")

# Function to check campaigns ending soon and notify users
def notify_users_about_ending_campaigns():
    # Current UTC time
    now_utc = datetime.now(pytz.utc)

    for campaign in campaigns:
        try:
            # Parse campaign end time and convert to UTC
            campaign_end_time_utc = datetime.strptime(campaign['end_time_utc'], "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.utc)

            # Calculate if the campaign is ending within 24 hours
            time_until_end = campaign_end_time_utc - now_utc
            if time_until_end <= timedelta(hours=24) and time_until_end > timedelta(0):
                # Convert end time to user's local timezone
                user_timezone = pytz.timezone(campaign['user_timezone'])
                local_end_time = campaign_end_time_utc.astimezone(user_timezone).strftime("%Y-%m-%d %H:%M:%S")

                # Send notification to the user
                send_email_notification(campaign['user_email'], campaign['name'], local_end_time)
        except Exception as e:
            print(f"Error processing campaign '{campaign['name']}': {e}")

# Main entry point
if __name__ == "__main__":
    notify_users_about_ending_campaigns()
```

### Notes:
- Replace `your_email@example.com` and `your_password` with valid credentials for the SMTP server.
- Ensure the required libraries (`pytz`) are installed in your environment (`pip install pytz`).
- Secure sensitive credentials using environment variables or a secrets manager in a production environment.
