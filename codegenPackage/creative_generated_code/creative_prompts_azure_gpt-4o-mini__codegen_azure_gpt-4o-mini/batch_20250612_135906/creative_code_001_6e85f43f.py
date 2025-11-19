"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Write a Python script that sends an email to BCHDEkontakt@perrigo.com using SMTP, mimicking the communication methods mentioned in the Impressum of the Perrigo Claims site.
Generated: DETERMINISTIC_6e85f43f44a67818
Batch ID: 20250612_135906
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, sender_name, recipient_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    """
    Sends an email using the specified SMTP server.

    :param sender_email: Email address of the sender
    :param sender_name: Name of the sender
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body of the email
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_username: SMTP username for authentication
    :param smtp_password: SMTP password for authentication
    :raises Exception: Raises an exception if sending email fails
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for security
            server.login(smtp_username, smtp_password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise  # Re-raise the exception for further handling if needed

if __name__ == "__main__":
    # Email configuration
    SENDER_EMAIL = 'your_email@example.com'  # Replace with your email address
    SENDER_NAME = 'Your Name'  # Replace with your name
    RECIPIENT_EMAIL = 'BCHDEkontakt@perrigo.com'
    SUBJECT = 'Subject of the Email'
    BODY = 'This is the body of the email.'
    
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # SMTP port
    SMTP_USERNAME = 'your_smtp_username'  # Replace with your SMTP username
    SMTP_PASSWORD = 'your_smtp_password'  # Replace with your SMTP password

    try:
        send_email(SENDER_EMAIL, SENDER_NAME, RECIPIENT_EMAIL, SUBJECT, BODY, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)
    except Exception as e:
        logging.error("An error occurred while sending the email.")
```

Make sure to replace placeholders with actual values before running the script.
