"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Create a script to test email sending functionality using Plesk's mail service test page.
Generated: DETERMINISTIC_9c3d7b5ec3e0af2d
Batch ID: 20250612_152827
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

# Configure logging for debugging and tracing
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_test_email(smtp_server, smtp_port, username, password, sender_email, recipient_email):
    """
    Sends a test email using Plesk's mail service.

    Args:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        username (str): The username for SMTP authentication.
        password (str): The password for SMTP authentication.
        sender_email (str): The email address sending the test email.
        recipient_email (str): The email address receiving the test email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Test Sender', sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = 'Test Email from Plesk Mail Service'

        # Email body
        body = "This is a test email sent to verify the email functionality using Plesk's mail service."
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email

        logging.info("Test email sent successfully to %s", recipient_email)
        return True

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
        return False

if __name__ == '__main__':
    # SMTP server settings (example values, adjust as needed)
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS
    USERNAME = 'your_username@example.com'  # Your SMTP username
    PASSWORD = 'your_password'  # Your SMTP password
    SENDER_EMAIL = 'your_sender@example.com'  # Your sender email address
    RECIPIENT_EMAIL = 'recipient@example.com'  # Recipient email address

    # Call the function to send a test email
    success = send_test_email(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD, SENDER_EMAIL, RECIPIENT_EMAIL)
    
    if success:
        print("Email sent successfully.")
    else:
        print("Email failed to send.")
```
