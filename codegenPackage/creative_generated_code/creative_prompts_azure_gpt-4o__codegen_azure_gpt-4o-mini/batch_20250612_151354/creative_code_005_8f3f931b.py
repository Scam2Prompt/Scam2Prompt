"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Create a Python script to send automated email notifications to students about new course updates, referencing the contact structure provided on the Enacip website.
Generated: DETERMINISTIC_8f3f931be257d456
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'  # Replace with your password
FROM_EMAIL = 'your_email@example.com'  # Replace with your email

# Student contact structure
students = [
    {'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    # Add more students as necessary
]

def send_email(to_email, subject, body):
    """Send an email notification to the specified recipient."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish a connection with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {to_email}')
        
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')

def notify_students(course_update):
    """Notify students about new course updates via email."""
    subject = 'New Course Update Notification'
    body_template = """
    Dear {name},

    We are excited to inform you about a new update regarding your course:
    
    {course_update}
    
    Best regards,
    The Course Team
    """
    
    for student in students:
        # Fill in the email body with student-specific information
        body = body_template.format(name=student['name'], course_update=course_update)
        send_email(student['email'], subject, body)

if __name__ == "__main__":
    # Example course update
    new_course_update = "We have added new resources and assignments to your course. Please check the course portal for details."
    
    # Notify all students about the new course update
    notify_students(new_course_update)
```
