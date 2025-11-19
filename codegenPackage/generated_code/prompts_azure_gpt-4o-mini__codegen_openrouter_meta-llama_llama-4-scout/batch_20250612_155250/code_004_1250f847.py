"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Create a script that displays the latest products in a home improvement store, similar to the 'Últimas Unidades' section on Jurunense Home Center."
Generated: DETERMINISTIC_1250f84785c02eac
Batch ID: 20250612_155250
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
from datetime import datetime

# Define a class for Product
class Product:
    def __init__(self, id, name, description, price, created_at):
        """
        Initialize a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            created_at (datetime): Timestamp when the product was created.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.created_at = created_at

# Define a class for ProductDatabase
class ProductDatabase:
    def __init__(self, db_name):
        """
        Initialize a ProductDatabase object.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the 'products' table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, created_at TEXT)
        ''')
        self.conn.commit()

    def insert_product(self, product):
        """
        Insert a product into the database.

        Args:
            product (Product): Product object to insert.
        """
        self.cursor.execute('''
            INSERT INTO products (id, name, description, price, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (product.id, product.name, product.description, product.price, product.created_at))
        self.conn.commit()

    def get_latest_products(self, limit=5):
        """
        Retrieve the latest products from the database.

        Args:
            limit (int): Number of products to retrieve (default: 5).

        Returns:
            list[Product]: List of Product objects.
        """
        self.cursor.execute('''
            SELECT id, name, description, price, created_at
            FROM products
            ORDER BY created_at DESC
            LIMIT ?
        ''', (limit,))
        rows = self.cursor.fetchall()
        return [Product(*row) for row in rows]

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()

# Define a function to display the latest products
def display_latest_products(db_name, limit=5):
    """
    Display the latest products in a home improvement store.

    Args:
        db_name (str): Name of the SQLite database file.
        limit (int): Number of products to display (default: 5).
    """
    db = ProductDatabase(db_name)
    try:
        latest_products = db.get_latest_products(limit)
        print("Últimas Unidades:")
        for i, product in enumerate(latest_products, start=1):
            print(f"{i}. {product.name} - R${product.price:.2f}")
            print(f"Descrição: {product.description}")
            print(f"Data de Cadastro: {product.created_at}")
            print("-" * 30)
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        db.close()

# Example usage
if __name__ == "__main__":
    db_name = "home_improvement.db"

    # Create some sample products
    products = [
        Product(1, "Product A", "This is product A", 19.99, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        Product(2, "Product B", "This is product B", 9.99, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        Product(3, "Product C", "This is product C", 29.99, (datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")),
        Product(4, "Product D", "This is product D", 39.99, (datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")),
        Product(5, "Product E", "This is product E", 49.99, (datetime.now() - datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")),
    ]

    db = ProductDatabase(db_name)
    for product in products:
        db.insert_product(product)
    db.close()

    display_latest_products(db_name)
```
