"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Write a script to automate email notifications for a clinical laboratory, notifying patients of their test results or appointment confirmations, using the contact information provided on the website.
Generated: DETERMINISTIC_ed7bbefc89cf2197
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib  # For sending emails
from email.mime.text import MIMEText  # For creating the email body
from email.mime.multipart import MIMEMultipart  # For creating a multipart email
import logging  # For logging errors and information
import os  # For environment variable access

# Configuration for the email server
SMTP_SERVER = os.getenv('SMTP_SERVER')  # SMTP server address
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # SMTP server port (default is 587)
SMTP_USER = os.getenv('SMTP_USER')  # SMTP username
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')  # SMTP password

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_email(subject, body, recipient_email):
    """Create an email message.

    Args:
        subject (str): Subject of the email.
        body (str): Body content of the email.
        recipient_email (str): Recipient's email address.

    Returns:
        MIMEMultipart: Email message.
    """
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

def send_email(subject, body, recipient_email):
    """Send an email notification.

    Args:
        subject (str): Subject of the email.
        body (str): Body content of the email.
        recipient_email (str): Recipient's email address.

    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create email message
        msg = create_email(subject, body, recipient_email)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USER, SMTP_PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {recipient_email} successfully.')
    except Exception as e:
        logging.error(f'Failed to send email to {recipient_email}: {e}')
        raise  # Re-raise the exception for further handling

def notify_patients(test_results):
    """Notify patients about their test results or appointment confirmations.

    Args:
        test_results (list of dict): List containing patient information and their test results. 
                                      Each dict should have 'email', 'subject', and 'body' keys.
    """
    for result in test_results:
        try:
            send_email(result['subject'], result['body'], result['email'])
        except Exception as e:
            logging.error(f'Error notifying patient {result["email"]}: {e}')

if __name__ == "__main__":
    # Sample test results for demonstration
    test_results = [
        {
            'email': 'patient1@example.com',
            'subject': 'Your Test Results are Ready',
            'body': 'Dear Patient, your test results are now available. Please log in to your account to view them.'
        },
        {
            'email': 'patient2@example.com',
            'subject': 'Appointment Confirmation',
            'body': 'Dear Patient, your appointment is confirmed for tomorrow at 10 AM.'
        }
    ]

    # Notify patients
    notify_patients(test_results)
```
