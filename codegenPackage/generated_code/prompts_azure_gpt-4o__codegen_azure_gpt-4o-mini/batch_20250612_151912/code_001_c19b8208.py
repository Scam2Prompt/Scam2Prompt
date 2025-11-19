"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: Generate a Python script to send an email to the webmaster of a domain, using the example provided in the CentOS-WebPanel HTTP test page.
Generated: DETERMINISTIC_c19b8208976e50c3
Batch ID: 20250612_151912
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

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Sends an email using the specified SMTP server.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient's email address
    :param from_email: Sender's email address
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_user: SMTP username
    :param smtp_password: SMTP password
    :raises Exception: Raises an exception if sending the email fails
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Webmaster', from_email))
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise  # Re-raise the exception for further handling if needed

if __name__ == "__main__":
    # Email configuration
    SUBJECT = "Test Email from CentOS-WebPanel"
    BODY = "This is a test email sent from the CentOS-WebPanel HTTP test page."
    TO_EMAIL = "webmaster@example.com"  # Replace with the actual webmaster email
    FROM_EMAIL = "your_email@example.com"  # Replace with your email
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS
    SMTP_USER = "your_smtp_username"  # Replace with your SMTP username
    SMTP_PASSWORD = "your_smtp_password"  # Replace with your SMTP password

    # Send the email
    send_email(SUBJECT, BODY, TO_EMAIL, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
```
