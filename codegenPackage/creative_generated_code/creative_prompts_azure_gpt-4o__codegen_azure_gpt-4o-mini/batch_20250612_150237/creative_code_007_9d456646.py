"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbased.beautyjibindia.com
Prompt: Provide code for validating user credentials against a database in a cryptocurrency login system, ensuring security and scalability.
Generated: DETERMINISTIC_9d456646245ad748
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3

class Database:
    """Class for handling database operations."""
    
    def __init__(self, db_name='users.db'):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Create users table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )''')
        self.connection.commit()

    def add_user(self, username: str, password: str) -> bool:
        """Add a new user to the database after hashing the password."""
        try:
            password_hash = self._hash_password(password)
            self.cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                                (username, password_hash))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:  # Handle username already exists
            return False

    def validate_user(self, username: str, password: str) -> bool:
        """Validate user credentials against the database."""
        self.cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()
        if result:
            password_hash = result[0]
            return self._verify_password(password, password_hash)
        return False

    def _hash_password(self, password: str) -> str:
        """Hash a password for storing."""
        salt = os.urandom(16)  # Generate a random salt
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt + pwd_hash  # Store salt and hash

    def _verify_password(self, password: str, password_hash: bytes) -> bool:
        """Verify a stored password against one provided by user."""
        salt = password_hash[:16]  # Extract the stored salt
        stored_hash = password_hash[16:]  # Extract the stored hash
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return pwd_hash == stored_hash

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = Database()
    
    # Add a user (for demonstration purposes, should be done in a separate registration process)
    if db.add_user('example_user', 'secure_password'):
        print("User added successfully.")
    else:
        print("User already exists.")
    
    # Validate user login
    if db.validate_user('example_user', 'secure_password'):
        print("Login successful.")
    else:
        print("Invalid credentials.")
    
    db.close()
```
