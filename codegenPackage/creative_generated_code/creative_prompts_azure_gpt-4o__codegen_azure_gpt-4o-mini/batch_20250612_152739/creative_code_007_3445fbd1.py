"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Create a Python script to send email notifications to customers about weekend sales (e.g., "up to 50% off summer items"), as advertised on ActiveSport.cz.
Generated: DETERMINISTIC_3445fbd1bbc1e4f9
Batch ID: 20250612_152739
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
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                     # Commonly used port for TLS
SMTP_USERNAME = 'your_email@example.com'  # Your email address
SMTP_PASSWORD = 'your_password'     # Your email password
FROM_EMAIL = 'your_email@example.com'  # Sender's email address
SUBJECT = 'Weekend Sale: Up to 50% Off Summer Items!'

def send_email(to_email: str, body: str) -> None:
    """Send an email notification to a customer.

    Args:
        to_email (str): Recipient's email address.
        body (str): Body of the email.

    Raises:
        Exception: If an error occurs during sending the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = SUBJECT
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to use TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email successfully sent to {to_email}')

    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')
        raise

def notify_customers(customers: List[str]) -> None:
    """Notify a list of customers about the weekend sale.

    Args:
        customers (List[str]): List of customer email addresses.
    """
    email_body = ("Dear Customer,\n\n"
                  "We're excited to announce our weekend sale! "
                  "Enjoy up to 50% off on all summer items!\n\n"
                  "Don't miss out on these fantastic deals!\n\n"
                  "Best regards,\n"
                  "ActiveSport.cz Team")

    for customer in customers:
        try:
            send_email(customer, email_body)
        except Exception as e:
            logging.error(f'Error notifying {customer}: {e}')

if __name__ == "__main__":
    # Example list of customer emails (replace with actual emails)
    customer_emails = [
        'customer1@example.com',
        'customer2@example.com',
        'customer3@example.com'
    ]

    # Notify customers about the weekend sale
    notify_customers(customer_emails)
```
