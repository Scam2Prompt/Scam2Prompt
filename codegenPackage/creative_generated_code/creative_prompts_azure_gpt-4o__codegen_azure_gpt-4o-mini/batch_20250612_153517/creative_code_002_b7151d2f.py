"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeworkinggdeadd.pages.dev
Prompt: Generate a script to send automated emails to "[email protected]" and "[email protected]" for inquiries about "The Working Dead" FREE MINT process.
Generated: DETERMINISTIC_b7151d2ffd915d82
Batch ID: 20250612_153517
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
from typing import List

# Define constants for the email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                    # Commonly used port for SMTP
USERNAME = 'your_email@example.com' # Your email address
PASSWORD = 'your_email_password'     # Your email password

# List of recipients
RECIPIENTS: List[str] = [
    'recipient1@example.com',
    'recipient2@example.com'
]

# Subject of the email
SUBJECT = "Inquiry about The Working Dead FREE MINT process"

# Body of the email
BODY = """
Hello,

I would like to inquire about The Working Dead FREE MINT process.

Thank you,
Automated Email System
"""

def send_email(to_emails: List[str], subject: str, body: str) -> None:
    """
    Sends an email to the specified recipients.

    :param to_emails: List of recipient email addresses
    :param subject: Subject of the email
    :param body: Body of the email
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(USERNAME, PASSWORD)  # Log in to the server
            server.sendmail(USERNAME, to_emails, msg.as_string())  # Send the email
            print(f"Email successfully sent to: {', '.join(to_emails)}")
    
    except smtplib.SMTPException as e:
        # Handle any SMTP-related errors
        print(f"Error occurred while sending email: {e}")

if __name__ == "__main__":
    # Send the email when the script is executed
    send_email(RECIPIENTS, SUBJECT, BODY)
```
