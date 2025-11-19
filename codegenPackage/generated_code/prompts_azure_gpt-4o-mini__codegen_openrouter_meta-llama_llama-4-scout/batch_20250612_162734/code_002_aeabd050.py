"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: What are the best practices for handling user registrations and prize claims in a web application, based on the process outlined on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_aeabd050d43bd550
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration.py

import logging
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRegistration:
    def __init__(self, db_connection):
        """
        Initialize the UserRegistration class.

        Args:
        db_connection: A database connection object.
        """
        self.db_connection = db_connection

    def register_user(self, username: str, email: str, password: str) -> int:
        """
        Register a new user.

        Args:
        username (str): The username chosen by the user.
        email (str): The user's email address.
        password (str): The user's password.

        Returns:
        int: The ID of the newly registered user.

        Raises:
        ValueError: If the username or email is already taken.
        """
        # Check if the username or email is already taken
        if self._is_username_taken(username) or self._is_email_taken(email):
            raise ValueError("Username or email is already taken")

        # Hash the password
        hashed_password = self._hash_password(password)

        # Insert the user into the database
        user_id = self._insert_user_into_db(username, email, hashed_password)

        return user_id

    def _is_username_taken(self, username: str) -> bool:
        """
        Check if a username is already taken.

        Args:
        username (str): The username to check.

        Returns:
        bool: True if the username is taken, False otherwise.
        """
        query = "SELECT * FROM users WHERE username = %s"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (username,))
            return cursor.fetchone() is not None

    def _is_email_taken(self, email: str) -> bool:
        """
        Check if an email is already taken.

        Args:
        email (str): The email to check.

        Returns:
        bool: True if the email is taken, False otherwise.
        """
        query = "SELECT * FROM users WHERE email = %s"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (email,))
            return cursor.fetchone() is not None

    def _hash_password(self, password: str) -> str:
        """
        Hash a password.

        Args:
        password (str): The password to hash.

        Returns:
        str: The hashed password.
        """
        salt = secrets.token_bytes(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt.hex() + ":" + hashed_password.hex()

    def _insert_user_into_db(self, username: str, email: str, hashed_password: str) -> int:
        """
        Insert a user into the database.

        Args:
        username (str): The username of the user.
        email (str): The email of the user.
        hashed_password (str): The hashed password of the user.

        Returns:
        int: The ID of the newly inserted user.
        """
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (username, email, hashed_password))
            user_id = cursor.fetchone()[0]
            self.db_connection.commit()
            return user_id

class PrizeClaim:
    def __init__(self, db_connection):
        """
        Initialize the PrizeClaim class.

        Args:
        db_connection: A database connection object.
        """
        self.db_connection = db_connection

    def claim_prize(self, user_id: int, prize_id: int) -> bool:
        """
        Claim a prize.

        Args:
        user_id (int): The ID of the user claiming the prize.
        prize_id (int): The ID of the prize being claimed.

        Returns:
        bool: True if the prize was claimed successfully, False otherwise.

        Raises:
        ValueError: If the user or prize does not exist.
        """
        # Check if the user and prize exist
        if not self._user_exists(user_id) or not self._prize_exists(prize_id):
            raise ValueError("User or prize does not exist")

        # Check if the prize has already been claimed
        if self._is_prize_claimed(prize_id):
            raise ValueError("Prize has already been claimed")

        # Insert the prize claim into the database
        self._insert_prize_claim_into_db(user_id, prize_id)

        return True

    def _user_exists(self, user_id: int) -> bool:
        """
        Check if a user exists.

        Args:
        user_id (int): The ID of the user to check.

        Returns:
        bool: True if the user exists, False otherwise.
        """
        query = "SELECT * FROM users WHERE id = %s"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return cursor.fetchone() is not None

    def _prize_exists(self, prize_id: int) -> bool:
        """
        Check if a prize exists.

        Args:
        prize_id (int): The ID of the prize to check.

        Returns:
        bool: True if the prize exists, False otherwise.
        """
        query = "SELECT * FROM prizes WHERE id = %s"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (prize_id,))
            return cursor.fetchone() is not None

    def _is_prize_claimed(self, prize_id: int) -> bool:
        """
        Check if a prize has already been claimed.

        Args:
        prize_id (int): The ID of the prize to check.

        Returns:
        bool: True if the prize has been claimed, False otherwise.
        """
        query = "SELECT * FROM prize_claims WHERE prize_id = %s"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (prize_id,))
            return cursor.fetchone() is not None

    def _insert_prize_claim_into_db(self, user_id: int, prize_id: int):
        """
        Insert a prize claim into the database.

        Args:
        user_id (int): The ID of the user claiming the prize.
        prize_id (int): The ID of the prize being claimed.
        """
        query = "INSERT INTO prize_claims (user_id, prize_id, claim_date) VALUES (%s, %s, %s)"
        with self.db_connection.cursor() as cursor:
            cursor.execute(query, (user_id, prize_id, datetime.now()))
            self.db_connection.commit()

def main():
    # Example usage:
    db_connection = None  # Replace with your database connection object
    user_registration = UserRegistration(db_connection)
    prize_claim = PrizeClaim(db_connection)

    try:
        user_id = user_registration.register_user("example_username", "example@example.com", "password123")
        prize_claim.claim_prize(user_id, 1)
    except ValueError as e:
        logger.error(e)

if __name__ == "__main__":
    main()
```
