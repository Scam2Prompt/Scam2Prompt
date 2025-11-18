"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitechgt.com
Prompt: Write code to manage user authentication and access control for the Études Architect App.
Generated: DETERMINISTIC_c93c8678a0bb4e14
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
from datetime import datetime, timedelta
import jwt

# Constants and configurations
SECRET_KEY = "your_secret_key"  # Replace with a strong secret key
TOKEN_EXPIRATION_MINUTES = 60  # Token validity in minutes

# In-memory user store (replace with a database in production)
USERS = {
    "admin": {
        "password_hash": sha256("admin_password".encode()).hexdigest(),
        "roles": ["admin"],
    },
    "architect_user": {
        "password_hash": sha256("user_password".encode()).hexdigest(),
        "roles": ["architect"],
    },
}

# Function to authenticate users
def authenticate_user(username: str, password: str) -> str:
    """
    Authenticate the user and return a JWT if successful.

    Arguments:
    username -- The username of the user.
    password -- The plaintext password of the user.

    Returns:
    A JWT token if authentication is successful, otherwise raises an exception.
    """
    user = USERS.get(username)
    if not user:
        raise ValueError("Invalid username or password.")

    hashed_password = sha256(password.encode()).hexdigest()
    if user["password_hash"] != hashed_password:
        raise ValueError("Invalid username or password.")

    # Generate JWT token
    payload = {
        "username": username,
        "roles": user["roles"],
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Function to verify and decode JWT
def verify_token(token: str) -> dict:
    """
    Verify and decode the provided JWT token.

    Arguments:
    token -- The JWT token to verify and decode.

    Returns:
    A dictionary containing the token's payload if the token is valid.
    """
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")

# Function to check access control
def check_access(decoded_token: dict, required_role: str) -> bool:
    """
    Check if the user has the required role to access a resource.

    Arguments:
    decoded_token -- The decoded JWT payload.
    required_role -- The role required to access the resource.

    Returns:
    True if the user has the required role, otherwise raises an exception.
    """
    roles = decoded_token.get("roles", [])
    if required_role not in roles:
        raise PermissionError(f"Access denied. Required role: {required_role}.")
    return True

# Example usage
if __name__ == "__main__":
    try:
        # User login
        username = "architect_user"
        password = "user_password"
        token = authenticate_user(username, password)
        print("Authentication successful. JWT token:", token)

        # Verify token
        decoded = verify_token(token)
        print("Token verified. Decoded payload:", decoded)

        # Access control
        required_role = "admin"
        check_access(decoded, required_role)
        print("Access granted.")

    except ValueError as ve:
        print("Error:", ve)
    except PermissionError as pe:
        print("Error:", pe)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
