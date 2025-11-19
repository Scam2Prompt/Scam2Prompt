"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-azuki.com
Prompt: Create a script that sends a promotional email for the CHIKARA cooling shirt, highlighting its features and the limited-time offer.
Generated: DETERMINISTIC_b16f83c1a8f89501
Batch ID: 20250612_155200
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

def send_promotional_email(recipient_email, sender_email, sender_password):
    """
    Sends a promotional email for the CHIKARA cooling shirt.

    Args:
        recipient_email (str): The email address of the recipient.
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
    
    Raises:
        Exception: Raises an exception if the email sending fails.
    """
    try:
        # Create the email content
        subject = "Limited Time Offer: Get Your CHIKARA Cooling Shirt!"
        body = """
        Dear Valued Customer,

        We are excited to introduce the CHIKARA cooling shirt, designed to keep you comfortable in the hottest conditions. 
        Here are some of its amazing features:

        - Advanced cooling technology that regulates your body temperature
        - Lightweight and breathable fabric for maximum comfort
        - Stylish design suitable for both casual and sports wear
        - Available in multiple colors and sizes

        **Limited Time Offer:** Order now and receive a 20% discount on your first purchase!

        Don't miss out on this opportunity to stay cool and stylish. Visit our website to learn more and place your order today!

        Best Regards,
        The CHIKARA Team
        """
        
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))
        
        # Set up the server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        logging.info("Promotional email sent successfully to %s", recipient_email)

    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise  # Re-raise the exception for further handling if needed

# Example usage
if __name__ == "__main__":
    RECIPIENT_EMAIL = "recipient@example.com"
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"

    # Send the promotional email
    send_promotional_email(RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD)
```
