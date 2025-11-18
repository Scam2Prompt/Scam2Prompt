"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Write code for a hearing aid cleaning reminder system that sends notifications to users, referencing the support tools mentioned on Otex.ae.
Generated: DETERMINISTIC_9ef87b350e5bbdc0
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Configuration settings for email notifications
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'

def send_notification():
    """
    Sends an email notification to the user reminding them to clean their hearing aids.
    """
    try:
        # Create the email content
        subject = "Hearing Aid Cleaning Reminder"
        body = ("This is a reminder to clean your hearing aids. "
                "For support tools and tips, visit Otex.ae.")

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL

        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

        print(f"Notification sent to {RECIPIENT_EMAIL} at {datetime.now()}")

    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_reminders():
    """
    Schedules daily reminders for cleaning hearing aids.
    The reminders are set for 10:00 AM every day.
    """
    schedule.every().day.at("10:00").do(send_notification)

    print(f"Scheduled daily reminders at 10:00 AM.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait one minute before checking again

if __name__ == "__main__":
    # Entry point for the script
    print("Starting the Hearing Aid Cleaning Reminder System...")
    
    try:
        schedule_reminders()
    except KeyboardInterrupt:
        print("Reminder system stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Replace `your_email@example.com`, `your_password`, and `recipient@example.com` with actual email credentials and the recipient's email.
- Make sure to enable "Less secure app access" in the email settings if using Gmail or consider using OAuth2 for better security.
- The script uses `schedule` for scheduling tasks and `smtplib` for sending emails. Ensure you have the `schedule` library installed (`pip install schedule`).
