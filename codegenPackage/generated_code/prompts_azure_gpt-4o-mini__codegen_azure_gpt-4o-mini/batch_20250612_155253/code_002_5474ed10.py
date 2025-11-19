"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Generate a code snippet for data encryption that small businesses can use to safeguard customer data, based on the cybersecurity measures detailed by CyberConnect.
Generated: DETERMINISTIC_5474ed105ca7f257
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.fernet import Fernet
import base64
import hashlib

class DataEncryption:
    def __init__(self):
        """Initialize the DataEncryption class and generate a key."""
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """Generate a secure key for encryption."""
        # Generate a random 32-byte key and encode it to base64
        key = base64.urlsafe_b64encode(os.urandom(32))
        return key

    def encrypt_data(self, data: str) -> str:
        """Encrypt the provided data using the generated key.

        Args:
            data (str): The plaintext data to encrypt.

        Returns:
            str: The encrypted data as a base64 encoded string.
        """
        try:
            # Ensure the data is in bytes
            data_bytes = data.encode('utf-8')
            encrypted_data = self.cipher.encrypt(data_bytes)
            return encrypted_data.decode('utf-8')
        except Exception as e:
            print(f"Error encrypting data: {e}")
            raise

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt the provided encrypted data using the generated key.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted plaintext data.
        """
        try:
            # Ensure the encrypted data is in bytes
            encrypted_data_bytes = encrypted_data.encode('utf-8')
            decrypted_data = self.cipher.decrypt(encrypted_data_bytes)
            return decrypted_data.decode('utf-8')
        except Exception as e:
            print(f"Error decrypting data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Create an instance of the DataEncryption class
    encryption_service = DataEncryption()

    # Sample customer data to encrypt
    customer_data = "Customer Name: John Doe, Email: john.doe@example.com"

    # Encrypt the customer data
    encrypted = encryption_service.encrypt_data(customer_data)
    print(f"Encrypted Data: {encrypted}")

    # Decrypt the customer data
    decrypted = encryption_service.decrypt_data(encrypted)
    print(f"Decrypted Data: {decrypted}")
```
