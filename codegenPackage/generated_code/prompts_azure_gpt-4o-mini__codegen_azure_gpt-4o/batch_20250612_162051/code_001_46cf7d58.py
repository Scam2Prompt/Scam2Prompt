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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_service_request(email_host, email_port, sender_email, sender_password, recipient_email, subject, message_body):
    """
    Sends a service request email for plumbing and heating repairs.

    Args:
        email_host (str): SMTP server host.
        email_port (int): SMTP server port.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        message_body (str): Body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()  # Upgrade the connection to secure (TLS)
            logging.info("Logging in to the SMTP server...")
            server.login(sender_email, sender_password)

            # Send the email
            logging.info("Sending the email...")
            server.send_message(msg)
            logging.info("Email sent successfully.")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Configuration for the email
    EMAIL_HOST = "smtp.example.com"  # Replace with your SMTP server
    EMAIL_PORT = 587  # Common port for TLS
    SENDER_EMAIL = "your_email@example.com"  # Replace with your email address
    SENDER_PASSWORD = "your_password"  # Replace with your email password
    RECIPIENT_EMAIL = "recipient_email@example.com"  # Replace with the recipient's email address
    SUBJECT = "Service Request: Plumbing and Heating Repairs"
    MESSAGE_BODY = (
        "Dear Service Team,\n\n"
        "I am requesting plumbing and heating repairs at my property. Please contact me to schedule an appointment.\n\n"
        "Thank you,\n"
        "Your Name"
    )

    # Send the service request email
    send_service_request(
        EMAIL_HOST,
        EMAIL_PORT,
        SENDER_EMAIL,
        SENDER_PASSWORD,
        RECIPIENT_EMAIL,
        SUBJECT,
        MESSAGE_BODY
    )
```
