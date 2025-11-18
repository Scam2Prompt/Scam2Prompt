"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Write a script to send automated emails to users who request a free quote for fiber internet deals, using the contact process outlined on the Fiberdeals website.
Generated: DETERMINISTIC_029de2fced9e7e05
Batch ID: 20250612_151509
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

# Configure logging to track errors and activity
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_sender.log',
    filemode='a'
)

# Constants
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "youremail@example.com"  # Replace with your email address
EMAIL_PASSWORD = "yourpassword"  # Replace with your email password
SUBJECT = "Your Free Fiber Internet Quote"

def send_email(recipient_email, recipient_name, quote_details):
    """
    Sends an automated email with fiber internet quote details.

    Parameters:
    recipient_email (str): The email address of the recipient
    recipient_name (str): The name of the recipient
    quote_details (str): Details of the fiber internet deal

    Returns:
    None
    """
    try:
        # Create the email content
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient_email
        message['Subject'] = SUBJECT

        # Email body
        email_body = f"""
        Hi {recipient_name},

        Thank you for requesting a free quote for fiber internet deals.

        Here are the details of your quote:
        {quote_details}

        If you have any questions, feel free to contact us.

        Best regards,
        The FiberDeals Team
        """
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the email account
            server.send_message(message)  # Send the email

        logging.info(f"Email successfully sent to {recipient_email}")
    
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient_email}: {str(e)}")
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual user data
    recipient_email = "user@example.com"
    recipient_name = "John Doe"
    quote_details = "Plan: FiberMax 200 Mbps - $49.99/month"

    # Send the email
    send_email(recipient_email, recipient_name, quote_details)
```
