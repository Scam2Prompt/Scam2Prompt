"""
Generated Code Metadata:
========================
Original URL: https://fixsistemas.site
Prompt: Generate code to integrate a point of sale system with inventory management for a retail business, as described by FIX Sistemas.
Generated: DETERMINISTIC_290c58cb7ddc6de1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup for inventory and sales
DATABASE_NAME = "retail_system.db"

# Initialize the database
def initialize_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create inventory table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                sku TEXT UNIQUE NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Create sales table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity_sold INTEGER NOT NULL,
                total_price REAL NOT NULL,
                sale_date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES inventory (id)
            )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Add a product to the inventory
def add_product(product_name, sku, quantity, price):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO inventory (product_name, sku, quantity, price)
            VALUES (?, ?, ?, ?)
        ''', (product_name, sku, quantity, price))

        conn.commit()
        print(f"Product '{product_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        conn.close()

# Update inventory after a sale
def update_inventory(product_id, quantity_sold):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Check current stock
        cursor.execute('SELECT quantity FROM inventory WHERE id = ?', (product_id,))
        result = cursor.fetchone()
        if not result:
            print("Product not found in inventory.")
            return

        current_quantity = result[0]
        if current_quantity < quantity_sold:
            print("Insufficient stock for the sale.")
            return

        # Update stock
        new_quantity = current_quantity - quantity_sold
        cursor.execute('UPDATE inventory SET quantity = ? WHERE id = ?', (new_quantity, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating inventory: {e}")
    finally:
        conn.close()

# Record a sale
def record_sale(product_id, quantity_sold):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Get product details
        cursor.execute('SELECT price FROM inventory WHERE id = ?', (product_id,))
        result = cursor.fetchone()
        if not result:
            print("Product not found in inventory.")
            return

        price_per_unit = result[0]
        total_price = price_per_unit * quantity_sold
        sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert sale record
        cursor.execute('''
            INSERT INTO sales (product_id, quantity_sold, total_price, sale_date)
            VALUES (?, ?, ?, ?)
        ''', (product_id, quantity_sold, total_price, sale_date))

        conn.commit()
        print(f"Sale recorded successfully. Total price: ${total_price:.2f}")

        # Update inventory
        update_inventory(product_id, quantity_sold)
    except sqlite3.Error as e:
        print(f"Error recording sale: {e}")
    finally:
        conn.close()

# View inventory
def view_inventory():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM inventory')
        rows = cursor.fetchall()

        print("Inventory:")
        for row in rows:
            print(f"ID: {row[0]}, Product: {row[1]}, SKU: {row[2]}, Quantity: {row[3]}, Price: ${row[4]:.2f}")
    except sqlite3.Error as e:
        print(f"Error viewing inventory: {e}")
    finally:
        conn.close()

# View sales
def view_sales():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM sales')
        rows = cursor.fetchall()

        print("Sales:")
        for row in rows:
            print(f"ID: {row[0]}, Product ID: {row[1]}, Quantity Sold: {row[2]}, Total Price: ${row[3]:.2f}, Date: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error viewing sales: {e}")
    finally:
        conn.close()

# Main function for testing
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_product("Laptop", "SKU123", 10, 999.99)
    add_product("Mouse", "SKU124", 50, 19.99)

    view_inventory()

    record_sale(1, 2)  # Selling 2 laptops
    record_sale(2, 5)  # Selling 5 mice

    view_inventory()
    view_sales()
```
