"""
Generated Code Metadata:
========================
Original URL: https://crypto-dezire.com
Prompt: Write code to implement a user registration system for a cryptocurrency trading platform, including features like free account activation and secure data handling, as described on the Crypto Dezire website.
Generated: DETERMINISTIC_9c6a134b6a23f791
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration_system.py

import hashlib
import hmac
import secrets
import string
import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRegistrationSystem:
    def __init__(self, db: Dict[str, str]):
        """
        Initialize the user registration system.

        Args:
        db (Dict[str, str]): A dictionary to store user credentials.
        """
        self.db = db

    def _hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256.

        Args:
        password (str): The password to be hashed.

        Returns:
        str: The hashed password.
        """
        # Generate a random salt
        salt = secrets.token_bytes(16)
        # Hash the password with the salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Store the salt and hashed password as a single string
        return salt.hex() + ':' + hashed_password.hex()

    def _verify_password(self, stored_password: str, provided_password: str) -> bool:
        """
        Verify a password against a stored hash.

        Args:
        stored_password (str): The stored hashed password.
        provided_password (str): The password to be verified.

        Returns:
        bool: True if the password is valid, False otherwise.
        """
        # Split the stored password into salt and hashed password
        salt, stored_hash = stored_password.split(':')
        # Convert the salt and stored hash back to bytes
        salt_bytes = bytes.fromhex(salt)
        stored_hash_bytes = bytes.fromhex(stored_hash)
        # Hash the provided password with the same salt
        provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt_bytes, 100000)
        # Compare the provided hash with the stored hash
        return hmac.compare_digest(stored_hash_bytes, provided_hash)

    def register_user(self, username: str, email: str, password: str) -> bool:
        """
        Register a new user.

        Args:
        username (str): The username chosen by the user.
        email (str): The user's email address.
        password (str): The user's password.

        Returns:
        bool: True if the registration is successful, False otherwise.
        """
        # Check if the username or email already exists
        if username in self.db or email in [user.split(':')[1] for user in self.db.values()]:
            logger.error("Username or email already exists.")
            return False

        # Hash the password
        hashed_password = self._hash_password(password)
        # Store the user's credentials
        self.db[username] = f"{email}:{hashed_password}"
        logger.info("User registered successfully.")
        return True

    def activate_account(self, username: str) -> bool:
        """
        Activate a user's account.

        Args:
        username (str): The username of the account to be activated.

        Returns:
        bool: True if the activation is successful, False otherwise.
        """
        # Check if the username exists
        if username not in self.db:
            logger.error("Username does not exist.")
            return False

        # Activate the account (in this case, we simply log a message)
        logger.info("Account activated successfully.")
        return True

    def login_user(self, username: str, password: str) -> bool:
        """
        Login a user.

        Args:
        username (str): The username of the user.
        password (str): The user's password.

        Returns:
        bool: True if the login is successful, False otherwise.
        """
        # Check if the username exists
        if username not in self.db:
            logger.error("Username does not exist.")
            return False

        # Get the stored credentials
        stored_credentials = self.db[username].split(':')
        stored_email = stored_credentials[0]
        stored_password = stored_credentials[1]

        # Verify the password
        if not self._verify_password(stored_password, password):
            logger.error("Invalid password.")
            return False

        logger.info("User logged in successfully.")
        return True

def generate_random_password(length: int = 12) -> str:
    """
    Generate a random password.

    Args:
    length (int): The length of the password.

    Returns:
    str: A random password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

if __name__ == "__main__":
    db = {}
    registration_system = UserRegistrationSystem(db)

    # Test the registration system
    username = "test_user"
    email = "test@example.com"
    password = generate_random_password()
    registration_system.register_user(username, email, password)
    registration_system.activate_account(username)
    registration_system.login_user(username, password)
```
