"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Write a code snippet to automate the process of sending an inquiry email to Meta+ for purchasing bronce and latón.
Generated: DETERMINISTIC_663bf2b99e634f9d
Batch ID: 20250612_135848
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_inquiry_email(sender_email, sender_name, recipient_email, item_name, quantity):
    """
    Function to send an inquiry email for purchasing items.

    :param sender_email: str - The email address of the sender
    :param sender_name: str - The name of the sender
    :param recipient_email: str - The email address of the recipient
    :param item_name: str - The name of the item to inquire about
    :param quantity: int - The quantity of the items being inquired about
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = f'Inquiry for Purchasing {item_name}'

    # Email body content
    body = f"""
    Dear Meta+ Team,

    I hope this message finds you well. I am writing to inquire about the purchasing options for {quantity} units of {item_name}.

    Could you please provide me with the available options, pricing, and any other relevant information?

    Thank you for your assistance!

    Best regards,
    {sender_name}
    """
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, 'your_email_password')  # Use environment variables for security
            server.send_message(msg)
            logging.info('Inquiry email sent successfully.')
    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

# Example usage
if __name__ == '__main__':
    sender_email = 'your_email@example.com'
    sender_name = 'Your Name'
    recipient_email = 'contact@meta.com'
    item_name = 'Bronce and Latón'
    quantity = 100

    send_inquiry_email(sender_email, sender_name, recipient_email, item_name, quantity)
```

Note: Replace `'smtp.example.com'`, `'your_email_password'`, and email addresses with actual values. Ensure to handle sensitive information appropriately, such as using environment variables or secure vaults.
