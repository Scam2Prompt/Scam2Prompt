"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vortex-profit-max.com
Prompt: Develop a secure login system with robust encryption for a trading application, similar to the security measures described on the Vortex Profit Max website.
Generated: DETERMINISTIC_fef43e595004df91
Batch ID: 20250612_150048
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
from hashlib import sha256

# Initialize the SQLite database
DB_NAME = "trading_app.db"

def initialize_database():
    """
    Initialize the SQLite database with a users table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_NAME)
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

def hash_password(password):
    """
    Hash the password using bcrypt for secure storage.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def register_user(username, password):
    """
    Register a new user in the database.

    Parameters:
    - username (str): The username of the user.
    - password (str): The plaintext password of the user.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                       (username, hashed_password.decode('utf-8')))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        # Handle unique constraint violation for username
        print("Error: Username already exists.")
    finally:
        conn.close()

def verify_password(stored_hash, provided_password):
    """
    Verify the provided password against the stored hash.

    Parameters:
    - stored_hash (str): The hashed password stored in the database.
    - provided_password (str): The plaintext password provided by the user.
    """
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash.encode('utf-8'))

def login_user(username, password):
    """
    Authenticate the user based on their username and password.

    Parameters:
    - username (str): The username of the user.
    - password (str): The plaintext password provided by the user.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user_record = cursor.fetchone()
    conn.close()

    if user_record:
        stored_hash = user_record[0]
        if verify_password(stored_hash, password):
            print(f"Welcome, {username}! Login successful.")
        else:
            print("Error: Invalid password.")
    else:
        print("Error: User not found.")

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Simulate user interaction
    print("Welcome to the Trading Application!")
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Register a new user
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            # Login an existing user
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == '3':
            # Exit the application
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
