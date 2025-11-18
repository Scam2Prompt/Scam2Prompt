"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Recommend a library or API to manage inventory tracking for an online store selling equipment such as "MOTORES NÁUTICO" and "ROCADEIRA A GASOLINA SKIM 5500."
Generated: DETERMINISTIC_0b0940e4fa5f25a2
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for an Online Store
This script uses the `sqlite3` library for inventory tracking.
For a more robust solution, consider using a dedicated library like SQLAlchemy ORM or external APIs like Shopify or WooCommerce APIs.
"""

import sqlite3

# Constants
DATABASE_NAME = "inventory.db"

# Initialize the database
def initialize_database():
    """Create the inventory table if it doesn't already exist."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                product_category TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity >= 0),
                price REAL NOT NULL CHECK(price >= 0.0)
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

# Add a new product
def add_product(product_name, product_category, quantity, price):
    """Add a new product to the inventory."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inventory (product_name, product_category, quantity, price)
            VALUES (?, ?, ?, ?)
        """, (product_name, product_category, quantity, price))

        conn.commit()
        print(f"Product '{product_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        conn.close()

# Update the quantity of an existing product
def update_quantity(product_name, new_quantity):
    """Update the quantity of a specific product."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE inventory
            SET quantity = ?
            WHERE product_name = ?
        """, (new_quantity, product_name))

        if cursor.rowcount == 0:
            print(f"Product '{product_name}' not found.")
        else:
            print(f"Quantity of '{product_name}' updated to {new_quantity}.")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating quantity: {e}")
    finally:
        conn.close()

# Delete a product from inventory
def delete_product(product_name):
    """Delete a product from the inventory."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM inventory
            WHERE product_name = ?
        """, (product_name,))

        if cursor.rowcount == 0:
            print(f"Product '{product_name}' not found.")
        else:
            print(f"Product '{product_name}' deleted successfully.")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting product: {e}")
    finally:
        conn.close()

# Fetch and display all products
def display_inventory():
    """Display the current inventory."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM inventory
        """)
        rows = cursor.fetchall()

        if not rows:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            print("ID | Product Name | Category | Quantity | Price")
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | ${row[4]:.2f}")
    except sqlite3.Error as e:
        print(f"Error fetching inventory: {e}")
    finally:
        conn.close()

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample products
    add_product("MOTORES NÁUTICO", "Equipment", 10, 499.99)
    add_product("ROCADEIRA A GASOLINA SKIM 5500", "Equipment", 15, 299.99)

    # Display inventory
    display_inventory()

    # Update the quantity of a product
    update_quantity("MOTORES NÁUTICO", 12)

    # Display inventory after update
    display_inventory()

    # Delete a product
    delete_product("ROCADEIRA A GASOLINA SKIM 5500")

    # Display inventory after deletion
    display_inventory()
```

This code is a simple inventory management system using SQLite, and it fulfills the requirements outlined above. It provides error handling, comments for clarity, follows Python best practices, and is production-ready for small-scale applications. For larger-scale systems, integration with external APIs or more robust database solutions would be recommended.
