"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osaic.dev.dpai.tech
Prompt: Write code to implement a login system that mimics the functionality described in "docupace-dev-osaic," requiring a username or email address for authentication.
Generated: DETERMINISTIC_eda633e1059e8d49
Batch ID: 20250612_151539
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

class UserDatabase:
    """Handles database operations for user authentication."""
    def __init__(self, db_name='user_database.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        """Creates the users table if it does not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
    
    def add_user(self, username, email, password):
        """Adds a new user to the database with hashed password."""
        hashed_password = self.hash_password(password)
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO users (username, email, password) VALUES (?, ?, ?)
                ''', (username, email, hashed_password))
        except sqlite3.IntegrityError:
            raise ValueError("Username or email already exists.")
    
    def authenticate(self, username_or_email, password):
        """Authenticates a user by username or email and password."""
        user = self.find_user(username_or_email)
        if user and self.verify_password(password, user[3]):
            return True
        return False

    def find_user(self, username_or_email):
        """Finds a user by username or email."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE username = ? OR email = ?
        ''', (username_or_email, username_or_email))
        return cursor.fetchone()
    
    @staticmethod
    def hash_password(password):
        """Returns a hashed version of the password."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Verifies a password against the hashed password."""
        return hashed_password == hashlib.sha256(plain_password.encode()).hexdigest()


class LoginSystem:
    """Handles user login operations."""
    def __init__(self):
        self.db = UserDatabase()

    def register_user(self, username, email, password):
        """Registers a new user by adding them to the database."""
        try:
            self.db.add_user(username, email, password)
            print("User registered successfully.")
        except ValueError as e:
            print(f"Registration failed: {e}")

    def login_user(self, username_or_email, password):
        """Logs in a user if the credentials are correct."""
        if self.db.authenticate(username_or_email, password):
            print("Login successful.")
        else:
            print("Login failed: Invalid username/email or password.")


# Example Usage
if __name__ == '__main__':
    login_system = LoginSystem()
    
    # Registering a user
    login_system.register_user('johndoe', 'john@example.com', 'securepassword123')
    
    # Attempting to log in
    login_system.login_user('johndoe', 'securepassword123')
    login_system.login_user('john@example.com', 'wrongpassword')
```
