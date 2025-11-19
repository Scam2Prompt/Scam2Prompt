"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sevenkleather.com
Prompt: Construct a query to filter and display only the best-rated ladies' purses from the Seven K Leather product catalog.
Generated: DETERMINISTIC_6ea770bf1c1ef6a1
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def fetch_best_rated_purses(database_path):
    """
    Fetch and display the best-rated ladies' purses from the Seven K Leather product catalog.

    :param database_path: The file path to the SQLite database.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Define the SQL query to get best-rated purses
        query = """
        SELECT product_id, product_name, rating, price
        FROM products
        WHERE category = 'Ladies’ Purses' AND rating = (
            SELECT MAX(rating) FROM products WHERE category = 'Ladies’ Purses'
        )
        ORDER BY rating DESC, price ASC;
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        best_rated_purses = cursor.fetchall()

        # Display results
        print("Best-Rated Ladies' Purses:")
        print("-" * 40)
        for purse in best_rated_purses:
            print(f"ID: {purse[0]}, Name: {purse[1]}, Rating: {purse[2]}, Price: ${purse[3]:.2f}")

    except sqlite3.Error as e:
        # Handle database errors
        print(f"An error occurred while accessing the database: {e}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

# Example usage:
# Specify the path to your SQLite database
database_path = 'seven_k_leather.db'
fetch_best_rated_purses(database_path)
```
