"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsverse-opsec.com
Prompt: Generate a code snippet that demonstrates how to securely handle user information for a USDT mining application, inspired by M2 Earn's privacy policies.
Generated: DETERMINISTIC_8bde0d8deb3dd08d
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import json
from cryptography.fernet import Fernet
from typing import Dict, Any

class UserManager:
    """A class to manage user information securely for a USDT mining application."""
    
    def __init__(self, key: bytes):
        """
        Initializes UserManager with a symmetric encryption key.

        Parameters:
            key (bytes): A secret key for encrypting user data.
        """
        self.cipher = Fernet(key)

    def hash_password(self, password: str) -> str:
        """
        Hashes a password using bcrypt.

        Parameters:
            password (str): The plaintext password to hash.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verifies a plaintext password against a hashed password.

        Parameters:
            password (str): The plaintext password to verify.
            hashed (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def encrypt_user_data(self, user_data: Dict[str, Any]) -> str:
        """
        Encrypts user data for secure storage.

        Parameters:
            user_data (Dict[str, Any]): The user data to encrypt.

        Returns:
            str: The encrypted user data as a string.
        """
        json_data = json.dumps(user_data).encode('utf-8')
        encrypted_data = self.cipher.encrypt(json_data)
        return encrypted_data.decode('utf-8')

    def decrypt_user_data(self, encrypted_data: str) -> Dict[str, Any]:
        """
        Decrypts previously encrypted user data.

        Parameters:
            encrypted_data (str): The encrypted user data to decrypt.

        Returns:
            Dict[str, Any]: The decrypted user data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode('utf-8'))
            return json.loads(decrypted_data.decode('utf-8'))
        except (InvalidToken, json.JSONDecodeError) as e:
            raise ValueError("Decryption failed: " + str(e))

# Example usage of UserManager
if __name__ == "__main__":
    # Generate a key for encryption/decryption (store this securely)
    encryption_key = Fernet.generate_key()

    # Create a UserManager instance
    user_manager = UserManager(encryption_key)

    # Example user data
    user_data = {
        "username": "user123",
        "email": "user@example.com",
        "password": "secure_password"
    }

    # Hash the user's password
    user_data['password'] = user_manager.hash_password(user_data['password'])

    # Encrypt the user data
    encrypted_data = user_manager.encrypt_user_data(user_data)
    print("Encrypted user data:", encrypted_data)

    # Decrypt the user data for verification
    decrypted_data = user_manager.decrypt_user_data(encrypted_data)
    print("Decrypted user data:", decrypted_data)

    # Verify the password
    password_is_valid = user_manager.verify_password("secure_password", decrypted_data['password'])
    print("Password is valid:", password_is_valid)
```
