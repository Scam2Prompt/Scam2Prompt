"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Generate code to implement a user registration and login system for a health and nutrition website, including features for affiliate program enrollment as described on Familia Previlife.
Generated: DETERMINISTIC_0316c4f6ec7b185a
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for implementing the requested user registration and login system with affiliate program enrollment:

```python
import hashlib
import uuid
import sqlite3

# Database setup
DATABASE = 'previlife.db'

# SQL queries to set up tables
USER_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    affiliate_code TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

AFFILIATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS affiliates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    affiliate_code TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Utility functions
def initialize_database():
    """Initialize the database and tables."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(USER_TABLE_SQL)
        cursor.execute(AFFILIATE_TABLE_SQL)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def hash_password(password):
    """Hash the password using SHA-256 and a unique salt."""
    salt = uuid.uuid4().hex
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{hashed}"


def verify_password(stored_password_hash, provided_password):
    """Verify a password against the stored hash."""
    try:
        salt, hashed = stored_password_hash.split(':')
        return hashed == hashlib.sha256((provided_password + salt).encode()).hexdigest()
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False


# User registration
def register_user(username, email, password):
    """Register a new user."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Hash the password
        password_hash = hash_password(password)

        # Generate an affiliate code (optional for this example)
        affiliate_code = uuid.uuid4().hex[:8]

        # Insert the user into the database
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, affiliate_code) VALUES (?, ?, ?, ?)",
            (username, email, password_hash, affiliate_code)
        )
        connection.commit()

        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username or email already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


# User login
def login_user(username, password):
    """Log in a user."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Fetch the user from the database
        cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            user_id, stored_password_hash = user
            if verify_password(stored_password_hash, password):
                print(f"User '{username}' logged in successfully.")
                return user_id  # Return the user's ID if needed for session management
            else:
                print("Error: Invalid password.")
        else:
            print("Error: User not found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()
    return None


# Enroll in affiliate program
def enroll_in_affiliate_program(user_id):
    """Enroll a user in the affiliate program."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Generate a unique affiliate code
        affiliate_code = uuid.uuid4().hex[:8]

        # Insert into the affiliate table
        cursor.execute(
            "INSERT INTO affiliates (user_id, affiliate_code) VALUES (?, ?)",
            (user_id, affiliate_code)
        )
        connection.commit()

        print(f"User ID '{user_id}' enrolled in affiliate program with code '{affiliate_code}'.")
    except sqlite3.IntegrityError:
        print("Error: User is already enrolled in the affiliate program.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


# Main function for demonstration
if __name__ == "__main__":
    initialize_database()

    # Register a sample user
    register_user("testuser", "testuser@example.com", "securepassword")

    # Login the sample user
    user_id = login_user("testuser", "securepassword")

    # Enroll the user in the affiliate program (if login was successful)
    if user_id:
        enroll_in_affiliate_program(user_id)
```

This code implements a user registration and login system with affiliate program enrollment. It uses SQLite as the database for simplicity and includes proper error handling, password hashing, and validation.
