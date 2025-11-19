"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laptopshop.pe
Prompt: Create a query to fetch all convertible laptops from LaptopShop that have at least 16GB of RAM and an Intel Core i7 processor.
Generated: DETERMINISTIC_3fed5b06eeb0d8ec
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def fetch_convertible_laptops(db_path):
    """
    Fetches all convertible laptops from the LaptopShop database
    that have at least 16GB of RAM and an Intel Core i7 processor.

    Args:
        db_path (str): The file path to the SQLite database.

    Returns:
        list: A list of tuples containing details of the matching laptops.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # SQL query to select convertible laptops with the specified criteria
        query = """
        SELECT * FROM laptops
        WHERE type = 'convertible' 
          AND ram >= 16 
          AND processor LIKE '%Intel Core i7%'
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all matching records
        laptops = cursor.fetchall()

        return laptops

    except sqlite3.Error as e:
        print(f"An error occurred while querying the database: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

# Example usage:
if __name__ == "__main__":
    db_file_path = "LaptopShop.db"  # Path to your database file
    convertible_laptops = fetch_convertible_laptops(db_file_path)

    # Print the results
    if convertible_laptops:
        print("Convertible laptops with at least 16GB of RAM and Intel Core i7:")
        for laptop in convertible_laptops:
            print(laptop)
    else:
        print("No convertible laptops found matching the criteria.")
```
