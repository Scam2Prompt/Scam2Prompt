"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: Generate a code example for sending a login code via email in a Cloudflare Access setup.
Generated: DETERMINISTIC_24c40eaafa340191
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration settings (replace these with your actual values)
SMTP_SERVER = "smtp.example.com"  # SMTP server address
SMTP_PORT = 587                  # SMTP port (e.g., 587 for TLS)
SMTP_USERNAME = "your_email@example.com"  # Sender email username
SMTP_PASSWORD = "your_password"          # Sender email password
EMAIL_FROM = "your_email@example.com"    # Email address to send from

def generate_login_code(length=6):
    """
    Generate a random login code consisting of alphanumeric characters.
    
    Args:
        length (int): Length of the login code. Defaults to 6.
    
    Returns:
        str: Generated login code.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def send_email(recipient_email, subject, body):
    """
    Send an email via SMTP.

    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body of the email.

    Raises:
        Exception: If unable to send the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, recipient_email, msg.as_string())
            
    except Exception as e:
        # Log or handle the error appropriately in production code
        raise Exception(f"Failed to send email: {str(e)}")


def send_login_code(recipient_email):
    """
    Generate a login code and send it to the user's email address.

    Args:
        recipient_email (str): Email address of the recipient.
    
    Raises:
        Exception: If unable to send the login code.
    """
    try:
        # Generate a login code
        login_code = generate_login_code()
        
        # Create the email subject and body
        subject = "Your Login Code"
        body = f"Your login code is: {login_code}\n\nPlease use this code to log in. It is valid for a limited time."
        
        # Send the email
        send_email(recipient_email, subject, body)
        
        print(f"Login code successfully sent to {recipient_email}")
        
    except Exception as e:
        # Log or handle the error appropriately in production code
        print(f"Error: {str(e)}")
        raise


# Example usage (replace with actual recipient email)
if __name__ == "__main__":
    recipient = "recipient_email@example.com"
    send_login_code(recipient)
```
