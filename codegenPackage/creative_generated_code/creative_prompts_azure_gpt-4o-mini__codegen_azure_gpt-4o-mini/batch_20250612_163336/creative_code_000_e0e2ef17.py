"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.caimaosheng.com
Prompt: How can I implement dual verification in a cryptocurrency wallet using TPWallet's security features?
Generated: DETERMINISTIC_e0e2ef17c7117473
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import hashlib

class TPWallet:
    def __init__(self):
        self.users = {}
        self.verification_codes = {}

    def create_user(self, username, password):
        """Create a new user in the wallet."""
        if username in self.users:
            raise ValueError("Username already exists.")
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        print(f"User {username} created successfully.")

    def hash_password(self, password):
        """Hash the user's password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_verification_code(self):
        """Generate a random 6-digit verification code."""
        return str(random.randint(100000, 999999))

    def send_verification_code(self, username):
        """Simulate sending a verification code to the user."""
        if username not in self.users:
            raise ValueError("User not found.")
        code = self.generate_verification_code()
        self.verification_codes[username] = code
        print(f"Verification code for {username}: {code}")

    def verify_code(self, username, code):
        """Verify the provided code against the stored code."""
        if username not in self.verification_codes:
            raise ValueError("No verification code sent to this user.")
        if self.verification_codes[username] == code:
            print(f"Verification successful for {username}.")
            del self.verification_codes[username]  # Remove code after successful verification
            return True
        else:
            raise ValueError("Invalid verification code.")

    def login(self, username, password):
        """Log in a user after verifying their password and sending a verification code."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        hashed_password = self.hash_password(password)
        if self.users[username] != hashed_password:
            raise ValueError("Incorrect password.")
        
        self.send_verification_code(username)
        print("Check your verification code and confirm.")

# Example usage:
if __name__ == "__main__":
    wallet = TPWallet()

    # Create a user
    try:
        wallet.create_user("alice", "securePassword123")
    except ValueError as e:
        print(e)

    # Log in the user
    try:
        wallet.login("alice", "securePassword123")
        # Simulate user input for verification
        user_code = input("Enter the verification code sent to your device: ")
        wallet.verify_code("alice", user_code)
    except ValueError as e:
        print(e)
```
