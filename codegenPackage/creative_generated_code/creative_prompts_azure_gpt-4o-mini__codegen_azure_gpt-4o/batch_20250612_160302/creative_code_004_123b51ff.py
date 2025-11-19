"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifemedicos.com.br
Prompt: Suggest a library or API that can help manage sensitive personal data securely when offering life insurance products, similar to MetLife's approach.
Generated: DETERMINISTIC_123b51ff4a72d058
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example using the `cryptography` library to securely manage sensitive personal data. This code demonstrates encryption and decryption of sensitive data, which is essential for handling personal information securely.

```python
from cryptography.fernet import Fernet
import os

class SensitiveDataManager:
    """
    A class to manage sensitive personal data securely using encryption.
    """

    def __init__(self, key_file="secret.key"):
        """
        Initializes the SensitiveDataManager.

        Args:
            key_file (str): Path to the key file for storing the encryption key.
        """
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self):
        """
        Loads an existing encryption key from the key file or generates a new one.

        Returns:
            bytes: Encryption key.
        """
        if os.path.exists(self.key_file):
            # Load the existing key
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        else:
            # Generate a new key and save it securely
            new_key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(new_key)
            return new_key

    def encrypt_data(self, sensitive_data):
        """
        Encrypts sensitive data.

        Args:
            sensitive_data (str): The data to be encrypted.

        Returns:
            str: The encrypted data (in base64 format).
        """
        try:
            encrypted_data = self.cipher.encrypt(sensitive_data.encode())
            return encrypted_data.decode()  # Convert bytes to string for easy storage
        except Exception as e:
            raise ValueError(f"Error encrypting data: {e}")

    def decrypt_data(self, encrypted_data):
        """
        Decrypts encrypted data.

        Args:
            encrypted_data (str): The encrypted data to be decrypted (in base64 format).

        Returns:
            str: The original sensitive data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            return decrypted_data.decode()  # Convert bytes to string
        except Exception as e:
            raise ValueError(f"Error decrypting data: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize manager
    manager = SensitiveDataManager()

    # Sensitive personal data example
    sensitive_info = "John Doe, SSN: 123-45-6789"

    # Encrypt data
    encrypted_info = manager.encrypt_data(sensitive_info)
    print(f"Encrypted Data: {encrypted_info}")

    # Decrypt data
    decrypted_info = manager.decrypt_data(encrypted_info)
    print(f"Decrypted Data: {decrypted_info}")
```

### Dependencies
Install the required `cryptography` library:
```bash
pip install cryptography
```

### Features
1. **Secure Key Management**: Encryption key is stored in a file (`secret.key`). If absent, a new key is generated.
2. **Encryption and Decryption**: Sensitive data is securely encrypted and decrypted.
3. **Error Handling**: Proper exceptions are raised for encryption/decryption errors.

This code can be used to manage sensitive personal data securely in a life insurance product scenario.
