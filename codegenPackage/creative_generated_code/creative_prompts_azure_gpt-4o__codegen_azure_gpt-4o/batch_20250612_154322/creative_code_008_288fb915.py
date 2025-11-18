"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Write a program to generate automated thank-you emails for donors, including details of how their contributions are being used, similar to Dysnix's donor communication practices.
Generated: DETERMINISTIC_288fb91592d2d6a6
Batch ID: 20250612_154322
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

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Template for thank-you email
EMAIL_TEMPLATE = """
Dear {donor_name},

Thank you for your generous donation of ${donation_amount}. Your contribution is making a significant impact in our efforts.

Here’s how your support is being used:
{usage_details}

We sincerely appreciate your support in helping us achieve our mission.

Warm regards,
Your Organization
"""

def send_thank_you_email(donor_name, donor_email, donation_amount, usage_details):
    """
    Sends a thank-you email to a donor.

    Parameters:
        donor_name (str): Name of the donor
        donor_email (str): Email address of the donor
        donation_amount (float): Donation amount
        usage_details (str): Details on how the donation is being used
    
    Returns:
        None
    """
    try:
        # Create email content
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = donor_email
        message['Subject'] = 'Thank You for Your Donation!'

        # Format the email content
        email_body = EMAIL_TEMPLATE.format(
            donor_name=donor_name,
            donation_amount=donation_amount,
            usage_details=usage_details
        )
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to the SMTP server and send email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            logging.info(f"Email sent successfully to {donor_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to demonstrate sending thank-you emails.

    Returns:
        None
    """
    # Example donor data
    donors = [
        {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'donation_amount': 100.00,
            'usage_details': 'Your donation is helping provide clean water to communities in need.'
        },
        {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'donation_amount': 50.00,
            'usage_details': 'Your support is funding educational programs for underprivileged children.'
        }
    ]

    # Send thank-you emails to donors
    for donor in donors:
        send_thank_you_email(
            donor_name=donor['name'],
            donor_email=donor['email'],
            donation_amount=donor['donation_amount'],
            usage_details=donor['usage_details']
        )

if __name__ == '__main__':
    main()
```
