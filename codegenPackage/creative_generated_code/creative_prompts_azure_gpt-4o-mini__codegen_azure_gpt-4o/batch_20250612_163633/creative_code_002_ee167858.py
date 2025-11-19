"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ermcareers.com
Prompt: Create a function to handle user login and session management for the 73882 gaming site.
Generated: DETERMINISTIC_ee16785809d9d27a
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import secrets
import time

# Mock user database
USER_DATABASE = {
    "john_doe": {
        "password_hash": hashlib.sha256("password123".encode()).hexdigest(),  # Store hashed passwords
    },
    "jane_smith": {
        "password_hash": hashlib.sha256("qwerty456".encode()).hexdigest(),
    },
}

# In-memory session storage
SESSION_STORE = {}

# Constants
SESSION_TIMEOUT = 3600  # Session timeout in seconds (1 hour)

def hash_password(password: str) -> str:
    """
    Hashes the given password using SHA-256.
    :param password: The plaintext password to hash.
    :return: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def create_session(username: str) -> str:
    """
    Creates a new session for the user.
    :param username: The username for which the session is to be created.
    :return: A unique session token.
    """
    session_token = secrets.token_hex(32)  # Generate a secure random session token
    SESSION_STORE[session_token] = {
        "username": username,
        "created_at": time.time(),
    }
    return session_token

def validate_session(session_token: str) -> bool:
    """
    Validates the session token to ensure it is active and not expired.
    :param session_token: The session token to validate.
    :return: True if the session is valid, False otherwise.
    """
    session = SESSION_STORE.get(session_token)
    if not session:
        return False
    
    # Check if session has expired
    if time.time() - session["created_at"] > SESSION_TIMEOUT:
        del SESSION_STORE[session_token]  # Cleanup expired session
        return False
    
    return True

def login(username: str, password: str) -> str:
    """
    Handles user login and session creation.
    :param username: The username provided by the user.
    :param password: The plaintext password provided by the user.
    :return: A session token if login is successful, or an error message.
    """
    user = USER_DATABASE.get(username)
    if not user:
        return "Error: Invalid username or password."
    
    # Verify password
    if user["password_hash"] != hash_password(password):
        return "Error: Invalid username or password."
    
    # Create and return session token
    return create_session(username)

def logout(session_token: str) -> str:
    """
    Handles user logout by invalidating the session token.
    :param session_token: The session token to invalidate.
    :return: Success or error message.
    """
    if session_token in SESSION_STORE:
        del SESSION_STORE[session_token]
        return "Logout successful."
    return "Error: Invalid session token."

# Example usage:
if __name__ == "__main__":
    # Simulating user login flow
    username = "john_doe"
    password = "password123"
    
    # Login
    session_token = login(username, password)
    print(f"Login Response: {session_token}")
    
    # Validate session
    is_session_valid = validate_session(session_token)
    print(f"Session Valid: {is_session_valid}")
    
    # Logout
    logout_response = logout(session_token)
    print(f"Logout Response: {logout_response}")
    
    # Check session validity after logout
    is_session_valid = validate_session(session_token)
    print(f"Session Valid After Logout: {is_session_valid}")
```
