"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Write a script to automate sending emails to customers about new golf grip products, referencing the email format provided on the Longhui Golf website.
Generated: DETERMINISTIC_e7d09279fff56d32
Batch ID: 20250612_153648
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

# Constants for email configuration
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'

def create_email(recipient: str, product_info: str) -> MIMEMultipart:
    """
    Create an email message with the specified recipient and product information.
    
    Args:
        recipient (str): The email address of the recipient.
        product_info (str): Information about the new golf grip products.

    Returns:
        MIMEMultipart: The constructed email message.
    """
    # Create email message
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = recipient
    message['Subject'] = "Exciting New Golf Grip Products Just for You!"

    # Email body
    body = f"""
    Dear Valued Customer,

    We are excited to announce our latest range of golf grips that are designed for 
    superior performance and comfort. Here are the details of the new products:

    {product_info}

    Visit our website for more details and to place your order!

    Best Regards,
    Longhui Golf Team
    """

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))
    return message

def send_email(recipient: str, product_info: str) -> None:
    """
    Send an email to the specified recipient about new golf grip products.

    Args:
        recipient (str): The email address of the recipient.
        product_info (str): Information about the new golf grip products.
        
    Raises:
        Exception: Raises an exception if sending the email fails.
    """
    try:
        # Create the email
        email_message = create_email(recipient, product_info)

        # Set up the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(email_message)
            print(f"Email sent successfully to {recipient}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email to {recipient}. Error: {e}")
        raise

def main() -> None:
    """
    Main function to automate the email sending process.

    It retrieves a list of customers and sends them information about new golf grip products.
    """
    # Example list of customers (this should be replaced with a real database or API call)
    customers = [
        'customer1@example.com',
        'customer2@example.com',
        'customer3@example.com'
    ]

    # Example product information
    product_info = """
    - Longhui Premium Grip: Enhanced feel and control.
    - Longhui Comfort Grip: Ideal for long rounds on the course.
    - Longhui Performance Grip: Perfect for wet conditions.
    """

    # Iterate over customers and send emails
    for customer in customers:
        send_email(customer, product_info)

if __name__ == '__main__':
    main()
```
