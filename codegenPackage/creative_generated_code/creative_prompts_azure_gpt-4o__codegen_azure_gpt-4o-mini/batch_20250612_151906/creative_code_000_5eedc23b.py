"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Write code to integrate a custom POS system for managing sales and inventory, referencing features similar to those offered by Conficarnes del Valle.
Generated: DETERMINISTIC_5eedc23b20b5a780
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

class POSSystem:
    def __init__(self, db_name='pos_system.db'):
        """Initialize the POS system with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for sales and inventory."""
        with self.conn:
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
            ''')
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                sale_date TEXT NOT NULL,
                FOREIGN KEY(product_id) REFERENCES Inventory(id)
            )
            ''')

    def add_product(self, product_name: str, quantity: int, price: float):
        """Add a new product to the inventory."""
        try:
            with self.conn:
                self.conn.execute('''
                INSERT INTO Inventory (product_name, quantity, price)
                VALUES (?, ?, ?)
                ''', (product_name, quantity, price))
            print(f'Product {product_name} added successfully.')
        except sqlite3.Error as e:
            print(f'Error adding product: {e}')

    def update_inventory(self, product_id: int, quantity: int):
        """Update the quantity of a product in the inventory."""
        try:
            with self.conn:
                self.conn.execute('''
                UPDATE Inventory
                SET quantity = quantity + ?
                WHERE id = ?
                ''', (quantity, product_id))
            print(f'Product ID {product_id} updated successfully.')
        except sqlite3.Error as e:
            print(f'Error updating inventory: {e}')

    def record_sale(self, product_id: int, quantity: int):
        """Record a sale in the sales table."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT price, quantity FROM Inventory WHERE id = ?', (product_id,))
            product = cursor.fetchone()
            if product is None:
                print(f'Product ID {product_id} not found.')
                return
            price, available_quantity = product
            if quantity > available_quantity:
                print('Insufficient stock for this sale.')
                return

            total_price = price * quantity
            with self.conn:
                cursor.execute('''
                INSERT INTO Sales (product_id, quantity, total_price, sale_date)
                VALUES (?, ?, ?, ?)
                ''', (product_id, quantity, total_price, datetime.now().isoformat()))
                self.update_inventory(product_id, -quantity)  # Update inventory after sale

            print(f'Sale recorded for Product ID {product_id}, Quantity: {quantity}, Total Price: {total_price:.2f}')
        except sqlite3.Error as e:
            print(f'Error recording sale: {e}')

    def get_inventory(self):
        """Fetch and display all products in the inventory."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM Inventory')
            products = cursor.fetchall()
            print("Current Inventory:")
            for product in products:
                print(f'ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]:.2f}')
        except sqlite3.Error as e:
            print(f'Error fetching inventory: {e}')

    def close(self):
        """Close the database connection."""
        self.conn.close()


# Example usage of the POSSystem class
if __name__ == "__main__":
    pos_system = POSSystem()

    # Adding products to the inventory
    pos_system.add_product('Beef', 100, 10.5)
    pos_system.add_product('Chicken', 50, 8.0)

    # Display current inventory
    pos_system.get_inventory()

    # Recording a sale
    pos_system.record_sale(1, 2)  # Sell 2 units of product with ID 1

    # Display updated inventory
    pos_system.get_inventory()

    # Close the POS system
    pos_system.close()
```
