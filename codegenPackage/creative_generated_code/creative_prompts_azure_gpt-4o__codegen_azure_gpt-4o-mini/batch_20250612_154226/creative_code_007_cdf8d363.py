"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoclaim.rf.gd
Prompt: Provide code examples for setting up email accounts on a hosting platform that supports multiple email accounts and modern cPanel, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_cdf8d3631e8400e6
Batch ID: 20250612_154226
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

# Constants for email server configuration
SMTP_SERVER = 'smtp.ifastnet.com'  # Update with actual SMTP server if different
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@ifastnet.com'  # Your email account
PASSWORD = 'your_password'  # Your email account password

def create_email_account(email_address, email_password):
    """
    Function to set up a new email account on iFastNet hosting.
    
    Args:
        email_address (str): The email address to create.
        email_password (str): The password for the new email account.
    
    Returns:
        bool: True if account creation was successful, False otherwise.
    """
    try:
        # Simulate account creation process (e.g., via cPanel API)
        print(f"Creating email account: {email_address}...")
        # Here would be the code to interact with the iFastNet API.
        # For example, make an API call to create the email.
        return True  # Simulate a successful account creation
    except Exception as e:
        print(f"Error creating email account: {e}")
        return False


def send_welcome_email(to_email):
    """
    Sends a welcome email to the newly created email account.
    
    Args:
        to_email (str): The recipient email address.
    """
    try:
        # Setting up the email content
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = 'Welcome to iFastNet Email Service'
        
        body = 'Your email account has been successfully created!'
        msg.attach(MIMEText(body, 'plain'))

        # Sending the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f"Welcome email sent to {to_email}.")
    except Exception as e:
        print(f"Error sending welcome email: {e}")


if __name__ == "__main__":
    # Example usage of creating an email account
    email_to_create = "newuser@ifastnet.com"
    email_password = "secure_password"

    if create_email_account(email_to_create, email_password):
        send_welcome_email(email_to_create)
```
