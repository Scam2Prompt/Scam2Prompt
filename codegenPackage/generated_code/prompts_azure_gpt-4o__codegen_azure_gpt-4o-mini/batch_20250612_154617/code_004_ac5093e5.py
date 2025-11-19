"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Develop a script to send automated email inquiries to "Гарант" about bulk orders for automotive glass installation materials, using the contact information provided on their website.
Generated: DETERMINISTIC_ac5093e52941f5e3
Batch ID: 20250612_154617
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

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'contact@garant.com'  # Replace with the actual contact email from Гарант

def create_email(subject, body):
    """Create an email message."""
    msg = MIMEMultipart()
    msg['From'] = formataddr(('Your Name', USERNAME))
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    return msg

def send_email(msg):
    """Send an email message using SMTP."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
            logging.info("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

def main():
    """Main function to send an automated email inquiry."""
    subject = "Inquiry about Bulk Orders for Automotive Glass Installation Materials"
    body = (
        "Dear Гарант Team,\n\n"
        "I hope this message finds you well. I am writing to inquire about bulk orders for automotive glass installation materials. "
        "Could you please provide me with the pricing, availability, and any other relevant information?\n\n"
        "Thank you for your assistance.\n\n"
        "Best regards,\n"
        "Your Name\n"
        "Your Company\n"
        "Your Contact Information"
    )

    # Create the email
    email_message = create_email(subject, body)

    # Send the email
    send_email(email_message)

if __name__ == "__main__":
    main()
```
