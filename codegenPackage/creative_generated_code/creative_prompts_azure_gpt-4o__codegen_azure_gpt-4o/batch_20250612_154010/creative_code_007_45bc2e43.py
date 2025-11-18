"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Generate a user authentication system for a cloud-based time-tracking platform designed for legal professionals, referencing BillYourTime.com's approach.
Generated: DETERMINISTIC_45bc2e43005584df
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_authentication.py
# A simple user authentication system for a cloud-based time-tracking platform
# This system supports user registration, login, and token-based authentication.

import bcrypt
import jwt
import datetime
from typing import Dict, Optional

# Secret key for JWT encoding/decoding (should be stored securely in environment variables)
JWT_SECRET = "supersecretkey123"
JWT_ALGORITHM = "HS256"
TOKEN_EXPIRY_HOURS = 24

# In-memory user store (for demonstration purposes; replace with a database in production)
users_db: Dict[str, Dict[str, str]] = {}


def hash_password(password: str) -> str:
    """
    Hashes the password using bcrypt.

    :param password: Raw password string
    :return: Hashed password string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password.

    :param password: Raw password string
    :param hashed_password: Stored hashed password
    :return: True if the password matches the hash, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_token(username: str) -> str:
    """
    Generates a JWT token for the user.

    :param username: Username to encode in the token
    :return: Encoded JWT token
    """
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRY_HOURS)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> Optional[Dict]:
    """
    Decodes a JWT token.

    :param token: Encoded JWT token
    :return: Decoded token data (None if decoding fails)
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None


def register_user(username: str, password: str) -> bool:
    """
    Registers a new user with a username and password.

    :param username: Unique username of the user
    :param password: Password for the user
    :return: True if registration is successful, False if the username already exists
    """
    if username in users_db:
        print(f"Username '{username}' is already taken.")
        return False

    users_db[username] = {"password": hash_password(password)}
    print(f"User '{username}' registered successfully.")
    return True


def login_user(username: str, password: str) -> Optional[str]:
    """
    Logs in a user and returns a JWT token.

    :param username: Username for login
    :param password: Password for login
    :return: JWT token if login is successful, None otherwise
    """
    user = users_db.get(username)
    if not user:
        print(f"User '{username}' not found.")
        return None

    if not verify_password(password, user["password"]):
        print(f"Invalid password for user '{username}'.")
        return None

    print(f"User '{username}' logged in successfully.")
    return generate_token(username)


def authenticate_request(token: str) -> Optional[str]:
    """
    Authenticates a request using the provided token.

    :param token: JWT token provided by the user
    :return: Username if authentication is successful, None otherwise
    """
    decoded_token = decode_token(token)
    if decoded_token:
        return decoded_token["username"]
    return None


# Example usage
if __name__ == "__main__":
    # Register a user
    register_user("john_doe", "securepassword123")

    # Login as the user
    token = login_user("john_doe", "securepassword123")
    if token:
        print(f"Generated token: {token}")

    # Authenticate a request using the token
    username = authenticate_request(token)
    if username:
        print(f"Authenticated username: {username}")
```
