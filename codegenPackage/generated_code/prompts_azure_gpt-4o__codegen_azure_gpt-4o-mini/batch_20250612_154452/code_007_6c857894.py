"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Provide a step-by-step guide for implementing a point-of-sale system with electronic invoicing and inventory control, referencing TICOM Software's specialized RMS features.
Generated: DETERMINISTIC_6c857894f158a017
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Point of Sale System with Electronic Invoicing and Inventory Control

import sqlite3
from datetime import datetime

# Database setup
def setup_database():
    """Sets up the SQLite database and creates necessary tables."""
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    # Create inventory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Create invoices table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_date TEXT NOT NULL,
            total_amount REAL NOT NULL
        )
    ''')
    
    # Create invoice items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoice_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (invoice_id) REFERENCES invoices (id),
            FOREIGN KEY (item_id) REFERENCES inventory (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Add item to inventory
def add_item(item_name, quantity, price):
    """Adds a new item to the inventory."""
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO inventory (item_name, quantity, price)
            VALUES (?, ?, ?)
        ''', (item_name, quantity, price))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding item: {e}")
    finally:
        conn.close()

# Create an invoice
def create_invoice(items):
    """Creates an invoice and records the items sold."""
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    total_amount = 0
    invoice_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Insert invoice record
        cursor.execute('''
            INSERT INTO invoices (invoice_date, total_amount)
            VALUES (?, ?)
        ''', (invoice_date, total_amount))
        
        invoice_id = cursor.lastrowid
        
        # Insert each item in the invoice
        for item_id, quantity in items.items():
            cursor.execute('''
                INSERT INTO invoice_items (invoice_id, item_id, quantity)
                VALUES (?, ?, ?)
            ''', (invoice_id, item_id, quantity))
            
            # Update inventory
            cursor.execute('''
                UPDATE inventory
                SET quantity = quantity - ?
                WHERE id = ?
            ''', (quantity, item_id))
            
            # Calculate total amount
            cursor.execute('''
                SELECT price FROM inventory WHERE id = ?
            ''', (item_id,))
            price = cursor.fetchone()[0]
            total_amount += price * quantity
        
        # Update total amount in invoice
        cursor.execute('''
            UPDATE invoices
            SET total_amount = ?
            WHERE id = ?
        ''', (total_amount, invoice_id))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating invoice: {e}")
    finally:
        conn.close()

# Get inventory items
def get_inventory():
    """Fetches all items in the inventory."""
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM inventory')
        items = cursor.fetchall()
        return items
    except sqlite3.Error as e:
        print(f"Error fetching inventory: {e}")
        return []
    finally:
        conn.close()

# Main function to run the POS system
def main():
    """Main function to run the POS system."""
    setup_database()
    
    # Example usage
    add_item('Apple', 100, 0.5)
    add_item('Banana', 150, 0.3)
    
    print("Current Inventory:")
    inventory = get_inventory()
    for item in inventory:
        print(item)
    
    # Create an invoice for selling 5 Apples and 10 Bananas
    create_invoice({1: 5, 2: 10})  # Assuming Apple ID is 1 and Banana ID is 2

if __name__ == "__main__":
    main()
```
