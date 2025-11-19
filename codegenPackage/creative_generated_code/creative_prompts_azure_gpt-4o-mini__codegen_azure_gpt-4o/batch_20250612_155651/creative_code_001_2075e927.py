"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://closeloopapp.online
Prompt: What are the best practices for handling user authentication in Closeloop applications?
Generated: DETERMINISTIC_2075e9274d6e4c5c
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import os
import jwt
from datetime import datetime, timedelta

# Constants for JWT
SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")  # Use a secure environment variable for production
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY = 60  # Expiry time in minutes

# User Database (Example for demonstration purposes. Use a proper database in production.)
USER_DATABASE = {
    "example_user": {
        "password_hash": hashlib.sha256(b"example_password").hexdigest(),  # Example hashed password
        "roles": ["user"],  # User roles for authorization checks
    }
}

# Function to securely hash passwords
def hash_password(password: str) -> str:
    """
    Hashes the password using SHA-256. In production, consider using a stronger hash like bcrypt.
    
    :param password: User's plain text password
    :return: Hexadecimal representation of the hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate user
def authenticate_user(username: str, password: str) -> bool:
    """
    Authenticate a user by verifying username and password.
    
    :param username: The username of the user
    :param password: The plain text password provided by the user
    :return: True if authentication is successful, False otherwise
    """
    user = USER_DATABASE.get(username)
    if not user:
        return False  # User not found
    return user["password_hash"] == hash_password(password)

# Function to generate a JWT access token
def generate_access_token(username: str) -> str:
    """
    Generate a JWT access token for the authenticated user.
    
    :param username: The username of the authenticated user
    :return: A JWT access token
    """
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

# Function to decode and verify a JWT access token
def verify_access_token(token: str) -> dict:
    """
    Verify and decode a JWT access token.
    
    :param token: The JWT access token
    :return: Decoded token payload if verification is successful
    :raises jwt.ExpiredSignatureError: If the token has expired
    :raises jwt.InvalidTokenError: If the token is invalid or cannot be decoded
    """
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")

# Example usage
if __name__ == "__main__":
    # Simulate user login
    username = "example_user"
    password = "example_password"
    
    if authenticate_user(username, password):
        print("Authentication successful!")
        access_token = generate_access_token(username)
        print("Access Token:", access_token)
        
        # Simulate token verification
        try:
            decoded_payload = verify_access_token(access_token)
            print("Token verified! Payload:", decoded_payload)
        except ValueError as e:
            print("Token verification failed:", str(e))
    else:
        print("Authentication failed! Invalid username/password.")
```
