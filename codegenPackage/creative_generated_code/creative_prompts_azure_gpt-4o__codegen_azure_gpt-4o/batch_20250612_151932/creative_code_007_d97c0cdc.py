"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registrations-arcium.hq.net
Prompt: Create code to search for products by name, such as "개성고려인삼탕" or "단너삼," and return their category and company information.
Generated: DETERMINISTIC_d97c0cdc9ec96483
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class ProductSearcher:
    def __init__(self, db_path):
        """
        Initialize the ProductSearcher class.
        
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def search_product_by_name(self, product_name):
        """
        Search for a product by name and return its category and company information.
        
        :param product_name: Name of the product to search for.
        :return: A list of dictionaries containing category and company information.
        """
        try:
            # Connect to the database
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Prepare and execute the SQL query
            query = """
                SELECT Category, Company 
                FROM Products 
                WHERE Name = ?
            """
            cursor.execute(query, (product_name,))
            
            # Fetch all matching records
            results = cursor.fetchall()
            
            # Parse the results into a list of dictionaries
            product_info = [
                {"Category": result[0], "Company": result[1]}
                for result in results
            ]

            return product_info
        
        except sqlite3.Error as e:
            # Log and handle database errors
            print(f"Database error occurred: {e}")
            return None
        
        finally:
            # Ensure the database connection is closed
            if connection:
                connection.close()


# Example usage
if __name__ == "__main__":
    # Path to your SQLite database file
    DATABASE_PATH = "products.db"

    # Create an instance of the ProductSearcher
    searcher = ProductSearcher(DATABASE_PATH)

    # Search for a specific product
    product_name = "개성고려인삼탕"
    results = searcher.search_product_by_name(product_name)

    # Print the results
    if results:
        for idx, result in enumerate(results, start=1):
            print(f"Result {idx}: Category - {result['Category']}, Company - {result['Company']}")
    else:
        print("No matching product found.")
```

**Notes:**
- Ensure you have a SQLite database named `products.db` with a table `Products` containing columns `Name`, `Category`, and `Company`.
- Replace `products.db` with the actual path to your database file, and adjust the table/column names as necessary to match your schema.
