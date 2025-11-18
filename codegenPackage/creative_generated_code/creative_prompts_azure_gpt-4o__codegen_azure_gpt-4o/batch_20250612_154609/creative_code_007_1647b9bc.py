"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Generate code for a user authentication system tailored for organizations with diverse membership bases, like IACI’s member login feature.
Generated: DETERMINISTIC_1647b9bce4adc203
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication System
This code implements a user authentication system tailored for organizations with diverse membership bases.
It includes user registration, login, and basic role-based access control for organizational members.
"""

import bcrypt
import sqlite3
import os
from hashlib import sha256

DATABASE_PATH = "auth_system.db"

class UserAuthenticationSystem:
    def __init__(self, db_path=DATABASE_PATH):
        """
        Initialize the system and connect to the database. Create tables if they do not exist.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Create database tables if they do not already exist.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL
            )
            """)

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def register_user(self, username, password, role="member"):
        """
        Register a new user with a username, password, and role.
        Passwords are securely hashed using bcrypt.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Check for empty fields
            if not username or not password:
                raise ValueError("Username and password cannot be empty.")

            # Hash the password
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt).decode()

            # Insert user into the database
            cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                           (username, password_hash, role))
            conn.commit()
            conn.close()

            print("User successfully registered!")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
        except Exception as e:
            print(f"Error during registration: {e}")

    def authenticate_user(self, username, password):
        """
        Authenticate a user by verifying their username and password.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Fetch user information
            cursor.execute("SELECT password_hash, role FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if result is None:
                print("Authentication failed: User not found.")
                return None

            stored_password_hash, role = result

            # Verify the password
            if bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
                print("Authentication successful!")
                return role
            else:
                print("Authentication failed: Incorrect password.")
                return None
        except Exception as e:
            print(f"Error during authentication: {e}")
            return None
        finally:
            conn.close()

    def change_password(self, username, old_password, new_password):
        """
        Allow a user to change their password after verifying their old password.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Fetch user information
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if result is None:
                print("Error: User not found.")
                return False

            stored_password_hash = result[0]

            # Verify old password
            if not bcrypt.checkpw(old_password.encode(), stored_password_hash.encode()):
                print("Error: Incorrect old password.")
                return False

            # Hash the new password
            salt = bcrypt.gensalt()
            new_password_hash = bcrypt.hashpw(new_password.encode(), salt).decode()

            # Update password in the database
            cursor.execute("UPDATE users SET password_hash = ? WHERE username = ?", (new_password_hash, username))
            conn.commit()
            conn.close()

            print("Password successfully changed!")
            return True
        except Exception as e:
            print(f"Error during password change: {e}")
            return False

    def delete_user(self, username):
        """
        Delete a user from the system.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            conn.close()

            print("User successfully deleted!")
        except Exception as e:
            print(f"Error during user deletion: {e}")

# Example Usage
if __name__ == "__main__":
    auth_system = UserAuthenticationSystem()

    # Register a new user
    auth_system.register_user("admin", "securepassword", "admin")

    # Authenticate user
    role = auth_system.authenticate_user("admin", "securepassword")
    if role:
        print(f"User role: {role}")

    # Change password
    auth_system.change_password("admin", "securepassword", "newpassword")

    # Delete user
    auth_system.delete_user("admin")
```
