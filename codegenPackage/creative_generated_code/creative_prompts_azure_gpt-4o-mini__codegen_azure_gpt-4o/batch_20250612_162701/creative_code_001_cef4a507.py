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
# Import necessary libraries
import hashlib  # For hashing passwords
import sqlite3  # For managing the database connection

# Function to hash passwords securely
def hash_password(password):
    """
    Hashes a password using SHA-256.
    Args:
        password (str): The plain text password entered by the user.
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify username and password
def verify_login(username, password):
    """
    Verifies if the username and password combination is valid.
    Args:
        username (str): The username provided by the user.
        password (str): The plain text password provided by the user.
    Returns:
        str: A login success or failure message.
    """
    try:
        # Establish database connection
        conn = sqlite3.connect("login_system.db")
        cursor = conn.cursor()

        # Check if the username exists in the database
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        # If a match is found, verify the password
        if result:
            stored_password = result[0]
            if hash_password(password) == stored_password:
                return "Login successful!"
            else:
                return "Invalid password. Please try again."
        else:
            return "Invalid username. Please try again."

    except sqlite3.Error as e:
        # Handle database errors
        return f"An error occurred while processing your request: {str(e)}"

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

# Example usage (for demonstration purposes only)
if __name__ == "__main__":
    # Sample input: Replace these with user-provided values
    sample_username = input("Enter your username: ")
    sample_password = input("Enter your password: ")

    # Verify login
    print(verify_login(sample_username, sample_password))
```

### Notes:
- This code assumes an SQLite database `login_system.db` with a table `users` containing columns `username` (TEXT) and `password` (TEXT, storing hashed passwords).
- Before using this code in production, ensure that user passwords are hashed during registration using the same `hash_password` function.
