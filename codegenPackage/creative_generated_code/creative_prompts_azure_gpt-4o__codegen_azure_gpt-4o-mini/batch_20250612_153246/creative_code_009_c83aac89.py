"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Write code to generate a customer management system for tracking orders from private companies, NGOs, government offices, and learning institutions, as described on Sanuri Supplies' site.
Generated: DETERMINISTIC_c83aac89292a086a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

# Constants for database
DATABASE = 'customer_management.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to SQLite")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the orders table if it does not exist."""
    try:
        sql_create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_type TEXT NOT NULL,
            order_date TEXT NOT NULL,
            order_details TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total_amount REAL NOT NULL
        );"""
        conn.execute(sql_create_orders_table)
        print("Orders table created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

def add_order(conn, order):
    """Insert a new order into the orders table."""
    sql = '''INSERT INTO orders(customer_name, customer_type, order_date, order_details, quantity, total_amount)
             VALUES(?,?,?,?,?,?)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, order)
        conn.commit()
        print("Order added successfully")
        return cur.lastrowid
    except Error as e:
        print(f"Error adding order: {e}")
        return None

def get_orders(conn):
    """Fetch all orders from the orders table."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(f"Error retrieving orders: {e}")
        return []

def main():
    # Create a database connection
    conn = create_connection(DATABASE)

    # Create orders table
    if conn:
        create_table(conn)

        # Sample data: Adding orders
        order1 = ('Company A', 'Private Company', '2023-10-01', 'Office Supplies', 10, 150.00)
        order2 = ('NGO B', 'NGO', '2023-10-02', 'Stationery', 5, 75.00)
        
        add_order(conn, order1)
        add_order(conn, order2)

        # Fetch and display all orders
        orders = get_orders(conn)
        print("Orders in the database:")
        for order in orders:
            print(order)

        # Close the database connection
        conn.close()

if __name__ == '__main__':
    main()
```
