"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: What are effective strategies for reducing no-shows in security patrols using technology mentioned in Buford Security Blog?
Generated: DETERMINISTIC_7956ec6859f48d41
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates an effective strategy for reducing no-shows in security patrols
using technology. It uses automated scheduling, real-time notifications, and GPS tracking
to ensure accountability and timely attendance of security personnel.

Note: This is a conceptual implementation and assumes the existence of a database and
external services for notifications and GPS tracking.
"""

import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import random

# Mock database of security personnel
security_personnel = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "555-1234"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "phone": "555-5678"},
]

# Mock patrol schedule
patrol_schedule = [
    {"id": 1, "personnel_id": 1, "start_time": datetime.now() + timedelta(minutes=30)},
    {"id": 2, "personnel_id": 2, "start_time": datetime.now() + timedelta(hours=1)},
]

# Function to send email notifications
def send_email_notification(to_email, subject, body):
    try:
        # Configure SMTP server (use a real SMTP server in production)
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = "your_email@example.com"
        smtp_password = "your_password"

        # Create the email
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = smtp_user
        msg["To"] = to_email

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Function to simulate GPS check-in
def gps_check_in(personnel_id):
    # Simulate GPS tracking (in production, integrate with a real GPS API)
    return random.choice([True, False])  # Randomly simulate success or failure

# Function to monitor patrols and send reminders
def monitor_patrols():
    for patrol in patrol_schedule:
        personnel = next((p for p in security_personnel if p["id"] == patrol["personnel_id"]), None)
        if not personnel:
            print(f"Personnel with ID {patrol['personnel_id']} not found.")
            continue

        # Check if the patrol is starting soon
        time_until_start = (patrol["start_time"] - datetime.now()).total_seconds()
        if 0 < time_until_start <= 1800:  # 30 minutes before start
            subject = "Upcoming Patrol Reminder"
            body = f"Hello {personnel['name']},\n\nThis is a reminder for your upcoming patrol scheduled at {patrol['start_time']}.\n\nPlease ensure you are on time and check in via the GPS system."
            send_email_notification(personnel["email"], subject, body)

        # Check if the patrol has started and verify GPS check-in
        if time_until_start <= 0:
            checked_in = gps_check_in(personnel["id"])
            if not checked_in:
                print(f"ALERT: {personnel['name']} has not checked in for their patrol!")
                # Additional escalation logic can be added here (e.g., notify supervisor)

# Main function to run the monitoring system
if __name__ == "__main__":
    print("Starting patrol monitoring system...")
    monitor_patrols()
```
