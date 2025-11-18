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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Typically, 587 for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_email_password'  # Replace with your email password

# APN Hardware contact email
TO_EMAIL = 'contact@apnhardware.com'  # Replace with APN Hardware's contact email

def send_inquiry(screw_type, screw_size):
    """Send an inquiry email to APN Hardware for custom manufacturing of fasteners.
    
    Args:
        screw_type (str): The type of screw (e.g., 'Phillips', 'Flat').
        screw_size (str): The size of the screw (e.g., 'M10', '1/4 inch').
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = TO_EMAIL
        msg['Subject'] = 'Inquiry for Custom Manufacturing of Fasteners'

        # Email body
        body = f"""
        Dear APN Hardware Team,

        I would like to inquire about the custom manufacturing of fasteners. 
        Below are the specifications I am interested in:

        Screw Type: {screw_type}
        Screw Size: {screw_size}

        Please let me know the pricing and lead time for these specifications.

        Thank you,
        [Your Name]
        [Your Contact Information]
        """
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email

        logging.info(f'Inquiry sent successfully for {screw_type} {screw_size}')

    except smtplib.SMTPException as e:
        logging.error(f"An error occurred while sending the email: {e}")

if __name__ == '__main__':
    # Example usage
    screw_type = 'Phillips'
    screw_size = 'M10'
    send_inquiry(screw_type, screw_size)
```

Make sure to replace SMTP_SERVER, USERNAME, PASSWORD, and TO_EMAIL with the appropriate values for your email setup. Ensure the email server settings are compatible with your email provider.
