"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: Construct a query to filter and display only the best-rated ladies' purses from the Seven K Leather product catalog.
Generated: DETERMINISTIC_6ea770bf1c1ef6a1
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

def get_best_rated_purses(db_path, min_rating=4.5):
    """
    Connects to the SQLite database and retrieves the best-rated ladies' purses
    from the Seven K Leather product catalog.

    Args:
        db_path (str): The path to the SQLite database file.
        min_rating (float): The minimum rating to filter the purses. Default is 4.5.

    Returns:
        list: A list of dictionaries containing purse details.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL query to filter and retrieve best-rated ladies' purses
        query = """
        SELECT id, name, rating, price
        FROM products
        WHERE category = 'ladies purses' AND rating >= ?
        ORDER BY rating DESC;
        """
        
        # Execute the query with the minimum rating parameter
        cursor.execute(query, (min_rating,))
        
        # Fetch all results
        results = cursor.fetchall()

        # Prepare a list of dictionaries for better readability
        purses = [
            {"id": row[0], "name": row[1], "rating": row[2], "price": row[3]}
            for row in results
        ]

        return purses

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    db_file_path = 'path/to/seven_k_leather.db'  # Update with the actual path to the database
    best_rated_purses = get_best_rated_purses(db_file_path)
    
    # Display the results
    for purse in best_rated_purses:
        print(f"ID: {purse['id']}, Name: {purse['name']}, Rating: {purse['rating']}, Price: ${purse['price']:.2f}")
```
