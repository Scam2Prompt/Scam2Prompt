"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Generate code to build a searchable database for the Homefoods Ghana product catalog, including fields for product name, category, and description.
Generated: DETERMINISTIC_27734c68d1eb27a7
Batch ID: 20250612_154420
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

# Define the database path
DATABASE_PATH = "homefoods_ghana.db"

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """ Create a table for the product catalog """
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
    except Error as e:
        print(f"Error creating table: {e}")

def insert_product(conn, product):
    """ Insert a new product into the products table """
    sql = '''INSERT INTO products(name, category, description)
             VALUES(?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error inserting product: {e}")

def search_products(conn, search_term):
    """ Search for products by name or category """
    sql = '''SELECT * FROM products
             WHERE name LIKE ? OR category LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{search_term}%', f'%{search_term}%'))
        return cursor.fetchall()
    except Error as e:
        print(f"Error searching products: {e}")
        return []

def main():
    # Create a database connection
    conn = create_connection(DATABASE_PATH)

    # Create products table
    if conn:
        create_table(conn)

        # Example of inserting products
        insert_product(conn, ('Tomato', 'Vegetable', 'Fresh tomatoes for cooking'))
        insert_product(conn, ('Rice', 'Grain', 'White rice for meals'))

        # Example of searching for products
        search_results = search_products(conn, 'Rice')
        print("Search Results:")
        for product in search_results:
            print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Description: {product[3]}")

        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
```
