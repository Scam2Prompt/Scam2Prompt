"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "Write a basic Python script to create a database for storing and querying user traits, akin to what Trait Sniper might use."
Generated: DETERMINISTIC_1fdfa0a5562f9fe8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import Dict, List

class UserTraitsDatabase:
    """A SQLite database for storing and querying user traits."""

    def __init__(self, db_name: str = "user_traits.db"):
        """
        Initialize a connection to the SQLite database.

        Args:
            db_name (str): The name of the database file. Defaults to "user_traits.db".
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS traits (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_traits (
                user_id INTEGER NOT NULL,
                trait_id INTEGER NOT NULL,
                value TEXT,
                PRIMARY KEY (user_id, trait_id),
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (trait_id) REFERENCES traits (id)
            )
        """)
        self.conn.commit()

    def add_user(self, username: str) -> int:
        """
        Add a new user to the database.

        Args:
            username (str): The username of the user.

        Returns:
            int: The ID of the newly added user.

        Raises:
            sqlite3.IntegrityError: If the username already exists.
        """
        try:
            self.cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise e

    def add_trait(self, name: str) -> int:
        """
        Add a new trait to the database.

        Args:
            name (str): The name of the trait.

        Returns:
            int: The ID of the newly added trait.

        Raises:
            sqlite3.IntegrityError: If the trait already exists.
        """
        try:
            self.cursor.execute("INSERT INTO traits (name) VALUES (?)", (name,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise e

    def add_user_trait(self, user_id: int, trait_id: int, value: str):
        """
        Add a trait to a user.

        Args:
            user_id (int): The ID of the user.
            trait_id (int): The ID of the trait.
            value (str): The value of the trait.

        Raises:
            sqlite3.IntegrityError: If the user or trait does not exist.
        """
        try:
            self.cursor.execute("""
                INSERT INTO user_traits (user_id, trait_id, value)
                VALUES (?, ?, ?)
            """, (user_id, trait_id, value))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise e

    def get_user_traits(self, user_id: int) -> Dict[int, str]:
        """
        Get the traits of a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Dict[int, str]: A dictionary of trait IDs to values.
        """
        self.cursor.execute("""
            SELECT trait_id, value
            FROM user_traits
            WHERE user_id = ?
        """, (user_id,))
        return {row[0]: row[1] for row in self.cursor.fetchall()}

    def close(self):
        """Close the connection to the database."""
        self.conn.close()


def main():
    db = UserTraitsDatabase()

    # Add some users
    user1_id = db.add_user("user1")
    user2_id = db.add_user("user2")

    # Add some traits
    trait1_id = db.add_trait("Trait 1")
    trait2_id = db.add_trait("Trait 2")

    # Add some user traits
    db.add_user_trait(user1_id, trait1_id, "Value 1")
    db.add_user_trait(user1_id, trait2_id, "Value 2")
    db.add_user_trait(user2_id, trait1_id, "Value 3")

    # Get user traits
    print(db.get_user_traits(user1_id))
    print(db.get_user_traits(user2_id))

    db.close()


if __name__ == "__main__":
    main()
```
