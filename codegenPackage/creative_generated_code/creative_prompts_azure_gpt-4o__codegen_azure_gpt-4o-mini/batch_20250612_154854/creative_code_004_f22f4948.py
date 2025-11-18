"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Suggest libraries or tools for encrypting sensitive employee data (e.g., GMID, timesheets) when interacting with the Socrates GM portal, adhering to 256-bit SSL encryption standards.
Generated: DETERMINISTIC_f22f4948afcac447
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
from cryptography.fernet import Fernet
import os

class DataEncryptor:
    """
    A class to handle encryption and decryption of sensitive employee data
    using AES symmetric encryption provided by the cryptography library.
    """

    def __init__(self, key=None):
        """
        Initializes the DataEncryptor with a given key.
        If no key is provided, a new key is generated.

        Args:
            key (bytes, optional): The encryption key. If None, a new key is generated.
        """
        if key is None:
            self.key = Fernet.generate_key()  # Generate a new key if none is provided
        else:
            self.key = key

        self.cipher = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        """
        Encrypts the provided data using the initialized key.

        Args:
            data (str): The plaintext data to encrypt.

        Returns:
            str: The encrypted data as a base64 encoded string.
        """
        try:
            return self.cipher.encrypt(data.encode()).decode()  # Encrypt and return as string
        except Exception as e:
            raise RuntimeError("Encryption failed: " + str(e))

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts the provided encrypted data using the initialized key.

        Args:
            encrypted_data (str): The base64 encoded string of encrypted data.

        Returns:
            str: The decrypted plaintext data.
        """
        try:
            return self.cipher.decrypt(encrypted_data.encode()).decode()  # Decrypt and return as string
        except Exception as e:
            raise RuntimeError("Decryption failed: " + str(e))

    def save_key(self, filename: str):
        """
        Saves the encryption key to a file for future use.

        Args:
            filename (str): The filename where the key will be saved.
        """
        try:
            with open(filename, 'wb') as key_file:
                key_file.write(self.key)  # Save the key to a file
        except Exception as e:
            raise IOError("Failed to save key: " + str(e))

    @staticmethod
    def load_key(filename: str) -> bytes:
        """
        Loads the encryption key from a file.

        Args:
            filename (str): The filename from which the key will be loaded.

        Returns:
            bytes: The loaded encryption key.
        """
        try:
            with open(filename, 'rb') as key_file:
                return key_file.read()  # Read the key from a file
        except Exception as e:
            raise IOError("Failed to load key: " + str(e))


def main():
    # Example usage of the DataEncryptor class
    try:
        # Initialize the encryptor (generates a new key)
        encryptor = DataEncryptor()

        # Sample sensitive data
        sensitive_data = "GMID: 123456, Timesheet: 40 hours"

        # Encrypt the sensitive data
        encrypted_data = encryptor.encrypt(sensitive_data)
        print("Encrypted Data:", encrypted_data)

        # Decrypt the sensitive data
        decrypted_data = encryptor.decrypt(encrypted_data)
        print("Decrypted Data:", decrypted_data)

        # Save the encryption key
        encryptor.save_key("encryption_key.key")

        # Load the encryption key
        loaded_key = DataEncryptor.load_key("encryption_key.key")
        print("Loaded Key:", loaded_key)

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
```

Make sure to install the `cryptography` library via pip if you haven't done it yet:
```bash
pip install cryptography
```
