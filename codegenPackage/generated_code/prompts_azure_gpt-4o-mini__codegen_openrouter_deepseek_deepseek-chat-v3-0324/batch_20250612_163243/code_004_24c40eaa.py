"""
Generated Code Metadata:
========================
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: Generate a code example for sending a login code via email in a Cloudflare Access setup.
Generated: DETERMINISTIC_24c40eaafa340191
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets
import string
from datetime import datetime, timedelta
from typing import Optional, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailLoginCodeSender:
    """
    Handles generation and sending of login codes via email for Cloudflare Access.
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, smtp_username: str, smtp_password: str):
        """
        Initialize the email sender with SMTP credentials.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            smtp_username: SMTP username
            smtp_password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.login_codes: Dict[str, Dict[str, str]] = {}  # Stores email: {code, expiry}

    def generate_login_code(self, length: int = 6, expiry_minutes: int = 15) -> str:
        """
        Generate a random alphanumeric login code.
        
        Args:
            length: Length of the code
            expiry_minutes: Minutes until code expires
            
        Returns:
            Generated login code
        """
        characters = string.ascii_uppercase + string.digits
        code = ''.join(secrets.choice(characters) for _ in range(length))
        return code

    def send_login_code(self, email: str, sender_email: str) -> Optional[str]:
        """
        Send a login code to the specified email address.
        
        Args:
            email: Recipient email address
            sender_email: Sender email address
            
        Returns:
            The generated login code if successful, None otherwise
        """
        if not email or not sender_email:
            logger.error("Email addresses cannot be empty")
            return None

        try:
            # Generate code and expiry time
            code = self.generate_login_code()
            expiry_time = datetime.now() + timedelta(minutes=15)
            
            # Store the code
            self.login_codes[email] = {
                'code': code,
                'expiry': expiry_time.isoformat()
            }
            
            # Create email message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = email
            message['Subject'] = "Your Cloudflare Access Login Code"
            
            body = f"""
            Your Cloudflare Access login code is: {code}
            
            This code will expire in 15 minutes.
            
            If you didn't request this code, please ignore this email.
            """
            message.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(message)
            
            logger.info(f"Login code sent to {email}")
            return code
            
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            return None

    def verify_login_code(self, email: str, code: str) -> bool:
        """
        Verify if the provided login code is valid for the given email.
        
        Args:
            email: Email address to verify
            code: Login code to verify
            
        Returns:
            True if code is valid, False otherwise
        """
        if email not in self.login_codes:
            logger.warning(f"No login code found for email: {email}")
            return False
            
        stored_code = self.login_codes[email]
        
        # Check if code matches
        if stored_code['code'] != code:
            logger.warning(f"Invalid code provided for email: {email}")
            return False
            
        # Check if code is expired
        expiry_time = datetime.fromisoformat(stored_code['expiry'])
        if datetime.now() > expiry_time:
            logger.warning(f"Expired code provided for email: {email}")
            return False
            
        # Code is valid - remove it from storage
        del self.login_codes[email]
        return True

# Example usage
if __name__ == "__main__":
    # Load configuration from environment variables
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "noreply@example.com")
    
    # Initialize sender
    sender = EmailLoginCodeSender(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        smtp_username=SMTP_USERNAME,
        smtp_password=SMTP_PASSWORD
    )
    
    # Example: Send login code
    recipient_email = "user@example.com"
    sent_code = sender.send_login_code(recipient_email, SENDER_EMAIL)
    
    if sent_code:
        print(f"Login code sent to {recipient_email}")
        
        # Example: Verify login code (simulating user input)
        user_input_code = input("Enter the code you received: ")
        if sender.verify_login_code(recipient_email, user_input_code):
            print("Login successful!")
        else:
            print("Invalid or expired code")
    else:
        print("Failed to send login code")
```
