"""
Generated Code Metadata:
========================
Original URL: https://immediate5-serax.com
Prompt: Design a secure authentication system for Immediate 5.0 Serax users, incorporating best practices for protecting user data and assets in the cryptocurrency trading environment.
Generated: DETERMINISTIC_1c460af38f849d09
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# authentication_system.py

import os
import secrets
import string
import hashlib
import hmac
import time
from typing import Optional

class AuthenticationSystem:
    def __init__(self, secret_key: str, token_expiration: int = 3600):
        """
        Initialize the authentication system.

        Args:
        - secret_key (str): The secret key used for token signing.
        - token_expiration (int): The token expiration time in seconds. Defaults to 3600 (1 hour).
        """
        self.secret_key = secret_key.encode('utf-8')
        self.token_expiration = token_expiration

    def generate_password_hash(self, password: str) -> str:
        """
        Generate a password hash.

        Args:
        - password (str): The password to hash.

        Returns:
        - str: The password hash.
        """
        salt = secrets.token_bytes(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt.hex() + ':' + key.hex()

    def verify_password(self, password: str, password_hash: str) -> bool:
        """
        Verify a password against a password hash.

        Args:
        - password (str): The password to verify.
        - password_hash (str): The password hash.

        Returns:
        - bool: True if the password is valid, False otherwise.
        """
        salt, stored_key = password_hash.split(':')
        salt = bytes.fromhex(salt)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hmac.compare_digest(key.hex(), stored_key)

    def generate_token(self, user_id: int) -> str:
        """
        Generate a token for a user.

        Args:
        - user_id (int): The user ID.

        Returns:
        - str: The token.
        """
        payload = {
            'user_id': user_id,
            'exp': int(time.time()) + self.token_expiration
        }
        token = self._create_token(payload)
        return token

    def verify_token(self, token: str) -> Optional[int]:
        """
        Verify a token.

        Args:
        - token (str): The token to verify.

        Returns:
        - Optional[int]: The user ID if the token is valid, None otherwise.
        """
        try:
            payload = self._verify_token(token)
            return payload['user_id']
        except Exception:
            return None

    def _create_token(self, payload: dict) -> str:
        """
        Create a token.

        Args:
        - payload (dict): The payload.

        Returns:
        - str: The token.
        """
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def _verify_token(self, token: str) -> dict:
        """
        Verify a token.

        Args:
        - token (str): The token to verify.

        Returns:
        - dict: The payload if the token is valid.

        Raises:
        - Exception: If the token is invalid.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception('Token has expired')
        except jwt.InvalidTokenError:
            raise Exception('Invalid token')

import jwt

def main():
    # Example usage
    secret_key = os.urandom(32).hex()
    auth_system = AuthenticationSystem(secret_key)

    # Generate a password hash
    password = 'mysecretpassword'
    password_hash = auth_system.generate_password_hash(password)
    print(f'Password Hash: {password_hash}')

    # Verify a password
    is_valid = auth_system.verify_password(password, password_hash)
    print(f'Password Valid: {is_valid}')

    # Generate a token
    user_id = 1
    token = auth_system.generate_token(user_id)
    print(f'Token: {token}')

    # Verify a token
    verified_user_id = auth_system.verify_token(token)
    print(f'Verified User ID: {verified_user_id}')

if __name__ == '__main__':
    main()
```
