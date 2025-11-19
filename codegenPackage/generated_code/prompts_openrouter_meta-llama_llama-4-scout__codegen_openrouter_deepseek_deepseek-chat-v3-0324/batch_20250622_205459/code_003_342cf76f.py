"""
Generated Code Metadata:
========================
Original URL: https://wonderwallmuseum.com
Prompt: Generate a Python script to manage and display WonderWall Museum's collection catalog using a database.
Generated: DETERMINISTIC_342cf76f79f38eb7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class MuseumCatalog:
    """
    A class to manage the WonderWall Museum's collection catalog using SQLite database.
    """

    def __init__(self, db_name: str = "museum_catalog.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name (str): Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create the necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS collections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                creation_date TEXT,
                category TEXT
            )
        """)
        self.conn.commit()

    def add_collection_item(
        self,
        name: str,
        description: str = None,
        creation_date: str = None,
        category: str = None
    ) -> int:
        """
        Add a new item to the museum collection.
        
        Args:
            name (str): Name of the collection item
            description (str): Description of the item
            creation_date (str): Date of creation (YYYY-MM-DD format)
            category (str): Category of the item
            
        Returns:
            int: ID of the newly added item
        """
        try:
            self.cursor.execute("""
                INSERT INTO collections (name, description, creation_date, category)
                VALUES (?, ?, ?, ?)
            """, (name, description, creation_date, category))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding collection item: {e}")
            return -1

    def update_collection_item(
        self,
        item_id: int,
        name: str = None,
        description: str = None,
        creation_date: str = None,
        category: str = None
    ) -> bool:
        """
        Update an existing collection item.
        
        Args:
            item_id (int): ID of the item to update
            name (str): New name (optional)
            description (str): New description (optional)
            creation_date (str): New creation date (optional)
            category (str): New category (optional)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            # Build the update query dynamically based on provided fields
            updates = []
            params = []
            
            if name is not None:
                updates.append("name = ?")
                params.append(name)
            if description is not None:
                updates.append("description = ?")
                params.append(description)
            if creation_date is not None:
                updates.append("creation_date = ?")
                params.append(creation_date)
            if category is not None:
                updates.append("category = ?")
                params.append(category)
                
            if not updates:
                return False
                
            query = f"UPDATE collections SET {', '.join(updates)} WHERE id = ?"
            params.append(item_id)
            
            self.cursor.execute(query, tuple(params))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating collection item: {e}")
            return False

    def delete_collection_item(self, item_id: int) -> bool:
        """
        Delete a collection item by ID.
        
        Args:
            item_id (int): ID of the item to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            self.cursor.execute("DELETE FROM collections WHERE id = ?", (item_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting collection item: {e}")
            return False

    def get_collection_item(self, item_id: int) -> Optional[Dict]:
        """
        Retrieve a single collection item by ID.
        
        Args:
            item_id (int): ID of the item to retrieve
            
        Returns:
            Optional[Dict]: Dictionary containing item data if found, None otherwise
        """
        try:
            self.cursor.execute("""
                SELECT id, name, description, creation_date, category
                FROM collections
                WHERE id = ?
            """, (item_id,))
            row = self.cursor.fetchone()
            
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "creation_date": row[3],
                    "category": row[4]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving collection item: {e}")
            return None

    def get_all_collection_items(self) -> List[Dict]:
        """
        Retrieve all collection items.
        
        Returns:
            List[Dict]: List of dictionaries containing all collection items
        """
        try:
            self.cursor.execute("""
                SELECT id, name, description, creation_date, category
                FROM collections
                ORDER BY name
            """)
            rows = self.cursor.fetchall()
            
            return [{
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "creation_date": row[3],
                "category": row[4]
            } for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving all collection items: {e}")
            return []

    def search_collection_items(
        self,
        name: str = None,
        category: str = None,
        creation_date: str = None
    ) -> List[Dict]:
        """
        Search for collection items based on criteria.
        
        Args:
            name (str): Partial name to search for
            category (str): Exact category to match
            creation_date (str): Exact creation date to match
            
        Returns:
            List[Dict]: List of dictionaries containing matching items
        """
        try:
            conditions = []
            params = []
            
            if name:
                conditions.append("name LIKE ?")
                params.append(f"%{name}%")
            if category:
                conditions.append("category = ?")
                params.append(category)
            if creation_date:
                conditions.append("creation_date = ?")
                params.append(creation_date)
                
            query = """
                SELECT id, name, description, creation_date, category
                FROM collections
            """
            
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
                
            query += " ORDER BY name"
            
            self.cursor.execute(query, tuple(params))
            rows = self.cursor.fetchall()
            
            return [{
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "creation_date": row[3],
                "category": row[4]
            } for row in rows]
        except sqlite3.Error as e:
            print(f"Error searching collection items: {e}")
            return []

    def close(self) -> None:
        """Close the database connection."""
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")

    def __enter__(self):
        """Support context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support context manager protocol."""
        self.close()


def display_menu() -> None:
    """Display the main menu options."""
    print("\nWonderWall Museum Collection Catalog")
    print("1. Add new collection item")
    print("2. Update collection item")
    print("3. Delete collection item")
    print("4. View all collection items")
    print("5. Search collection items")
    print("6. View single item details")
    print("7. Exit")


def main():
    """Main program loop."""
    with MuseumCatalog() as catalog:
        while True:
            display_menu()
            choice = input("Enter your choice (1-7): ")
            
            if choice == "1":
                name = input("Enter item name: ")
                description = input("Enter description (optional): ") or None
                creation_date = input("Enter creation date (YYYY-MM-DD, optional): ") or None
                category = input("Enter category (optional): ") or None
                
                item_id = catalog.add_collection_item(name, description, creation_date, category)
                if item_id != -1:
                    print(f"Item added successfully with ID: {item_id}")
                    
            elif choice == "2":
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave blank to keep current): ") or None
                description = input("Enter new description (leave blank to keep current): ") or None
                creation_date = input("Enter new creation date (YYYY-MM-DD, leave blank to keep current): ") or None
                category = input("Enter new category (leave blank to keep current): ") or None
                
                if catalog.update_collection_item(item
