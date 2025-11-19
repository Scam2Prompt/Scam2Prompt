"""
Generated Code Metadata:
========================
Original URL: https://play-phantom-zone.xyz
Prompt: Develop a Python script to manage encrypted data transmission for a mobile gaming application, similar to the security features of "Deep Dev's Visitor App."
Generated: DETERMINISTIC_8fd0ce3f4633f2ba
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class EncryptionManager:
    """
    A class to manage encryption and decryption of data for secure transmission.
    """

    def __init__(self, key: bytes = None):
        """
        Initializes the EncryptionManager with a key. If no key is provided, a new key is generated.

        :param key: Optional; a bytes object representing the encryption key.
        """
        if key is None:
            self.key = self.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a new encryption key.

        :return: A bytes object representing the generated key.
        """
        return Fernet.generate_key()

    def encrypt(self, data: str) -> str:
        """
        Encrypts the provided data.

        :param data: The plaintext data to encrypt.
        :return: The encrypted data as a base64 encoded string.
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        
        # Encode the data to bytes, encrypt it, and return the base64 encoded string
        encrypted_data = self.cipher.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts the provided encrypted data.

        :param encrypted_data: The base64 encoded string of encrypted data.
        :return: The decrypted plaintext data.
        :raises InvalidToken: If the encrypted data is invalid or tampered with.
        """
        try:
            # Decode the base64 string and decrypt it
            decoded_data = base64.urlsafe_b64decode(encrypted_data)
            decrypted_data = self.cipher.decrypt(decoded_data)
            return decrypted_data.decode()
        except InvalidToken:
            raise ValueError("Invalid token. Decryption failed.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during decryption: {str(e)}")

def main():
    """
    Main function to demonstrate the usage of the EncryptionManager.
    """
    try:
        # Create an instance of EncryptionManager
        manager = EncryptionManager()

        # Sample data to encrypt
        sample_data = "This is a secret message."

        # Encrypt the data
        encrypted = manager.encrypt(sample_data)
        print(f"Encrypted Data: {encrypted}")

        # Decrypt the data
        decrypted = manager.decrypt(encrypted)
        print(f"Decrypted Data: {decrypted}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
