"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Develop a code snippet that connects to the Jai Gurudev Industries database to insert new product entries for their confectionery items.
Generated: DETERMINISTIC_e10cf77bc9d18a64
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mysql.connector
from mysql.connector import Error

def insert_product_into_database(product_name, product_price, product_quantity):
    """
    Inserts a new product into the 'products' table of the Jai Gurudev Industries database.

    Args:
        product_name (str): The name of the product.
        product_price (float): The price of the product.
        product_quantity (int): The quantity of the product.

    Returns:
        None
    """
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host='localhost',                     # Replace with your database host
            database='jai_gurudev_industries',    # Replace with your database name
            user='your_username',                 # Replace with your database username
            password='your_password'              # Replace with your database password
        )

        if connection.is_connected():
            # Prepare an SQL query to insert a new product
            insert_query = """
            INSERT INTO products (product_name, product_price, product_quantity)
            VALUES (%s, %s, %s)
            """
            data = (product_name, product_price, product_quantity)

            # Create a cursor and execute the SQL query
            cursor = connection.cursor()
            cursor.execute(insert_query, data)

            # Commit the transaction
            connection.commit()

            print(f"Product '{product_name}' successfully inserted into the database.")

    except Error as e:
        # Handle database connection or query errors
        print(f"Error occurred while connecting to the database: {e}")

    finally:
        # Ensure the database connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example usage
# Replace the arguments with actual product details
insert_product_into_database("Chocolate Bar", 1.99, 500)
```
