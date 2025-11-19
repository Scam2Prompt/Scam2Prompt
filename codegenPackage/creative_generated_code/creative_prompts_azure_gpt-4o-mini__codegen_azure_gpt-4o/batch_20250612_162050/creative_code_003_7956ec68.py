"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bufordsecurityblog.com
Prompt: What are effective strategies for reducing no-shows in security patrols using technology mentioned in Buford Security Blog?
Generated: DETERMINISTIC_7956ec6859f48d41
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements strategies to reduce no-shows in security patrols using technology.
This solution assumes the use of scheduling, automated reminders, and GPS-based tracking 
as discussed in the Buford Security Blog.
"""

import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import random

# Constants
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'

# Mock database for security guards and their patrol schedules
guards = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com", "phone": "123-456-7890", "shift_start": "2023-10-01 08:00"},
    {"id": 2, "name": "Jane Smith", "email": "janesmith@example.com", "phone": "987-654-3210", "shift_start": "2023-10-01 16:00"},
]

# Function to send email reminders to security guards
def send_email_reminder(guard):
    try:
        # Create email content
        subject = "Reminder: Upcoming Security Patrol Shift"
        body = f"Hello {guard['name']},\n\nThis is a reminder that your security patrol shift starts at {guard['shift_start']}.\nPlease ensure you're on time.\n\nThank you,\nBuford Security"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = guard['email']
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email reminder sent to {guard['name']} at {guard['email']}.")
    except Exception as e:
        print(f"Failed to send email to {guard['name']} at {guard['email']}. Error: {e}")

# Function to check GPS location of security guards during their shift
def check_gps_location(guard):
    try:
        # Simulate GPS tracking (mock GPS locations)
        patrol_locations = ["Checkpoint A", "Checkpoint B", "Checkpoint C"]
        current_location = random.choice(patrol_locations)  # Mock current location
        
        # Simulate a check to ensure guard is at the correct location
        print(f"Checking GPS location for {guard['name']}: Current location is {current_location}.")
        if current_location not in patrol_locations:
            print(f"Alert: {guard['name']} is not at the designated patrol location!")
    except Exception as e:
        print(f"Failed to check GPS location for {guard['name']}. Error: {e}")

# Function to send automated reminders
def send_reminders():
    current_time = datetime.now()
    for guard in guards:
        # Parse shift start time
        shift_start = datetime.strptime(guard['shift_start'], "%Y-%m-%d %H:%M")
        
        # Calculate time difference between now and shift start
        reminder_time = shift_start - timedelta(hours=1)  # Send reminder 1 hour prior to shift start
        if current_time >= reminder_time and current_time < shift_start:
            send_email_reminder(guard)

# Main function
def main():
    print("Starting patrol monitoring system...")
    send_reminders()
    for guard in guards:
        check_gps_location(guard)
    print("Patrol monitoring system finished.")

if __name__ == "__main__":
    main()
```
