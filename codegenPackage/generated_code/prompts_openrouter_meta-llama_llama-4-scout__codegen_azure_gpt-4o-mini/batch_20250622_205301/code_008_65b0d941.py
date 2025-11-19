"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Create a data model for storing and retrieving information about various metal products, including Nickel 200 Forged Fittings and Alloy Steel Pipes."
Generated: DETERMINISTIC_65b0d941f9b3a15e
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class MetalProduct:
    """Class representing a metal product."""
    
    def __init__(self, product_id, name, material, dimensions, weight):
        self.product_id = product_id
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.weight = weight

class MetalProductDatabase:
    """Class to handle database operations for metal products."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the metal_products table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS metal_products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            material TEXT NOT NULL,
            dimensions TEXT NOT NULL,
            weight REAL NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, product):
        """Insert a new metal product into the database."""
        sql = '''INSERT INTO metal_products(name, material, dimensions, weight)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (product.name, product.material, product.dimensions, product.weight))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding product: {e}")
            return None

    def get_product(self, product_id):
        """Retrieve a metal product by its ID."""
        sql = 'SELECT * FROM metal_products WHERE product_id=?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (product_id,))
            row = cursor.fetchone()
            if row:
                return MetalProduct(*row)
            else:
                print("Product not found.")
                return None
        except Error as e:
            print(f"Error retrieving product: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    db = MetalProductDatabase("metal_products.db")
    
    # Create a new metal product
    nickel_200 = MetalProduct(None, "Nickel 200 Forged Fittings", "Nickel 200", "2 inch", 5.0)
    product_id = db.add_product(nickel_200)
    
    # Retrieve the product
    retrieved_product = db.get_product(product_id)
    if retrieved_product:
        print(f"Retrieved Product: {retrieved_product.name}, Material: {retrieved_product.material}")

    # Close the database connection
    db.close_connection()
```
