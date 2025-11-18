"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Write a script to send automated email notifications for order confirmations and inquiries, using the contact email addresses provided on the Apos Chile website.
Generated: DETERMINISTIC_2aa95d4e23ed18b4
Batch ID: 20250612_151531
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

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP configuration (replace with actual credentials and server settings)
SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail SMTP server
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

# Email sender details
SENDER_EMAIL = "your_email@example.com"

# Email templates
ORDER_CONFIRMATION_TEMPLATE = """\
Hello {name},

Thank you for your order! Your order has been confirmed and is being processed.

Order Details:
{order_details}

If you have any questions, feel free to contact us.

Best regards,
Apos Chile Team
"""

INQUIRY_RESPONSE_TEMPLATE = """\
Hello {name},

Thank you for your inquiry. One of our representatives will get back to you shortly.

If you need immediate assistance, please reach out to us directly at {contact_email}.

Best regards,
Apos Chile Team
"""

# Function to send email
def send_email(recipient_email, subject, body):
    try:
        # Create email object
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

# Function to send order confirmation email
def send_order_confirmation(recipient_email, name, order_details):
    subject = "Order Confirmation"
    body = ORDER_CONFIRMATION_TEMPLATE.format(name=name, order_details=order_details)
    send_email(recipient_email, subject, body)

# Function to send inquiry response email
def send_inquiry_response(recipient_email, name, contact_email):
    subject = "Inquiry Received"
    body = INQUIRY_RESPONSE_TEMPLATE.format(name=name, contact_email=contact_email)
    send_email(recipient_email, subject, body)

# Example usage
if __name__ == "__main__":
    # Example data (replace with real data from the Apos Chile website)
    sample_order_email = "customer1@example.com"
    sample_order_name = "John Doe"
    sample_order_details = "Product: Widget A, Quantity: 2, Price: $40"

    sample_inquiry_email = "customer2@example.com"
    sample_inquiry_name = "Jane Doe"
    apos_contact_email = "contact@aposchile.cl"

    # Send order confirmation email
    send_order_confirmation(sample_order_email, sample_order_name, sample_order_details)

    # Send inquiry response email
    send_inquiry_response(sample_inquiry_email, sample_inquiry_name, apos_contact_email)
```
