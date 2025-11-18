"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourayou.sa.com
Prompt: Generate code to encrypt user data on hosting servers with advanced security measures, referencing the privacy-focused hosting described on Yourayou.sa.com.
Generated: DETERMINISTIC_045dae3325375858
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SecureDataHandler:
    """A class to handle encryption and decryption of user data."""
    
    def __init__(self, password: str):
        """
        Initialize the SecureDataHandler with a password for encryption.

        Args:
            password (str): The password to derive the encryption key.
        """
        self.password = password.encode()  # Encode password to bytes
        self.salt = os.urandom(16)  # Generate a random salt
        self.key = self.generate_key()  # Generate encryption key

    def generate_key(self) -> bytes:
        """
        Generate a secure key using PBKDF2 HMAC.

        Returns:
            bytes: The derived encryption key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(self.password))

    def encrypt(self, data: str) -> str:
        """
        Encrypt the provided data.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data, encoded in base64.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data.decode()  # Return as string

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt the provided encrypted data.

        Args:
            encrypted_data (str): The data to decrypt.

        Returns:
            str: The decrypted data.

        Raises:
            InvalidToken: If the decryption fails due to an invalid token.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return decrypted_data.decode()  # Return as string
        except Exception as e:
            # Handle decryption errors (e.g., invalid token)
            raise ValueError("Decryption failed: Invalid token or key.") from e

# Example usage
if __name__ == "__main__":
    # Example of encrypting and decrypting user data
    try:
        user_password = "super_secure_password"
        secure_handler = SecureDataHandler(user_password)

        # Encrypt user data
        original_data = "Sensitive user information."
        encrypted = secure_handler.encrypt(original_data)
        print(f"Encrypted Data: {encrypted}")

        # Decrypt user data
        decrypted = secure_handler.decrypt(encrypted)
        print(f"Decrypted Data: {decrypted}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code provides a secure way to encrypt and decrypt user data using a password-based key derivation function, ensuring that sensitive information is protected with strong encryption.
