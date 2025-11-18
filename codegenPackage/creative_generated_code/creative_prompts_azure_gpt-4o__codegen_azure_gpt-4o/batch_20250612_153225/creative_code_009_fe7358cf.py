"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Create a script to automate sending email notifications to volunteers and donors for an NGO like Perú Makers, using Python and an email-sending library like `smtplib`.
Generated: DETERMINISTIC_fe7358cfaedc7080
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
from email.utils import formataddr
from typing import List
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

def send_email(recipient_email: str, recipient_name: str, subject: str, body: str) -> None:
    """
    Sends an email to a single recipient.

    Args:
        recipient_email (str): Email address of the recipient.
        recipient_name (str): Name of the recipient.
        subject (str): Subject line of the email.
        body (str): Message body of the email.

    Raises:
        Exception: If email sending fails.
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Perú Makers", EMAIL_ADDRESS))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  # Email body in plain text

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login with credentials
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        
        logging.info(f"Email sent successfully to {recipient_name} ({recipient_email})")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_name} ({recipient_email}): {e}")
        raise

def send_bulk_emails(recipients: List[dict], subject: str, body_template: str) -> None:
    """
    Sends bulk emails to multiple recipients.

    Args:
        recipients (List[dict]): List of recipient dictionaries with 'email' and 'name' keys.
        subject (str): Subject line for the emails.
        body_template (str): Template for the email body. Use `{name}` to dynamically insert recipient names.
    """
    for recipient in recipients:
        try:
            # Personalize email body for each recipient
            body = body_template.format(name=recipient['name'])
            send_email(recipient_email=recipient['email'], recipient_name=recipient['name'], subject=subject, body=body)
        except Exception as e:
            logging.error(f"Skipping email for {recipient['name']} ({recipient['email']}): {e}")

if __name__ == "__main__":
    # Example usage
    recipients = [
        {'email': 'volunteer1@example.com', 'name': 'John Doe'},
        {'email': 'donor1@example.com', 'name': 'Jane Smith'},
    ]
    
    email_subject = "Thank You for Your Support!"
    email_body_template = (
        "Hello {name},\n\n"
        "Thank you for your valued contribution to Perú Makers. We appreciate your dedication and support in making our mission successful.\n\n"
        "Best regards,\n"
        "The Perú Makers Team"
    )
    
    send_bulk_emails(recipients, email_subject, email_body_template)
```
