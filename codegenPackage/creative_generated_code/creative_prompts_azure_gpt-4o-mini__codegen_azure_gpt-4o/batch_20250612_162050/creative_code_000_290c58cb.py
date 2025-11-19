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
"""
Point of Sale (POS) system integrated with Inventory Management.
This script provides functionalities to process sales and manage inventory for a retail business.

Dependencies:
- Python >= 3.7
- SQLite3 (built-in Python module for database management)

Features:
1. Add items to inventory.
2. Process sales and update inventory.
3. View current inventory.
"""

import sqlite3

# Database setup
DB_NAME = "pos_inventory.db"

def create_tables():
    """
    Creates tables for inventory and sales in the database if they don't exist.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Inventory table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )
        """)

        # Sales table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            total_price REAL NOT NULL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(item_id) REFERENCES inventory(item_id)
        )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        connection.close()


def add_item(item_name, price, quantity):
    """
    Adds a new item to the inventory.

    Args:
    - item_name (str): Name of the item.
    - price (float): Price of the item.
    - quantity (int): Quantity of the item.

    Raises:
    - ValueError: If price or quantity is invalid.
    """
    if price <= 0 or quantity < 0:
        raise ValueError("Price must be positive and quantity must be non-negative.")

    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO inventory (item_name, price, quantity)
        VALUES (?, ?, ?)
        """, (item_name, price, quantity))

        connection.commit()
        print("Item added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding item: {e}")
    finally:
        connection.close()


def process_sale(item_id, quantity):
    """
    Processes a sale and updates inventory.

    Args:
    - item_id (int): ID of the item being sold.
    - quantity (int): Quantity being sold.

    Raises:
    - ValueError: If quantity is invalid or insufficient stock.
    - KeyError: If item_id is not found.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Check stock availability
        cursor.execute("SELECT price, quantity FROM inventory WHERE item_id = ?", (item_id,))
        item = cursor.fetchone()

        if item is None:
            raise KeyError(f"Item with ID {item_id} not found.")
        
        price, stock_quantity = item
        if stock_quantity < quantity:
            raise ValueError("Insufficient stock.")

        # Process sale
        total_price = price * quantity
        cursor.execute("""
        INSERT INTO sales (item_id, quantity, total_price)
        VALUES (?, ?, ?)
        """, (item_id, quantity, total_price))

        # Update inventory
        cursor.execute("""
        UPDATE inventory
        SET quantity = quantity - ?
        WHERE item_id = ?
        """, (quantity, item_id))

        connection.commit()
        print(f"Sale processed successfully. Total Price: ${total_price:.2f}")
    except sqlite3.Error as e:
        print(f"Error processing sale: {e}")
    finally:
        connection.close()


def view_inventory():
    """
    Displays the current inventory.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("SELECT item_id, item_name, price, quantity FROM inventory")
        items = cursor.fetchall()

        if not items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Quantity':<10}")
            print("-" * 45)
            for item_id, item_name, price, quantity in items:
                print(f"{item_id:<5} {item_name:<20} ${price:<10.2f} {quantity:<10}")
    except sqlite3.Error as e:
        print(f"Error viewing inventory: {e}")
    finally:
        connection.close()


# Example usage
if __name__ == "__main__":
    create_tables()  # Ensure necessary tables exist

    # Add sample items to inventory (only run once to avoid duplicates)
    # add_item("Apples", 0.5, 100)
    # add_item("Bananas", 0.3, 150)

    # Process a sample sale
    # process_sale(1, 20)

    # View the inventory
    view_inventory()
```
