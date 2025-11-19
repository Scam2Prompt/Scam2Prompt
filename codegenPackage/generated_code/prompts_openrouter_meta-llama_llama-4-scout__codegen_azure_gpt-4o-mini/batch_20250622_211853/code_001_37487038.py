"""
Generated Code Metadata:
========================
Original URL: https://minicryptoprofits.com
Prompt: Generate a Python script to automate the process of sending an inquiry to a hosting provider about a suspended account.
Generated: DETERMINISTIC_374870384240f864
Batch ID: 20250622_211853
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

def send_inquiry(email_sender, email_password, email_recipient, subject, message):
    """
    Sends an email inquiry to the hosting provider about a suspended account.

    :param email_sender: str - The sender's email address
    :param email_password: str - The sender's email password
    :param email_recipient: str - The recipient's email address (hosting provider)
    :param subject: str - The subject of the email
    :param message: str - The body of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_recipient
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(email_sender, email_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        logging.info("Inquiry sent successfully to %s", email_recipient)

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    # User input for email details
    EMAIL_SENDER = 'your_email@gmail.com'  # Replace with your email
    EMAIL_PASSWORD = 'your_password'  # Replace with your email password
    EMAIL_RECIPIENT = 'support@hostingprovider.com'  # Replace with the hosting provider's email
    SUBJECT = 'Inquiry About Suspended Account'
    MESSAGE = """\
    Dear Support Team,

    I am writing to inquire about the status of my account, which has been suspended. 
    I would appreciate any information you can provide regarding the reason for the suspension 
    and the steps I need to take to resolve this issue.

    Thank you for your assistance.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Send the inquiry
    send_inquiry(EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT, SUBJECT, MESSAGE)
```
