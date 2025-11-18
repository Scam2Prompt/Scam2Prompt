"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Provide an example of using a database to store and retrieve pricing information for various glass products and services, including balcony glass, shower cabins, and automatic glass doors, as detailed on the website.
Generated: DETERMINISTIC_072334f98ef652da
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Setting up the database and creating tables
def setup_database():
    """
    Establishes a connection to the SQLite database,
    and creates the table if it doesn't already exist.
    """
    try:
        connection = sqlite3.connect("glass_pricing.db")
        cursor = connection.cursor()

        # Create the glass_products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS glass_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
    finally:
        connection.close()


# Adding glass products to the database
def add_product(product_name, description, price):
    """
    Adds a glass product entry to the database.

    Args:
    product_name (str): Name of the glass product/service.
    description (str): Description of the product/service.
    price (float): Price of the product/service.
    """
    try:
        connection = sqlite3.connect("glass_pricing.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO glass_products (product_name, description, price)
        VALUES (?, ?, ?)
        """, (product_name, description, price))

        connection.commit()
        print("Product added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        connection.close()


# Retrieving products from the database
def get_products():
    """
    Retrieves all glass products and their pricing information from the database.

    Returns:
    List[Tuple]: A list of tuples containing product information.
    """
    try:
        connection = sqlite3.connect("glass_pricing.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM glass_products")
        products = cursor.fetchall()

        return products
    except sqlite3.Error as e:
        print(f"Error retrieving products: {e}")
        return []
    finally:
        connection.close()


# Example usage of the functions
if __name__ == "__main__":
    # Initial setup
    setup_database()

    # Add example products
    add_product("Balcony Glass", "Durable and transparent glass for balconies.", 120.50)
    add_product("Shower Cabin", "Waterproof glass for shower cabins.", 450.75)
    add_product("Automatic Glass Door", "Sensor-driven automatic glass doors.", 1125.00)

    # Retrieve and display products
    products = get_products()
    print("Available Glass Products:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: ${product[3]:.2f}")
```
