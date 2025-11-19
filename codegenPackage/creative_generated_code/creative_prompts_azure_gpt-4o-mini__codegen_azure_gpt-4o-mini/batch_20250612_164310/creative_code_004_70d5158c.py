"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Construct a SQL query to fetch all bracelet products from a database, ensuring it includes details like price variations for the Hoorainz collection.
Generated: DETERMINISTIC_70d5158cbe4b56a1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def fetch_bracelet_products(collection_name):
    """
    Fetch all bracelet products from the database for a specific collection.

    Args:
        collection_name (str): The name of the collection to filter products.

    Returns:
        list: A list of tuples containing bracelet product details including price variations.
    """
    # Establish a connection to the SQLite database
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Define the SQL query to fetch bracelet products from the specified collection
        query = """
        SELECT 
            p.product_id,
            p.product_name,
            p.description,
            v.price AS price_variation
        FROM 
            products p
        JOIN 
            price_variations v ON p.product_id = v.product_id
        WHERE 
            p.category = 'Bracelet'
            AND p.collection = ?
        """
        
        # Execute the query with the collection name as a parameter
        cursor.execute(query, (collection_name,))
        
        # Fetch all results
        results = cursor.fetchall()

        # Return the fetched product details
        return results

    except sqlite3.Error as e:
        # Handle any errors that occur during the database operation
        print(f"An error occurred: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage: Fetching bracelet products from the Hoorainz collection
bracelet_products = fetch_bracelet_products('Hoorainz')
for product in bracelet_products:
    print(product)
```
