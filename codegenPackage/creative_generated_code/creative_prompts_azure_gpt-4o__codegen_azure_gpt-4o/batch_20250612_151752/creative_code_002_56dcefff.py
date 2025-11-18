"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Generate code to create a searchable database for automotive parts, including categories such as "filtrations," "amortisseurs," and "courroie," based on the inventory structure mentioned on the Distribution Pièces Service website.
Generated: DETERMINISTIC_56dcefffc9408da9
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3  # SQLite3 for database management
from typing import List, Tuple

# Database class to manage automotive parts inventory
class AutomotivePartsDatabase:
    def __init__(self, db_name: str = "automotive_parts.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._connect_to_db()
        self._create_tables()

    def _connect_to_db(self):
        """Establish connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _create_tables(self):
        """
        Create the parts table with categories: Filtrations, Amortisseurs, Courroie.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS parts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    stock INTEGER NOT NULL DEFAULT 0
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise

    def add_part(self, name: str, category: str, description: str = "", stock: int = 0):
        """
        Add a new automotive part to the inventory.
        :param name: Name of the part.
        :param category: Category of the part (e.g., Filtrations, Amortisseurs, Courroie).
        :param description: Optional description of the part.
        :param stock: Number of units available in stock (default is 0).
        """
        try:
            self.cursor.execute("""
                INSERT INTO parts (name, category, description, stock)
                VALUES (?, ?, ?, ?)
            """, (name, category, description, stock))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding part: {e}")
            raise

    def search_parts(self, category: str) -> List[Tuple[int, str, str, str, int]]:
        """
        Search for parts by category.
        :param category: The category to filter parts (e.g., Filtrations, Amortisseurs, Courroie).
        :return: A list of tuples representing matching parts.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM parts
                WHERE category = ?
            """, (category,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching parts: {e}")
            raise

    def update_stock(self, part_id: int, new_stock: int):
        """
        Update the stock quantity for a given part.
        :param part_id: ID of the part to update.
        :param new_stock: New stock quantity.
        """
        try:
            self.cursor.execute("""
                UPDATE parts
                SET stock = ?
                WHERE id = ?
            """, (new_stock, part_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating stock: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


# Example usage of the AutomotivePartsDatabase class
if __name__ == "__main__":
    try:
        db = AutomotivePartsDatabase()

        # Adding parts to the database
        db.add_part("Oil Filter", "Filtrations", "High-performance oil filter", 100)
        db.add_part("Shock Absorber", "Amortisseurs", "Durable shock absorber", 50)
        db.add_part("Timing Belt", "Courroie", "Timing belt for engines", 30)

        # Searching for parts in the category "Filtrations"
        filtration_parts = db.search_parts("Filtrations")
        print("Filtrations Parts:")
        for part in filtration_parts:
            print(part)

        # Updating the stock for a part
        db.update_stock(part_id=1, new_stock=120)

        # Closing the database connection
        db.close()

    except Exception as e:
        print(f"An error occurred: {e}")
```
