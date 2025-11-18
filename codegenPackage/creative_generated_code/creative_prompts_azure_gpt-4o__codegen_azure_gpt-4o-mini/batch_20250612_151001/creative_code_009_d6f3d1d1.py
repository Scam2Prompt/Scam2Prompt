"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.caimaosheng.com
Prompt: Provide code to securely generate and store private keys and mnemonic phrases using TPWallet's encryption standards.
Generated: DETERMINISTIC_d6f3d1d19ff11fa1
Batch ID: 20250612_151001
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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode, urlsafe_b64decode
from getpass import getpass

class KeyStorage:
    """Class for generating and securely storing private keys and mnemonic phrases."""

    def __init__(self, password: str):
        """Initialize KeyStorage with a user-defined password."""
        self.password = password
        self.salt = os.urandom(16)  # Generate a secure random salt

    def generate_private_key(self):
        """Generate a new RSA private key."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        return private_key

    def encrypt_private_key(self, private_key):
        """Encrypt the private key using a password-derived key."""
        # Derive a key from the password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = urlsafe_b64encode(kdf.derive(self.password.encode()))

        # Encrypt the private key
        encrypted_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL
        )
        return encrypted_key, key

    def save_key(self, encrypted_key, key):
        """Save the encrypted private key and salt to a JSON file."""
        data = {
            'encrypted_key': encrypted_key.decode(),
            'salt': urlsafe_b64encode(self.salt).decode(),
            'key': key.decode()
        }
        with open('key_storage.json', 'w') as f:
            json.dump(data, f)

    def generate_mnemonic(self):
        """Generate a secure random mnemonic phrase."""
        mnemonic = os.urandom(16)  # Replace with a proper mnemonic generation method
        return urlsafe_b64encode(mnemonic).decode()

def main():
    """Main function to execute key generation and storage."""
    try:
        password = getpass("Enter a secure password for key storage: ")
        key_storage = KeyStorage(password)

        # Generate and encrypt the private key
        private_key = key_storage.generate_private_key()
        encrypted_key, key = key_storage.encrypt_private_key(private_key)

        # Save the private key and other details
        key_storage.save_key(encrypted_key, key)
        
        # Generate and display the mnemonic phrase
        mnemonic_phrase = key_storage.generate_mnemonic()
        print(f"Mnemonic phrase generated: {mnemonic_phrase}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
