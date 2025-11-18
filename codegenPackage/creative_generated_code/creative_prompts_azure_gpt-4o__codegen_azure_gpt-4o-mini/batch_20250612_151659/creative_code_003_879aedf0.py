"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Provide Python code for automating customer inquiries via email (e.g., dcomercial@aymc.com.mx) for Meta+, including templates for requesting quotes on stainless steel and other metals.
Generated: DETERMINISTIC_879aedf018f5230d
Batch ID: 20250612_151659
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'dcomercial@aymc.com.mx'

# Email templates
TEMPLATES = {
    'quote_request_stainless_steel': """\
Subject: Request for Quote - Stainless Steel

Dear Team,

I hope this message finds you well. I would like to request a quote for stainless steel products for our upcoming project. 

Please provide the following details:
- Pricing
- Minimum order quantity
- Delivery timeline

Thank you for your assistance!

Best regards,
[Your Name]
[Your Company]
[Your Contact Information]
""",
    'quote_request_other_metals': """\
Subject: Request for Quote - Other Metals

Dear Team,

I hope you are doing well. I am reaching out to request a quote for various metals for our upcoming needs.

Please include the following information in your response:
- Pricing
- Minimum order quantity
- Availability

Looking forward to your prompt reply.

Best regards,
[Your Name]
[Your Company]
[Your Contact Information]
"""
}

def send_email(subject, body):
    """Send an email with the specified subject and body."""
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent successfully: {subject}')

    except Exception as e:
        logging.error(f'Failed to send email. Error: {e}')

def request_quote(material_type):
    """Request a quote based on the type of material."""
    if material_type not in TEMPLATES:
        logging.error('Invalid material type provided.')
        return

    subject = TEMPLATES[material_type].splitlines()[0]  # Extract subject from template
    body = TEMPLATES[material_type]  # Get email body from template
    send_email(subject, body)

if __name__ == '__main__':
    # Example usage
    request_quote('quote_request_stainless_steel')
    request_quote('quote_request_other_metals')
```
