"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write code to implement a password recovery feature that sends a 10-digit code via email, as described on the Vertiv portal.
Generated: DETERMINISTIC_6b7c2d7a6d9d6f5a
Batch ID: 20250612_145223
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

# Configuration for SMTP server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587                  # Common SMTP port
SMTP_USERNAME = "your_email@example.com"  # Replace with your email address
SMTP_PASSWORD = "your_password"           # Replace with your email password

def generate_recovery_code():
    """
    Generates a random 10-digit recovery code.
    """
    return ''.join(random.choices(string.digits, k=10))

def send_recovery_email(recipient_email, recovery_code):
    """
    Sends the recovery code to the user's email.
    
    Args:
        recipient_email (str): The recipient's email address.
        recovery_code (str): The recovery code to be sent.
    
    Raises:
        Exception: If there is an error in sending the email.
    """
    try:
        # Create the email message
        subject = "Password Recovery Code"
        body = f"Your password recovery code is: {recovery_code}"
        
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, recipient_email, message.as_string())
        
        print(f"Recovery code sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send recovery email: {str(e)}")
        raise

def password_recovery_flow(user_email):
    """
    Main function to handle the password recovery process.
    
    Args:
        user_email (str): The user's email address.
    """
    try:
        # Generate a recovery code
        recovery_code = generate_recovery_code()
        
        # Send the recovery code to the user's email
        send_recovery_email(user_email, recovery_code)
        
    except Exception as e:
        print(f"An error occurred during the password recovery process: {str(e)}")

# Example usage:
if __name__ == "__main__":
    user_email = input("Enter your email address: ").strip()
    password_recovery_flow(user_email)
```
