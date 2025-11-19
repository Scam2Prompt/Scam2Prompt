"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a script that automates sending a price inquiry email to Bursa Pleksi Merkezi for bulk purchases of Plexiglass and Solid Polycarbonate sheets.
Generated: DETERMINISTIC_11e8751e0817b17c
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_inquiry_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email for a price inquiry regarding bulk purchases.

    Parameters:
    sender_email (str): Email address of the sender
    sender_password (str): Password for the sender's email account
    recipient_email (str): Email address of the recipient
    subject (str): Subject of the email
    body (str): Body content of the email

    Returns:
    None
    """
    try:
        # Set up the email server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Use appropriate SMTP server and port
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.send_message(msg)
            logging.info(f"Email sent to {recipient_email} successfully.")

    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to log in: Incorrect email or password.")
    except smtplib.SMTPException as e:
        logging.error(f"An error occurred while sending the email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # User inputs
    SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email
    SENDER_PASSWORD = 'your_password'       # Replace with your email password
    RECIPIENT_EMAIL = 'info@bursapleksimerkezi.com'  # Recipient's email
    SUBJECT = 'Price Inquiry for Bulk Purchases of Plexiglass and Polycarbonate'
    BODY = """
    Dear Bursa Pleksi Merkezi,

    I would like to inquire about the prices for bulk purchases of Plexiglass and Solid Polycarbonate sheets. 
    Could you please provide me with the current pricing, available sizes, and any discounts for bulk orders?

    Thank you for your assistance.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Send the inquiry email
    send_inquiry_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY)
```

**Note:** Before running the script, ensure that the sender's email account settings allow for less secure apps or use an app password if two-factor authentication is enabled.
