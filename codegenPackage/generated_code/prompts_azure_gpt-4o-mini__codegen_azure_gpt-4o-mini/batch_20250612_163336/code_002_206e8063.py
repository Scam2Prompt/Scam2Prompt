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
from sqlite3 import Error

# Define a function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database established.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Define a function to retrieve product information
def get_product_info(conn, product_id):
    """Retrieve product information from the database based on product_id."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
        product = cursor.fetchone()
        
        if product:
            return {
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": product[3],
                "stock": product[4],
                "features": product[5]
            }
        else:
            print(f"No product found with ID: {product_id}")
            return None
    except Error as e:
        print(f"Error retrieving product information: {e}")
        return None

# Define a function to display product information
def display_product_info(product):
    """Display the product information in a readable format."""
    if product:
        print("Product Information:")
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Description: {product['description']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print(f"Features: {product['features']}")
    else:
        print("No product information to display.")

# Main function to execute the script
def main():
    database = "hardware_retailer.db"  # Path to the database file
    product_id = 1  # Example product ID to retrieve

    # Create a database connection
    conn = create_connection(database)

    # Retrieve and display product information if connection is successful
    if conn:
        product_info = get_product_info(conn, product_id)
        display_product_info(product_info)
        conn.close()  # Close the database connection
    else:
        print("Failed to create database connection.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
