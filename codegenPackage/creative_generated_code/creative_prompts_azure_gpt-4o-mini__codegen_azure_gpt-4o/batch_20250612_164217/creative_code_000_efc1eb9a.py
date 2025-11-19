"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sin88.makeup
Prompt: Generate code for a secure user login system for an online betting platform like SIN88.
Generated: DETERMINISTIC_efc1eb9a8c784a8d
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
import re

# Database setup (use a proper DB in production)
DATABASE_FILE = "user_data.db"

def initialize_database():
    """
    Initialize the database with the users table if it doesn't exist.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def validate_username(username):
    """
    Validate username according to defined rules:
    - Must be between 3 and 20 characters
    - Can only contain alphanumeric characters, underscores, or dots
    """
    return re.match(r"^[a-zA-Z0-9_.]{3,20}$", username) is not None

def hash_password(password):
    """
    Hash the password using bcrypt for secure storage.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def register_user(username, password):
    """
    Register a new user with a hashed password.
    """
    if not validate_username(username):
        raise ValueError("Invalid username! Must be 3-20 characters and can only contain alphanumeric, underscores, or dots.")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists!")
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticate a user by verifying the provided password against the stored hash.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        raise ValueError("Invalid username or password.")

    stored_password_hash = result[0]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
        print("Login successful!")
        return True
    else:
        raise ValueError("Invalid username or password.")

# Example usage
if __name__ == "__main__":
    try:
        initialize_database()  # Ensure the database is set up

        print("Welcome to SIN88 Login System")
        action = input("Do you want to register or login? (register/login): ").lower()

        if action == "register":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)

        elif action == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticate_user(username, password)

        else:
            print("Invalid option. Please choose 'register' or 'login'.")
    except Exception as e:
        print(f"Error: {e}")
```
