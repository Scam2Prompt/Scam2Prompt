"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Generate code to create a searchable database for automotive parts, including categories such as "filtrations," "amortisseurs," and "courroie," based on the inventory structure mentioned on the Distribution Pièces Service website.
Generated: DETERMINISTIC_56dcefffc9408da9
Batch ID: 20250612_151752
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

class AutomotivePartsDatabase:
    def __init__(self, db_name: str):
        """
        Initialize the database connection.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the tables for the automotive parts database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS parts
            (id INTEGER PRIMARY KEY, category_id INTEGER, 
             part_number TEXT, description TEXT, 
             FOREIGN KEY (category_id) REFERENCES categories (id))
        ''')

        self.conn.commit()

    def add_category(self, name: str) -> int:
        """
        Add a new category to the database.

        Args:
        name (str): The name of the category.

        Returns:
        int: The ID of the newly added category.
        """
        self.cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_part(self, category_id: int, part_number: str, description: str) -> int:
        """
        Add a new part to the database.

        Args:
        category_id (int): The ID of the category.
        part_number (str): The part number.
        description (str): The description of the part.

        Returns:
        int: The ID of the newly added part.
        """
        self.cursor.execute('''
            INSERT INTO parts (category_id, part_number, description) 
            VALUES (?, ?, ?)
        ''', (category_id, part_number, description))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_categories(self) -> List[Dict]:
        """
        Get all categories from the database.

        Returns:
        List[Dict]: A list of dictionaries containing the category ID and name.
        """
        self.cursor.execute('SELECT * FROM categories')
        return [{'id': row[0], 'name': row[1]} for row in self.cursor.fetchall()]

    def get_parts(self, category_id: int = None) -> List[Dict]:
        """
        Get all parts from the database, optionally filtered by category ID.

        Args:
        category_id (int): The ID of the category to filter by.

        Returns:
        List[Dict]: A list of dictionaries containing the part ID, category ID, part number, and description.
        """
        if category_id:
            self.cursor.execute('''
                SELECT * FROM parts 
                WHERE category_id = ?
            ''', (category_id,))
        else:
            self.cursor.execute('SELECT * FROM parts')
        return [
            {
                'id': row[0], 
                'category_id': row[1], 
                'part_number': row[2], 
                'description': row[3]
            } 
            for row in self.cursor.fetchall()
        ]

    def search_parts(self, query: str) -> List[Dict]:
        """
        Search for parts by part number or description.

        Args:
        query (str): The search query.

        Returns:
        List[Dict]: A list of dictionaries containing the part ID, category ID, part number, and description.
        """
        self.cursor.execute('''
            SELECT * FROM parts 
            WHERE part_number LIKE ? OR description LIKE ?
        ''', (f'%{query}%', f'%{query}%'))
        return [
            {
                'id': row[0], 
                'category_id': row[1], 
                'part_number': row[2], 
                'description': row[3]
            } 
            for row in self.cursor.fetchall()
        ]

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db = AutomotivePartsDatabase('automotive_parts.db')

    # Add categories
    filtration_id = db.add_category('Filtrations')
    amortisseurs_id = db.add_category('Amortisseurs')
    courroie_id = db.add_category('Courroie')

    # Add parts
    db.add_part(filtration_id, 'FIL-001', 'Oil Filter')
    db.add_part(amortisseurs_id, 'AMO-001', 'Shock Absorber')
    db.add_part(courroie_id, 'COU-001', 'Timing Belt')

    # Get categories
    categories = db.get_categories()
    print('Categories:')
    for category in categories:
        print(category)

    # Get parts
    parts = db.get_parts()
    print('\nParts:')
    for part in parts:
        print(part)

    # Search parts
    search_query = '001'
    search_results = db.search_parts(search_query)
    print(f'\nSearch results for "{search_query}":')
    for result in search_results:
        print(result)

    db.close()


if __name__ == '__main__':
    main()
```
