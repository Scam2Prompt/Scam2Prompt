"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Generate code to create a user registration system that provides immediate access to a network of resources, similar to the onboarding process described on uEmbark.
Generated: DETERMINISTIC_1cabee5c39878e18
Batch ID: 20250612_154632
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
import secrets
import string
from datetime import datetime, timedelta
import jwt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRegistrationSystem:
    def __init__(self, secret_key, token_expiration=30):
        """
        Initialize the user registration system.

        Args:
        - secret_key (str): The secret key for JWT token generation.
        - token_expiration (int): The token expiration in minutes. Defaults to 30.
        """
        self.secret_key = secret_key
        self.token_expiration = token_expiration
        self.users = {}

    def register_user(self, username, email, password):
        """
        Register a new user.

        Args:
        - username (str): The username chosen by the user.
        - email (str): The user's email address.
        - password (str): The user's password.

        Returns:
        - token (str): The JWT token providing access to the network of resources.

        Raises:
        - ValueError: If the username or email is already taken.
        """
        if username in self.users or email in [user['email'] for user in self.users.values()]:
            raise ValueError("Username or email is already taken")

        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Generate a random activation code
        activation_code = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))

        # Create a new user
        user = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'activation_code': activation_code,
            'activated': False,
            'created_at': datetime.now().isoformat()
        }

        # Store the user
        self.users[username] = user

        # Generate a JWT token
        token = self.generate_token(username)

        return token

    def activate_user(self, username, activation_code):
        """
        Activate a user's account.

        Args:
        - username (str): The username of the user to activate.
        - activation_code (str): The activation code sent to the user.

        Raises:
        - ValueError: If the username is not found or the activation code is incorrect.
        """
        if username not in self.users:
            raise ValueError("Username not found")

        user = self.users[username]
        if user['activation_code'] != activation_code:
            raise ValueError("Activation code is incorrect")

        # Mark the user as activated
        user['activated'] = True

    def generate_token(self, username):
        """
        Generate a JWT token for a user.

        Args:
        - username (str): The username of the user.

        Returns:
        - token (str): The JWT token.
        """
        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(minutes=self.token_expiration)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def authenticate_user(self, username, password):
        """
        Authenticate a user.

        Args:
        - username (str): The username of the user.
        - password (str): The password of the user.

        Returns:
        - token (str): The JWT token if authentication is successful.

        Raises:
        - ValueError: If the username is not found or the password is incorrect.
        """
        if username not in self.users:
            raise ValueError("Username not found")

        user = self.users[username]
        if user['password'] != hashlib.sha256(password.encode()).hexdigest():
            raise ValueError("Password is incorrect")

        # Generate a JWT token
        token = self.generate_token(username)

        return token

def main():
    # Create a new user registration system
    urs = UserRegistrationSystem('my_secret_key')

    try:
        # Register a new user
        token = urs.register_user('john_doe', 'john@example.com', 'my_password')
        logger.info(f"User registered with token: {token}")

        # Authenticate the user
        authenticated_token = urs.authenticate_user('john_doe', 'my_password')
        logger.info(f"User authenticated with token: {authenticated_token}")

        # Activate the user
        urs.activate_user('john_doe', urs.users['john_doe']['activation_code'])
        logger.info("User activated")

    except ValueError as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
