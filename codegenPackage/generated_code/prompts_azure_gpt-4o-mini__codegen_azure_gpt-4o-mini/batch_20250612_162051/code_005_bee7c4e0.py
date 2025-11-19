"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: What programming techniques can be used to ensure offline functionality for agricultural management apps like Azagros?
Generated: DETERMINISTIC_bee7c4e0c743cae0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import sqlite3
from typing import Any, Dict, List

class OfflineDatabase:
    """Class to handle offline data storage using SQLite."""
    
    def __init__(self, db_name: str = 'agriculture_management.db'):
        """Initialize the database connection."""
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_tables()

    def create_connection(self) -> sqlite3.Connection:
        """Create a database connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Create necessary tables for storing agricultural data."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS crops (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_crop(self, name: str, quantity: int) -> None:
        """Add a new crop to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO crops (name, quantity) VALUES (?, ?)', (name, quantity))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding crop: {e}")

    def get_crops(self) -> List[Dict[str, Any]]:
        """Retrieve all crops from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM crops')
            rows = cursor.fetchall()
            return [{'id': row[0], 'name': row[1], 'quantity': row[2], 'last_updated': row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving crops: {e}")
            return []

    def update_crop(self, crop_id: int, quantity: int) -> None:
        """Update the quantity of an existing crop."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('UPDATE crops SET quantity = ?, last_updated = CURRENT_TIMESTAMP WHERE id = ?', (quantity, crop_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating crop: {e}")

    def delete_crop(self, crop_id: int) -> None:
        """Delete a crop from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM crops WHERE id = ?', (crop_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting crop: {e}")

    def close_connection(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()

def main():
    """Main function to demonstrate offline functionality."""
    db = OfflineDatabase()

    # Example usage
    db.add_crop('Tomato', 100)
    db.add_crop('Potato', 200)

    crops = db.get_crops()
    print("Crops in database:", json.dumps(crops, indent=2))

    db.update_crop(1, 150)  # Update quantity of Tomato
    db.delete_crop(2)       # Delete Potato

    crops = db.get_crops()
    print("Updated crops in database:", json.dumps(crops, indent=2))

    db.close_connection()

if __name__ == "__main__":
    main()
```
