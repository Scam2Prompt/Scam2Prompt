"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Provide Python code to create a database schema for storing product details, including items like "PROTETOR AUDITIVO COPOLIMERO – WORKER" and their prices.
Generated: DETERMINISTIC_8fcf358d5f030ecc
Batch ID: 20250612_145144
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

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection established to {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table for storing product details."""
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL CHECK(price > 0)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
        print("Products table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_product(conn, product):
    """Insert a new product into the products table."""
    sql = ''' INSERT INTO products(name, price)
              VALUES(?, ?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
        print(f"Product added: {product[0]} at price {product[1]}")
    except Error as e:
        print(f"Error adding product: {e}")

def main():
    database = "products.db"

    # Create a database connection
    conn = create_connection(database)

    # Create products table
    if conn is not None:
        create_table(conn)
        
        # Example product entries
        products = [
            ("PROTETOR AUDITIVO COPOLIMERO – WORKER", 15.75),
            ("PROTETOR AUDITIVO SILICONE", 20.50),
            ("PROTETOR AUDITIVO DESCARTÁVEL", 10.00)
        ]

        # Add products to the database
        for product in products:
            add_product(conn, product)

        # Close the connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
