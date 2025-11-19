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

# Constants
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                     # Standard port for TLS
SMTP_USER = 'your_email@example.com'  # Email address for sending
SMTP_PASSWORD = 'your_password'      # Your email password
FROM_EMAIL = 'your_email@example.com'  # From email address
TO_EMAIL = 'recipient@example.com'    # Recipient email address

def generate_login_code(length=6):
    """
    Generate a random numeric code for login.
    
    Args:
        length (int): The length of the generated code.
        
    Returns:
        str: The generated login code.
    """
    return ''.join(random.choices(string.digits, k=length))

def send_email(subject, body, to_email):
    """
    Send an email using SMTP.
    
    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_email (str): The recipient's email address.
        
    Raises:
        Exception: Raises an exception if email sending fails.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USER, SMTP_PASSWORD)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
        
        print("Email sent successfully.")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise  # Reraise the exception for further handling if needed

def main():
    """
    Main function that generates a login code and sends it via email.
    """
    # Generate a random login code
    login_code = generate_login_code()
    
    # Define email subject and body
    subject = "Your Login Code"
    body = f"Your login code is: {login_code}"
    
    # Send the email
    try:
        send_email(subject, body, TO_EMAIL)
    except Exception as e:
        print(f"Error in sending login code: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
