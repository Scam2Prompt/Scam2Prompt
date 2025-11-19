"""
Generated Code Metadata:
========================
Original URL: https://cancellationflights.com
Prompt: Write a Python script to automate sending an email to a hosting provider for account suspension issues related to flight cancellation services.
Generated: DETERMINISTIC_c47aee077af432c9
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, sender_name, recipient_email, subject, body, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Sends an email using the specified SMTP server.

    :param sender_email: Email address of the sender
    :param sender_name: Name of the sender
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body content of the email
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_user: SMTP username
    :param smtp_password: SMTP password
    :raises Exception: Raises an exception if sending the email fails
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info("Email sent successfully to %s", recipient_email)

    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise

if __name__ == "__main__":
    # Email configuration
    SENDER_EMAIL = "your_email@example.com"
    SENDER_NAME = "Your Name"
    RECIPIENT_EMAIL = "provider@example.com"
    SUBJECT = "Account Suspension Issue - Flight Cancellation Services"
    BODY = """\
Dear Hosting Provider,

I am writing to address an urgent issue regarding the suspension of my account related to flight cancellation services. 
Please provide clarification on the reasons for this suspension and any necessary steps I need to take to resolve the matter.

Thank you for your prompt attention to this issue.

Best regards,
Your Name
"""
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = "your_password"

    # Send the email
    send_email(SENDER_EMAIL, SENDER_NAME, RECIPIENT_EMAIL, SUBJECT, BODY, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
```
