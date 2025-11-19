"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Generate code for a simple database to store and manage product catalogs for a company like CristalesGraf that offers various glass, aluminum, and PVC products."
Generated: DETERMINISTIC_a0c04701bc0b9f6c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

import sqlite3
from typing import Dict, List

class Product:
    def __init__(self, id: int, name: str, material: str, description: str, price: float):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        material (str): Product material (glass, aluminum, or PVC).
        description (str): Product description.
        price (float): Product price.
        """
        self.id = id
        self.name = name
        self.material = material
        self.description = description
        self.price = price

class ProductCatalog:
    def __init__(self, db_name: str):
        """
        Initialize a ProductCatalog object.

        Args:
        db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the products table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY, name TEXT, material TEXT, description TEXT, price REAL)
        ''')
        self.conn.commit()

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        Args:
        product (Product): Product object to add.
        """
        try:
            self.cursor.execute('''
                INSERT INTO products (id, name, material, description, price)
                VALUES (?, ?, ?, ?, ?)
            ''', (product.id, product.name, product.material, product.description, product.price))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def get_product(self, id: int) -> Product:
        """
        Get a product by ID.

        Args:
        id (int): ID of the product to retrieve.

        Returns:
        Product: Product object if found, None otherwise.
        """
        try:
            self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
            row = self.cursor.fetchone()
            if row:
                return Product(*row)
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting product: {e}")
            return None

    def update_product(self, product: Product):
        """
        Update a product in the catalog.

        Args:
        product (Product): Product object to update.
        """
        try:
            self.cursor.execute('''
                UPDATE products
                SET name = ?, material = ?, description = ?, price = ?
                WHERE id = ?
            ''', (product.name, product.material, product.description, product.price, product.id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating product: {e}")

    def delete_product(self, id: int):
        """
        Delete a product from the catalog.

        Args:
        id (int): ID of the product to delete.
        """
        try:
            self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting product: {e}")

    def get_all_products(self) -> List[Product]:
        """
        Get all products in the catalog.

        Returns:
        List[Product]: List of Product objects.
        """
        try:
            self.cursor.execute('SELECT * FROM products')
            rows = self.cursor.fetchall()
            return [Product(*row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting products: {e}")
            return []

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    catalog = ProductCatalog('product_catalog.db')

    # Add some products
    products = [
        Product(1, 'Glass Window', 'glass', 'A standard glass window.', 100.0),
        Product(2, 'Aluminum Door', 'aluminum', 'A sturdy aluminum door.', 200.0),
        Product(3, 'PVC Pipe', 'PVC', 'A PVC pipe for plumbing.', 50.0),
    ]
    for product in products:
        catalog.add_product(product)

    # Get a product
    product = catalog.get_product(1)
    if product:
        print(f"Product {product.id}: {product.name} ({product.material}) - ${product.price:.2f}")

    # Update a product
    product.name = 'Glass Window (Updated)'
    catalog.update_product(product)

    # Get all products
    all_products = catalog.get_all_products()
    print("\nAll Products:")
    for product in all_products:
        print(f"{product.id}: {product.name} ({product.material}) - ${product.price:.2f}")

    # Delete a product
    catalog.delete_product(2)

    # Close the catalog
    catalog.close()


if __name__ == '__main__':
    main()
```
