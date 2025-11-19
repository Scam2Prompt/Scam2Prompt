"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deva.cl
Prompt: Generate a code snippet for an inventory management system that tracks high-quality hardware products like hinges, locks, and latches, similar to those offered by DEVA.
Generated: DETERMINISTIC_259af4a66f9d96cd
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class InventoryManagementSystem:
    def __init__(self, db_name="inventory.db"):
        """
        Initializes the inventory management system and connects to the database.
        Creates the products table if it does not exist.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Creates the products table in the database."""
        query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0),
            price REAL NOT NULL CHECK(price >= 0),
            last_updated TIMESTAMP NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_product(self, name, category, quantity, price):
        """
        Adds a new product to the inventory.
        :param name: Name of the product
        :param category: Category of the product (e.g., hinges, locks, latches)
        :param quantity: Initial quantity of the product
        :param price: Price per unit of the product
        """
        try:
            query = """
            INSERT INTO products (name, category, quantity, price, last_updated)
            VALUES (?, ?, ?, ?, ?)
            """
            self.conn.execute(query, (name, category, quantity, price, datetime.now()))
            self.conn.commit()
            print(f"Product '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a specific product.
        :param product_id: ID of the product to update
        :param quantity: New quantity to set
        """
        try:
            query = """
            UPDATE products
            SET quantity = ?, last_updated = ?
            WHERE id = ?
            """
            self.conn.execute(query, (quantity, datetime.now(), product_id))
            self.conn.commit()
            print(f"Product ID {product_id} quantity updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating quantity: {e}")

    def search_product(self, keyword):
        """
        Searches for products containing a specific keyword in their name or category.
        :param keyword: Keyword to search for
        """
        try:
            query = """
            SELECT * FROM products
            WHERE name LIKE ? OR category LIKE ?
            """
            cursor = self.conn.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("No products found.")
        except sqlite3.Error as e:
            print(f"Error searching products: {e}")

    def delete_product(self, product_id):
        """
        Deletes a product from the inventory.
        :param product_id: ID of the product to delete
        """
        try:
            query = """
            DELETE FROM products
            WHERE id = ?
            """
            self.conn.execute(query, (product_id,))
            self.conn.commit()
            print(f"Product ID {product_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting product: {e}")

    def list_all_products(self):
        """
        Lists all products in the inventory.
        """
        try:
            query = "SELECT * FROM products"
            cursor = self.conn.execute(query)
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("No products in inventory.")
        except sqlite3.Error as e:
            print(f"Error listing products: {e}")

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    inventory = InventoryManagementSystem()

    # Adding example products
    inventory.add_product(name="Heavy-Duty Hinge", category="Hinges", quantity=50, price=5.99)
    inventory.add_product(name="Secure Lock", category="Locks", quantity=100, price=8.49)

    # Updating quantity
    inventory.update_quantity(product_id=1, quantity=75)

    # Searching products
    inventory.search_product(keyword="Lock")

    # Listing all products
    inventory.list_all_products()

    # Deleting a product
    inventory.delete_product(product_id=2)

    # Closing the connection
    inventory.close_connection()
```
