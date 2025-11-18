"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Write code to generate automated email reminders for enrolled students in Debridge Advisory's certified courses, ensuring timely updates and notifications.
Generated: DETERMINISTIC_eac55975573b15b1
Batch ID: 20250612_151705
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    filename='email_reminders.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configurations
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"  # Replace with your sender email address
EMAIL_PASSWORD = "your-email-password"  # Replace with your sender email password

# Sample data for students and their course details
students = [
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "course": "Certified Financial Analyst",
        "start_date": datetime(2023, 10, 1),
        "reminder_days": [7, 3, 1]  # Days before start_date to send reminders
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "course": "Certified Tax Advisor",
        "start_date": datetime(2023, 10, 15),
        "reminder_days": [7, 3, 1]
    }
]

def send_email(student, days_left):
    """
    Sends an email reminder to the student about their upcoming course.

    :param student: Dictionary containing student information.
    :param days_left: Days remaining before the course starts.
    """
    try:
        # Create email content
        subject = f"Reminder: {student['course']} starts in {days_left} day(s)"
        body = f"Dear {student['name']},\n\nThis is a reminder that your course, '{student['course']}', will start in {days_left} day(s) on {student['start_date'].strftime('%Y-%m-%d')}.\n\nPlease prepare accordingly.\n\nBest regards,\nDebridge Advisory"
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = student['email']
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable secure connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        # Log success
        logging.info(f"Email sent to {student['email']} for course '{student['course']}' ({days_left} day(s) left).")

    except Exception as e:
        # Log any errors
        logging.error(f"Failed to send email to {student['email']} for course '{student['course']}': {e}")

def schedule_reminders():
    """
    Schedules and sends email reminders to students based on their courses' start dates.
    """
    today = datetime.now()
    for student in students:
        for days in student['reminder_days']:
            reminder_date = student['start_date'] - timedelta(days=days)
            if reminder_date.date() == today.date():
                send_email(student, days)

if __name__ == "__main__":
    # Run the reminder scheduling function
    schedule_reminders()
```
