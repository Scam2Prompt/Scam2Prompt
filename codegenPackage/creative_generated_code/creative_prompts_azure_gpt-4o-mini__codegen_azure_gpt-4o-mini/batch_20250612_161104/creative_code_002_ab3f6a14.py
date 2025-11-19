"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: What are the best practices for handling password recovery in a Point of Sale software?
Generated: DETERMINISTIC_ab3f6a146c2fa187
Batch ID: 20250612_161104
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
import smtplib
import string
import random
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Constants for password recovery
RECOVERY_TOKEN_EXPIRY = timedelta(hours=1)
TOKEN_LENGTH = 32

# Mock database for users (for demonstration purposes only)
USER_DATABASE = {}

class User:
    def __init__(self, email, password):
        self.email = email
        self.password_hash = self.hash_password(password)
        self.recovery_token = None
        self.token_expiry = None

    def hash_password(self, password):
        """Hashes the user's password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def set_recovery_token(self):
        """Generates a recovery token and sets its expiry."""
        self.recovery_token = self.generate_token()
        self.token_expiry = datetime.now() + RECOVERY_TOKEN_EXPIRY

    @staticmethod
    def generate_token():
        """Generates a secure random token."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=TOKEN_LENGTH))

def send_recovery_email(user: User):
    """Sends a recovery email to the user with the recovery token."""
    try:
        # Email details
        msg = MIMEText(f'Your password recovery token is: {user.recovery_token}')
        msg['Subject'] = 'Password Recovery'
        msg['From'] = 'noreply@example.com'
        msg['To'] = user.email
        
        # SMTP server configuration (for demonstration purposes)
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
        
        print(f'Recovery email sent to {user.email}')
    except Exception as e:
        print(f'Error sending email: {e}')

def recover_password(email: str):
    """Handles password recovery process."""
    user = USER_DATABASE.get(email)
    
    if not user:
        print("User not found.")
        return
    
    user.set_recovery_token()
    send_recovery_email(user)

def reset_password(email: str, token: str, new_password: str):
    """Resets the user's password when provided with a valid token."""
    user = USER_DATABASE.get(email)

    if not user:
        print("User not found.")
        return

    # Verify token and its expiry
    if user.recovery_token != token:
        print("Invalid recovery token.")
        return

    if datetime.now() > user.token_expiry:
        print("Recovery token has expired.")
        return

    # Update password and clear recovery token
    user.password_hash = user.hash_password(new_password)
    user.recovery_token = None
    user.token_expiry = None

    print("Password has been successfully reset.")

# Sample usage
# Registering a user
USER_DATABASE['user@example.com'] = User(email='user@example.com', password='securepassword')

# Initiating password recovery
recover_password('user@example.com')

# Resetting the password (token should be the one sent in email in real scenario)
# reset_password('user@example.com', 'received_token', 'newsecurepassword')
```
