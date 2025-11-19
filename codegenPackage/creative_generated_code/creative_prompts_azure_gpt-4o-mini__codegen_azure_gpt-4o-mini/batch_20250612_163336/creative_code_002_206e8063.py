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
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database successful.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def fetch_product_info(conn, product_id):
    """Fetch product information from the database by product ID."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=?", (product_id,))
        product = cur.fetchone()
        return product
    except Error as e:
        print(f"Error fetching product information: {e}")
        return None

def display_product_info(product):
    """Display product information in a readable format."""
    if product:
        print("\nProduct Information:")
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Description: {product[2]}")
        print(f"Price: ${product[3]:.2f}")
        print(f"Stock: {product[4]}")
        print(f"Category: {product[5]}")
    else:
        print("No product information found.")

def main():
    """Main function to run the script."""
    database = "hardware_retailer.db"  # Specify the path to your database

    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Example product ID to fetch; this should be dynamically set as needed
        product_id = 1
        
        # Fetch and display product information
        product = fetch_product_info(conn, product_id)
        display_product_info(product)
        
        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```
