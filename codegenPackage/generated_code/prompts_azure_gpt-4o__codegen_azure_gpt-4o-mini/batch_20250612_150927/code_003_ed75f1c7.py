"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Write a script to filter and display products from an e-commerce database based on categories like "гидрокостюмы," "перчатки неопреновые," and "удилища," as seen on acula.com.ua.
Generated: DETERMINISTIC_ed75f1c75722bd5c
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

# Define a class to handle product filtering from the database
class ProductFilter:
    def __init__(self, db_path: str):
        """Initialize the ProductFilter with the path to the database."""
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        """Establish a connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def fetch_products(self, categories: List[str]) -> List[Tuple[int, str, str]]:
        """
        Fetch products from the database based on the specified categories.

        Args:
            categories (List[str]): A list of product categories to filter by.

        Returns:
            List[Tuple[int, str, str]]: A list of tuples containing product details.
        """
        # Create a connection to the database
        conn = self.connect()
        cursor = conn.cursor()

        # Prepare the SQL query with placeholders for categories
        query = "SELECT id, name, category FROM products WHERE category IN ({})".format(
            ','.join('?' for _ in categories)
        )

        try:
            # Execute the query with the provided categories
            cursor.execute(query, categories)
            products = cursor.fetchall()
            return products
        except sqlite3.Error as e:
            print(f"Error fetching products: {e}")
            return []
        finally:
            # Ensure the connection is closed
            conn.close()

    def display_products(self, products: List[Tuple[int, str, str]]) -> None:
        """
        Display the filtered products in a readable format.

        Args:
            products (List[Tuple[int, str, str]]): A list of product tuples to display.
        """
        if not products:
            print("No products found for the specified categories.")
            return

        print("Filtered Products:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}")

def main():
    # Define the path to the database
    db_path = 'ecommerce.db'
    
    # Define the categories to filter
    categories = ["гидрокостюмы", "перчатки неопреновые", "удилища"]

    # Create an instance of ProductFilter
    product_filter = ProductFilter(db_path)

    # Fetch and display products based on the specified categories
    products = product_filter.fetch_products(categories)
    product_filter.display_products(products)

if __name__ == "__main__":
    main()
```
