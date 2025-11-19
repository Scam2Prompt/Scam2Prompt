"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixsistemas.site
Prompt: Generate code to integrate a point of sale system with inventory management for a retail business, as described by FIX Sistemas.
Generated: DETERMINISTIC_290c58cb7ddc6de1
Batch ID: 20250612_162050
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

# Database setup: Create tables for inventory and sales
def setup_database():
    conn = sqlite3.connect('retail_business.db')
    cursor = conn.cursor()

    # Create inventory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
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
            sale_date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES inventory (id)
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a new product to the inventory
def add_product(product_name, quantity, price):
    try:
        conn = sqlite3.connect('retail_business.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO inventory (product_name, quantity, price)
            VALUES (?, ?, ?)
        ''', (product_name, quantity, price))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while adding product: {e}")
    finally:
        conn.close()

# Function to process a sale
def process_sale(product_id, quantity_sold):
    try:
        conn = sqlite3.connect('retail_business.db')
        cursor = conn.cursor()

        # Check if there is enough inventory
        cursor.execute('''
            SELECT quantity FROM inventory WHERE id = ?
        ''', (product_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"Product with ID {product_id} does not exist.")
            return
        
        current_quantity = result[0]

        if current_quantity < quantity_sold:
            print(f"Not enough inventory for product ID {product_id}. Available: {current_quantity}, Requested: {quantity_sold}")
            return

        # Deduct the quantity from inventory
        cursor.execute('''
            UPDATE inventory SET quantity = quantity - ? WHERE id = ?
        ''', (quantity_sold, product_id))

        # Record the sale transaction
        sale_date = datetime.now().isoformat()
        cursor.execute('''
            INSERT INTO sales (product_id, quantity_sold, sale_date)
            VALUES (?, ?, ?)
        ''', (product_id, quantity_sold, sale_date))

        conn.commit()
        print(f"Sale processed for Product ID {product_id}: Quantity Sold {quantity_sold}")
    except sqlite3.Error as e:
        print(f"An error occurred while processing sale: {e}")
    finally:
        conn.close()

# Function to view current inventory
def view_inventory():
    try:
        conn = sqlite3.connect('retail_business.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM inventory')
        products = cursor.fetchall()

        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]:.2f}")

    except sqlite3.Error as e:
        print(f"An error occurred while viewing inventory: {e}")
    finally:
        conn.close()

# Initialize the database
setup_database()

# Example use case
if __name__ == "__main__":
    add_product("Widget", 100, 19.99)
    add_product("Gadget", 50, 29.99)
    view_inventory()
    process_sale(1, 10)
    view_inventory()
```
