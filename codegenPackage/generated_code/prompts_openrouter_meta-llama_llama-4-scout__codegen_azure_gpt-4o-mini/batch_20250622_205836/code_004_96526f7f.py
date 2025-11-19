"""
Generated Code Metadata:
========================
Original URL: https://app-mercle.pages.dev
Prompt: What are the best practices for integrating cryptographic functions into a web app?
Generated: DETERMINISTIC_96526f7f8462c4e4
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import hmac
import base64
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class CryptoUtils:
    """
    A utility class for cryptographic functions used in web applications.
    """

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a secure random key for symmetric encryption.
        
        Returns:
            bytes: A base64 encoded key.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt_message(key: bytes, message: str) -> str:
        """
        Encrypts a message using the provided key.
        
        Args:
            key (bytes): The encryption key.
            message (str): The plaintext message to encrypt.
        
        Returns:
            str: The encrypted message, base64 encoded.
        """
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message.decode()

    @staticmethod
    def decrypt_message(key: bytes, encrypted_message: str) -> str:
        """
        Decrypts an encrypted message using the provided key.
        
        Args:
            key (bytes): The encryption key.
            encrypted_message (str): The encrypted message to decrypt.
        
        Returns:
            str: The decrypted plaintext message.
        
        Raises:
            InvalidToken: If the decryption fails due to an invalid token.
        """
        fernet = Fernet(key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode())
            return decrypted_message.decode()
        except InvalidToken:
            raise ValueError("Invalid decryption key or message.")

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a password using SHA-256.
        
        Args:
            password (str): The password to hash.
        
        Returns:
            str: The hashed password, hex encoded.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_hash: str, password: str) -> bool:
        """
        Verifies a password against a stored hash.
        
        Args:
            stored_hash (str): The stored hashed password.
            password (str): The password to verify.
        
        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        return stored_hash == CryptoUtils.hash_password(password)

    @staticmethod
    def generate_hmac(key: bytes, message: str) -> str:
        """
        Generates an HMAC for a given message using the provided key.
        
        Args:
            key (bytes): The HMAC key.
            message (str): The message to hash.
        
        Returns:
            str: The HMAC, base64 encoded.
        """
        hmac_result = hmac.new(key, message.encode(), hashlib.sha256)
        return base64.b64encode(hmac_result.digest()).decode()

    @staticmethod
    def verify_hmac(key: bytes, message: str, hmac_to_verify: str) -> bool:
        """
        Verifies an HMAC against a given message and key.
        
        Args:
            key (bytes): The HMAC key.
            message (str): The original message.
            hmac_to_verify (str): The HMAC to verify.
        
        Returns:
            bool: True if the HMAC is valid, False otherwise.
        """
        expected_hmac = CryptoUtils.generate_hmac(key, message)
        return hmac_to_verify == expected_hmac

# Example usage
if __name__ == "__main__":
    try:
        # Generate a key for encryption
        key = CryptoUtils.generate_key()
        
        # Encrypt a message
        original_message = "Hello, secure world!"
        encrypted = CryptoUtils.encrypt_message(key, original_message)
        print(f"Encrypted: {encrypted}")
        
        # Decrypt the message
        decrypted = CryptoUtils.decrypt_message(key, encrypted)
        print(f"Decrypted: {decrypted}")
        
        # Hash a password
        password = "my_secure_password"
        hashed_password = CryptoUtils.hash_password(password)
        print(f"Hashed Password: {hashed_password}")
        
        # Verify the password
        is_verified = CryptoUtils.verify_password(hashed_password, password)
        print(f"Password Verified: {is_verified}")
        
        # Generate and verify HMAC
        hmac_key = os.urandom(32)  # Secure random key for HMAC
        message = "Important message"
        hmac_value = CryptoUtils.generate_hmac(hmac_key, message)
        print(f"HMAC: {hmac_value}")
        
        is_hmac_valid = CryptoUtils.verify_hmac(hmac_key, message, hmac_value)
        print(f"HMAC Valid: {is_hmac_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
