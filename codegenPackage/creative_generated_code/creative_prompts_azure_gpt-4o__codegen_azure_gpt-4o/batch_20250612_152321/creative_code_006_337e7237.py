"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Create a script to automate sending inquiries to APN Hardware's contact email for custom manufacturing of fasteners, including specifications like screw type and size.
Generated: DETERMINISTIC_337e7237d2cf3f8f
Batch ID: 20250612_152321
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Email settings
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
SENDER_NAME = "Your Name"
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Use environment variables for sensitive information
RECIPIENT_EMAIL = "contact@apnhardware.com"  # Replace with APN Hardware's contact email

# Inquiry details
INQUIRY_SUBJECT = "Custom Manufacturing Inquiry for Fasteners"
INQUIRY_BODY_TEMPLATE = """
Dear APN Hardware Team,

I am reaching out to inquire about custom manufacturing of fasteners with the following specifications:

- Screw Type: {screw_type}
- Size: {size}

Please let me know if you require any additional information to process this inquiry.

Thank you,
{sender_name}
"""

def send_inquiry(screw_type, size):
    """
    Sends an inquiry email to APN Hardware for custom manufacturing of fasteners.

    Args:
        screw_type (str): Type of screw (e.g., "Phillips", "Flat Head").
        size (str): Size of the screw (e.g., "M4", "M6 x 40mm").
    """
    try:
        # Prepare the email body
        email_body = INQUIRY_BODY_TEMPLATE.format(screw_type=screw_type, size=size, sender_name=SENDER_NAME)

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = INQUIRY_SUBJECT

        # Attach the email body
        msg.attach(MIMEText(email_body, "plain"))

        # Establish connection to SMTP server
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the SMTP server
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())  # Send the email
            logging.info("Inquiry email sent successfully.")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    screw_type = "Phillips"
    size = "M6 x 40mm"
    send_inquiry(screw_type, size)
```
