"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Provide an example of using a database to store and retrieve pricing information for various glass products and services, including balcony glass, shower cabins, and automatic glass doors, as detailed on the website.
Generated: DETERMINISTIC_072334f98ef652da
Batch ID: 20250612_153224
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

# Database connection function
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to SQLite database.")
    except Error as e:
        print(f"Error occurred during connection: {e}")
    return conn

# Function to create a table for glass products
def create_table(conn):
    """ Create a table for storing glass product pricing information. """
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
        print("Products table created or already exists.")
    except Error as e:
        print(f"Error occurred during table creation: {e}")

# Function to insert product pricing information
def insert_product(conn, product_name, price):
    """ Insert a new product into the products table. """
    try:
        sql = """INSERT INTO products(product_name, price)
                 VALUES(?, ?)"""
        cursor = conn.cursor()
        cursor.execute(sql, (product_name, price))
        conn.commit()
        print(f"Inserted product: {product_name} with price: {price}")
    except Error as e:
        print(f"Error occurred during product insertion: {e}")

# Function to retrieve all products and their pricing
def retrieve_products(conn):
    """ Query all rows in the products table. """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        print("Retrieved products:")
        for row in rows:
            print(f"ID: {row[0]}, Product Name: {row[1]}, Price: {row[2]}")
    except Error as e:
        print(f"Error occurred during product retrieval: {e}")

# Main function to execute database operations
def main():
    database = "glass_products.db"

    # Create a database connection
    conn = create_connection(database)

    # Create products table
    if conn:
        create_table(conn)

        # Insert sample products
        insert_product(conn, "Balcony Glass", 150.00)
        insert_product(conn, "Shower Cabin", 320.50)
        insert_product(conn, "Automatic Glass Door", 800.00)

        # Retrieve and display products
        retrieve_products(conn)

        # Close the database connection
        conn.close()

if __name__ == '__main__':
    main()
```
