"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Create a script to automate customer support inquiries for sealing system products, integrating the contact details and global export information from Silver Seals.
Generated: DETERMINISTIC_33231902fd94a061
Batch ID: 20250612_153225
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for email configuration
SMTP_SERVER = "smtp.your-email-provider.com"
SMTP_PORT = 587
EMAIL_SENDER = "support@silverseals.com"
EMAIL_PASSWORD = "your-email-password"

# Customer support template
SUPPORT_TEMPLATE = """
Dear {customer_name},

Thank you for reaching out to Silver Seals customer support regarding our sealing system products.
We pride ourselves on providing high-quality products and global export services.

If you have any questions or need further assistance, please feel free to contact us directly.
Our export team is available at export@silverseals.com, and we are happy to assist with any inquiries you may have.

Best regards,
Silver Seals Support Team
"""

def send_email(recipient_email, customer_name):
    """
    Sends a customer support email to the given recipient.

    Args:
        recipient_email (str): The recipient's email address.
        customer_name (str): The name of the customer.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient_email
        msg['Subject'] = "Customer Support Inquiry - Silver Seals"

        # Customize the email content
        body = SUPPORT_TEMPLATE.format(customer_name=customer_name)
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())
        
        logging.info(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {str(e)}")


def main():
    """
    Main function to handle customer inquiries.
    """
    # Example customer data (this could be dynamically fetched from an API or database)
    customer_inquiries = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"},
    ]

    logging.info("Starting customer support automation...")

    for customer in customer_inquiries:
        send_email(customer["email"], customer["name"])

    logging.info("Customer support automation completed.")

if __name__ == "__main__":
    main()
```
