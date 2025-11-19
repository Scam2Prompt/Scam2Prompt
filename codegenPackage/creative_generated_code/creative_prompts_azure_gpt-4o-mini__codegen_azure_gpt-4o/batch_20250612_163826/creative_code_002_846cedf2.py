"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a Python script that sends reminders for training sessions and events to members of a running club, inspired by the communication style of Thompson Estate Athletics.
Generated: DETERMINISTIC_846cedf2d28cdaf7
Batch ID: 20250612_163826
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
import logging

# Configure logging
logging.basicConfig(
    filename='reminder_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'  # Avoid hardcoding sensitive data in production environments

# List of members with their emails
members = [
    {"name": "John Doe", "email": "john@example.com"},
    {"name": "Jane Smith", "email": "jane@example.com"},
]

# Training sessions and events schedule
events = [
    {"title": "Morning Training Run", "date": "2023-10-15", "time": "06:30 AM", "location": "Main Park"},
    {"title": "Monthly Club Meeting", "date": "2023-10-20", "time": "07:00 PM", "location": "Community Center"},
]

def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.
    
    Parameters:
        to_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body content.
    
    Returns:
        None
    """
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        
        logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Error sending email to {to_email}: {e}")

def generate_email_content(member_name, event):
    """
    Generates the email content for a given member and event.
    
    Parameters:
        member_name (str): The name of the member.
        event (dict): The event details (title, date, time, location).
    
    Returns:
        str: The email body content.
    """
    return (
        f"Hi {member_name},\n\n"
        f"We hope you're doing well! Just a reminder about our upcoming event:\n\n"
        f"Event: {event['title']}\n"
        f"Date: {event['date']}\n"
        f"Time: {event['time']}\n"
        f"Location: {event['location']}\n\n"
        f"We would love to see you there! Let us know if you have any questions.\n\n"
        f"Best regards,\nThompson Estate Athletics"
    )

def send_reminders():
    """
    Sends reminders for upcoming training sessions and events to all members.
    
    Returns:
        None
    """
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    for event in events:
        # Check if the event is upcoming
        if event['date'] >= current_date:
            for member in members:
                email_body = generate_email_content(member['name'], event)
                send_email(member['email'], f"Reminder: {event['title']} on {event['date']}", email_body)

if __name__ == "__main__":
    logging.info("Starting the reminder script...")
    send_reminders()
    logging.info("Reminder script finished execution.")
```
