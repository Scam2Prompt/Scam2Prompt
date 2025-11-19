"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drpharmacy.in
Prompt: Write a Python script that utilizes a library for managing customer data and order processing in a pharmacy application.
Generated: DETERMINISTIC_bc345fd0bca37661
Batch ID: 20250612_162519
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

# Constants for database connection
DATABASE = "pharmacy.db"

# Create a connection to the SQLite database
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables for customers and orders
def create_tables(conn):
    """ Create tables for customers and orders in the database """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            );
        """)
        conn.commit()
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a new customer
def add_customer(conn, name, email):
    """ Add a new customer to the database """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"Customer {name} added successfully.")
    except Error as e:
        print(f"Error adding customer: {e}")

# Function to place a new order
def place_order(conn, customer_id, product_name, quantity):
    """ Place a new order for a customer """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (customer_id, product_name, quantity, order_date) VALUES (?, ?, ?, DATE('now'))", 
                       (customer_id, product_name, quantity))
        conn.commit()
        print(f"Order for {quantity} of {product_name} placed successfully.")
    except Error as e:
        print(f"Error placing order: {e}")

# Function to fetch customer orders
def fetch_customer_orders(conn, customer_id):
    """ Fetch all orders for a specific customer """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
        orders = cursor.fetchall()
        return orders
    except Error as e:
        print(f"Error fetching orders: {e}")
        return []

# Main function to execute the pharmacy application logic
def main():
    # Create a database connection
    conn = create_connection(DATABASE)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example usage
        add_customer(conn, "John Doe", "john.doe@example.com")
        add_customer(conn, "Jane Smith", "jane.smith@example.com")
        
        # Assume customer ID 1 exists
        place_order(conn, 1, "Aspirin", 2)
        place_order(conn, 1, "Ibuprofen", 1)

        # Fetch orders for customer ID 1
        orders = fetch_customer_orders(conn, 1)
        print("Orders for customer ID 1:")
        for order in orders:
            print(order)
        
        # Close the database connection
        conn.close()

if __name__ == "__main__":
    main()
```
