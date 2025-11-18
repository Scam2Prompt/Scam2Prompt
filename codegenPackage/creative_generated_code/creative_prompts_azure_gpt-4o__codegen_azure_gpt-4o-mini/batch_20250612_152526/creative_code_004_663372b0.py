"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Write a Python script to automate sending order tracking emails for purchases made on an e-commerce site, referencing the store's location in Portimão, Portugal.
Generated: DETERMINISTIC_663372b0acf39a0c
Batch ID: 20250612_152526
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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
USERNAME = 'your_email@example.com'
PASSWORD = 'your_email_password'
FROM_EMAIL = 'your_email@example.com'
STORE_LOCATION = 'Portimão, Portugal'

# Function to send order tracking email
def send_order_tracking_email(to_email, order_id, tracking_number):
    """
    Sends an order tracking email to the customer.

    Parameters:
    to_email (str): The recipient's email address.
    order_id (str): The order ID for reference.
    tracking_number (str): The tracking number for the shipment.

    Returns:
    bool: True if email sent successfully, False otherwise.
    """
    subject = f'Your Order #{order_id} is On Its Way!'
    body = (
        f'Hello,\n\n'
        f'Thank you for your purchase from our store located in {STORE_LOCATION}!\n\n'
        f'Your order #{order_id} has been shipped.\n'
        f'You can track your package using the following tracking number:\n'
        f'{tracking_number}\n\n'
        f'Best regards,\n'
        f'The Team'
    )

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email server
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())  # Send the email
        logging.info(f'Order tracking email sent to {to_email} for order {order_id}.')
        return True
    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email to {to_email}: {e}')
        return False

if __name__ == '__main__':
    # Example use case
    recipient_email = 'customer@example.com'
    order_id = '123456'
    tracking_number = 'TRK123456789'

    # Send the order tracking email
    success = send_order_tracking_email(recipient_email, order_id, tracking_number)
    if success:
        print('Email sent successfully.')
    else:
        print('Failed to send email.')
```
