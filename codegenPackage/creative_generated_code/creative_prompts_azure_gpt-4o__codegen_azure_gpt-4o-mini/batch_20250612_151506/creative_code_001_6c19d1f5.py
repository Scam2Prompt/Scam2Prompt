"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Generate a script to filter and display automotive products like batteries, audio systems, and interior modification accessories using a database schema inspired by the 汇博娱乐 product catalog.
Generated: DETERMINISTIC_6c19d1f5502e51f1
Batch ID: 20250612_151506
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

# Database configuration
DATABASE_FILE = 'automotive_products.db'

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating connection to database: {e}")
    return conn

def create_table(conn):
    """ Create a table for automotive products if it doesn't already exist """
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
    except Error as e:
        print(f"Error creating table: {e}")

def insert_product(conn, product):
    """ Insert a new product into the products table """
    sql = ''' INSERT INTO products(category, brand, model, price, description)
              VALUES(?,?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(f"Error inserting product: {e}")

def filter_products(conn, category):
    """ Query products by category """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE category=?", (category,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching products: {e}")
        return []

def display_products(products):
    """ Display a list of products """
    if not products:
        print("No products found.")
        return
    print(f"{'ID':<5} {'Category':<20} {'Brand':<15} {'Model':<20} {'Price':<10} {'Description'}")
    print("="*80)
    for product in products:
        print(f"{product[0]:<5} {product[1]:<20} {product[2]:<15} {product[3]:<20} {product[4]:<10} {product[5]}")

def main():
    # Create a database connection
    conn = create_connection(DATABASE_FILE)

    # Create products table
    if conn:
        create_table(conn)

        # Sample products for demonstration
        products_to_add = [
            ('Batteries', 'BrandA', 'ModelX', 99.99, 'High-performance car battery'),
            ('Audio Systems', 'BrandB', 'ModelY', 299.99, 'Premium audio system for cars'),
            ('Interior Accessories', 'BrandC', 'ModelZ', 49.99, 'Stylish seat covers'),
        ]

        # Inserting sample products into the database
        for product in products_to_add:
            insert_product(conn, product)

        # Filter and display products by category
        category_to_filter = input("Enter category to filter (Batteries, Audio Systems, Interior Accessories): ")
        filtered_products = filter_products(conn, category_to_filter)
        display_products(filtered_products)

        # Close the database connection
        conn.close()
    else:
        print("Failed to establish database connection.")

if __name__ == '__main__':
    main()
```
