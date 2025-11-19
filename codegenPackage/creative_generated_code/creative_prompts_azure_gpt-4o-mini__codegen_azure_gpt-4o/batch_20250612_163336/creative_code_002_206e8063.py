"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startec.com.my
Prompt: Write a Python script that retrieves and displays product information from a hardware retailer's database, focusing on features relevant to StarTec Computer System Sdn Bhd.
Generated: DETERMINISTIC_206e8063fc4e2d9d
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import sys

# Constants for the database connection
DATABASE_FILE = 'hardware_retailer.db'

def connect_to_database(db_file):
    """
    Establish a connection to the SQLite database.
    :param db_file: Path to the SQLite database file.
    :return: Connection object or None if connection fails.
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}", file=sys.stderr)
        return None

def fetch_product_information(connection, company_name):
    """
    Fetch product information from the database for the specified company.
    :param connection: SQLite connection object.
    :param company_name: Name of the company to filter products by.
    :return: List of products or empty list if no products found.
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT product_id, product_name, price, features
        FROM products
        WHERE seller_name = ?
        """
        cursor.execute(query, (company_name,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving product information: {e}", file=sys.stderr)
        return []

def display_product_information(products):
    """
    Display product information in a readable format.
    :param products: List of product tuples retrieved from the database.
    """
    if not products:
        print("No products found.")
        return

    print("Product Information:")
    print("-" * 50)
    for product in products:
        product_id, product_name, price, features = product
        print(f"Product ID: {product_id}")
        print(f"Product Name: {product_name}")
        print(f"Price: ${price:.2f}")
        print(f"Features: {features}")
        print("-" * 50)

def main():
    """
    Main function to execute the script logic.
    """
    company_name = "StarTec Computer System Sdn Bhd"

    # Connect to the database
    connection = connect_to_database(DATABASE_FILE)
    if not connection:
        print("Failed to connect to the database. Exiting...", file=sys.stderr)
        return

    try:
        # Retrieve product information for the specified company
        products = fetch_product_information(connection, company_name)

        # Display the product information
        display_product_information(products)

    finally:
        # Ensure the database connection is closed
        connection.close()

if __name__ == "__main__":
    main()
```
