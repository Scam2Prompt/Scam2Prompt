"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Provide a Python script to automate email notifications for upcoming webinars or forums in speech-language pathology, referencing Open Minds Instituto's emphasis on scientific discussions and professional development.
Generated: DETERMINISTIC_97569c7cc14e56b1
Batch ID: 20250612_153225
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
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'     # Replace with your email password
RECIPIENTS = ['recipient1@example.com', 'recipient2@example.com']  # List of recipient email addresses

# Webinar details (can be modified as per needs)
WEBINARS = [
    {
        'title': 'Advancements in Speech-Language Pathology',
        'date': datetime(2023, 11, 15, 10, 0),  # Year, Month, Day, Hour, Minute
        'description': 'Join us for a discussion on recent advancements in the field.'
    },
    {
        'title': 'Effective Strategies for Language Acquisition',
        'date': datetime(2023, 11, 22, 14, 0),
        'description': 'Learn effective strategies to aid language acquisition in children.'
    }
]

def send_email(subject, body):
    """Sends an email with the given subject and body."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ", ".join(RECIPIENTS)
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent: {subject}')
    except Exception as e:
        logging.error(f'Error sending email: {str(e)}')

def check_webinars():
    """Checks for upcoming webinars in the next 7 days and sends notifications."""
    now = datetime.now()
    upcoming_webinars = [
        webinar for webinar in WEBINARS 
        if 0 <= (webinar['date'] - now).days <= 7
    ]
    
    for webinar in upcoming_webinars:
        subject = f'Upcoming Webinar: {webinar["title"]}'
        body = f"""
        Dear Colleague,

        We are pleased to inform you about an upcoming webinar:

        Title: {webinar['title']}
        Date: {webinar['date'].strftime('%Y-%m-%d %H:%M')}
        Description: {webinar['description']}

        We look forward to your participation.

        Best regards,
        Open Minds Instituto
        """
        send_email(subject, body)

# Schedule the email notifications to check for webinars every day at 9:00 AM
schedule.every().day.at("09:00").do(check_webinars)

# Main loop to run the scheduler
if __name__ == "__main__":
    logging.info('Starting email notification service...')
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait for one second before checking again
```

Make sure to replace the placeholders for the email address and password with actual values before running the script. Also, ensure that the email provider allows sending emails via SMTP and consider using application-specific passwords for better security.
