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
from contextlib import closing

# Define a class to represent the inventory management system
class InventoryManager:
    def __init__(self, db_name='inventory.db'):
        """Initialize the Inventory Manager with a SQLite database."""
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Create the inventory table if it does not exist."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            ''')
            conn.commit()

    def connect_db(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def add_product(self, name, category, quantity, price):
        """Add a new product to the inventory."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO products (name, category, quantity, price)
                    VALUES (?, ?, ?, ?)
                ''', (name, category, quantity, price))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error adding product: {e}")

    def update_product(self, product_id, quantity):
        """Update the quantity of an existing product."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    UPDATE products
                    SET quantity = ?
                    WHERE id = ?
                ''', (quantity, product_id))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error updating product: {e}")

    def delete_product(self, product_id):
        """Remove a product from the inventory."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    DELETE FROM products WHERE id = ?
                ''', (product_id,))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error deleting product: {e}")

    def get_all_products(self):
        """Retrieve all products from the inventory."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            return cursor.fetchall()

    def get_product(self, product_id):
        """Retrieve a single product by its ID."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
            return cursor.fetchone()

# Example usage:
if __name__ == "__main__":
    inventory = InventoryManager()

    # Adding products
    inventory.add_product('Hinge Model A', 'Hinges', 100, 2.99)
    inventory.add_product('Lock Model B', 'Locks', 50, 15.50)
    inventory.add_product('Latch Model C', 'Latches', 75, 5.75)

    # Display all products
    print("Current Inventory:")
    for product in inventory.get_all_products():
        print(product)

    # Update a product
    inventory.update_product(1, 120)

    # Get details of a single product
    product = inventory.get_product(1)
    print("Updated Product:", product)

    # Delete a product
    inventory.delete_product(2)

    print("Inventory after deletion:")
    for product in inventory.get_all_products():
        print(product)
```
