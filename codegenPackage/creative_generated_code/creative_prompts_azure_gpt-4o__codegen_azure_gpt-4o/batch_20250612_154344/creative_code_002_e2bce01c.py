"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Generate Python code to build a user login system for a content discovery app, referencing features like personalized feeds and connecting with like-minded members as described on the Stumble! ® website.
Generated: DETERMINISTIC_e2bce01cb6b8c8ad
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from datetime import datetime

# Database setup and user table creation
def setup_database():
    """Initialize the database and create the users table if it doesn't exist."""
    conn = sqlite3.connect("content_discovery_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Secure password hashing function
def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# User registration
def register_user(username, password):
    """
    Register a new user with a username and password.
    Returns True if registration is successful, False if the username already exists.
    """
    conn = sqlite3.connect("content_discovery_app.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password_hash, created_at)
            VALUES (?, ?, ?)
        """, (username, hash_password(password), datetime.now()))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Username already exists
        conn.close()
        return False

# User login
def login_user(username, password):
    """
    Authenticate a user with a username and password.
    Returns True if credentials are valid, False otherwise.
    """
    conn = sqlite3.connect("content_discovery_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT password_hash FROM users WHERE username = ?
    """, (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        return True
    return False

# Main application logic
if __name__ == "__main__":
    setup_database()  # Ensure database is ready
    
    print("Welcome to the Content Discovery App!")
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        # User registration flow
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        if register_user(username, password):
            print(f"User '{username}' successfully registered!")
        else:
            print(f"Username '{username}' is already taken. Please try again.")
    elif choice == "2":
        # User login flow
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        if login_user(username, password):
            print(f"Welcome back, {username}!")
            print("Your personalized feed and like-minded member connections are loading...")
        else:
            print("Invalid username or password. Please try again.")
    else:
        print("Invalid option selected. Please restart the application.")
```
