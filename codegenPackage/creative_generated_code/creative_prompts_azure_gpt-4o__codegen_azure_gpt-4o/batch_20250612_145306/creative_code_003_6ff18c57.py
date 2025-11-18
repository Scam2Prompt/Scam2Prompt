"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write code to optimize inventory management for fittings and accessories like Phase Conductor Clamps and Connectors, referencing Swamiji Transmission Pvt. Ltd.'s product offerings.
Generated: DETERMINISTIC_6ff18c571958de52
Batch ID: 20250612_145306
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


class InventoryManager:
    """
    A class to manage inventory for fittings and accessories such as 
    Phase Conductor Clamps and Connectors for Swamiji Transmission Pvt. Ltd.
    """

    def __init__(self, db_name="inventory.db"):
        """
        Initializes the InventoryManager and sets up the database connection.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None
        self._connect_db()
        self._setup_tables()

    def _connect_db(self):
        """Connect to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _setup_tables(self):
        """Create necessary tables for inventory management if they don't exist."""
        try:
            with self.connection:
                self.connection.execute("""
                    CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_name TEXT NOT NULL,
                        product_category TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        last_updated TIMESTAMP NOT NULL
                    )
                """)
        except sqlite3.Error as e:
            print(f"Error setting up tables: {e}")
            raise

    def add_product(self, product_name, product_category, quantity):
        """
        Add a new product to the inventory.
        :param product_name: Name of the product.
        :param product_category: Category of the product (e.g., Clamps or Connectors).
        :param quantity: Initial quantity of the product.
        """
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO inventory (product_name, product_category, quantity, last_updated)
                    VALUES (?, ?, ?, ?)
                """, (product_name, product_category, quantity, datetime.now()))
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            raise

    def update_quantity(self, product_name, quantity_change):
        """
        Update the quantity of a product in the inventory.
        :param product_name: Name of the product to update.
        :param quantity_change: Positive or negative integer denoting the change in quantity.
        """
        try:
            with self.connection:
                current_quantity = self.get_quantity(product_name)
                if current_quantity is None:
                    print(f"Product '{product_name}' does not exist in the inventory.")
                    return
                
                new_quantity = current_quantity + quantity_change
                if new_quantity < 0:
                    print(f"Insufficient inventory to reduce '{product_name}' by {abs(quantity_change)} units.")
                    return
                
                self.connection.execute("""
                    UPDATE inventory
                    SET quantity = ?, last_updated = ?
                    WHERE product_name = ?
                """, (new_quantity, datetime.now(), product_name))
        except sqlite3.Error as e:
            print(f"Error updating quantity: {e}")
            raise

    def get_quantity(self, product_name):
        """
        Retrieve the current quantity of a product.
        :param product_name: Name of the product.
        :return: Quantity of the product, or None if the product does not exist.
        """
        try:
            with self.connection:
                cursor = self.connection.execute("""
                    SELECT quantity FROM inventory WHERE product_name = ?
                """, (product_name,))
                result = cursor.fetchone()
                return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Error fetching quantity: {e}")
            raise

    def list_inventory(self):
        """
        List all products in the inventory with their details.
        :return: List of dictionaries containing product details.
        """
        try:
            with self.connection:
                cursor = self.connection.execute("""
                    SELECT product_name, product_category, quantity, last_updated FROM inventory
                """)
                return [
                    {
                        "product_name": row[0],
                        "product_category": row[1],
                        "quantity": row[2],
                        "last_updated": row[3]
                    }
                    for row in cursor.fetchall()
                ]
        except sqlite3.Error as e:
            print(f"Error listing inventory: {e}")
            raise

    def delete_product(self, product_name):
        """
        Delete a product from the inventory.
        :param product_name: Name of the product to delete.
        """
        try:
            with self.connection:
                self.connection.execute("""
                    DELETE FROM inventory WHERE product_name = ?
                """, (product_name,))
        except sqlite3.Error as e:
            print(f"Error deleting product: {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    # Create an inventory manager instance
    inventory = InventoryManager()

    # Adding products
    inventory.add_product("Phase Conductor Clamp", "Clamps", 50)
    inventory.add_product("Connector Type A", "Connectors", 30)

    # Updating quantities
    inventory.update_quantity("Phase Conductor Clamp", -10)  # Reduce by 10 units
    inventory.update_quantity("Connector Type A", 20)       # Add 20 units

    # Listing all products
    print("Current Inventory:")
    for product in inventory.list_inventory():
        print(product)

    # Deleting a product
    inventory.delete_product("Connector Type A")

    # Closing the connection
    inventory.close_connection()
```
