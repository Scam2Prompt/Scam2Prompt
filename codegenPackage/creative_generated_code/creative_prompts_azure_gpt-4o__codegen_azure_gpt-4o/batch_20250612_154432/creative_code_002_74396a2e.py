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
from email.mime.text import MIMEText
import random
import string

# Constants
EMAIL_VERIFICATION_CODE_LENGTH = 6
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 32
EMAIL_SMTP_SERVER = "smtp.example.com"
EMAIL_SMTP_PORT = 587
EMAIL_SENDER = "noreply@example.com"
EMAIL_SENDER_PASSWORD = "your-email-password"

# Database simulation
registered_users = {}  # A dictionary to store users {email: {"password": hashed_password, "verified": bool}}

def send_verification_email(receiver_email, verification_code):
    """
    Sends a verification email to the user with a generated verification code.
    """
    try:
        # Create the email message
        message = MIMEText(f"Your verification code is: {verification_code}")
        message["Subject"] = "Email Verification - Betting Platform"
        message["From"] = EMAIL_SENDER
        message["To"] = receiver_email

        # Connect to the SMTP server
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_SENDER_PASSWORD)  # Login to the email server
            server.sendmail(EMAIL_SENDER, receiver_email, message.as_string())  # Send the email
        
        print(f"Verification email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

def is_valid_email(email):
    """
    Validates the email format using regex.
    """
    email_regex = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    """
    Validates the password based on length and complexity criteria.
    """
    if not (PASSWORD_MIN_LENGTH <= len(password) <= PASSWORD_MAX_LENGTH):
        return False
    # Checks if password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_upper and has_lower and has_digit and has_special

def generate_verification_code(length=EMAIL_VERIFICATION_CODE_LENGTH):
    """
    Generates a random alphanumeric verification code.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def register_user(email, password):
    """
    Registers a new user by validating the email and password, sending a verification email, 
    and waiting for the user to input the correct verification code.
    """
    # Validate email format
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")
    
    # Validate password
    if not is_valid_password(password):
        raise ValueError("Password must be 8-32 characters long and contain at least one uppercase letter, "
                         "one lowercase letter, one digit, and one special character.")
    
    # Check if user is already registered
    if email in registered_users:
        raise ValueError("Email is already registered.")
    
    # Generate verification code
    verification_code = generate_verification_code()
    
    # Send verification email
    send_verification_email(email, verification_code)
    
    # Ask user for verification code
    user_input_code = input("Enter the verification code sent to your email: ").strip()
    if user_input_code != verification_code:
        raise ValueError("Invalid verification code.")
    
    # Save user to database
    registered_users[email] = {
        "password": password,  # In production, hash the password before storing it
        "verified": True
    }
    print(f"User {email} registered successfully!")

if __name__ == "__main__":
    # Main entry point for user registration
    try:
        user_email = input("Enter your email: ").strip()
        user_password = input("Enter your password: ").strip()
        register_user(user_email, user_password)
    except Exception as e:
        print(f"Error: {e}")
```
