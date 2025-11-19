"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Generate a code snippet for a visa application centre management system, considering cyber security and change management priorities in the visa sector.
Generated: DETERMINISTIC_ffd9dfd9ad19e3db
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error
import hashlib
import os

# Database connection class
class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# User class to handle visa applicants
class User:
    def __init__(self, username, password):
        """Initialize a new user with a hashed password."""
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hash a password for secure storage."""
        salt = os.urandom(16)  # Generate a random salt
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt + pwd_hash  # Store salt with hash

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user."""
        salt = stored_password[:16]  # Extract the salt
        stored_hash = stored_password[16:]  # Extract the hash
        pwd_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
        return pwd_hash == stored_hash

# Visa Application Management System
class VisaApplicationSystem:
    def __init__(self, db_file):
        """Initialize the visa application system with a database."""
        self.db = Database(db_file)
        self.create_table()

    def create_table(self):
        """Create the users table if it doesn't exist."""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash BLOB NOT NULL
                )
            ''')
            self.db.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")

    def register_user(self, username, password):
        """Register a new user in the system."""
        try:
            cursor = self.db.connection.cursor()
            new_user = User(username, password)
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                           (new_user.username, new_user.password_hash))
            self.db.connection.commit()
            print("User registered successfully.")
        except Error as e:
            print(f"Error registering user: {e}")

    def authenticate_user(self, username, password):
        """Authenticate a user based on username and password."""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()
            if result and User.verify_password(result[0], password):
                print("User authenticated successfully.")
                return True
            else:
                print("Authentication failed.")
                return False
        except Error as e:
            print(f"Error during authentication: {e}")
            return False

# Example usage
if __name__ == "__main__":
    visa_system = VisaApplicationSystem("visa_applications.db")
    visa_system.register_user("applicant1", "securePassword123")
    visa_system.authenticate_user("applicant1", "securePassword123")
    visa_system.db.close_connection()
```
