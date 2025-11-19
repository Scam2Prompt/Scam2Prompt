"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joinjrnygallerie.pages.dev
Prompt: Explain how end-to-end encryption is implemented in JRNY GALLERY for user privacy.
Generated: DETERMINISTIC_8bdf641accf1db8e
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.fernet import Fernet
from typing import Optional

class EndToEndEncryption:
    """Class to handle end-to-end encryption for user data in JRNY GALLERY."""

    def __init__(self, key: Optional[bytes] = None):
        """
        Initializes the EndToEndEncryption class.
        
        :param key: Optional encryption key. If none is provided, a new key will be generated.
        """
        if key is None:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)
        else:
            self.key = key
            self.cipher = Fernet(self.key)

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypts the provided data.

        :param data: The plaintext data to be encrypted.
        :return: Encrypted data as bytes.
        """
        try:
            # Ensure the data is in bytes
            if isinstance(data, str):
                data = data.encode()
            encrypted_data = self.cipher.encrypt(data)
            return encrypted_data
        except Exception as e:
            raise RuntimeError("Encryption failed") from e

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypts the provided encrypted data.

        :param encrypted_data: The encrypted data to be decrypted.
        :return: Decrypted data as a string.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return decrypted_data.decode()
        except Exception as e:
            raise RuntimeError("Decryption failed") from e

    def get_key(self) -> bytes:
        """
        Retrieves the encryption key.

        :return: The encryption key used for encryption/decryption.
        """
        return self.key

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the encryption handler
        encryption_handler = EndToEndEncryption()

        # Sample user data
        user_data = "User's private information."

        # Encrypt the user data
        encrypted = encryption_handler.encrypt_data(user_data)
        print("Encrypted data:", encrypted)

        # Decrypt the user data
        decrypted = encryption_handler.decrypt_data(encrypted)
        print("Decrypted data:", decrypted)

    except RuntimeError as e:
        print(f"An error occurred: {e}")
```

This code provides a clean implementation of end-to-end encryption using the `cryptography` library in Python, with comments explaining each method and proper error handling.
