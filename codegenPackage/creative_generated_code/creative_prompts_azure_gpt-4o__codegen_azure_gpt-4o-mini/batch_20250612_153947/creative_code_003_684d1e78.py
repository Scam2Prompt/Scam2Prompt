"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Create a script to categorize research products (e.g., peptides, bioregulators, creams, vials) into a database for a chemical supplier, referencing the structure used on BioLongevity Labs.
Generated: DETERMINISTIC_684d1e78fd0fb825
Batch ID: 20250612_153947
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

# Define the ResearchProduct class to represent each product
class ResearchProduct:
    def __init__(self, product_id, name, category, description, price):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name                # Name of the product
        self.category = category        # Category of the product (e.g., peptides, creams)
        self.description = description  # Description of the product
        self.price = price              # Price of the product

# Function to create a connection to the SQLite database
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database established.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create the Products table
def create_table(conn):
    """ Create the Products table if it doesn't exist. """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        );"""
        conn.execute(sql_create_table)
        print("Products table created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to insert a new product into the Products table
def insert_product(conn, product):
    """ Insert a new product into the Products table. """
    sql_insert_product = """
    INSERT INTO Products (name, category, description, price)
    VALUES (?, ?, ?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_product, (product.name, product.category, product.description, product.price))
        conn.commit()  # Commit the changes
        print(f"Product '{product.name}' added to the database.")
    except Error as e:
        print(f"Error inserting product: {e}")

# Function to categorize and add research products to the database
def categorize_and_add_products(conn, products):
    """ Categorize and add each product to the database. """
    for product in products:
        insert_product(conn, product)

# Main function to demonstrate functionality
def main():
    database = "chemical_supplier.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create the Products table
        create_table(conn)

        # Example list of research products
        products = [
            ResearchProduct(1, "Peptide A", "Peptides", "Description of Peptide A", 150.00),
            ResearchProduct(2, "Bioregulator B", "Bioregulators", "Description of Bioregulator B", 200.00),
            ResearchProduct(3, "Cream C", "Creams", "Description of Cream C", 50.00),
            ResearchProduct(4, "Vial D", "Vials", "Description of Vial D", 75.00),
        ]

        # Categorize and add products to the database
        categorize_and_add_products(conn, products)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
```
