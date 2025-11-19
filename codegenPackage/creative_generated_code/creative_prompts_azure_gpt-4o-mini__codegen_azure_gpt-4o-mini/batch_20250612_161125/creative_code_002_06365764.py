"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcoinik.vip
Prompt: Can you provide code examples for implementing security verification methods mentioned on dcoinik.vip?
Generated: DETERMINISTIC_06365764d7992bb4
Batch ID: 20250612_161125
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
import hmac
import base64
from cryptography.fernet import Fernet
from typing import Optional

class SecurityManager:
    """A class to manage security verification methods."""

    def __init__(self):
        """Initialize the SecurityManager with a generated key for encryption."""
        self.key = Fernet.generate_key()  # Generate a new key for encryption
        self.fernet = Fernet(self.key)     # Create a Fernet object for encryption/decryption

    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256.

        Parameters:
            password (str): The password to hash.

        Returns:
            str: The hashed password in hexadecimal format.
        """
        if not password:
            raise ValueError("Password cannot be empty")
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_hmac(self, message: str, secret: str) -> str:
        """
        Generate an HMAC for a given message using a secret key.

        Parameters:
            message (str): The message to hash.
            secret (str): The secret key used for HMAC generation.

        Returns:
            str: The Base64 encoded HMAC.
        """
        if not message or not secret:
            raise ValueError("Message and secret cannot be empty")
        hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
        return base64.b64encode(hmac_obj.digest()).decode()

    def encrypt_message(self, message: str) -> str:
        """
        Encrypt a message using Fernet symmetric encryption.

        Parameters:
            message (str): The message to encrypt.

        Returns:
            str: The encrypted message, Base64 encoded.
        """
        if not message:
            raise ValueError("Message cannot be empty")
        return self.fernet.encrypt(message.encode()).decode()

    def decrypt_message(self, encrypted_message: str) -> Optional[str]:
        """
        Decrypt a Fernet encrypted message.

        Parameters:
            encrypted_message (str): The encrypted message to decrypt.

        Returns:
            str: The original message.

        Raises:
            InvalidToken: If the token is invalid or expired.
        """
        if not encrypted_message:
            raise ValueError("Encrypted message cannot be empty")
        try:
            return self.fernet.decrypt(encrypted_message.encode()).decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

# Example usage:
if __name__ == "__main__":
    security_manager = SecurityManager()

    # Hash a password
    hashed_password = security_manager.hash_password("my_secure_password")
    print(f"Hashed Password: {hashed_password}")

    # Generate an HMAC
    hmac_value = security_manager.generate_hmac("This is a message", "my_secret_key")
    print(f"HMAC: {hmac_value}")

    # Encrypt and decrypt a message
    encrypted_message = security_manager.encrypt_message("This is a secret message")
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = security_manager.decrypt_message(encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
```
