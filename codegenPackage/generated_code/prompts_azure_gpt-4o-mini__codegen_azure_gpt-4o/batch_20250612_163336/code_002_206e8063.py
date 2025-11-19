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

def connect_to_database(db_name):
    """
    Connects to the SQLite database.
    :param db_name: Name of the database file.
    :return: Connection object.
    """
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_product_information(connection, company_name):
    """
    Fetches product information from the database for the specified company.
    :param connection: SQLite connection object.
    :param company_name: Name of the company to filter products.
    :return: List of product information.
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT product_id, product_name, price, stock_quantity, features
        FROM products
        WHERE company_name = ?
        """
        cursor.execute(query, (company_name,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching product information: {e}")
        return []

def display_product_information(products):
    """
    Displays product information in a readable format.
    :param products: List of product information tuples.
    """
    if not products:
        print("No products found.")
        return

    print(f"{'Product ID':<15}{'Product Name':<30}{'Price':<10}{'Stock':<10}{'Features':<50}")
    print("-" * 115)
    for product in products:
        product_id, product_name, price, stock_quantity, features = product
        print(f"{product_id:<15}{product_name:<30}{price:<10}{stock_quantity:<10}{features:<50}")

def main():
    """
    Main function to retrieve and display product information for StarTec Computer System Sdn Bhd.
    """
    # Database file name
    db_name = "hardware_retailer.db"
    
    # Company name to filter products
    company_name = "StarTec Computer System Sdn Bhd"
    
    # Connect to the database
    connection = connect_to_database(db_name)
    if not connection:
        return
    
    # Fetch product information
    products = fetch_product_information(connection, company_name)
    
    # Display product information
    display_product_information(products)
    
    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
```
