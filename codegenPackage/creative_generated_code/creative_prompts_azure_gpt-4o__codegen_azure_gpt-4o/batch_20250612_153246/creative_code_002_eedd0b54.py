"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Generate code to fetch and display product details, including discounts, for items like "Wireless Headphones" and "Tile Cutting Pliers" from a database, mimicking the structure of the Techno City webpage.
Generated: DETERMINISTIC_eedd0b54d270f5cc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database connection and setup
def get_database_connection():
    """
    Establish a connection to the SQLite database.
    Returns:
        Connection object to interact with the database.
    """
    try:
        connection = sqlite3.connect('techno_city.db')  # Replace with your database path
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def fetch_product_details(product_name):
    """
    Fetch product details including discounts from the database by product name.
    Parameters:
        product_name (str): Name of the product to fetch details for.
    Returns:
        dict: Dictionary containing product details if found, otherwise None.
    """
    try:
        conn = get_database_connection()
        if conn is None:
            return None

        # Prepare and execute the query
        cursor = conn.cursor()
        query = """
        SELECT name, price, discount_percentage, description 
        FROM products 
        WHERE name = ?
        """
        cursor.execute(query, (product_name,))
        result = cursor.fetchone()

        # Close database connection
        conn.close()

        if result:
            # Parse and return the product details
            product_details = {
                'name': result[0],
                'price': result[1],
                'discount_percentage': result[2],
                'description': result[3]
            }
            return product_details
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error while fetching product details: {e}")
        return None

def display_product_details(product_name):
    """
    Display the product details retrieved from the database.
    Parameters:
        product_name (str): Name of the product to display.
    """
    product_details = fetch_product_details(product_name)
    if product_details:
        print("Product Details:")
        print(f"Name: {product_details['name']}")
        print(f"Price: ${product_details['price']:.2f}")
        print(f"Discount: {product_details['discount_percentage']}%")
        print(f"Description: {product_details['description']}")
    else:
        print(f"No details found for product: {product_name}")

# Main runtime logic
if __name__ == "__main__":
    # Products to fetch details for
    products_to_display = ["Wireless Headphones", "Tile Cutting Pliers"]

    for product_name in products_to_display:
        print("-" * 40)
        display_product_details(product_name)
        print("-" * 40)
```

### Notes:
- Ensure that the database `techno_city.db` exists and contains a `products` table with columns: `name`, `price`, `discount_percentage`, and `description`.
- Populate the database with data for products like "Wireless Headphones" and "Tile Cutting Pliers" for testing purposes.
- Adjust the database connection path as needed for your environment.
