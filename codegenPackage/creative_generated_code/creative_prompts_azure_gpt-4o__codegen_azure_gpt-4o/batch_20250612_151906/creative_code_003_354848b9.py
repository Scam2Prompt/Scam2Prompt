"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Create a program to track and manage inventory for products like valves, flanges, and drilling equipment, using Cedar International Inc.'s procurement strategy as a model.
Generated: DETERMINISTIC_354848b9ff61f046
Batch ID: 20250612_151906
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

# Constants for products and categories
PRODUCT_CATEGORIES = ["Valves", "Flanges", "Drilling Equipment"]

# Database setup
DB_NAME = "inventory.db"

class InventoryManager:
    def __init__(self):
        """Initialize the inventory manager and set up the database."""
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        self._setup_database()

    def _setup_database(self):
        """Create necessary tables if they do not exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_per_unit REAL NOT NULL,
            last_updated TIMESTAMP NOT NULL
        )
        """)
        self.connection.commit()

    def add_product(self, name, category, quantity, price_per_unit):
        """Add a new product to the inventory."""
        if category not in PRODUCT_CATEGORIES:
            raise ValueError(f"Invalid category. Valid categories are: {PRODUCT_CATEGORIES}")
        
        self.cursor.execute("""
        INSERT INTO products (name, category, quantity, price_per_unit, last_updated)
        VALUES (?, ?, ?, ?, ?)
        """, (name, category, quantity, price_per_unit, datetime.now()))
        self.connection.commit()
        print(f"Product '{name}' added successfully.")

    def update_product_quantity(self, product_id, new_quantity):
        """Update the quantity of a specific product."""
        self.cursor.execute("""
        UPDATE products
        SET quantity = ?, last_updated = ?
        WHERE id = ?
        """, (new_quantity, datetime.now(), product_id))
        if self.cursor.rowcount == 0:
            print("No product found with the given ID.")
        else:
            self.connection.commit()
            print(f"Product ID {product_id} quantity updated to {new_quantity}.")

    def delete_product(self, product_id):
        """Remove a product from the inventory."""
        self.cursor.execute("""
        DELETE FROM products
        WHERE id = ?
        """, (product_id,))
        if self.cursor.rowcount == 0:
            print("No product found with the given ID.")
        else:
            self.connection.commit()
            print(f"Product ID {product_id} deleted from inventory.")

    def list_products(self):
        """List all products in the inventory."""
        self.cursor.execute("""
        SELECT id, name, category, quantity, price_per_unit, last_updated
        FROM products
        """)
        products = self.cursor.fetchall()
        if not products:
            print("No products found in inventory.")
        else:
            print("Inventory:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, "
                      f"Quantity: {product[3]}, Price per Unit: ${product[4]:.2f}, "
                      f"Last Updated: {product[5]}")

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        inventory = InventoryManager()

        # Add some products
        inventory.add_product("Valve A", "Valves", 100, 15.75)
        inventory.add_product("Flange B", "Flanges", 50, 25.50)
        inventory.add_product("Drilling Rig C", "Drilling Equipment", 10, 5000.00)

        # List all products
        inventory.list_products()

        # Update a product's quantity
        inventory.update_product_quantity(1, 120)

        # Delete a product
        inventory.delete_product(3)

        # List products after updates
        inventory.list_products()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        inventory.close()
```
