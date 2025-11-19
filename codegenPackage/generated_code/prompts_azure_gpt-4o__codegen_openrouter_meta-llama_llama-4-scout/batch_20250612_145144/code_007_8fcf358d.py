"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Provide Python code to create a database schema for storing product details, including items like "PROTETOR AUDITIVO COPOLIMERO – WORKER" and their prices.
Generated: DETERMINISTIC_8fcf358d5f030ecc
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database
    specified by db_file

    Args:
        db_file (str): Path to the SQLite database file

    Returns:
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite Database at {db_file}")
        return conn
    except Error as e:
        print(e)

# Function to create table
def create_table(conn, table_name):
    """Create table in the SQLite database

    Args:
        conn (Connection object): Connection to the SQLite database
        table_name (str): Name of the table to create

    Returns:
        None
    """
    sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            );"""
    try:
        c = conn.cursor()
        c.execute(sql)
        print(f"Table {table_name} created successfully")
    except Error as e:
        print(e)

# Function to insert product into table
def insert_product(conn, table_name, product):
    """Insert product into the table

    Args:
        conn (Connection object): Connection to the SQLite database
        table_name (str): Name of the table to insert into
        product (dict): Dictionary containing product details

    Returns:
        None
    """
    sql = f"""INSERT INTO {table_name}(product_name, price, description)
              VALUES (?, ?, ?)"""
    try:
        c = conn.cursor()
        c.execute(sql, (product['product_name'], product['price'], product['description']))
        conn.commit()
        print("Product inserted successfully")
    except Error as e:
        print(e)

# Function to get all products from table
def get_all_products(conn, table_name):
    """Get all products from the table

    Args:
        conn (Connection object): Connection to the SQLite database
        table_name (str): Name of the table to retrieve from

    Returns:
        list: List of products
    """
    sql = f"""SELECT * FROM {table_name}"""
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)

# Main function
def main():
    database = "products.db"
    table_name = "product_details"

    # Create a database connection
    conn = create_connection(database)
    with conn:
        # Create table
        create_table(conn, table_name)

        # Example product
        product = {
            'product_name': "PROTETOR AUDITIVO COPOLIMERO – WORKER",
            'price': 50.00,
            'description': "Auditory protector"
        }

        # Insert product
        insert_product(conn, table_name, product)

        # Get all products
        products = get_all_products(conn, table_name)
        for row in products:
            print(row)

if __name__ == '__main__':
    main()
```
