"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Write code to send automated email reminders for upcoming Driver CPC training sessions, using course details from CoLa Training Services.
Generated: DETERMINISTIC_dcaed22bc4e11f52
Batch ID: 20250612_154520
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send email reminders
def send_email_reminder(subject, recipient_email, body):
    """Send an email with the provided subject and body to the recipient."""
    try:
        # Email configuration
        sender_email = "your_email@example.com"  # Replace with your email
        password = "your_password"  # Replace with your email password
        smtp_server = "smtp.example.com"  # Replace with your SMTP server
        smtp_port = 587  # Common port for SMTP

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, password)
            server.send_message(msg)

        logging.info(f"Email sent to {recipient_email} with subject: '{subject}'")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {str(e)}")

# Function to generate email body for training session
def generate_email_body(course_details):
    """Generate the body of the email using course details."""
    body = (f"Dear Participant,\n\n"
            f"This is a reminder for your upcoming Driver CPC training session.\n\n"
            f"Course Title: {course_details['title']}\n"
            f"Date: {course_details['date'].strftime('%Y-%m-%d')}\n"
            f"Time: {course_details['time']}\n"
            f"Location: {course_details['location']}\n\n"
            f"We look forward to seeing you!\n\n"
            f"Best regards,\n"
            f"CoLa Training Services")
    return body

# Main function to check for upcoming training sessions
def check_and_send_reminders(courses):
    """Check courses for upcoming sessions and send reminders."""
    # Set a threshold for sending reminders (e.g., 3 days before the session)
    reminder_days = 3
    today = datetime.now()

    for course in courses:
        if today <= course['date'] <= today + timedelta(days=reminder_days):
            email_body = generate_email_body(course)
            send_email_reminder(f"Reminder: {course['title']} Training Session", 
                                 course['participant_email'], 
                                 email_body)

# Example course data
courses = [
    {
        'title': 'Driver CPC Module 1',
        'date': datetime(2023, 10, 15),  # Replace with actual course date
        'time': '09:00 AM',
        'location': 'CoLa Training Center',
        'participant_email': 'participant@example.com'  # Replace with actual participant email
    },
    {
        'title': 'Driver CPC Module 2',
        'date': datetime(2023, 10, 20),
        'time': '09:00 AM',
        'location': 'CoLa Training Center',
        'participant_email': 'another_participant@example.com'  # Replace with actual participant email
    }
]

# Execute the reminder check
if __name__ == "__main__":
    check_and_send_reminders(courses)
```
