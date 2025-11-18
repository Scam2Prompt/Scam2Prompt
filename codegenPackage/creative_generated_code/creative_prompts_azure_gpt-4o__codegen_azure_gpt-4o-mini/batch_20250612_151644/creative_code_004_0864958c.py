"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Develop a script to send an email inquiry to info@stts.ch for private transfer bookings between Geneva and Morzine, using the contact details provided on the website.
Generated: DETERMINISTIC_0864958c6a33e5e3
Batch ID: 20250612_151644
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

def send_email(sender_email, sender_name, recipient_email, subject, body):
    """
    Sends an email using the SMTP protocol.

    :param sender_email: The email address of the sender
    :param sender_name: The name of the sender
    :param recipient_email: The email address of the recipient
    :param subject: The subject of the email
    :param body: The body of the email
    :raises Exception: Raises an exception if the email fails to send
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
            server.starttls()  # Secure the connection
            server.login(sender_email, 'your_password')  # Use actual email and password
            server.send_message(msg)
            logging.info("Email sent successfully to %s", recipient_email)
    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise

def main():
    # Email details
    sender_email = 'your_email@example.com'  # Replace with your email
    sender_name = 'Your Name'  # Replace with your name
    recipient_email = 'info@stts.ch'
    subject = 'Inquiry for Private Transfer Booking'
    body = (
        "Dear STTS Team,\n\n"
        "I would like to inquire about booking a private transfer between Geneva and Morzine. "
        "Please provide any available options and pricing details.\n\n"
        "Thank you!\n\n"
        "Best regards,\n"
        f"{sender_name}"
    )

    try:
        send_email(sender_email, sender_name, recipient_email, subject, body)
    except Exception as e:
        logging.critical("Terminating the script due to an error: %s", e)

if __name__ == "__main__":
    main()
```
