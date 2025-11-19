"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: Write a Python script that retrieves and displays product information from a hardware retailer's database, focusing on features relevant to StarTec Computer System Sdn Bhd.
Generated: DETERMINISTIC_206e8063fc4e2d9d
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class HardwareRetailerDB:
    """
    A class to interact with a hardware retailer's database to retrieve product information.
    This is tailored for StarTec Computer System Sdn Bhd's requirements.
    """

    def __init__(self, db_path: str = 'hardware_retailer.db'):
        """
        Initialize the database connection.

        Args:
            db_path (str): Path to the SQLite database file. Defaults to 'hardware_retailer.db'.
        """
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Context manager entry: establish database connection."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit: ensure connection is closed."""
        self.close()

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Access columns by name
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to connect to database: {e}")

    def close(self):
        """Close the database connection if it's open."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def get_products_by_category(self, category: str) -> List[Dict]:
        """
        Retrieve all products in a specific category.

        Args:
            category (str): The product category to filter by.

        Returns:
            List[Dict]: A list of product dictionaries with their details.

        Raises:
            RuntimeError: If there's a database error during the query.
        """
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                SELECT product_id, name, description, price, stock_quantity, category
                FROM products
                WHERE category = ?
                ORDER BY name
                """,
                (category,)
            )
            products = [dict(row) for row in cursor.fetchall()]
            return products
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error while fetching products: {e}")

    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """
        Retrieve a single product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Optional[Dict]: The product details as a dictionary, or None if not found.

        Raises:
            RuntimeError: If there's a database error during the query.
        """
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                SELECT product_id, name, description, price, stock_quantity, category
                FROM products
                WHERE product_id = ?
                """,
                (product_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error while fetching product: {e}")

    def display_products(self, products: List[Dict]):
        """
        Display product information in a user-friendly format.

        Args:
            products (List[Dict]): List of product dictionaries to display.
        """
        if not products:
            print("No products found.")
            return

        for product in products:
            print(f"\nProduct ID: {product['product_id']}")
            print(f"Name: {product['name']}")
            print(f"Description: {product['description']}")
            print(f"Price: RM{product['price']:.2f}")
            print(f"Stock Quantity: {product['stock_quantity']}")
            print(f"Category: {product['category']}")
            print("-" * 40)

def main():
    """
    Main function to demonstrate retrieving and displaying product information.
    """
    try:
        with HardwareRetailerDB() as db:
            print("Fetching computer hardware products...")
            computer_products = db.get_products_by_category("Computer Hardware")
            db.display_products(computer_products)

            print("\nFetching details for product ID 101...")
            product = db.get_product_by_id(101)
            if product:
                db.display_products([product])
            else:
                print("Product not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
