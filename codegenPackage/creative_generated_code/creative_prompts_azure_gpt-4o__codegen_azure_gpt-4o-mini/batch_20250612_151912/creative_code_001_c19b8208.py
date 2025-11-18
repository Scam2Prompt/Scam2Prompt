"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Generate a Python script to send an email to the webmaster of a domain, using the example provided in the CentOS-WebPanel HTTP test page.
Generated: DETERMINISTIC_c19b8208976e50c3
Batch ID: 20250612_151912
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
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, sender_name, recipient_email, subject, body, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Sends an email using the specified SMTP server.

    :param sender_email: Email address of the sender
    :param sender_name: Name of the sender
    :param recipient_email: Email address of the recipient (webmaster)
    :param subject: Subject of the email
    :param body: Body content of the email
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_user: SMTP user for authentication
    :param smtp_password: SMTP password for authentication
    :raises Exception: Raises an exception for any errors during email sending
    """
    
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        logging.info("Email sent successfully to %s", recipient_email)

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
        raise Exception("Email sending failed") from e

if __name__ == "__main__":
    # Email details
    SENDER_EMAIL = "your_email@example.com"
    SENDER_NAME = "Your Name"
    RECIPIENT_EMAIL = "webmaster@example.com"  # Replace with the actual webmaster email
    SUBJECT = "Test Email from Python Script"
    BODY = "This is a test email sent from a Python script."
    
    # SMTP server configuration
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS
    SMTP_USER = "your_smtp_user"  # Replace with your SMTP username
    SMTP_PASSWORD = "your_smtp_password"  # Replace with your SMTP password

    # Send the email
    send_email(SENDER_EMAIL, SENDER_NAME, RECIPIENT_EMAIL, SUBJECT, BODY, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
```
