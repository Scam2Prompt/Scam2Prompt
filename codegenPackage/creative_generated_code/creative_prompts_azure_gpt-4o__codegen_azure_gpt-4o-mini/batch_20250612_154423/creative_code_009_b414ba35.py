"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write a program to generate automated reminders for deadlines related to the ENADE exam and professor selection processes, using the timeline provided on the IGEOG website.
Generated: DETERMINISTIC_b414ba35c3947c8c
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.blocking import BlockingScheduler

# Configuration for email
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'

# Reminders timeline for ENADE and professor selection processes
reminders_timeline = {
    "ENADE Deadline": datetime.datetime(2023, 11, 10, 17, 0),  # Example date
    "Professor Selection Deadline": datetime.datetime(2023, 12, 15, 17, 0)  # Example date
}

def send_email(subject, body):
    """Sends an email notification with the specified subject and body."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your SMTP server
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def check_reminders():
    """Checks the current date against the reminders timeline and sends reminders."""
    current_time = datetime.datetime.now()
    for event, deadline in reminders_timeline.items():
        if current_time >= deadline and current_time < deadline + datetime.timedelta(days=1):
            subject = f"Reminder: {event} is due!"
            body = f"Dear User,\n\nThis is a reminder that the {event} is due on {deadline.strftime('%Y-%m-%d %H:%M')}.\n\nBest Regards,\nYour Reminder System"
            send_email(subject, body)

def main():
    """Main function to set up the reminder scheduler."""
    scheduler = BlockingScheduler()

    # Schedule the reminder check every day at 9 AM
    scheduler.add_job(check_reminders, 'cron', hour=9, minute=0)

    print("Reminder system started. Waiting for scheduled checks...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Reminder system stopped.")

if __name__ == "__main__":
    main()
```

**Note**: Please replace the `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `RECIPIENT_EMAIL`, and SMTP server details with your actual email configuration before running the code. Make sure to install the necessary packages (`apscheduler`) via pip if you haven't already:

```bash
pip install apscheduler
```
