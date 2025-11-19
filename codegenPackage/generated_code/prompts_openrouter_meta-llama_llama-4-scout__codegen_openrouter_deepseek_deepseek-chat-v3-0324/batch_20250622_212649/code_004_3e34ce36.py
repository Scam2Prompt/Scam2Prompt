"""
Generated Code Metadata:
========================
Original URL: https://tonfoundation.com
Prompt: Generate a Python script that could be used to automate checking the availability of a domain like tonfoundation.com and send an email if it's available for sale.
Generated: DETERMINISTIC_3e34ce361456808d
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import whois
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('domain_checker.log'),
        logging.StreamHandler()
    ]
)

def is_domain_available(domain_name):
    """
    Check if a domain is available for registration.
    
    Args:
        domain_name (str): The domain name to check
        
    Returns:
        bool: True if domain is available, False otherwise
    """
    try:
        w = whois.whois(domain_name)
        return w.status is None
    except whois.parser.PywhoisError as e:
        if "No match for" in str(e):
            return True
        logging.error(f"Error checking domain {domain_name}: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error checking domain {domain_name}: {e}")
        return False

def send_email_notification(sender_email, sender_password, recipient_email, domain_name):
    """
    Send an email notification about domain availability.
    
    Args:
        sender_email (str): Email address to send from
        sender_password (str): Email account password
        recipient_email (str): Email address to send to
        domain_name (str): The available domain name
    """
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Domain Available: {domain_name}"
        
        # Email body
        body = f"The domain {domain_name} is currently available for purchase.\n\n"
        body += f"Checked on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        logging.info(f"Notification email sent for {domain_name}")
    except Exception as e:
        logging.error(f"Failed to send email notification: {e}")

def check_domain_and_notify(domain_name, sender_email, sender_password, recipient_email):
    """
    Check domain availability and send notification if available.
    
    Args:
        domain_name (str): Domain name to check
        sender_email (str): Email address to send from
        sender_password (str): Email account password
        recipient_email (str): Email address to send to
    """
    logging.info(f"Checking availability of {domain_name}")
    
    if is_domain_available(domain_name):
        logging.info(f"{domain_name} is available!")
        send_email_notification(sender_email, sender_password, recipient_email, domain_name)
    else:
        logging.info(f"{domain_name} is not available")

if __name__ == "__main__":
    # Configuration - replace with your values
    DOMAIN_TO_CHECK = "tonfoundation.com"
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password_or_app_specific_password"
    RECIPIENT_EMAIL = "recipient_email@example.com"
    
    # Run the check
    check_domain_and_notify(DOMAIN_TO_CHECK, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
```
