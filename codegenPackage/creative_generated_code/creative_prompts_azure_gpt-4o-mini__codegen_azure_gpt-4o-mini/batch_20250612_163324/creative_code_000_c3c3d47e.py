"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zelenina-hrbek.cz
Prompt: Generate a Python script that sends an email to info@zelenina-hrbek.cz with a subject line "Inquiry about new website".
Generated: DETERMINISTIC_c3c3d47e47905bed
Batch ID: 20250612_163324
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

# Constants for the email configuration
SMTP_SERVER = 'smtp.example.com'  # Update with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
SMTP_USER = 'your_email@example.com'  # Update with your email
SMTP_PASSWORD = 'your_password'  # Update with your email password
TO_EMAIL = 'info@zelenina-hrbek.cz'
SUBJECT = 'Inquiry about new website'
BODY = 'Hello,\n\nI would like to inquire about your new website.\n\nBest regards,\nYour Name'

def send_email(to_email, subject, body):
    """
    Sends an email using the specified SMTP server.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Raises:
        Exception: Raises an exception if an error occurs while sending the email.
    """
    try:
        # Create a multipart email message
        message = MIMEMultipart()
        message['From'] = SMTP_USER
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the body text to the email message
        message.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SMTP_USER, SMTP_PASSWORD)  # Log in to the server
            server.send_message(message)  # Send the email

        print(f"Email sent successfully to {to_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    send_email(TO_EMAIL, SUBJECT, BODY)
```
