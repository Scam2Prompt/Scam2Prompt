"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Write code to create an e-commerce product catalog for items like "Car Mounts," "Mount Plates," and "3M Sticky Adhesive," using a database schema that supports categories and subcategories as described on the Volport website.
Generated: DETERMINISTIC_62df4486a97a53b6
Batch ID: 20250612_153225
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

# Database connection and creation
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to the database.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables for categories, subcategories, and products
def create_tables(conn):
    """Create the tables for categories, subcategories, and products."""
    try:
        cursor = conn.cursor()
        
        # Create categories table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')
        
        # Create subcategories table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subcategories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
            );
        ''')
        
        # Create products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                subcategory_id INTEGER NOT NULL,
                FOREIGN KEY (subcategory_id) REFERENCES subcategories (id) ON DELETE CASCADE
            );
        ''')
        
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Insert categories into the database
def insert_category(conn, category_name):
    """Insert a new category into the categories table."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO categories (name) VALUES (?);', (category_name,))
        conn.commit()
        print(f"Category '{category_name}' inserted.")
    except Error as e:
        print(f"Error inserting category: {e}")

# Insert subcategories into the database
def insert_subcategory(conn, subcategory_name, category_id):
    """Insert a new subcategory into the subcategories table."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subcategories (name, category_id) VALUES (?, ?);', (subcategory_name, category_id))
        conn.commit()
        print(f"Subcategory '{subcategory_name}' inserted under category ID {category_id}.")
    except Error as e:
        print(f"Error inserting subcategory: {e}")

# Insert products into the database
def insert_product(conn, product_name, description, price, subcategory_id):
    """Insert a new product into the products table."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, description, price, subcategory_id) VALUES (?, ?, ?, ?);', 
                       (product_name, description, price, subcategory_id))
        conn.commit()
        print(f"Product '{product_name}' inserted under subcategory ID {subcategory_id}.")
    except Error as e:
        print(f"Error inserting product: {e}")

# Main function to execute the code
def main():
    database = "ecommerce_catalog.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn is not None:
        # Create tables
        create_tables(conn)
        
        # Insert categories
        insert_category(conn, "Car Accessories")
        insert_category(conn, "Mounts")
        
        # Insert subcategories
        insert_subcategory(conn, "Car Mounts", 1)  # Assuming Car Accessories is category ID 1
        insert_subcategory(conn, "Mount Plates", 2)  # Assuming Mounts is category ID 2
        insert_subcategory(conn, "3M Sticky Adhesive", 2)  # Assuming Mounts is category ID 2
        
        # Insert products
        insert_product(conn, "Universal Car Mount", "A versatile car mount for smartphones.", 19.99, 1)  # Assuming Car Mounts is subcategory ID 1
        insert_product(conn, "Mount Plate", "Plate for mounting devices securely.", 9.99, 2)  # Assuming Mount Plates is subcategory ID 2
        insert_product(conn, "3M Sticky Adhesive", "Strong adhesive for mounting.", 5.99, 3)  # Assuming 3M Sticky Adhesive is subcategory ID 3
        
        # Close the connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
