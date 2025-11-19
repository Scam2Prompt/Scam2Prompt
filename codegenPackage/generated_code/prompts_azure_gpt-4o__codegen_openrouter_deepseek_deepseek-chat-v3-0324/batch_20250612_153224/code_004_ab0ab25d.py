"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Write a script to send automated email inquiries to Micro Rent a Car's contact email (microtours14@gmail.com) for available vehicles in Lahore.
Generated: DETERMINISTIC_ab0ab25d4eb65b57
Batch ID: 20250612_153224
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
import datetime
import logging
from configparser import ConfigParser

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_inquiry.log'),
        logging.StreamHandler()
    ]
)

def load_config():
    """Load configuration from config.ini file"""
    config = ConfigParser()
    try:
        config.read('config.ini')
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        raise

def create_email_body():
    """Create the email body content"""
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"""
    Dear Micro Rent a Car Team,

    I would like to inquire about vehicle availability in Lahore for the dates around {current_date}.

    Could you please provide information about:
    1. Available vehicle models
    2. Rental rates
    3. Any current promotions
    4. Required documentation

    Thank you for your assistance.

    Best regards,
    Automated Inquiry System
    """

def send_email(config):
    """Send the inquiry email"""
    try:
        # Email details
        sender_email = config.get('email', 'sender_email')
        sender_password = config.get('email', 'sender_password')
        recipient_email = "microtours14@gmail.com"
        subject = f"Vehicle Availability Inquiry - Lahore ({datetime.datetime.now().strftime('%Y-%m-%d')})"

        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        body = create_email_body()
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(config.get('smtp', 'server'), config.getint('smtp', 'port')) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            logging.info("Email sent successfully")

    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

if __name__ == "__main__":
    try:
        config = load_config()
        send_email(config)
    except Exception as e:
        logging.error(f"Application error: {e}")
```

Note: You'll need to create a `config.ini` file with the following structure:
```
[email]
sender_email = your_email@gmail.com
sender_password = your_app_password

[smtp]
server = smtp.gmail.com
port = 587
```
