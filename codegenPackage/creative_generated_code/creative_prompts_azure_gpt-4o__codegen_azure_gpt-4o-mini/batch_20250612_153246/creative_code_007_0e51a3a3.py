"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Write a script to automate email notifications for new product launches, such as "Gladiator Safety Shoes 003 Black" or "Gladiator Safety Boots 1068 Honey," using the contact information provided on the Gladiator Shoes website.
Generated: DETERMINISTIC_0e51a3a3508681c3
Batch ID: 20250612_153246
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

# Configure logging to capture events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_HOST = 'smtp.your-email-provider.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # For TLS
EMAIL_USER = 'your-email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your-email-password'  # Replace with your email password

# Function to send email notifications
def send_email_notification(product_name, recipient_email):
    """
    Sends an email notification for a new product launch.

    :param product_name: The name of the product to notify about
    :param recipient_email: The email address of the recipient
    """
    # Create the email content
    subject = f'New Product Launch: {product_name}'
    body = f'We are excited to announce the launch of our new product: {product_name}.\n\nStay tuned for more updates!'

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the email server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)  # Login to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent successfully to {recipient_email} regarding {product_name}')
    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email to {recipient_email}: {e}')

# Example usage: List of new products and sample recipient email
new_products = [
    "Gladiator Safety Shoes 003 Black",
    "Gladiator Safety Boots 1068 Honey"
]

recipient_emails = [
    'customer1@example.com',  # Replace with actual customer emails
    'customer2@example.com'
]

# Send notifications for each new product to each recipient
for product in new_products:
    for recipient in recipient_emails:
        send_email_notification(product, recipient)
```
