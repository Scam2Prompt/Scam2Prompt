"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Create a Python script to send automated email reminders to Nzotho FET College students about upcoming semester start dates and deadlines.
Generated: DETERMINISTIC_14592bcd580786c0
Batch ID: 20250612_153246
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Usually 587 for TLS
SMTP_USER = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'  # Replace with your email password

# Reminder details
REMINDER_SUBJECT = "Upcoming Semester Start Dates and Deadlines"
REMINDER_BODY_TEMPLATE = """\
Dear Student,

This is a reminder about the upcoming semester. Please note the following important dates:

- Semester Start Date: {start_date}
- Registration Deadline: {registration_deadline}
- Payment Deadline: {payment_deadline}

Make sure to mark these dates in your calendar!

Best regards,
Nzotho FET College
"""

# List of students with their email addresses
students = [
    {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'},
    {'name': 'Bob Smith', 'email': 'bob.smith@example.com'},
    # Add more students as needed
]

# Semester dates (Example dates)
SEMESTER_START_DATE = '2024-01-15'
REGISTRATION_DEADLINE = '2024-01-10'
PAYMENT_DEADLINE = '2024-01-12'


def send_email(to_email, subject, body):
    """Send an email to the specified recipient."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS for security
            server.login(SMTP_USER, SMTP_PASSWORD)  # Log in to SMTP server
            server.sendmail(SMTP_USER, to_email, msg.as_string())  # Send the email

        logging.info(f'Email sent successfully to {to_email}')
        
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')


def main():
    """Main function to send reminders to all students."""
    # Prepare the reminder body with actual dates
    reminder_body = REMINDER_BODY_TEMPLATE.format(
        start_date=SEMESTER_START_DATE,
        registration_deadline=REGISTRATION_DEADLINE,
        payment_deadline=PAYMENT_DEADLINE
    )

    # Send email to each student
    for student in students:
        student_email = student['email']
        send_email(student_email, REMINDER_SUBJECT, reminder_body)


if __name__ == '__main__':
    # Run the main function
    main()
```

**Important Notes:**
- Replace `smtp.example.com`, `your_email@example.com`, and `your_password` with your actual SMTP server details and credentials.
- Ensure that you have the necessary packages installed (`smtplib`, `email`, etc.), which are included in the Python standard library.
- Update the student email list and semester dates as required for your application.
