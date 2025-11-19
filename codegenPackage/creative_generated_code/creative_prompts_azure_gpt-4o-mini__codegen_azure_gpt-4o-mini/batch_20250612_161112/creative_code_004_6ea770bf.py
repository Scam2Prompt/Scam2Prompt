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

# Database connection configuration
DATABASE_NAME = 'seven_k_leather.db'

def get_best_rated_purses(min_rating=4.5):
    """
    Retrieve the best-rated ladies' purses from the Seven K Leather product catalog.

    Args:
        min_rating (float): The minimum rating to filter the purses. Default is 4.5.

    Returns:
        list: A list of dictionaries containing purse information with ratings above the specified minimum.
    """
    try:
        # Establish a database connection
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # SQL query to filter best-rated ladies' purses
        query = """
        SELECT id, name, description, price, rating
        FROM products
        WHERE category = 'ladies_purses' AND rating >= ?
        ORDER BY rating DESC;
        """
        
        # Execute the query with parameterized input
        cursor.execute(query, (min_rating,))
        results = cursor.fetchall()

        # Prepare the result in a more readable format
        best_rated_purses = []
        for row in results:
            purse = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'price': row[3],
                'rating': row[4]
            }
            best_rated_purses.append(purse)

        return best_rated_purses

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return []

    finally:
        # Ensure that the database connection is closed
        if connection:
            connection.close()

# Example usage
if __name__ == '__main__':
    best_purses = get_best_rated_purses()
    if best_purses:
        print("Best Rated Ladies' Purses:")
        for purse in best_purses:
            print(f"ID: {purse['id']}, Name: {purse['name']}, Price: ${purse['price']}, Rating: {purse['rating']}")
    else:
        print("No best-rated purses found.")
```
