"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deeper-net.works
Prompt: Write Python code to integrate enterprise-grade encryption for network security, referencing the features of Deeper Network's solutions.
Generated: DETERMINISTIC_1fe0605199249a6a
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken


class EncryptionManager:
    """A class to manage encryption and decryption of data using Fernet symmetric encryption."""

    def __init__(self):
        """Initialize the EncryptionManager and generate a key for encryption."""
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """Generate a new Fernet key."""
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> str:
        """Encrypt the provided data.

        Args:
            data (str): The plain text data to encrypt.

        Returns:
            str: The encrypted data encoded in URL-safe base64.
        """
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            return encrypted_data.decode()
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {e}")

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt the provided encrypted data.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted plain text data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except InvalidToken:
            raise ValueError("Invalid token! Decryption failed.")
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")


def main():
    """Main function to demonstrate encryption and decryption."""
    encryption_manager = EncryptionManager()

    # Sample data to encrypt
    plain_text_data = "Sensitive information that needs encryption."

    print("Original Data:", plain_text_data)

    # Encrypt the data
    encrypted_data = encryption_manager.encrypt_data(plain_text_data)
    print("Encrypted Data:", encrypted_data)

    # Decrypt the data
    try:
        decrypted_data = encryption_manager.decrypt_data(encrypted_data)
        print("Decrypted Data:", decrypted_data)
    except ValueError as ve:
        print(f"Decryption error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")

if __name__ == "__main__":
    main()
```

Make sure to install the required package by running:
```bash
pip install cryptography
```
