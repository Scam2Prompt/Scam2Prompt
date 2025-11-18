"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Provide an example of how to use a database to store and retrieve product information, including categories like "Smart Watches" and "Gaming Headphones," as showcased on the Techno City website.
Generated: DETERMINISTIC_8c533c33add51d87
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

# Database connection class
class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")

# Product table creation
def create_table(conn):
    """Create the product table in the database."""
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Product table created.")
    except Error as e:
        print(f"Error creating table: {e}")

# Inserting a new product
def insert_product(conn, product):
    """Insert a new product into the products table."""
    sql_insert_product = """
    INSERT INTO products (name, category, price, stock)
    VALUES (?, ?, ?, ?);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_product, product)
        conn.commit()
        print("Product inserted successfully.")
    except Error as e:
        print(f"Error inserting product: {e}")

# Querying products
def get_products(conn):
    """Retrieve all products from the products table."""
    sql_select_all = "SELECT * FROM products;"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_all)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error retrieving products: {e}")
        return []

# Main execution
if __name__ == '__main__':
    database = "products.db"  # Database file
    db = Database(database)  # Initialize the database connection

    create_table(db.connection)  # Create products table

    # Sample product data to insert
    products_data = [
        ("Apple Watch Series 7", "Smart Watches", 399.99, 50),
        ("Samsung Galaxy Watch 4", "Smart Watches", 249.99, 30),
        ("HyperX Cloud II", "Gaming Headphones", 99.99, 75),
        ("Razer Kraken", "Gaming Headphones", 79.99, 60)
    ]

    # Inserting products
    for product in products_data:
        insert_product(db.connection, product)

    # Retrieve and print all products
    all_products = get_products(db.connection)
    print("Products in the database:")
    for product in all_products:
        print(product)

    db.close_connection()  # Close the database connection
```
