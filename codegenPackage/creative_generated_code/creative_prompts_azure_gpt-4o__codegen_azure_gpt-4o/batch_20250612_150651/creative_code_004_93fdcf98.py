"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Write code to reset a user's password in the MultiTMS system, ensuring compliance with secure authentication protocols.
Generated: DETERMINISTIC_93fdcf9838065d24
Batch ID: 20250612_150651
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
import string
import random
from datetime import datetime, timedelta

# Simulated database interface
class Database:
    def __init__(self):
        self.users = {}  # Example: {'username': {'password_hash': ..., 'reset_token': ..., 'token_expiry': ...}}

    def get_user(self, username):
        return self.users.get(username)

    def update_user(self, username, updates):
        if username in self.users:
            self.users[username].update(updates)
        else:
            raise ValueError("User not found")

# Generate a secure random token
def generate_secure_token(length=64):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate a password hash using a secure hashing algorithm (SHA-256 for demonstration)
def hash_password(password, salt_length=16):
    salt = os.urandom(salt_length).hex()
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hashed}"

# Verify the hashed password
def verify_password(password, stored_hash):
    try:
        salt, hashed = stored_hash.split(':')
        return hashlib.sha256((salt + password).encode()).hexdigest() == hashed
    except ValueError:
        return False

# Send the password reset token (simulated for demonstration purposes)
def send_reset_token(username, reset_token):
    print(f"Reset token for user '{username}': {reset_token}")

# Reset password function
def reset_password(db, username, new_password, reset_token):
    """
    Reset the user's password in the MultiTMS system.

    :param db: Database instance
    :param username: Username of the user
    :param new_password: New password for the user
    :param reset_token: Reset token provided to the user
    :raises ValueError: If the user does not exist or token validation fails
    """
    user = db.get_user(username)
    if not user:
        raise ValueError("User not found")

    # Validate reset token and expiry
    if user.get('reset_token') != reset_token:
        raise ValueError("Invalid reset token")
    if datetime.utcnow() > user.get('token_expiry'):
        raise ValueError("Reset token has expired")

    # Hash the new password and update the user record
    hashed_password = hash_password(new_password)
    db.update_user(username, {'password_hash': hashed_password, 'reset_token': None, 'token_expiry': None})
    print(f"Password successfully reset for user '{username}'")

# Request password reset function
def request_password_reset(db, username):
    """
    Generates a secure reset token for the user and sends it.

    :param db: Database instance
    :param username: Username of the user
    :raises ValueError: If the user does not exist
    """
    user = db.get_user(username)
    if not user:
        raise ValueError("User not found")

    # Generate reset token and expiry time
    reset_token = generate_secure_token()
    expiry_time = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
    db.update_user(username, {'reset_token': reset_token, 'token_expiry': expiry_time})

    # Simulate sending the reset token
    send_reset_token(username, reset_token)

# Example usage
if __name__ == "__main__":
    # Initialize the database and add a sample user
    db = Database()
    username = "test_user"
    initial_password = "securepassword123"
    db.users[username] = {'password_hash': hash_password(initial_password)}

    # Request a password reset
    request_password_reset(db, username)

    # Simulate user resetting the password with the provided reset token
    try:
        user_data = db.get_user(username)
        reset_password(db, username, "new_secure_password456", user_data['reset_token'])
    except ValueError as e:
        print(f"Error: {e}")
```
