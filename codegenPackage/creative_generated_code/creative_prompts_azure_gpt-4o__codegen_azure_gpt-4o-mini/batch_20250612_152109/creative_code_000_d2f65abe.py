"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a Python script to categorize agricultural products such as "Thuốc trừ sâu," "Thuốc trừ cỏ," and "Phân bón lá" into a database, using product names like "Super Bomb 200EC" and "Nutri 123" as examples.
Generated: DETERMINISTIC_d2f65abef379826a
Batch ID: 20250612_152109
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

# Define the SQLite database connection and setup
DATABASE = 'agriculture_products.db'

# Categories for agricultural products
CATEGORIES = {
    "pesticide": ["Thuốc trừ sâu"],
    "herbicide": ["Thuốc trừ cỏ"],
    "fertilizer": ["Phân bón lá"]
}

# Sample products for testing
PRODUCTS = [
    ("Super Bomb 200EC", "Thuốc trừ sâu"),
    ("Nutri 123", "Phân bón lá"),
    ("Weed Away", "Thuốc trừ cỏ"),
    ("Plant Booster", "Phân bón lá"),
    ("Pest Control Max", "Thuốc trừ sâu"),
]

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table for storing agricultural products."""
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
    except Error as e:
        print(f"Error creating table: {e}")

def insert_product(conn, product):
    """Insert a new product into the products table."""
    sql = ''' INSERT INTO products(name, category)
              VALUES(?, ?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(f"Error inserting product {product[0]}: {e}")

def categorize_products(conn, products):
    """Categorize and insert products into the database based on their category."""
    for product_name, category in products:
        # Ensure category is valid before insertion
        for cat, aliases in CATEGORIES.items():
            if category in aliases:
                insert_product(conn, (product_name, cat))
                break
        else:
            print(f"Warning: Category '{category}' for product '{product_name}' is not recognized.")

def main():
    """Main function to run the categorization and insertion process."""
    conn = create_connection(DATABASE)

    if conn is not None:
        create_table(conn)  # Create products table
        categorize_products(conn, PRODUCTS)  # Categorize and insert products
        conn.close()  # Close the database connection
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
