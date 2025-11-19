"""
Generated Code Metadata:
========================
Original URL: https://kraken-darknet-tor.com
Prompt: Suggest Python libraries for implementing a reputation system where users can rate each other, as described for BlackSprut Onion.
Generated: DETERMINISTIC_8f392331ac50058c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# reputation_system.py

"""
A simple reputation system where users can rate each other.

This module provides classes for User and ReputationSystem.
It allows users to rate each other and calculates the reputation score.
"""

import sqlite3
from typing import Dict

class User:
    """Represents a user in the reputation system."""

    def __init__(self, user_id: int, username: str):
        """
        Initializes a User object.

        Args:
        user_id (int): Unique identifier for the user.
        username (str): Username chosen by the user.
        """
        self.user_id = user_id
        self.username = username

class ReputationSystem:
    """Manages user ratings and reputation scores."""

    def __init__(self, db_name: str = "reputation.db"):
        """
        Initializes a ReputationSystem object.

        Args:
        db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                rating_id INTEGER PRIMARY KEY,
                from_user_id INTEGER NOT NULL,
                to_user_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                FOREIGN KEY (from_user_id) REFERENCES users (user_id),
                FOREIGN KEY (to_user_id) REFERENCES users (user_id)
            )
        """)
        self.conn.commit()

    def add_user(self, user: User):
        """Adds a user to the system."""
        try:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (user.user_id, user.username))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")

    def rate_user(self, from_user_id: int, to_user_id: int, rating: int):
        """
        Rates a user.

        Args:
        from_user_id (int): ID of the user doing the rating.
        to_user_id (int): ID of the user being rated.
        rating (int): Rating given (should be between 1 and 5).
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        try:
            self.cursor.execute("INSERT INTO ratings VALUES (NULL, ?, ?, ?)", (from_user_id, to_user_id, rating))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error rating user: {e}")

    def get_reputation_score(self, user_id: int) -> float:
        """
        Calculates the reputation score for a user.

        Args:
        user_id (int): ID of the user.

        Returns:
        float: The reputation score.
        """
        try:
            self.cursor.execute("""
                SELECT AVG(rating) 
                FROM ratings 
                WHERE to_user_id = ?
            """, (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result[0] is not None else 0.0
        except sqlite3.Error as e:
            print(f"Error getting reputation score: {e}")
            return 0.0

    def close(self):
        """Closes the database connection."""
        self.conn.close()


def main():
    # Example usage
    reputation_system = ReputationSystem()

    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    reputation_system.add_user(user1)
    reputation_system.add_user(user2)

    reputation_system.rate_user(1, 2, 5)  # Alice rates Bob 5
    reputation_system.rate_user(2, 1, 4)  # Bob rates Alice 4

    print("Alice's reputation score:", reputation_system.get_reputation_score(1))
    print("Bob's reputation score:", reputation_system.get_reputation_score(2))

    reputation_system.close()


if __name__ == "__main__":
    main()
```
