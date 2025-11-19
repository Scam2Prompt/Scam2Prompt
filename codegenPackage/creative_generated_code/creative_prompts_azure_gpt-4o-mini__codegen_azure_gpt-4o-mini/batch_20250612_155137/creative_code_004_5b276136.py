"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pomrajufm.edu.bd
Prompt: Construct a code snippet that sends email notifications for important dates like admission deadlines from the Pomra Jameul Ulum Fazil Madrasha's calendar.
Generated: DETERMINISTIC_5b2761366a5d05c4
Batch ID: 20250612_155137
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
from datetime import datetime
import json

# Configuration for email
SMTP_SERVER = 'smtp.example.com'   # Replace with your SMTP server
SMTP_PORT = 587                     # Common port for TLS
USERNAME = 'your_email@example.com' # Replace with your email
PASSWORD = 'your_password'          # Replace with your email password

# Load important dates from a JSON file
def load_important_dates(file_path):
    """Load important dates from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading important dates: {e}")
        return []

# Send an email notification
def send_email(to_email, subject, body):
    """Send an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function to check dates and send notifications
def notify_upcoming_dates(dates, notification_email):
    """Notify about upcoming important dates."""
    today = datetime.now()
    
    for date in dates:
        # Assuming date is in "YYYY-MM-DD" format
        important_date = datetime.strptime(date['date'], '%Y-%m-%d')
        days_left = (important_date - today).days

        # Send notification if the date is within the next 7 days
        if 0 <= days_left <= 7:
            subject = f"Important Date Reminder: {date['event']}"
            body = f"Reminder: {date['event']} is on {date['date']}."
            send_email(notification_email, subject, body)

if __name__ == "__main__":
    # Specify the path to the JSON file containing important dates
    important_dates_file = 'important_dates.json'
    notification_email = 'recipient@example.com'  # Replace with recipient's email

    # Load important dates and send notifications
    important_dates = load_important_dates(important_dates_file)
    if important_dates:
        notify_upcoming_dates(important_dates, notification_email)
    else:
        print("No important dates found or unable to load dates.")
```

**Important Note:**
- Replace placeholders (`smtp.example.com`, `your_email@example.com`, `your_password`, `recipient@example.com`, and the path for the JSON file) with actual values before running the code. 
- Ensure that the JSON file `important_dates.json` is structured correctly, for example:
```json
[
    {"event": "Admission Deadline", "date": "2023-11-01"},
    {"event": "Application Review", "date": "2023-11-15"}
]
```
