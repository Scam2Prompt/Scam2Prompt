"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multidappsrectifier.pages.dev
Prompt: Create a Python script to reset a wallet password using the Resolver String protocol, ensuring secure synchronization and account recovery.
Generated: DETERMINISTIC_0fb08421010cd286
Batch ID: 20250612_152235
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
import json
import base64

class Wallet:
    def __init__(self, wallet_file='wallet.json'):
        self.wallet_file = wallet_file
        self.wallet_data = self.load_wallet()

    def load_wallet(self):
        """Load the wallet data from a JSON file."""
        try:
            with open(self.wallet_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Error decoding wallet JSON file.")
    
    def save_wallet(self):
        """Save the wallet data to a JSON file."""
        try:
            with open(self.wallet_file, 'w') as file:
                json.dump(self.wallet_data, file, indent=4)
        except IOError as e:
            raise IOError("Failed to save wallet data: " + str(e))

    def hash_password(self, password):
        """Create a secure hash of the password."""
        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return base64.b64encode(salt + password_hash).decode('utf-8')

    def reset_password(self, old_password, new_password):
        """
        Reset the wallet password.

        Args:
            old_password (str): The current wallet password.
            new_password (str): The new password to set.

        Raises:
            ValueError: If the old password does not match.
        """
        # Validate old password
        if not self.validate_password(old_password):
            raise ValueError("Old password is incorrect.")

        # Hash the new password and update the wallet
        self.wallet_data['password'] = self.hash_password(new_password)
        self.save_wallet()
        print("Password reset successfully.")

    def validate_password(self, password):
        """Validate the provided password against the stored hash."""
        stored_password = self.wallet_data.get('password')
        if not stored_password:
            return False

        salt_and_hash = base64.b64decode(stored_password.encode('utf-8'))
        salt = salt_and_hash[:16]
        stored_hash = salt_and_hash[16:]

        # Hash the provided password with the stored salt
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

        return password_hash == stored_hash

if __name__ == '__main__':
    # Example of how to use the Wallet class
    wallet = Wallet()

    # Example usage (for demonstration purposes only; handle with care)
    try:
        print("Resetting wallet password...")
        old_pass = input("Enter your old password: ")
        new_pass = input("Enter your new password: ")
        wallet.reset_password(old_pass, new_pass)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
