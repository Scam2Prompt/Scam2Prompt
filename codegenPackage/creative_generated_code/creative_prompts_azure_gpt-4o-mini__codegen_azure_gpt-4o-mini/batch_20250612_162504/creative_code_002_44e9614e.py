"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metisassets.com
Prompt: Write a Python script that automates sending cash offer emails to users who submit their property information through a form, inspired by the process described on Metis Assets' site.
Generated: DETERMINISTIC_44e9614e15b716be
Batch ID: 20250612_162504
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
USERNAME = 'your-email@example.com'
PASSWORD = 'your-email-password'

def send_cash_offer_email(recipient_email: str, property_info: Dict[str, str]) -> None:
    """
    Sends a cash offer email to the user based on their property information.

    Args:
        recipient_email (str): The email address of the recipient.
        property_info (Dict[str, str]): A dictionary containing property details.
        
    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = 'Cash Offer for Your Property'

        # Create the email body
        body = f"""
        Hi there,

        Thank you for submitting your property information. 
        Based on the details provided, we are pleased to present you with a cash offer.

        Property Details:
        - Address: {property_info.get('address')}
        - Price: {property_info.get('price')}
        - Bedrooms: {property_info.get('bedrooms')}
        - Bathrooms: {property_info.get('bathrooms')}
        
        If you're interested in our cash offer, please reply to this email or contact us directly.

        Best regards,
        The Metis Assets Team
        """
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
        
        logging.info(f"Email successfully sent to: {recipient_email}")
        
    except Exception as e:
        logging.error(f"Error sending email to {recipient_email}: {e}")
        raise

def automate_email_sending(users: List[Dict[str, str]]) -> None:
    """
    Automates the process of sending cash offer emails to multiple users.

    Args:
        users (List[Dict[str, str]]): A list of dictionaries containing user email and property info.
        
    Raises:
        Exception: If there is an error in processing any email.
    """
    for user in users:
        try:
            send_cash_offer_email(user['email'], user['property_info'])
        except Exception as e:
            logging.error(f"Failed to send email to {user['email']}: {e}")

if __name__ == "__main__":
    # Example user data
    users_data = [
        {
            'email': 'user1@example.com',
            'property_info': {
                'address': '123 Main St',
                'price': '$300,000',
                'bedrooms': '3',
                'bathrooms': '2'
            }
        },
        {
            'email': 'user2@example.com',
            'property_info': {
                'address': '456 Elm St',
                'price': '$450,000',
                'bedrooms': '4',
                'bathrooms': '3'
            }
        }
    ]

    # Automate the email sending process
    automate_email_sending(users_data)
```
