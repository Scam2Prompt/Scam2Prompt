"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastfair.com
Prompt: Generate a Python script to subscribe users to the Études Newsletter and send them exclusive architectural design insights.
Generated: DETERMINISTIC_137f9e3747698736
Batch ID: 20250612_152527
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
from email.utils import formataddr
import logging

# Set up logging for debugging and error monitoring
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration for SMTP server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"       # Replace with your email password

# Sender information
SENDER_NAME = "Études Newsletter"
SENDER_EMAIL = "newsletter@example.com"

# Sample newsletter content
NEWSLETTER_SUBJECT = "Études Newsletter: Exclusive Architectural Design Insights"
NEWSLETTER_BODY = """
Dear Subscriber,

Thank you for subscribing to the Études Newsletter! 

We are thrilled to share exclusive architectural design insights with you. 
Stay tuned for upcoming articles, case studies, and industry tips to inspire your creativity.

Warm regards,  
The Études Team
"""

def send_newsletter(recipient_name, recipient_email):
    """
    Sends a newsletter email to the specified recipient.

    :param recipient_name: Name of the recipient
    :param recipient_email: Email address of the recipient
    :return: None
    """
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = formataddr((recipient_name, recipient_email))
        msg['Subject'] = NEWSLETTER_SUBJECT
        
        # Attach the email body
        msg.attach(MIMEText(NEWSLETTER_BODY, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USER, SMTP_PASSWORD)  # Log in to the SMTP server
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        
        logging.info(f"Newsletter sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send newsletter to {recipient_email}. Error: {e}")

def subscribe_user():
    """
    Collects user information and subscribes them to the newsletter.

    :return: None
    """
    try:
        # Collect user details
        recipient_name = input("Enter your name: ").strip()
        recipient_email = input("Enter your email: ").strip()
        
        # Validate email format
        if '@' not in recipient_email or '.' not in recipient_email.split('@')[1]:
            raise ValueError("Invalid email format. Please enter a valid email address.")

        # Send the newsletter
        send_newsletter(recipient_name, recipient_email)
        print(f"Thank you, {recipient_name}! You have successfully subscribed to the Études Newsletter.")
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    logging.info("Études Newsletter Subscription Script Starting...")
    subscribe_user()
    logging.info("Études Newsletter Subscription Script Finished.")
```
