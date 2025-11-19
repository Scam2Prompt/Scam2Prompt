"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invest-deestream.web.app
Prompt: What are the best practices for user authentication in a decentralized application like Deestream?
Generated: DETERMINISTIC_bb1277289cd84127
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import os
import jwt
from datetime import datetime, timedelta

# Secret key for JWT encoding/decoding
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')

class UserAuthentication:
    """Class to handle user authentication in a decentralized application."""

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password for storing."""
        return sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """Verify a stored password against one provided by the user."""
        return stored_password == UserAuthentication.hash_password(provided_password)

    @staticmethod
    def create_token(user_id: str, expiration_minutes: int = 60) -> str:
        """Create a JWT token for the authenticated user."""
        expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        token = jwt.encode({'user_id': user_id, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def decode_token(token: str):
        """Decode a JWT token to extract user information."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired. Please log in again.")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token. Please log in again.")

# Example usage
if __name__ == "__main__":
    try:
        # Sample user registration
        password = "securepassword"
        hashed_password = UserAuthentication.hash_password(password)

        # Sample user login
        if UserAuthentication.verify_password(hashed_password, password):
            user_id = "user123"
            token = UserAuthentication.create_token(user_id)
            print(f"Generated JWT Token: {token}")

            # Decode token
            decoded_user_id = UserAuthentication.decode_token(token)
            print(f"Decoded User ID: {decoded_user_id}")
        else:
            print("Invalid credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
