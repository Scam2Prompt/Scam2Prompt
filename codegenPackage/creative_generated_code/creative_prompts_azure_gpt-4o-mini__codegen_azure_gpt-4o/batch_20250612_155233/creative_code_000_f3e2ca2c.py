"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travelobay.com
Prompt: Generate a code snippet to implement a secure login feature for an online casino platform like R7 Casino, ensuring user data protection and encryption.
Generated: DETERMINISTIC_f3e2ca2cf63fb04e
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
import sqlite3
from datetime import datetime, timedelta

# Constants for JWT
SECRET_KEY = "your_secret_key_here"  # Replace with a strong, unique secret key
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 30

# Database connection (Ensure SQLite database is set up properly)
DB_PATH = "casino_users.db"

# Secure Login Feature
class CasinoLogin:

    def __init__(self):
        self.db_connection = sqlite3.connect(DB_PATH)
        self.db_cursor = self.db_connection.cursor()
        self._setup_database()

    def _setup_database(self):
        """Sets up the user table if it doesn't already exist."""
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        self.db_connection.commit()

    def register_user(self, username, password):
        """
        Registers a new user with a hashed password.
        
        :param username: The username of the user
        :param password: The plaintext password of the user
        :raises ValueError: If the username is already taken
        """
        try:
            # Hash the password using bcrypt
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Insert the user into the database
            self.db_cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                                    (username, password_hash.decode('utf-8')))
            self.db_connection.commit()
        except sqlite3.IntegrityError:
            # Handle case where username already exists
            raise ValueError("Username already exists. Please choose a different username.")

    def login_user(self, username, password):
        """
        Logs in a user by verifying the password and returning a JWT token.
        
        :param username: The username of the user
        :param password: The plaintext password of the user
        :return: JWT token if login is successful
        :raises ValueError: If the username does not exist or password is incorrect
        """
        # Fetch the user from the database
        self.db_cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        user = self.db_cursor.fetchone()

        if not user:
            raise ValueError("Invalid username or password.")

        # Verify the password
        password_hash = user[0]
        if not bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
            raise ValueError("Invalid username or password.")
        
        # Generate JWT token
        payload = {
            "username": username,
            "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

        return token

    def verify_token(self, token):
        """
        Verifies the validity of a JWT token.
        
        :param token: JWT token to verify
        :return: Decoded payload if token is valid
        :raises jwt.ExpiredSignatureError: If the token has expired
        :raises jwt.InvalidTokenError: If the token is invalid
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")

    def close_connection(self):
        """Closes the database connection."""
        self.db_connection.close()


# Example usage (ensure proper user input handling in production)
if __name__ == "__main__":
    casino_login = CasinoLogin()
    try:
        # Register a user (replace with real user input in production)
        casino_login.register_user("testuser", "securepassword123")

        # Login the user
        token = casino_login.login_user("testuser", "securepassword123")
        print(f"Login successful. Your token: {token}")

        # Verify the token
        payload = casino_login.verify_token(token)
        print(f"Token verified. Welcome, {payload['username']}!")

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        casino_login.close_connection()
```
