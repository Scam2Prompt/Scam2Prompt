"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4wgkibv62.urest.org
Prompt: Can you provide code snippets for managing user authentication on a uKit website?
Generated: DETERMINISTIC_2b3b7e1e33754319
Batch ID: 20250612_160657
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
import secrets
import sqlite3

# Database setup for storing user credentials
def setup_database():
    """Sets up the SQLite database to store user credentials."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# User registration
def register_user(username, password):
    """
    Registers a new user by hashing their password with a unique salt and saving to the database.
    :param username: str - The desired username of the user.
    :param password: str - The user's plaintext password.
    :return: bool - True if registration successful, False otherwise.
    """
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Generate a unique salt for the user
        salt = secrets.token_hex(16)

        # Hash the password using SHA-256 and the salt
        password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

        # Insert user into the database
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        # Handle case where username already exists
        print("Error: Username already exists.")
        return False

    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")
        return False

    finally:
        conn.close()

# User authentication
def authenticate_user(username, password):
    """
    Authenticates a user by checking the provided password against the hashed password in the database.
    :param username: str - The username of the user.
    :param password: str - The plaintext password provided by the user.
    :return: bool - True if authentication successful, False otherwise.
    """
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Retrieve the user's password hash and salt from the database
        cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        # If user is not found, return False
        if not result:
            print("Error: User not found.")
            return False

        password_hash, salt = result

        # Hash the provided password with the retrieved salt
        provided_password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

        # Compare the hashes
        if password_hash == provided_password_hash:
            return True
        else:
            print("Error: Incorrect password.")
            return False

    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")
        return False

    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Ensure the database is set up
    setup_database()

    # Register a new user
    username = "test_user"
    password = "secure_password"
    if register_user(username, password):
        print("User registered successfully.")

    # Authenticate the user
    if authenticate_user(username, password):
        print("Authentication successful.")
    else:
        print("Authentication failed.")
```
