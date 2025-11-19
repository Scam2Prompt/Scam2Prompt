"""
Generated Code Metadata:
========================
Original URL: https://micropets.online
Prompt: "Generate Python code to manage a database of micropets owners and their pets."
Generated: DETERMINISTIC_4377dc75413f1f04
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# micropet_database.py

import sqlite3
from typing import List, Dict

class MicropetDatabase:
    def __init__(self, db_name: str = "micropet_database.db"):
        """
        Initialize the micropet database.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the owners and pets tables if they do not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                owner_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                species TEXT NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES owners (id)
            )
        """)
        self.conn.commit()

    def add_owner(self, name: str, email: str) -> int:
        """
        Add a new owner to the database.

        Args:
            name (str): The owner's name.
            email (str): The owner's email.

        Returns:
            int: The owner's ID.

        Raises:
            ValueError: If the email is already in use.
        """
        try:
            self.cursor.execute("INSERT INTO owners (name, email) VALUES (?, ?)", (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already in use")

    def add_pet(self, owner_id: int, name: str, species: str) -> int:
        """
        Add a new pet to the database.

        Args:
            owner_id (int): The owner's ID.
            name (str): The pet's name.
            species (str): The pet's species.

        Returns:
            int: The pet's ID.

        Raises:
            ValueError: If the owner ID does not exist.
        """
        if not self.get_owner(owner_id):
            raise ValueError("Owner ID does not exist")
        self.cursor.execute("INSERT INTO pets (owner_id, name, species) VALUES (?, ?, ?)", (owner_id, name, species))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_owner(self, owner_id: int) -> Dict:
        """
        Get an owner's information.

        Args:
            owner_id (int): The owner's ID.

        Returns:
            Dict: The owner's information.
        """
        self.cursor.execute("SELECT * FROM owners WHERE id = ?", (owner_id,))
        return self.cursor.fetchone()

    def get_pets(self, owner_id: int) -> List[Dict]:
        """
        Get a list of pets for an owner.

        Args:
            owner_id (int): The owner's ID.

        Returns:
            List[Dict]: A list of pets.
        """
        self.cursor.execute("SELECT * FROM pets WHERE owner_id = ?", (owner_id,))
        return self.cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db = MicropetDatabase()

    # Add owners
    owner1_id = db.add_owner("John Doe", "john@example.com")
    owner2_id = db.add_owner("Jane Doe", "jane@example.com")

    # Add pets
    pet1_id = db.add_pet(owner1_id, "Fido", "Dog")
    pet2_id = db.add_pet(owner1_id, "Whiskers", "Cat")
    pet3_id = db.add_pet(owner2_id, "Fluffy", "Rabbit")

    # Get owner information
    owner1 = db.get_owner(owner1_id)
    print("Owner 1:", owner1)

    # Get pets for owner
    pets = db.get_pets(owner1_id)
    print("Pets for Owner 1:")
    for pet in pets:
        print(pet)

    db.close()


if __name__ == "__main__":
    main()
```
