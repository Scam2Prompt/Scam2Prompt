"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Write a Python script to send automated email responses to inquiries received via the contact form on the website, using the email address "contact@maraboutreconnu.com."
Generated: DETERMINISTIC_8505f2dd783354f2
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SENDER_EMAIL = 'contact@maraboutreconnu.com'
SENDER_PASSWORD = 'your_email_password'  # Replace with your email password

def send_email(recipient_email, subject, body):
    """
    Sends an email to the specified recipient.

    :param recipient_email: str - The email address of the recipient
    :param subject: str - The subject of the email
    :param body: str - The body of the email
    :raises Exception: If the email sending fails
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the server
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {recipient_email} with subject: "{subject}"')

    except Exception as e:
        logging.error(f'Failed to send email to {recipient_email}: {e}')
        raise

def respond_to_inquiry(inquiry):
    """
    Responds to a user inquiry by sending an automated email.

    :param inquiry: dict - A dictionary containing 'email', 'name', 'message' keys
    """
    recipient_email = inquiry.get('email')
    user_name = inquiry.get('name')
    user_message = inquiry.get('message')

    # Prepare the email content
    subject = 'Thank you for contacting us!'
    body = f"Dear {user_name},\n\nThank you for your inquiry. We have received your message:\n\n{user_message}\n\nBest regards,\nMarabout Reconnu"

    # Send the automated response
    send_email(recipient_email, subject, body)

# Example usage
if __name__ == '__main__':
    # Sample inquiry data to test the function
    sample_inquiry = {
        'email': 'user@example.com',
        'name': 'John Doe',
        'message': 'I am interested in your services.'
    }

    respond_to_inquiry(sample_inquiry)
```

**Note**: Make sure to replace `smtp.example.com` and `your_email_password` with the actual SMTP server and the password for the email account used to send emails.
