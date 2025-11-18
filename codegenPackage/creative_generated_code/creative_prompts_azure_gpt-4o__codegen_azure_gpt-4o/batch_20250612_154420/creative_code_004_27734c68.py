"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Generate code to build a searchable database for the Homefoods Ghana product catalog, including fields for product name, category, and description.
Generated: DETERMINISTIC_27734c68d1eb27a7
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3

class ProductDatabase:
    """
    A class to handle a searchable database for the Homefoods Ghana product catalog.
    This includes fields for product name, category, and description.
    """

    def __init__(self, db_name="homefoods_catalog.db"):
        """
        Initialize the database connection and create the products table if it doesn't exist.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            # Create the products table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
            raise

    def add_product(self, name, category, description):
        """
        Add a new product to the database.
        :param name: Name of the product.
        :param category: Category of the product.
        :param description: Description of the product.
        """
        try:
            self.cursor.execute("""
                INSERT INTO products (name, category, description)
                VALUES (?, ?, ?)
            """, (name, category, description))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            raise

    def search_product(self, keyword):
        """
        Search for products based on a keyword in name or description.
        :param keyword: The keyword to search for.
        :return: List of matching products.
        """
        try:
            self.cursor.execute("""
                SELECT id, name, category, description
                FROM products
                WHERE name LIKE ? OR description LIKE ?
            """, (f"%{keyword}%", f"%{keyword}%"))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching for products: {e}")
            raise

    def list_products(self):
        """
        List all products in the database.
        :return: List of all products.
        """
        try:
            self.cursor.execute("SELECT id, name, category, description FROM products")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error listing products: {e}")
            raise

    def close(self):
        """
        Close the database connection.
        """
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")

# Usage Example (commented out for production scenarios)
# db = ProductDatabase()
# db.add_product("Palmnut Soup Base", "Soup Base", "A rich soup base made with palm nuts.")
# db.add_product("Shito", "Condiments", "Spicy Ghanaian chili sauce.")
# print("All Products:")
# print(db.list_products())
# print("Search Results for 'soup':")
# print(db.search_product("soup"))
# db.close()
```
