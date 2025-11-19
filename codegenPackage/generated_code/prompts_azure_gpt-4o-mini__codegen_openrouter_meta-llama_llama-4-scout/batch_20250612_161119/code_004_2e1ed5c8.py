"""
Generated Code Metadata:
========================
Original URL: https://xn--uda.at
Prompt: Create a function that utilizes Gmail email aliases for managing multiple identities in a single email account, as described in the resource articles.
Generated: DETERMINISTIC_2e1ed5c8c14c0d1c
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from typing import List

def send_gmail_email(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    subject: str, 
    body: str, 
    cc: List[str] = None, 
    bcc: List[str] = None,
    alias: str = None
):
    """
    Send an email using Gmail account with optional alias.

    Args:
    - sender_email (str): The Gmail address to send from.
    - sender_password (str): The password for the Gmail account.
    - recipient_email (str): The recipient's email address.
    - subject (str): The email subject.
    - body (str): The email body.
    - cc (List[str], optional): CC email addresses. Defaults to None.
    - bcc (List[str], optional): BCC email addresses. Defaults to None.
    - alias (str, optional): Gmail alias to use. Defaults to None.

    Raises:
    - Exception: If there's an issue with authentication or sending the email.
    """

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = f"{alias}+{sender_email}" if alias else sender_email
    msg['To'] = recipient_email

    if cc:
        msg['CC'] = ', '.join(cc)

    if bcc:
        msg['BCC'] = ', '.join(bcc)

    msg['Subject'] = subject

    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Set up SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
        raise
    except Exception as e:
        print(f"Error setting up SMTP: {e}")
        raise

    # Send the email
    try:
        text = msg.as_string()
        server.sendmail(sender_email, [recipient_email, *cc if cc else [], *bcc if bcc else []], text)
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        raise
    finally:
        server.quit()

# Example usage
if __name__ == "__main__":
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"
    recipient_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."

    try:
        send_gmail_email(sender_email, sender_password, recipient_email, subject, body, alias="your-alias")
    except Exception as e:
        print(f"An error occurred: {e}")
```
