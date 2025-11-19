"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Write a code snippet for a login system that verifies username and password, inspired by the login process described on bonnabdcc.com.
Generated: DETERMINISTIC_cef4a5070f74ec0c
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib

# Sample user database (for demonstration purposes)
USER_DATABASE = {
    "user1": hashlib.sha256("password123".encode()).hexdigest(),
    "user2": hashlib.sha256("mysecurepassword".encode()).hexdigest(),
}

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    :param password: The plain text password to hash.
    :return: The hashed password in hexadecimal format.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def verify_credentials(username: str, password: str) -> bool:
    """
    Verifies the provided username and password against the user database.

    :param username: The username to verify.
    :param password: The plain text password to verify.
    :return: True if credentials are valid, False otherwise.
    """
    try:
        # Check if the username exists in the database
        if username in USER_DATABASE:
            # Hash the provided password and compare with the stored hash
            return USER_DATABASE[username] == hash_password(password)
        else:
            # Log an attempt to access with a non-existent username
            print(f"Login attempt failed: User '{username}' does not exist.")
            return False
    except Exception as e:
        # Log the error (In a production system, consider logging to a file or monitoring system)
        print(f"Error during login verification: {e}")
        return False

def main():
    """
    Main function to handle user input and invoke the login verification.
    """
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Verify the credentials
    if verify_credentials(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
```
