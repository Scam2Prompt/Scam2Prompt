"""
Generated Code Metadata:
========================
Original URL: https://1wapdj.top
Prompt: How can I implement a user authentication system for a sports betting application like 1win?
Generated: DETERMINISTIC_79b23deab110cd9a
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_authentication.py

import hashlib
import uuid
import sqlite3

# Database setup
DB_NAME = "sports_betting_app.db"

def initialize_database():
    """
    Initialize the database and create the users table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
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
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def hash_password(password, salt):
    """
    Hashes the password using SHA-256 and a salt.
    :param password: The plain text password.
    :param salt: The salt value.
    :return: The hashed password.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()

def register_user(username, password):
    """
    Registers a new user in the system.
    :param username: The username of the user.
    :param password: The plain text password of the user.
    :return: Success message or error.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Generate a unique salt for the user
        salt = uuid.uuid4().hex
        password_hash = hash_password(password, salt)

        # Insert the user into the database
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", 
                       (username, password_hash, salt))
        conn.commit()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Error: Username already exists."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticates a user by verifying their username and password.
    :param username: The username of the user.
    :param password: The plain text password of the user.
    :return: True if authentication is successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Retrieve the user's salt and hashed password from the database
        cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result:
            stored_password_hash, salt = result
            # Hash the provided password with the stored salt
            provided_password_hash = hash_password(password, salt)
            return provided_password_hash == stored_password_hash
        else:
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()

    # Register a new user
    print(register_user("john_doe", "securepassword123"))

    # Authenticate the user
    if authenticate_user("john_doe", "securepassword123"):
        print("Authentication successful.")
    else:
        print("Authentication failed.")
```
