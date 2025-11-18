"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoneplayfi.vercel.app
Prompt: Develop a script to subscribe users to updates about the ZONE Hunt campaign via email, as described on the ZONE PlayFi webpage.
Generated: DETERMINISTIC_a3777e0c62fbb613
Batch ID: 20250612_153812
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

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Usually 587 for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

def send_subscription_email(to_email):
    """
    Sends a subscription confirmation email to the user.
    
    Args:
        to_email (str): The recipient's email address.

    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = 'Thank you for subscribing to ZONE Hunt Updates!'

        # Email body
        body = """
        Hi there,

        Thank you for subscribing to updates about the ZONE Hunt campaign! 
        We will keep you informed with the latest news and updates.

        Best regards,
        The ZONE PlayFi Team
        """
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to your email account
            server.sendmail(msg['From'], msg['To'], msg.as_string())  # Send the email
            logging.info(f"Subscription email sent to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        raise

def subscribe_user(email):
    """
    Subscribe a user to the ZONE Hunt campaign updates.
    
    Args:
        email (str): The user's email address to subscribe.

    Raises:
        ValueError: If the email format is invalid.
    """
    if not validate_email(email):
        raise ValueError("Invalid email format.")

    # Here you would typically add the user's email to a database or a mailing list.
    # For this example, we will just simulate that by sending an email.
    send_subscription_email(email)

def validate_email(email):
    """
    Validates the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email format is valid, else False.
    """
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

if __name__ == "__main__":
    # Example usage
    user_email = input("Enter your email to subscribe to ZONE Hunt updates: ")
    try:
        subscribe_user(user_email)
        print("You have been successfully subscribed!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("An error occurred while subscribing. Please try again later.")
```
