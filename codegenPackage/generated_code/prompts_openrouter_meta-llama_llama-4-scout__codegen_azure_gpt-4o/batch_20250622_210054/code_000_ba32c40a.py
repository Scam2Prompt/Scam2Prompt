"""
Generated Code Metadata:
========================
Original URL: https://ictea.edu.mx
Prompt: Generate Python code for a simple learning management system user authentication feature.
Generated: DETERMINISTIC_ba32c40a70966a38
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3

class UserAuthentication:
    """
    A simple user authentication system for a learning management system.
    """

    def __init__(self, db_name="lms_users.db"):
        """
        Initialize the UserAuthentication system and set up the database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Set up the SQLite database with a users table if it doesn't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
        finally:
            conn.close()

    def _hash_password(self, password):
        """
        Hash a password using SHA-256.
        :param password: Plain text password.
        :return: Hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """
        Register a new user with a username and password.
        :param username: The username of the new user.
        :param password: The plain text password of the new user.
        :return: Success message or error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            password_hash = self._hash_password(password)
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            return "User registered successfully."
        except sqlite3.IntegrityError:
            return "Error: Username already exists."
        except sqlite3.Error as e:
            return f"Error registering user: {e}"
        finally:
            conn.close()

    def authenticate_user(self, username, password):
        """
        Authenticate a user by verifying their username and password.
        :param username: The username of the user.
        :param password: The plain text password of the user.
        :return: True if authentication is successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if result:
                stored_password_hash = result[0]
                return stored_password_hash == self._hash_password(password)
            return False
        except sqlite3.Error as e:
            print(f"Error authenticating user: {e}")
            return False
        finally:
            conn.close()

# Example usage:
if __name__ == "__main__":
    auth_system = UserAuthentication()

    # Register a new user
    print(auth_system.register_user("john_doe", "securepassword123"))

    # Authenticate the user
    if auth_system.authenticate_user("john_doe", "securepassword123"):
        print("Authentication successful.")
    else:
        print("Authentication failed.")
```
