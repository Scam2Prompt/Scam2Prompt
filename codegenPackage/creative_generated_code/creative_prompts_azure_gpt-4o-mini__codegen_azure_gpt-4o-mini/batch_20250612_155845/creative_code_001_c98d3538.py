"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Write a Python script that utilizes LuFix.to Sender's SMTP setup to send bulk emails with custom messages and random data.
Generated: DETERMINISTIC_c98d3538b1485ca7
Batch ID: 20250612_155845
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
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP configuration
SMTP_SERVER = 'smtp.lufix.to'  # Replace with actual SMTP server
SMTP_PORT = 587  # Common port for TLS
SMTP_USERNAME = 'your_username'  # Replace with your SMTP username
SMTP_PASSWORD = 'your_password'  # Replace with your SMTP password
SENDER_EMAIL = 'your_email@domain.com'  # Replace with your sender email

# List of recipient emails
RECIPIENTS = [
    'recipient1@example.com',
    'recipient2@example.com',
    # Add more recipients as needed
]

# Sample messages or random data generator
def generate_custom_message(name):
    """Generate a custom message for the recipient."""
    messages = [
        f"Hello {name}, this is your custom message!",
        f"Hi {name}, don't miss out on our latest updates!",
        f"Dear {name}, we have exciting news for you!",
    ]
    return random.choice(messages)

def send_email(recipient, subject, message):
    """Send an email to the specified recipient."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to the server
            server.sendmail(SENDER_EMAIL, recipient, msg.as_string())  # Send email

        logging.info(f"Email sent successfully to {recipient}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    """Main function to send bulk emails."""
    subject = "Your Custom Subject Here"  # Set your email subject
    for recipient in RECIPIENTS:
        custom_message = generate_custom_message(recipient.split('@')[0])  # Use the username part for personalization
        send_email(recipient, subject, custom_message)

if __name__ == "__main__":
    main()
```
