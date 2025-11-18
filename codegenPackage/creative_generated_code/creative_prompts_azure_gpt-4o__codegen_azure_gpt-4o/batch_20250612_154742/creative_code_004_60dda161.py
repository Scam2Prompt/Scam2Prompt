"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_60dda1616b58cf08
Batch ID: 20250612_154742
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
import os

# Configuration for email server and accounts
SMTP_SERVER = "smtp.yourdomain.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically, 587 for TLS or 465 for SSL
EMAIL_USERNAME = "your_email@yourdomain.com"  # Replace with your email username
EMAIL_PASSWORD = "your_password"  # Replace with your email password
DEFAULT_SENDER_NAME = "Your Name"  # Replace with your sender name

# Function to send an email
def send_email(recipient_email, subject, body, sender_name=DEFAULT_SENDER_NAME):
    """
    Sends an email to the specified recipient.

    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body content of the email.
        sender_name (str): Sender's name. Defaults to DEFAULT_SENDER_NAME.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, EMAIL_USERNAME))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Log in to the server
            server.send_message(msg)  # Send the email

        print(f"Email successfully sent to {recipient_email}")
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace with recipient details
    recipient = "recipient@domain.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."

    # Send the email
    send_email(recipient, subject, body)
```

### Notes:
- Replace the placeholders (`SMTP_SERVER`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`, etc.) with actual credentials from your hosting service (e.g., iFastNet).
- Ensure your hosting account allows SMTP access and has valid credentials for the email accounts you're using.
- Avoid hardcoding sensitive information in production; use environment variables or a secure secrets manager.
