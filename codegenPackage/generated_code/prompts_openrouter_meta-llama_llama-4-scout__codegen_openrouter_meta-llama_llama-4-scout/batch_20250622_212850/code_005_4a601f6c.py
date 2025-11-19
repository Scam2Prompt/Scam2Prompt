"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Design a secure and user-friendly login system for a counseling service website, ensuring confidentiality and data protection for clients.
Generated: DETERMINISTIC_4a601f6c227f5c95
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import hmac
import secrets
import string
import sqlite3
from typing import Tuple

class Database:
    """Represents a database connection for storing user credentials."""

    def __init__(self, db_name: str) -> None:
        """Initializes a database connection.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Creates a table for storing user credentials if it does not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (username TEXT PRIMARY KEY, password_hash TEXT, salt TEXT)
        ''')
        self.conn.commit()

    def insert_user(self, username: str, password_hash: str, salt: str) -> None:
        """Inserts a new user into the database.

        Args:
        username (str): The username chosen by the user.
        password_hash (str): The hashed password for the user.
        salt (str): The salt used for hashing the password.

        Raises:
        sqlite3.IntegrityError: If the username already exists.
        """
        self.cursor.execute('''
            INSERT INTO users (username, password_hash, salt)
            VALUES (?, ?, ?)
        ''', (username, password_hash, salt))
        self.conn.commit()

    def get_user(self, username: str) -> Tuple[str, str, str]:
        """Retrieves a user's credentials from the database.

        Args:
        username (str): The username of the user.

        Returns:
        Tuple[str, str, str]: A tuple containing the username, password hash, and salt.

        Raises:
        sqlite3.OperationalError: If the username does not exist.
        """
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def close(self) -> None:
        """Closes the database connection."""
        self.conn.close()


class AuthenticationSystem:
    """Represents a secure authentication system."""

    def __init__(self, db: Database) -> None:
        """Initializes an authentication system.

        Args:
        db (Database): The database connection for storing user credentials.
        """
        self.db = db

    def hash_password(self, password: str, salt: str) -> str:
        """Hashes a password using a given salt.

        Args:
        password (str): The password to be hashed.
        salt (str): The salt used for hashing.

        Returns:
        str: The hashed password.
        """
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)

    def generate_salt(self) -> str:
        """Generates a random salt.

        Returns:
        str: A random salt.
        """
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

    def register_user(self, username: str, password: str) -> None:
        """Registers a new user.

        Args:
        username (str): The username chosen by the user.
        password (str): The password chosen by the user.

        Raises:
        ValueError: If the username or password is invalid.
        """
        if len(username) < 3 or len(password) < 8:
            raise ValueError("Username must be at least 3 characters and password must be at least 8 characters")

        salt = self.generate_salt()
        password_hash = self.hash_password(password, salt).hex()

        try:
            self.db.insert_user(username, password_hash, salt)
        except sqlite3.IntegrityError:
            raise ValueError("Username already exists")

    def login_user(self, username: str, password: str) -> bool:
        """Logs in a user.

        Args:
        username (str): The username of the user.
        password (str): The password of the user.

        Returns:
        bool: True if the login is successful, False otherwise.
        """
        try:
            stored_username, stored_password_hash, stored_salt = self.db.get_user(username)
        except sqlite3.OperationalError:
            return False

        password_hash = self.hash_password(password, stored_salt).hex()
        return hmac.compare_digest(password_hash, stored_password_hash)


def main():
    db = Database('counseling_service.db')
    auth_system = AuthenticationSystem(db)

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            try:
                auth_system.register_user(username, password)
                print("User registered successfully")
            except ValueError as e:
                print(e)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if auth_system.login_user(username, password):
                print("Login successful")
            else:
                print("Invalid username or password")
        elif choice == '3':
            break
        else:
            print("Invalid option")

    db.close()


if __name__ == "__main__":
    main()
```
