"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afunabb.cl
Prompt: Write a Python script that automates the process of sending notifications to university employees about upcoming training activities and support services provided by associations like AFUNABB Chillán.
Generated: DETERMINISTIC_13944a6e0bdef348
Batch ID: 20250612_161231
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
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
USERNAME = os.getenv('EMAIL_USERNAME')  # Your email username
PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your email password

# List of employees to notify
employees = [
    {'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    # Add more employees as needed
]

# Upcoming training activities
training_activities = [
    {
        'title': 'Python Programming Basics',
        'date': '2023-11-15',
        'time': '10:00 AM',
        'location': 'Room 101'
    },
    {
        'title': 'Data Analysis with Pandas',
        'date': '2023-11-20',
        'time': '1:00 PM',
        'location': 'Room 202'
    },
]

# Function to create the email body
def create_email_body(employee_name, activities):
    body = f"Dear {employee_name},\n\n"
    body += "We would like to inform you about the upcoming training activities:\n\n"
    for activity in activities:
        body += f"Title: {activity['title']}\n"
        body += f"Date: {activity['date']}\n"
        body += f"Time: {activity['time']}\n"
        body += f"Location: {activity['location']}\n\n"
    body += "Best regards,\nAFUNABB Chillán"
    return body

# Function to send email notifications
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

        logging.info(f"Email successfully sent to {to_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# Main function to automate notification sending
def notify_employees():
    subject = "Upcoming Training Activities and Support Services"
    
    for employee in employees:
        name = employee['name']
        email = employee['email']
        body = create_email_body(name, training_activities)
        send_email(email, subject, body)

if __name__ == "__main__":
    notify_employees()
```

**Note:** Ensure to set the environment variables `EMAIL_USERNAME` and `EMAIL_PASSWORD` for the script to run successfully. Adjust the SMTP server and port according to your email service provider.
