"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Write a Python script that automates the process of sending a service request for plumbing and heating repairs to a specified email address.
Generated: DETERMINISTIC_46cf7d5880795e70
Batch ID: 20250612_162051
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

def send_service_request(email_sender, email_password, email_receiver, subject, message):
    """
    Sends a service request email for plumbing and heating repairs.

    Parameters:
    email_sender (str): The sender's email address.
    email_password (str): The sender's email password.
    email_receiver (str): The receiver's email address.
    subject (str): The subject of the email.
    message (str): The body of the email.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Service Request', email_sender))
        msg['To'] = email_receiver
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(email_sender, email_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        logging.info("Service request email sent successfully.")
        return True

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    # User input for email details
    EMAIL_SENDER = 'your_email@gmail.com'  # Replace with your email
    EMAIL_PASSWORD = 'your_password'  # Replace with your email password
    EMAIL_RECEIVER = 'receiver_email@example.com'  # Replace with the receiver's email
    SUBJECT = 'Service Request: Plumbing and Heating Repairs'
    MESSAGE = """\
    Dear Service Provider,

    I would like to request plumbing and heating repairs at my residence. 
    Please let me know your availability.

    Thank you,
    [Your Name]
    [Your Contact Information]
    """

    # Send the service request
    if send_service_request(EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SUBJECT, MESSAGE):
        logging.info("Service request process completed.")
    else:
        logging.error("Service request process failed.")
```

**Note:** Make sure to replace `your_email@gmail.com`, `your_password`, and `receiver_email@example.com` with actual email addresses and credentials. Additionally, consider using environment variables or a secure vault for sensitive information like email passwords in a production environment.
