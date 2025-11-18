"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Provide code to implement user authentication and authorization for a software system, suitable for a development team like the one referenced on oppomobile.id.
Generated: DETERMINISTIC_1eb4a2117895940f
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_auth.py

"""
User Authentication and Authorization Module
Author: [Your Name]
Date: [Insert Date]

Description:
This module provides functionality for user authentication and role-based authorization.
It uses JWT (JSON Web Tokens) for session management and bcrypt for password hashing.
"""

import bcrypt
import jwt
import datetime
from typing import Dict

# Constants
SECRET_KEY = "your_secret_key_here"  # Replace with a secure secret key in production
TOKEN_EXPIRATION_MINUTES = 60       # JWT token expiration time
ROLES = ['admin', 'editor', 'viewer']  # Define user roles for authorization

# In-memory user store (replace with a database in production)
user_store = {
    "admin_user": {
        "password_hash": bcrypt.hashpw("secure_admin_password".encode('utf-8'), bcrypt.gensalt()),
        "role": "admin"
    },
    "editor_user": {
        "password_hash": bcrypt.hashpw("secure_editor_password".encode('utf-8'), bcrypt.gensalt()),
        "role": "editor"
    }
}

def hash_password(password: str) -> bytes:
    """
    Hashes the given password using bcrypt.
    
    Args:
        password (str): The plaintext password.
    
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password: str, hashed_password: bytes) -> bool:
    """
    Verifies a plaintext password against a hashed password.
    
    Args:
        password (str): Plaintext password.
        hashed_password (bytes): Hashed password.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def generate_jwt(username: str, role: str) -> str:
    """
    Generates a JWT token for the given username and role.
    
    Args:
        username (str): The user's username.
        role (str): The user's role.
    
    Returns:
        str: A JWT token.
    """
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt(token: str) -> Dict:
    """
    Verifies the validity of a JWT token and returns its payload.
    
    Args:
        token (str): The JWT token.
    
    Returns:
        Dict: The payload of the JWT token if valid.
    
    Raises:
        jwt.ExpiredSignatureError: If the token has expired.
        jwt.InvalidTokenError: If the token is invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")

def authenticate_user(username: str, password: str) -> str:
    """
    Authenticates the user using username and password, and returns a JWT token if successful.
    
    Args:
        username (str): The user's username.
        password (str): The user's plaintext password.
    
    Returns:
        str: A JWT token if authentication is successful.
    
    Raises:
        ValueError: If authentication fails.
    """
    user = user_store.get(username)
    if not user:
        raise ValueError("Invalid username or password.")
    
    if not verify_password(password, user['password_hash']):
        raise ValueError("Invalid username or password.")
    
    # Generate JWT token
    return generate_jwt(username, user['role'])

def authorize_user(token: str, required_role: str) -> bool:
    """
    Authorizes the user based on their role.
    
    Args:
        token (str): The user's JWT token.
        required_role (str): The required role for authorization.
    
    Returns:
        bool: True if the user is authorized, False otherwise.
    
    Raises:
        ValueError: If the token is invalid or expired.
    """
    payload = verify_jwt(token)
    user_role = payload.get("role")
    
    if user_role not in ROLES:
        raise ValueError("Invalid role.")
    
    if ROLES.index(user_role) <= ROLES.index(required_role):
        return True
    
    return False

# Example usage
if __name__ == "__main__":
    try:
        # User authentication
        username = "admin_user"
        password = "secure_admin_password"
        token = authenticate_user(username, password)
        print(f"Authentication successful. Token: {token}")
        
        # User authorization
        required_role = "editor"
        is_authorized = authorize_user(token, required_role)
        if is_authorized:
            print(f"User '{username}' is authorized for role '{required_role}'.")
        else:
            print(f"User '{username}' is NOT authorized for role '{required_role}'.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
