"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Generate Python code to send automated reminders to users about their upcoming online health sessions via LINE or email.
Generated: DETERMINISTIC_89f76ca6adc85152
Batch ID: 20250612_151513
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
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from datetime import datetime, timedelta

# Configuration for email and LINE API
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'
LINE_ACCESS_TOKEN = 'your_line_channel_access_token'

# List of user sessions with their contact details and session info
user_sessions = [
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "line_id": "LINE_USER_ID_1",  
        "session_time": "2023-10-12 14:00:00"
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "line_id": "LINE_USER_ID_2",
        "session_time": "2023-10-12 15:00:00"
    }
]

def send_email(to_email, subject, message):
    """
    Sends an email using SMTP.
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param message: Body of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Enable encryption
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

def send_line_message(to_line_id, message):
    """
    Sends a message through LINE Messaging API.
    :param to_line_id: Recipient's LINE user ID
    :param message: Message to be sent
    """
    try:
        line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
        line_bot_api.push_message(to_line_id, TextSendMessage(text=message))
        print(f"LINE message sent successfully to LINE ID: {to_line_id}")
    except Exception as e:
        print(f"Error sending LINE message to {to_line_id}: {e}")

def notify_users():
    """
    Notifies users about their upcoming online health sessions.
    Sends reminders via LINE or email.
    """
    current_time = datetime.now()
    reminder_time_threshold = timedelta(hours=24)  # Notify 24 hours before the session

    for session in user_sessions:
        try:
            session_time = datetime.strptime(session["session_time"], "%Y-%m-%d %H:%M:%S")
            time_until_session = session_time - current_time

            if time_until_session <= reminder_time_threshold and time_until_session > timedelta(0):  # Ensure session is within the threshold and not in the past
                reminder_message = f"Hello {session['name']},\n\nThis is a reminder for your upcoming online health session scheduled on {session_time.strftime('%Y-%m-%d at %H:%M:%S')}.\n\nThank you,\nHealth Services Team"

                # Send reminder via LINE if line_id is provided
                if session.get("line_id"):
                    send_line_message(session["line_id"], reminder_message)

                # Send reminder via email if email is provided
                if session.get("email"):
                    send_email(session["email"], "Reminder: Upcoming Online Health Session", reminder_message)
        except Exception as e:
            print(f"Error processing session for {session['name']}: {e}")

# Entry point for the script
if __name__ == "__main__":
    notify_users()
```
