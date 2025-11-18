"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Write code to implement secure user authentication for accessing reserved allocations in a blockchain presale, referencing $GROK's system.
Generated: DETERMINISTIC_b87ff2106dfaf30d
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import os
import jwt
from datetime import datetime, timedelta

# Constants
SECRET_KEY = os.environ.get("SECRET_KEY", "replace_this_with_a_secure_random_key")
JWT_EXPIRATION_MINUTES = 30
ALLOWED_USERNAME_LIST = ["user1", "user2", "user3"]  # Replace with actual authorized users
ALLOCATION_ACCESS_KEY = os.environ.get("ALLOCATION_ACCESS_KEY", "secure_access_key_to_presale")

# Utility function to hash passwords securely
def hash_password(password: str) -> str:
    """Hash a password using a secure hashing algorithm."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Utility function to generate a secure HMAC signature
def generate_signature(data: str, key: str) -> str:
    """Generate a secure HMAC signature."""
    return hmac.new(key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

# Function to authenticate user
def authenticate_user(username: str, password: str) -> bool:
    """
    Authenticate the user based on username and password.

    Args:
        username (str): Username provided by the user.
        password (str): Password provided by the user.

    Returns:
        bool: True if authentication succeeds, False otherwise.
    """
    if username not in ALLOWED_USERNAME_LIST:
        return False
    
    # Simulated password hashing (replace with actual password storage/check logic)
    stored_password_hash = hash_password("secure_password")  # Replace with real password storage logic
    provided_password_hash = hash_password(password)

    return stored_password_hash == provided_password_hash

# Function to generate JWT token for secure access
def generate_auth_token(username: str) -> str:
    """
    Generate a JWT token for authenticated users.

    Args:
        username (str): The username for which the token is generated.

    Returns:
        str: A JWT token.
    """
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES),
        "iat": datetime.utcnow(),
        "allocation_key": ALLOCATION_ACCESS_KEY  # Specific to $GROK presale access
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Function to validate JWT token
def validate_auth_token(token: str) -> dict:
    """
    Validate and decode a JWT token.

    Args:
        token (str): The JWT token to validate.

    Returns:
        dict: The decoded token payload if valid.
    """
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")

# Main function to handle authentication and token generation
def main():
    """
    Main entry point for user authentication and secure access handling.
    """
    try:
        # Example user input
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Authenticate user
        if authenticate_user(username, password):
            print("Authentication successful.")
            auth_token = generate_auth_token(username)
            print(f"Your access token: {auth_token}")
        else:
            print("Authentication failed. Invalid username or password.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```

**Note:** Ensure that sensitive information (like `SECRET_KEY` and `ALLOCATION_ACCESS_KEY`) is stored securely using environment variables or a secrets management system in production.
