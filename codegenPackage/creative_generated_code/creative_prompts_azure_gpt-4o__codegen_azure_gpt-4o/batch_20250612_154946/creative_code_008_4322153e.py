"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Implement a feature in an e-commerce platform to display products with the highest discounts, such as "-50% Perfume Al Wataniah Special Oud Eau de Parfum Unissex 100ml."
Generated: DETERMINISTIC_4322153ed23d7d47
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sqlite3  # For database operations
from typing import List, Tuple

# Database connection setup (assuming a SQLite database with a `products` table)
DB_PATH = 'ecommerce.db'

# Function to fetch products with the highest discounts
def get_top_discounted_products(limit: int = 10) -> List[Tuple[str, str, float, int]]:
    """
    Fetches the top discounted products from the database.
    
    Args:
        limit (int): Number of products to return. Default is 10.
        
    Returns:
        List[Tuple[str, str, float, int]]: A list of tuples containing product name,
                                           product description, discount percentage,
                                           and original price.
    """
    try:
        # Connect to the database
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        
        # Query to fetch the top discounted products
        query = """
        SELECT name, description, 
               ((price - discounted_price) * 100.0 / price) AS discount_percentage, 
               price
        FROM products
        WHERE price > 0 AND discounted_price > 0
        ORDER BY discount_percentage DESC
        LIMIT ?
        """
        
        # Execute the query and fetch the results
        cursor.execute(query, (limit,))
        products = cursor.fetchall()
        
        return products
    
    except sqlite3.Error as e:
        # Error handling for database operations
        print(f"Database error occurred: {str(e)}")
        return []
    
    except Exception as e:
        # General exception handling
        print(f"An unexpected error occurred: {str(e)}")
        return []
    
    finally:
        # Ensure the database connection is closed
        if 'connection' in locals():
            connection.close()

# Example usage
if __name__ == "__main__":
    # Fetch and display the top 10 discounted products
    top_discounted_products = get_top_discounted_products(10)
    
    # Print the products in a readable format
    if top_discounted_products:
        print("Top Discounted Products:")
        for name, description, discount_percentage, price in top_discounted_products:
            print(f"{discount_percentage:.2f}% - {name} - {description} - Original Price: ${price:.2f}")
    else:
        print("No products found or an error occurred.")
```
