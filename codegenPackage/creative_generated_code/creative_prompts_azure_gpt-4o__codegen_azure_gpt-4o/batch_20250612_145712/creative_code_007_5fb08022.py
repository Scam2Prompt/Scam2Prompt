"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Suggest best practices for securing user login credentials in a web application like MicroLab, including encryption and password hashing techniques.
Generated: DETERMINISTIC_5fb08022c36807f1
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from cryptography.fernet import Fernet


class UserAuth:
    """
    A class to handle user authentication securely using password hashing
    and encryption for sensitive data.
    """

    def __init__(self):
        # Generate a symmetric encryption key for securing sensitive data.
        # In production, store this key securely (e.g., environment variables, secure key management services).
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

    def hash_password(self, password: str) -> str:
        """
        Hashes a plain-text password using bcrypt and returns the hashed password.

        :param password: Plain-text password
        :return: Hashed password
        """
        # Use bcrypt's gensalt with a cost factor (default is sufficient for most cases)
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verifies a plain-text password against a hashed password.

        :param password: Plain-text password
        :param hashed_password: Hashed password
        :return: True if passwords match, otherwise False
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except ValueError as ve:
            # Handle invalid hash format or comparison issues
            print(f"Error verifying password: {ve}")
            return False

    def encrypt_sensitive_data(self, data: str) -> str:
        """
        Encrypts sensitive data using symmetric encryption.

        :param data: Plain-text sensitive data
        :return: Encrypted data
        """
        encrypted_data = self.cipher.encrypt(data.encode('utf-8'))
        return encrypted_data.decode('utf-8')

    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """
        Decrypts sensitive data that was encrypted using symmetric encryption.

        :param encrypted_data: Encrypted data
        :return: Decrypted plain-text data
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode('utf-8'))
            return decrypted_data.decode('utf-8')
        except Exception as e:
            # Handle decryption errors appropriately
            print(f"Error decrypting data: {e}")
            raise ValueError("Failed to decrypt data")


# Example usage
if __name__ == "__main__":
    auth = UserAuth()

    # Example password hashing and verification
    password = "SecureP@ssw0rd"
    hashed_password = auth.hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    is_valid = auth.verify_password("SecureP@ssw0rd", hashed_password)
    print(f"Password is valid: {is_valid}")

    # Example encryption and decryption
    sensitive_data = "This is some confidential information."
    encrypted_data = auth.encrypt_sensitive_data(sensitive_data)
    print(f"Encrypted Data: {encrypted_data}")

    decrypted_data = auth.decrypt_sensitive_data(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
```
