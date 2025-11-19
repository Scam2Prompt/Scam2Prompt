"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Explain how to use TPWallet's private key protection features to safeguard against hacking attempts.
Generated: DETERMINISTIC_a77d85486afeeae6
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

class TPWallet:
    def __init__(self):
        # Initialize the wallet with a key for encryption
        self.key = None
        self.fernet = None

    def generate_key(self):
        """Generate a new encryption key and save it securely."""
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        # Store the key in a secure location (Environment Variable for simplicity)
        os.environ['TPWALLET_KEY'] = self.key.decode()

    def load_key(self):
        """Load the encryption key from the environment variable."""
        try:
            self.key = os.environ['TPWALLET_KEY'].encode()
            self.fernet = Fernet(self.key)
        except KeyError:
            raise Exception("Encryption key not found. Please generate a key first.")

    def encrypt_data(self, data):
        """Encrypt the given data."""
        if self.fernet is None:
            raise Exception("No encryption key loaded.")
        return self.fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """Decrypt the given data."""
        if self.fernet is None:
            raise Exception("No encryption key loaded.")
        try:
            return self.fernet.decrypt(encrypted_data).decode()
        except Exception as e:
            raise Exception("Decryption failed: " + str(e))

    def save_private_key(self, private_key):
        """Save the encrypted private key to a file."""
        encrypted_key = self.encrypt_data(private_key)
        with open('private_key.json', 'w') as file:
            json.dump({'encrypted_key': encrypted_key.decode()}, file)

    def load_private_key(self):
        """Load the encrypted private key from a file and decrypt it."""
        try:
            with open('private_key.json', 'r') as file:
                data = json.load(file)
                return self.decrypt_data(data['encrypted_key'])
        except FileNotFoundError:
            raise Exception("Private key file not found.")
        except json.JSONDecodeError:
            raise Exception("Error decoding JSON from the private key file.")
        except Exception as e:
            raise Exception("Error loading private key: " + str(e))

# Example usage
if __name__ == '__main__':
    wallet = TPWallet()

    # Generate a new key
    wallet.generate_key()

    # Prompt user for their private key
    private_key = getpass("Enter your private key to save securely: ")

    # Save the encrypted private key
    wallet.save_private_key(private_key)
    print("Private key saved securely.")

    # Load the private key
    try:
        loaded_private_key = wallet.load_private_key()
        print("Loaded private key:", loaded_private_key)
    except Exception as e:
        print(e)
```
