"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Write a code snippet to handle user registration in MicroLab, including password recovery options.
Generated: DETERMINISTIC_2ebfb623997dcd70
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Registration and Password Recovery system for MicroLab.

This code snippet handles:
1. User registration with proper validation.
2. Password recovery via email.
"""

import re
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# In-memory database for demonstration purposes. Replace with a production database.
user_db = {}

# Configuration for SMTP (use environment variables in production)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
EMAIL_SENDER = "your_email@example.com"


def hash_password(password):
    """
    Hash the password using SHA-256 for secure storage.
    :param password: Plain text password.
    :return: Hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def validate_email(email):
    """
    Validate email format using regex.
    :param email: Email address to validate.
    :return: True if valid, False otherwise.
    """
    return re.match(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", email) is not None


def register_user(email, password):
    """
    Register a new user in the system.
    :param email: User's email address.
    :param password: User's plain text password.
    :return: Success message or error message.
    """
    if not validate_email(email):
        return "Invalid email format."

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if email in user_db:
        return "Email is already registered."

    user_db[email] = {
        "password": hash_password(password),
        "recovery_token": None
    }
    return "Registration successful."


def generate_recovery_token(email):
    """
    Generate a password recovery token for the user.
    :param email: User's email address.
    :return: Recovery token or error message.
    """
    if email not in user_db:
        return "Email not registered."

    # Simple token generation (use a stronger method in production)
    token = hashlib.sha256(email.encode()).hexdigest()
    user_db[email]["recovery_token"] = token
    return token


def send_recovery_email(email, recovery_token):
    """
    Send a password recovery email to the user.
    :param email: User's email address.
    :param recovery_token: Token for password recovery.
    """
    try:
        # Create email content
        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = email
        message["Subject"] = "MicroLab Password Recovery"

        body = f"""
        Hello,

        You requested a password recovery. Use the token below to reset your password:

        Recovery Token: {recovery_token}

        If you did not request this, please ignore this email.

        Regards,
        MicroLab Team
        """
        message.attach(MIMEText(body, "plain"))

        # Send email via SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, email, message.as_string())
        
        print("Recovery email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def recover_password(email, token, new_password):
    """
    Recover the user's password.
    :param email: User's email address.
    :param token: Recovery token provided to the user.
    :param new_password: New password for the user.
    :return: Success message or error message.
    """
    if email not in user_db:
        return "Email not registered."

    if user_db[email]["recovery_token"] != token:
        return "Invalid recovery token."

    if len(new_password) < 8:
        return "Password must be at least 8 characters long."

    user_db[email]["password"] = hash_password(new_password)
    user_db[email]["recovery_token"] = None  # Invalidate the token after use
    return "Password successfully updated."


# Example usage
if __name__ == "__main__":
    # User registration
    print(register_user("user@example.com", "securepassword"))

    # Generate recovery token
    token = generate_recovery_token("user@example.com")
    if token:
        print(f"Recovery Token: {token}")

        # Send recovery email
        send_recovery_email("user@example.com", token)

        # Password recovery
        print(recover_password("user@example.com", token, "newsecurepassword"))
```
