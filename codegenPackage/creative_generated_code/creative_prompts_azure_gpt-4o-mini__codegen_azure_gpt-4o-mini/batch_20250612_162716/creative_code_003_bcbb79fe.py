"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dwfiabs.app
Prompt: What are the best practices for securing user data against phishing, as mentioned in the Cloudflare phishing warning?
Generated: DETERMINISTIC_bcbb79fe30695e49
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
from cryptography.fernet import Fernet

class UserDataSecurity:
    """
    A class to handle user data security against phishing attacks.
    """

    def __init__(self, encryption_key: bytes):
        """
        Initialize the UserDataSecurity class with a given encryption key.

        :param encryption_key: A bytes object used for encrypting user data.
        """
        self.cipher = Fernet(encryption_key)

    def hash_password(self, password: str) -> str:
        """
        Hash the provided password using SHA-256.

        :param password: The user's password to hash.
        :return: A SHA-256 hashed password as a hexadecimal string.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def encrypt_data(self, data: str) -> str:
        """
        Encrypt the provided data.

        :param data: The data to encrypt.
        :return: The encrypted data as a base64-encoded string.
        """
        encrypted_data = self.cipher.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt the provided encrypted data.

        :param encrypted_data: The data to decrypt.
        :return: The decrypted data as a string.
        """
        decrypted_data = self.cipher.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Check if the provided email is valid.

        :param email: The email address to validate.
        :return: True if the email is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def secure_user_data(self, email: str, password: str) -> dict:
        """
        Securely store user data by hashing the password and encrypting the email.

        :param email: The user's email address.
        :param password: The user's password.
        :return: A dictionary containing the hashed password and encrypted email.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")

        hashed_password = self.hash_password(password)
        encrypted_email = self.encrypt_data(email)

        return {
            "hashed_password": hashed_password,
            "encrypted_email": encrypted_email
        }

# Example usage
if __name__ == "__main__":
    # Generate a key for encryption
    encryption_key = Fernet.generate_key()

    # Initialize the UserDataSecurity class
    security = UserDataSecurity(encryption_key)

    # Secure user data
    try:
        user_data = security.secure_user_data("user@example.com", "secure_password")
        print("Secured User Data:", user_data)
    except ValueError as e:
        print(f"Error: {e}")
```
