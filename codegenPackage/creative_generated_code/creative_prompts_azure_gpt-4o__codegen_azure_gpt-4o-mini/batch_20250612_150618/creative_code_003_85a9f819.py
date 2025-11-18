"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Suggest tools or libraries for implementing a search functionality that allows users to filter products by location (e.g., "Lambayeque" or "Lima") as described on "Mass Compras."
Generated: DETERMINISTIC_85a9f81962723236
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Any
import sqlite3

# Database setup for storing product information
def setup_database() -> None:
    """Sets up the SQLite database for storing products."""
    connection = sqlite3.connect('mass_compras.db')
    cursor = connection.cursor()
    
    # Create a table for products if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

# Function to add a product to the database
def add_product(name: str, location: str) -> None:
    """Adds a product to the database.
    
    Args:
        name (str): The name of the product.
        location (str): The location of the product.
    """
    try:
        connection = sqlite3.connect('mass_compras.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO products (name, location) VALUES (?, ?)', (name, location))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while adding a product: {e}")
    finally:
        connection.close()

# Function to search for products by location
def search_products_by_location(location: str) -> List[Dict[str, Any]]:
    """Searches for products in the given location.
    
    Args:
        location (str): The location to filter products by.
    
    Returns:
        List[Dict[str, Any]]: A list of products in the specified location.
    """
    try:
        connection = sqlite3.connect('mass_compras.db')
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, location FROM products WHERE location = ?', (location,))
        products = cursor.fetchall()
        
        # Convert results to a list of dictionaries
        result = [{'id': product[0], 'name': product[1], 'location': product[2]} for product in products]
        return result
    except sqlite3.Error as e:
        print(f"An error occurred while searching for products: {e}")
        return []
    finally:
        connection.close()

# Main function to demonstrate adding and searching products
if __name__ == "__main__":
    setup_database()

    # Adding sample products
    add_product("Product A", "Lima")
    add_product("Product B", "Lambayeque")
    add_product("Product C", "Lima")
    
    # Searching for products in Lima
    products_in_lima = search_products_by_location("Lima")
    print("Products in Lima:", products_in_lima)

    # Searching for products in Lambayeque
    products_in_lambayeque = search_products_by_location("Lambayeque")
    print("Products in Lambayeque:", products_in_lambayeque)
```
