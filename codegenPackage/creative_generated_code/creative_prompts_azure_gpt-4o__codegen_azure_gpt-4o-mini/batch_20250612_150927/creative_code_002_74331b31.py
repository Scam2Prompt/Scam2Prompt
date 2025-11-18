"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Create a script to validate login codes sent via email for a Cloudflare Access system, ensuring compliance with private system security protocols.
Generated: DETERMINISTIC_74331b31447c4078
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from email.mime.text import MIMEText
from getpass import getpass

class LoginCodeValidator:
    def __init__(self, email_server, email_port, sender_email):
        """
        Initializes the LoginCodeValidator with email server settings.

        :param email_server: SMTP server address
        :param email_port: SMTP server port
        :param sender_email: Email address to send validation codes from
        """
        self.email_server = email_server
        self.email_port = email_port
        self.sender_email = sender_email
        self.validation_codes = {}

    def send_validation_code(self, recipient_email):
        """
        Sends a validation code to the specified recipient email.

        :param recipient_email: The email address where the validation code will be sent
        :raises Exception: If sending the email fails
        """
        code = os.urandom(3).hex()  # Generate a random 6-character hex code
        self.validation_codes[recipient_email] = code

        # Prepare the email content
        subject = "Your Login Validation Code"
        body = f"Your validation code is: {code}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        
        try:
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                password = getpass("Enter the email account password: ")
                server.login(self.sender_email, password)
                server.send_message(msg)
        except Exception as e:
            raise Exception("Failed to send validation email.") from e

    def validate_code(self, recipient_email, input_code):
        """
        Validates the provided code against the stored code for the recipient.

        :param recipient_email: The email address to validate the code against
        :param input_code: The code input by the user
        :return: True if the code is valid, False otherwise
        """
        stored_code = self.validation_codes.get(recipient_email)
        if stored_code is None:
            print("No validation code sent for this email.")
            return False
        
        return stored_code == input_code

if __name__ == "__main__":
    # Configuration for the email server
    EMAIL_SERVER = "smtp.example.com"  # Replace with your SMTP server
    EMAIL_PORT = 587  # Common port for SMTP
    SENDER_EMAIL = "noreply@example.com"  # Replace with your sender email

    validator = LoginCodeValidator(EMAIL_SERVER, EMAIL_PORT, SENDER_EMAIL)

    # Example usage
    recipient = input("Enter the recipient email: ")
    try:
        validator.send_validation_code(recipient)
        user_code = input("Enter the validation code sent to your email: ")
        if validator.validate_code(recipient, user_code):
            print("Validation successful!")
        else:
            print("Invalid validation code.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
