"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Describe the process of setting up user accounts for an online course on Sui Foundation.
Generated: DETERMINISTIC_babe09da62aa45a1
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256

class UserAccountManager:
    def __init__(self, db_name='user_accounts.db'):
        """Initialize the database connection and user table."""
        self.connection = sqlite3.connect(db_name)
        self.create_user_table()

    def create_user_table(self):
        """Create the user table if it doesn't already exist."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def hash_password(self, password):
        """Hash the password using SHA-256."""
        return sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Register a new user with a unique username and hashed password."""
        password_hash = self.hash_password(password)
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO users (username, password_hash) VALUES (?, ?)
                ''', (username, password_hash))
            print(f"User '{username}' registered successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Username '{username}' is already taken.")
        except sqlite3.Error as e:
            print(f"Error registering user: {e}")

    def authenticate_user(self, username, password):
        """Authenticate a user by verifying username and password."""
        password_hash = self.hash_password(password)
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password_hash = ?
        ''', (username, password_hash))
        user = cursor.fetchone()
        if user:
            print(f"User '{username}' authenticated successfully.")
            return True
        else:
            print("Error: Invalid username or password.")
            return False

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    manager = UserAccountManager()
    
    # Register new users
    manager.register_user("alice", "password123")
    manager.register_user("bob", "securepass")

    # Authenticate users
    manager.authenticate_user("alice", "password123")
    manager.authenticate_user("bob", "wrongpass")

    # Close the database connection when done
    manager.close_connection()
```
