"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a function to handle user login and registration for an e-commerce site, inspired by the "Login | Cadastre-se" feature on ebrasilbrazz.
Generated: DETERMINISTIC_0bc53a99f9e3021f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt  # Library for hashing passwords
from typing import Optional, Dict

# Mock database using a dictionary to simulate user storage
user_db: Dict[str, str] = {}  # Maps username to hashed password

class UserAuthError(Exception):
    """Custom exception for user authentication errors."""
    pass

def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verifies a provided password against a hashed password.

    Args:
        stored_password (str): The stored hashed password.
        provided_password (str): The password provided by the user.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def register(username: str, password: str) -> None:
    """
    Handles user registration by storing the username and hashed password.

    Args:
        username (str): The username for the new account.
        password (str): The password for the new account.

    Raises:
        UserAuthError: If the username already exists.
    """
    if username in user_db:
        raise UserAuthError("Username already exists.")

    # Hash the password for secure storage
    hashed_password = hash_password(password)
    user_db[username] = hashed_password

def login(username: str, password: str) -> Optional[str]:
    """
    Handles user login by verifying the username and password.

    Args:
        username (str): The username of the user attempting to log in.
        password (str): The password provided by the user.

    Returns:
        Optional[str]: A success message if login is successful, otherwise None.

    Raises:
        UserAuthError: If the username does not exist or the password is incorrect.
    """
    if username not in user_db:
        raise UserAuthError("Username does not exist.")

    stored_password = user_db[username]
    if not verify_password(stored_password, password):
        raise UserAuthError("Incorrect password.")

    return "Login successful!"

# Example usage (commented out for production):
# try:
#     register("user1", "password123")
#     print(login("user1", "password123"))  # Should print "Login successful!"
# except UserAuthError as e:
#     print(f"Authentication error: {e}")
```
