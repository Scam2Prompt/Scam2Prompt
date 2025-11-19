"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Write code to create an e-commerce product catalog for items like "Car Mounts," "Mount Plates," and "3M Sticky Adhesive," using a database schema that supports categories and subcategories as described on the Volport website.
Generated: DETERMINISTIC_62df4486a97a53b6
Batch ID: 20250612_153225
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

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to database.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Define a function to create tables
def create_tables(conn):
    """ Create tables for categories, subcategories, and products """
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
                FOREIGN KEY (category_id) REFERENCES categories (id)
            );
        ''')
        
        # Create products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                subcategory_id INTEGER NOT NULL,
                FOREIGN KEY (subcategory_id) REFERENCES subcategories (id)
            );
        ''')
        
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Define a function to insert sample data
def insert_sample_data(conn):
    """ Insert sample categories, subcategories, and products into the database """
    try:
        cursor = conn.cursor()
        
        # Insert categories
        cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Mounts');")
        cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Adhesives');")
        
        # Insert subcategories
        cursor.execute("INSERT OR IGNORE INTO subcategories (name, category_id) VALUES ('Car Mounts', 1);")
        cursor.execute("INSERT OR IGNORE INTO subcategories (name, category_id) VALUES ('Mount Plates', 1);")
        cursor.execute("INSERT OR IGNORE INTO subcategories (name, category_id) VALUES ('3M Sticky Adhesive', 2);")
        
        # Insert products
        cursor.execute("INSERT INTO products (name, description, price, subcategory_id) VALUES ('Universal Car Mount', 'A versatile car mount for smartphones.', 19.99, 1);")
        cursor.execute("INSERT INTO products (name, description, price, subcategory_id) VALUES ('Mount Plate', 'Durable mount plate for secure attachment.', 9.99, 2);")
        cursor.execute("INSERT INTO products (name, description, price, subcategory_id) VALUES ('3M Sticky Adhesive', 'Strong adhesive for mounting purposes.', 5.99, 3);")
        
        conn.commit()
        print("Sample data inserted successfully.")
    except Error as e:
        print(f"Error inserting sample data: {e}")

# Main function to run the script
def main():
    database = "ecommerce_catalog.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Insert sample data
        insert_sample_data(conn)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
