"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Provide an example of a secure password reset function for a TMS application, referencing the user authentication process used in MultiTMS.
Generated: DETERMINISTIC_991915b5ef8d1cb0
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import random
import string
import smtplib
from email.mime.text import MIMEText
from your_database_module import User, get_user_by_email, save_user

# Constants
RESET_TOKEN_LENGTH = 32
EMAIL_SENDER = "no-reply@yourdomain.com"
SMTP_SERVER = "smtp.yourdomain.com"
SMTP_PORT = 587
SMTP_USER = "smtp_user"
SMTP_PASSWORD = "smtp_password"


def generate_reset_token(length=RESET_TOKEN_LENGTH):
    """Generate a secure password reset token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def hash_token(token):
    """Hash the reset token for secure storage."""
    return hashlib.sha256(token.encode()).hexdigest()


def send_reset_email(user_email, reset_token):
    """Send an email with the reset token to the user."""
    subject = "Password Reset Request"
    body = f"Please use the following token to reset your password: {reset_token}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = user_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        raise RuntimeError("Failed to send email: " + str(e))


def reset_password(email):
    """Reset a user's password via email."""
    # Find the user by email
    user = get_user_by_email(email)
    if user is None:
        raise ValueError("User not found.")

    # Generate a reset token
    reset_token = generate_reset_token()
    hashed_token = hash_token(reset_token)

    # Save the hashed token to the user record (in a real application, set an expiration time)
    user.reset_token = hashed_token
    save_user(user)

    # Send the reset email
    send_reset_email(user.email, reset_token)


def validate_reset_token(user, token):
    """Validate the provided reset token against the user's stored token."""
    hashed_token = hash_token(token)
    if user.reset_token != hashed_token:
        raise ValueError("Invalid or expired reset token.")
    

def update_password(user, new_password):
    """Update the user's password to a new one."""
    user.password_hash = hash_password(new_password)  # Implement hash_password securely
    user.reset_token = None  # Clear the reset token after successful reset
    save_user(user)


def hash_password(password):
    """Hash the password for secure storage."""
    # Use a strong hashing algorithm with a salt
    salt = os.urandom(16)  # Secure random salt
    hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed_pw  # Store both salt and hash


# Example usage:
# try:
#     reset_password("user@example.com")
# except ValueError as e:
#     print(e)
# except RuntimeError as e:
#     print(e)
```
