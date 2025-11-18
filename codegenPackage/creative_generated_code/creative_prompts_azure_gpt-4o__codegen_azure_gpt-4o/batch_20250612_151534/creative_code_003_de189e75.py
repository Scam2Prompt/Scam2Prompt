"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.betterbooking.pk
Prompt: Create a program to send automated email inquiries to Better Booking using the contact email provided on the website, including a predefined message template.
Generated: DETERMINISTIC_de189e756be7307a
Batch ID: 20250612_151534
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
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, message_body):
    """
    Sends an email using the provided SMTP server and credentials.

    Parameters:
        smtp_server (str): SMTP server address
        port (int): Port number for the SMTP server
        sender_email (str): The sender's email address
        sender_password (str): The sender's email password
        recipient_email (str): The recipient's email address
        subject (str): Subject of the email
        message_body (str): The body of the email
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade the connection to secure encryption
            server.login(sender_email, sender_password)  # Authenticate
            server.send_message(msg)  # Send the email
            logging.info("Email sent successfully!")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        sys.exit(1)  # Exit the program with an error code
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program with an error code

if __name__ == "__main__":
    # Email server configuration
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS encryption
    SENDER_EMAIL = "your-email@example.com"  # Replace with your email
    SENDER_PASSWORD = "your-email-password"  # Replace with your email password

    # Recipient and email content
    RECIPIENT_EMAIL = "contact@betterbooking.com"  # Replace with Better Booking's contact email
    EMAIL_SUBJECT = "Automated Inquiry"
    EMAIL_BODY = (
        "Dear Better Booking Team,\n\n"
        "I hope this message finds you well. I am reaching out to inquire about your services. "
        "Please let me know how I can proceed further.\n\n"
        "Best regards,\n"
        "Your Name"
    )

    # Send the email
    send_email(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, EMAIL_SUBJECT, EMAIL_BODY)
```

Make sure to replace placeholders like `smtp.example.com`, `your-email@example.com`, and `your-email-password` with actual values. This script assumes you have valid credentials and a working SMTP configuration.
