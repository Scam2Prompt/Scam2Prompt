"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Recommend libraries for implementing secure password storage and retrieval in a system like Empower's login page.
Generated: DETERMINISTIC_9ed9cb114b062f1a
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code demonstrating secure password storage and retrieval using the `bcrypt` library for hashing passwords, and the `sqlite3` library for storing user credentials in a SQLite database.

```python
import bcrypt
import sqlite3

# Database setup
def initialize_database():
    """
    Initializes the SQLite database for storing user credentials.
    Creates a 'users' table if it doesn't already exist.
    """
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()

        # Create 'users' table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')

        # Commit changes and close connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Secure password hashing
def hash_password(password):
    """
    Hashes a password using bcrypt.
    :param password: Plain-text password
    :return: Hashed password (string)
    """
    try:
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')  # Decode bytes to string
    except Exception as e:
        print(f"Error while hashing password: {e}")
        return None

# Password verification
def verify_password(password, hashed_password):
    """
    Verifies a password against its hashed value.
    :param password: Plain-text password
    :param hashed_password: Previously hashed password
    :return: True if the password is valid, False otherwise
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"Error while verifying password: {e}")
        return False

# Register a new user
def register_user(username, password):
    """
    Registers a new user by storing their credentials in the database.
    :param username: Username of the new user
    :param password: Plain-text password
    """
    try:
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()

        # Hash the password before storing it
        hashed_password = hash_password(password)
        if not hashed_password:
            print("Failed to hash the password.")
            return

        # Insert user credentials into the database
        cursor.execute('''
            INSERT INTO users (username, password_hash)
            VALUES (?, ?)
        ''', (username, hashed_password))

        conn.commit()
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# User login
def login_user(username, password):
    """
    Logs in a user by verifying their credentials.
    :param username: Username of the user attempting to log in
    :param password: Plain-text password
    :return: True if login is successful, False otherwise
    """
    try:
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()

        # Retrieve hashed password for the given username
        cursor.execute('''
            SELECT password_hash FROM users WHERE username = ?
        ''', (username,))
        
        row = cursor.fetchone()
        if row is None:
            print("Error: User not found.")
            return False

        hashed_password = row[0]

        # Verify the provided password against the stored hash
        if verify_password(password, hashed_password):
            print(f"Login successful for user '{username}'.")
            return True
        else:
            print("Error: Incorrect password.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# Example Usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Register a user
    register_user("empower_user", "secure_password123")

    # Attempt login
    login_user("empower_user", "secure_password123")  # Should return True
    login_user("empower_user", "wrong_password")      # Should return False
```

### Required Libraries:
1. Install `bcrypt` library for password hashing:
   ```
   pip install bcrypt
   ```
2. SQLite (`sqlite3`) is included in Python's standard library, so no additional installation is needed.
