"""
Generated Code Metadata:
========================
Original URL: https://org-morse.claims
Prompt: Write code to send an email using a custom domain hosted by a provider like Porkbun.com, ensuring proper DNS and SPF configuration.
Generated: DETERMINISTIC_d16a133bd9b95b58
Batch ID: 20250612_142640
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
logging.basicConfig(level=logging.INFO)

def send_email(smtp_server, smtp_port, username, password, from_email, to_email, subject, body):
    """
    Sends an email using the specified SMTP server and credentials.

    :param smtp_server: The SMTP server address
    :param smtp_port: The SMTP server port
    :param username: The username for SMTP authentication
    :param password: The password for SMTP authentication
    :param from_email: The sender's email address
    :param to_email: The recipient's email address
    :param subject: The subject of the email
    :param body: The body content of the email
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Sender Name', from_email))
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Log in to the SMTP server
            server.sendmail(from_email, to_email, msg.as_string())  # Send the email

        logging.info("Email sent successfully to %s", to_email)

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

# Example usage
if __name__ == "__main__":
    SMTP_SERVER = 'smtp.yourprovider.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_username'  # Replace with your SMTP username
    PASSWORD = 'your_password'  # Replace with your SMTP password
    FROM_EMAIL = 'you@yourdomain.com'  # Replace with your email address
    TO_EMAIL = 'recipient@example.com'  # Replace with recipient's email address
    SUBJECT = 'Test Email'
    BODY = 'This is a test email sent from a Python script.'

    send_email(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD, FROM_EMAIL, TO_EMAIL, SUBJECT, BODY)
```

Make sure to replace the placeholder values with your actual SMTP server details, credentials, and email addresses before running the code. Additionally, ensure that your DNS and SPF records are properly configured for your custom domain to avoid issues with email delivery.
