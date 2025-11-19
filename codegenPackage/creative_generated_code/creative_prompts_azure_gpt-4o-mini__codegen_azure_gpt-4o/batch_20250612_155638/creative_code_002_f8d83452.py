"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Generate code for a user account management system that includes features like password reset and terms acceptance, inspired by Signalrextrack's user interface.
Generated: DETERMINISTIC_f8d83452e58184e2
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
from datetime import datetime

# In-memory database simulation for user accounts
class UserAccountDatabase:
    def __init__(self):
        self.users = {}
        self.reset_tokens = {}

    def add_user(self, username, password, email):
        if username in self.users:
            raise ValueError("Username already exists.")
        if not username or not password or not email:
            raise ValueError("All fields are required.")
        
        hashed_password = self._hash_password(password)
        self.users[username] = {
            'username': username,
            'password': hashed_password,
            'email': email,
            'terms_accepted': False,
            'last_updated': datetime.utcnow()
        }

    def get_user(self, username):
        return self.users.get(username)

    def update_password(self, username, new_password):
        user = self.get_user(username)
        if user:
            user['password'] = self._hash_password(new_password)
            user['last_updated'] = datetime.utcnow()
        else:
            raise ValueError("User not found.")

    def generate_reset_token(self, username):
        user = self.get_user(username)
        if user:
            token = str(uuid.uuid4())
            self.reset_tokens[token] = {'username': username, 'expires': datetime.utcnow()}
            return token
        else:
            raise ValueError("User not found.")

    def reset_password_with_token(self, token, new_password):
        token_data = self.reset_tokens.get(token)
        if not token_data:
            raise ValueError("Invalid or expired reset token.")
        
        username = token_data['username']
        self.update_password(username, new_password)
        del self.reset_tokens[token]  # Remove token after use

    def accept_terms(self, username):
        user = self.get_user(username)
        if user:
            user['terms_accepted'] = True
            user['last_updated'] = datetime.utcnow()
        else:
            raise ValueError("User not found.")

    def _hash_password(self, password):
        # Hash the password using SHA-256 with a salt
        salt = uuid.uuid4().hex
        return hashlib.sha256((salt + password).encode()).hexdigest()


# Main functionality for user account management
class UserAccountManager:
    def __init__(self):
        self.db = UserAccountDatabase()

    def register_user(self, username, password, email):
        try:
            self.db.add_user(username, password, email)
            print(f"User '{username}' registered successfully.")
        except ValueError as e:
            print(f"Registration failed: {e}")

    def request_password_reset(self, username):
        try:
            token = self.db.generate_reset_token(username)
            print(f"Password reset token: {token}")
        except ValueError as e:
            print(f"Password reset request failed: {e}")

    def reset_password(self, token, new_password):
        try:
            self.db.reset_password_with_token(token, new_password)
            print("Password reset successful.")
        except ValueError as e:
            print(f"Password reset failed: {e}")

    def accept_terms_of_service(self, username):
        try:
            self.db.accept_terms(username)
            print(f"User '{username}' accepted terms of service.")
        except ValueError as e:
            print(f"Terms acceptance failed: {e}")


# Example usage
if __name__ == "__main__":
    manager = UserAccountManager()

    # Register a new user
    manager.register_user("john_doe", "securepassword123", "john.doe@example.com")

    # Request password reset
    reset_token = manager.db.generate_reset_token("john_doe")
    print(f"Generated token: {reset_token}")

    # Reset password using token
    manager.reset_password(reset_token, "new_secure_password")

    # Accept terms of service
    manager.accept_terms_of_service("john_doe")
```
