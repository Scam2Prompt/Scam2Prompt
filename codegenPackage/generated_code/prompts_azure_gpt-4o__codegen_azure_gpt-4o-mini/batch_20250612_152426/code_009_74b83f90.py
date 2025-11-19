"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Create a Python script to send automated email notifications to customers about new arrivals in categories like "Apositos" and "Cicatrizantes" on a wound care product website.
Generated: DETERMINISTIC_74b83f90f267e479
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'  # Replace with your email password

# Email content
SUBJECT = "New Arrivals in Wound Care Products"
BODY_TEMPLATE = """
Dear Customer,

We are excited to inform you about our new arrivals in the following categories:
- Apositos
- Cicatrizantes

Visit our website to explore the latest products!

Best regards,
Your Wound Care Team
"""

def send_email(to_email: str) -> None:
    """Send an email notification to the specified recipient."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = SUBJECT
        
        # Attach the email body
        msg.attach(MIMEText(BODY_TEMPLATE, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def notify_customers(email_list: List[str]) -> None:
    """Notify customers about new arrivals by sending emails."""
    for email in email_list:
        send_email(email)

if __name__ == "__main__":
    # List of customer emails to notify
    customer_emails = [
        'customer1@example.com',
        'customer2@example.com',
        # Add more customer emails as needed
    ]
    
    # Notify customers
    notify_customers(customer_emails)
```
