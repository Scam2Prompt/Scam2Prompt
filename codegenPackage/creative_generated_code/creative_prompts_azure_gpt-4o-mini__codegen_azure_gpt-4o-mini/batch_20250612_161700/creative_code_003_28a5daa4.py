"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Develop a script that sends a message to a bakery owner with order details, referencing the contact method mentioned on utterlybaked.com.
Generated: DETERMINISTIC_28a5daa43277b6d5
Batch ID: 20250612_161700
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

def send_order_confirmation(bakery_email, customer_name, order_details):
    """
    Sends an order confirmation email to the bakery owner.

    Args:
        bakery_email (str): The email address of the bakery owner.
        customer_name (str): The name of the customer placing the order.
        order_details (str): The details of the order.

    Raises:
        ValueError: If any of the input parameters are empty.
        Exception: For any other errors encountered during the email sending process.
    """
    # Validate input parameters
    if not bakery_email or not customer_name or not order_details:
        raise ValueError("All parameters (bakery_email, customer_name, order_details) must be provided.")

    # Create the email content
    subject = "New Order Confirmation from {}".format(customer_name)
    body = "Hello,\n\nYou have received a new order from {}.\n\nOrder Details:\n{}\n\nThank you!".format(customer_name, order_details)

    # Set up the email server and message
    try:
        # Set up the SMTP server
        smtp_server = "smtp.your-email-provider.com"  # Replace with your SMTP server
        smtp_port = 587  # Common SMTP port
        sender_email = "your-email@example.com"  # Replace with your email
        sender_password = "your-email-password"    # Replace with your email password

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = bakery_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect and authenticate with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            
            # Send the email
            server.sendmail(sender_email, bakery_email, msg.as_string())
            logging.info("Order confirmation email sent to {}".format(bakery_email))

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: {}".format(e))
        raise Exception("Error sending email. Please check the SMTP configuration and try again.")

# Example usage
if __name__ == "__main__":
    try:
        send_order_confirmation("bakery-owner@example.com", "John Doe", "2 dozen cupcakes, 1 birthday cake")
    except Exception as e:
        logging.error("An error occurred: {}".format(e))
```
