"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Generate Python code to automate user registration on a betting platform, including email verification and password validation as outlined in Parimatch's registration process.
Generated: DETERMINISTIC_74396a2e9720585b
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

class UserRegistration:
    def __init__(self):
        self.users = {}  # Stores users in a dictionary
        self.verification_codes = {}  # Stores verification codes for users

    def validate_email(self, email):
        """Validate email format using regex."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise RegistrationError("Invalid email format.")

    def validate_password(self, password):
        """Validate password strength."""
        if len(password) < 8:
            raise RegistrationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', password):
            raise RegistrationError("Password must contain at least one letter.")
        if not re.search(r'\d', password):
            raise RegistrationError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise RegistrationError("Password must contain at least one special character.")

    def generate_verification_code(self):
        """Generate a random 6-digit verification code."""
        return ''.join(random.choices(string.digits, k=6))

    def send_verification_email(self, email, code):
        """Send a verification email to the user."""
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = 'Email Verification Code'
        
        body = f"Your verification code is: {code}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the server
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Verification email sent to {email}.")
        except Exception as e:
            raise RegistrationError(f"Failed to send verification email: {e}")

    def register_user(self, email, password):
        """Register a new user after validation and send verification email."""
        self.validate_email(email)
        self.validate_password(password)

        if email in self.users:
            raise RegistrationError("Email is already registered.")

        # Store user data
        self.users[email] = {'password': password, 'verified': False}
        verification_code = self.generate_verification_code()
        self.verification_codes[email] = verification_code

        # Send verification email
        self.send_verification_email(email, verification_code)

    def verify_user(self, email, code):
        """Verify the user's email using the code sent."""
        if email not in self.users:
            raise RegistrationError("No user found with this email.")

        if self.verification_codes.get(email) == code:
            self.users[email]['verified'] = True
            del self.verification_codes[email]  # Remove used code
            print(f"Email {email} verified successfully.")
        else:
            raise RegistrationError("Invalid verification code.")

# Example usage
if __name__ == "__main__":
    registration_system = UserRegistration()
    try:
        email = "user@example.com"
        password = "Password123!"
        
        # Register user
        registration_system.register_user(email, password)
        
        # Simulate user input for verification
        verification_code = registration_system.verification_codes[email]
        registration_system.verify_user(email, verification_code)
    except RegistrationError as e:
        print(f"Registration error: {e}")
```
