"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.jobone.careers
Prompt: Generate a script to simulate the user login process on jobONE’s platform, including handling "Passwort vergessen" and "Jetzt registrieren" workflows.
Generated: DETERMINISTIC_6e690cea64a8a514
Batch ID: 20250612_153224
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
import re

# Simulated Database
users_db = {
    # Example user format: "username": {"password_hash": "hashed_pw", "email": "user_email@example.com"}
}

# Utility function to hash passwords for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Simulated user login process
def user_login(username, password):
    """
    Simulates the user login process.

    Args:
        username (str): The username of the user.
        password (str): The password provided by the user.

    Returns:
        str: Success or failure message.
    """
    if username in users_db:
        stored_password_hash = users_db[username]['password_hash']
        if hash_password(password) == stored_password_hash:
            return "Login successful."
        else:
            return "Error: Incorrect password."
    else:
        return "Error: Username does not exist."

# Passwort vergessen (Forgot Password) workflow
def forgot_password(username, email):
    """
    Handles the 'Passwort vergessen' (Forgot Password) workflow.

    Args:
        username (str): The username of the user.
        email (str): The email associated with the user.

    Returns:
        str: Success or failure message.
    """
    if username in users_db:
        if users_db[username]['email'] == email:
            # Generate a password reset link (simulated)
            return f"Password reset link has been sent to {email}."
        else:
            return "Error: Email does not match our records."
    else:
        return "Error: Username does not exist."

# Jetzt registrieren (Register Now) workflow
def register_user(username, password, email):
    """
    Handles the 'Jetzt registrieren' (Register Now) workflow.

    Args:
        username (str): The desired username for the new account.
        password (str): The desired password for the new account.
        email (str): The email address of the user.

    Returns:
        str: Success or failure message.
    """
    # Validate username
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return "Error: Username contains invalid characters."

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Error: Invalid email format."

    # Check if username already exists
    if username in users_db:
        return "Error: Username already exists. Please choose a different username."

    # Register the user
    users_db[username] = {
        "password_hash": hash_password(password),
        "email": email
    }
    return "Registration successful."

# Example usage
if __name__ == "__main__":
    # Register a new user
    print(register_user("testUser", "securePassword123", "testUser@example.com"))  # Example registration
    # Attempt login
    print(user_login("testUser", "securePassword123"))  # Example login
    # Forgot password
    print(forgot_password("testUser", "testUser@example.com"))  # Example password reset request
    # Invalid login attempt
    print(user_login("testUser", "wrongPassword"))  # Example incorrect login
```

This script simulates the requested functionalities (login, registration, and password reset) following the provided guidelines for clean, well-commented, and production-ready code.
