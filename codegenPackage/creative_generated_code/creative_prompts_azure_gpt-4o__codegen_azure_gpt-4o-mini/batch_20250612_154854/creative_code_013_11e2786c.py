"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Write a Python program to automate the registration process for new users on the Socrates GM portal, including email confirmation and password setup.
Generated: DETERMINISTIC_11e2786c79724c06
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import string
import random
from email.mime.text import MIMEText
from getpass import getpass

# Constants
SMTP_SERVER = 'smtp.example.com'  # Replace with your email server
SMTP_PORT = 587  # Typically 587 for TLS
EMAIL_SENDER = 'no-reply@example.com'
EMAIL_SUBJECT = 'Confirm Your Registration'
CONFIRMATION_CODE_LENGTH = 6

# User registration class
class UserRegistration:
    def __init__(self):
        self.users = {}  # To store user information
        self.confirmation_codes = {}  # To store confirmation codes

    def create_user(self, email, password):
        """Create a new user and store their details."""
        if email in self.users:
            raise ValueError("Email already registered.")

        self.users[email] = {
            'password': password,
            'confirmed': False
        }
        self.send_confirmation_email(email)

    def generate_confirmation_code(self):
        """Generate a random confirmation code."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=CONFIRMATION_CODE_LENGTH))

    def send_confirmation_email(self, email):
        """Send a confirmation email to the user."""
        code = self.generate_confirmation_code()
        self.confirmation_codes[email] = code
        
        msg = MIMEText(f'Your confirmation code is: {code}')
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_SENDER
        msg['To'] = email

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_SENDER, getpass("Enter your email password: "))  # Secure password input
                server.send_message(msg)
            print(f"Confirmation email sent to {email}.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def confirm_registration(self, email, code):
        """Confirm the user's registration with the provided confirmation code."""
        if email not in self.confirmation_codes:
            raise ValueError("No confirmation code found for this email.")

        if self.confirmation_codes[email] == code:
            self.users[email]['confirmed'] = True
            del self.confirmation_codes[email]  # Remove code after successful confirmation
            print(f"Registration confirmed for {email}.")
        else:
            raise ValueError("Invalid confirmation code.")

# Main logic
def main():
    registration = UserRegistration()
    
    # Get user details
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    try:
        # Create user and send confirmation email
        registration.create_user(email, password)
        
        # Get confirmation code from user
        code = input("Enter the confirmation code sent to your email: ")
        registration.confirm_registration(email, code)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
