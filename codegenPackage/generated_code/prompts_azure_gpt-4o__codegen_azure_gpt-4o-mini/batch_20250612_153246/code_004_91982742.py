"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Provide a step-by-step guide to implement a barcode-based inventory management system using DemirSoft's "Market Mağaza Barkodlu Satış Programı."
Generated: DETERMINISTIC_91982742b24b3687
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

# Database helper functions
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to database.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """ Create a table for inventory items """
    try:
        sql_create_inventory_table = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            barcode TEXT NOT NULL UNIQUE,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_inventory_table)
        print("Inventory table created.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_item(conn, name, barcode, quantity, price):
    """ Add a new item to the inventory """
    sql = ''' INSERT INTO inventory(name, barcode, quantity, price)
              VALUES(?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, barcode, quantity, price))
        conn.commit()
        print(f"Item '{name}' added to inventory.")
    except Error as e:
        print(f"Error adding item: {e}")

def update_item(conn, barcode, quantity):
    """ Update the quantity of an existing item in the inventory """
    sql = ''' UPDATE inventory
              SET quantity = ?
              WHERE barcode = ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (quantity, barcode))
        conn.commit()
        print(f"Item with barcode '{barcode}' updated.")
    except Error as e:
        print(f"Error updating item: {e}")

def delete_item(conn, barcode):
    """ Delete an item from the inventory """
    sql = ''' DELETE FROM inventory WHERE barcode = ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (barcode,))
        conn.commit()
        print(f"Item with barcode '{barcode}' deleted.")
    except Error as e:
        print(f"Error deleting item: {e}")

def view_inventory(conn):
    """ View all items in the inventory """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error retrieving inventory: {e}")

# Main function to run the inventory management system
def main():
    database = "inventory.db"  # Database file

    # Create a database connection
    conn = create_connection(database)

    # Create inventory table
    if conn:
        create_table(conn)

        # Example operations
        add_item(conn, "Apple", "1234567890123", 100, 0.50)
        add_item(conn, "Banana", "1234567890124", 150, 0.30)
        view_inventory(conn)
        update_item(conn, "1234567890123", 120)
        delete_item(conn, "1234567890124")
        view_inventory(conn)

        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
