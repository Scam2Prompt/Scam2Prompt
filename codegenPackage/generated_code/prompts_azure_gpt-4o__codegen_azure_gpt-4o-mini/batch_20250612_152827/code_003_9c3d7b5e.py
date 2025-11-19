"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Create a script to test email sending functionality using Plesk's mail service test page.
Generated: DETERMINISTIC_9c3d7b5ec3e0af2d
Batch ID: 20250612_152827
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_test_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email):
    """
    Sends a test email to verify the email sending functionality.

    :param smtp_server: The SMTP server address
    :param smtp_port: The SMTP server port
    :param sender_email: The email address of the sender
    :param sender_password: The password for the sender's email account
    :param recipient_email: The email address of the recipient
    :return: None
    """
    try:
        # Create the email content
        subject = "Test Email from Plesk Mail Service"
        body = "This is a test email to verify the email sending functionality."
        
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email

        logging.info("Test email sent successfully to %s", recipient_email)

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    # Configuration for the email sending
    SMTP_SERVER = "smtp.yourdomain.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    SENDER_EMAIL = "your_email@yourdomain.com"  # Replace with your sender email
    SENDER_PASSWORD = "your_password"  # Replace with your email password
    RECIPIENT_EMAIL = "recipient_email@example.com"  # Replace with the recipient email

    # Send the test email
    send_test_email(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
```
