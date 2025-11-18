"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write a script to filter and display products from an e-commerce database based on categories like "гидрокостюмы," "перчатки неопреновые," and "удилища," as seen on acula.com.ua.
Generated: DETERMINISTIC_ed75f1c75722bd5c
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def connect_to_database(db_path):
    """
    Establishes a connection to the SQLite database.

    :param db_path: Path to the SQLite database file
    :return: SQLite connection object
    """
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_products_by_category(connection, categories):
    """
    Fetches products from the database based on the given categories.

    :param connection: SQLite connection object
    :param categories: List of categories to filter products
    :return: List of filtered products
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT *
        FROM products
        WHERE category IN ({})
        """.format(','.join('?' for _ in categories))
        cursor.execute(query, categories)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching products: {e}")
        return []

def display_products(products):
    """
    Displays the list of products.

    :param products: List of products to display
    """
    if not products:
        print("No products found for the selected categories.")
        return

    print("Filtered Products:")
    for product in products:
        # Assume the product table has fields: id, name, price, and category
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Category: {product[3]}")

def main():
    """
    Main function to filter and display products based on categories.
    """
    # Define the path to your database
    db_path = "ecommerce.db"

    # Categories to filter products
    categories = ["гидрокостюмы", "перчатки неопреновые", "удилища"]

    # Connect to the database
    connection = connect_to_database(db_path)
    if not connection:
        return

    # Fetch products based on categories
    products = fetch_products_by_category(connection, categories)

    # Display the filtered products
    display_products(products)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
```
