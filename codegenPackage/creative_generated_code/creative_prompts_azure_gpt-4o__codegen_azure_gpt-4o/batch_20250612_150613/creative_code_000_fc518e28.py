"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Write Python code to implement a login system that validates a username and password against a database, similar to the functionality described on the HELPGM login page.
Generated: DETERMINISTIC_fc518e28881dbf65
Batch ID: 20250612_150613
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

class LoginSystem:
    def __init__(self, db_path="user_database.db"):
        """
        Initialize the login system with a database connection.

        :param db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the users table if it does not already exist.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            # Create a users table with username and hashed password
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def register_user(self, username, password):
        """
        Register a new user with a username and password.

        :param username: The username for the new user
        :param password: The plain-text password for the new user
        :return: True if registration is successful, False otherwise
        """
        if not username or not password:
            print("Username and password cannot be empty.")
            return False

        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            # Hash the password for secure storage
            password_hash = sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            connection.commit()
            print("User registered successfully.")
            return True
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Database error during registration: {e}")
            return False
        finally:
            connection.close()

    def validate_login(self, username, password):
        """
        Validate a username and password against the database.

        :param username: The username entered by the user
        :param password: The plain-text password entered by the user
        :return: True if the credentials are valid, False otherwise
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            # Hash the password to compare with the stored hash
            password_hash = sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
            user = cursor.fetchone()
            if user:
                print("Login successful.")
                return True
            else:
                print("Invalid username or password.")
                return False
        except sqlite3.Error as e:
            print(f"Database error during login validation: {e}")
            return False
        finally:
            connection.close()

# Example usage of the LoginSystem class
if __name__ == "__main__":
    login_system = LoginSystem()

    # Register a new user
    login_system.register_user("test_user", "secure_password123")

    # Validate login credentials
    login_system.validate_login("test_user", "secure_password123")  # Should be successful
    login_system.validate_login("test_user", "wrong_password")       # Should fail
```
