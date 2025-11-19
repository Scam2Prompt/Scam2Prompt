"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: Write a script to automate email notifications for new product launches, such as "Gladiator Safety Shoes 003 Black" or "Gladiator Safety Boots 1068 Honey," using the contact information provided on the Gladiator Shoes website.
Generated: DETERMINISTIC_0e51a3a3508681c3
Batch ID: 20250612_153246
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
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

def send_email(subject: str, body: str, recipients: List[str]) -> None:
    """
    Sends an email notification to the specified recipients.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param recipients: List of email addresses to send the notification to
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, recipients, msg.as_string())
            logging.info(f"Email sent successfully to: {', '.join(recipients)}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def notify_new_product(product_name: str, product_id: str, recipients: List[str]) -> None:
    """
    Notifies recipients about a new product launch.

    :param product_name: Name of the new product
    :param product_id: ID of the new product
    :param recipients: List of email addresses to notify
    """
    subject = f"New Product Launch: {product_name}"
    body = f"We are excited to announce the launch of our new product: {product_name} (ID: {product_id}).\n\n" \
           "Check it out on our website!"
    
    send_email(subject, body, recipients)

if __name__ == "__main__":
    # Example usage
    new_product_name = "Gladiator Safety Shoes 003 Black"
    new_product_id = "003"
    contact_list = ["customer1@example.com", "customer2@example.com"]  # Replace with actual contacts

    notify_new_product(new_product_name, new_product_id, contact_list)
```
