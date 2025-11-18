"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write a script to automate sending email notifications to applicants of the Gauntlet Trust grants, informing them of their application status.
Generated: DETERMINISTIC_7cb63f1e20306d79
Batch ID: 20250612_150651
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
from typing import List, Dict
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SMTP_USER = 'your_email@example.com'  # Sender email address
SMTP_PASSWORD = 'your_password'  # Password for the sender email

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Send an email notification.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body content of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email sent successfully to {to_email}")
    
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def notify_applicants(applicants: List[Dict[str, str]]) -> None:
    """
    Notify applicants of their application status.

    :param applicants: List of dictionaries containing applicant information
    """
    for applicant in applicants:
        email = applicant.get('email')
        status = applicant.get('status')
        
        if email and status:
            subject = "Gauntlet Trust Grant Application Status"
            body = f"Dear Applicant,\n\nYour application status is: {status}\n\nThank you for your interest in the Gauntlet Trust grants."
            send_email(email, subject, body)
        else:
            logging.warning(f"Missing email or status for applicant: {applicant}")

if __name__ == "__main__":
    # Example applicant data
    applicants_data = [
        {'email': 'applicant1@example.com', 'status': 'Approved'},
        {'email': 'applicant2@example.com', 'status': 'Rejected'},
        {'email': 'applicant3@example.com', 'status': 'Pending'},
    ]

    # Notify all applicants
    notify_applicants(applicants_data)
```
