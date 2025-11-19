"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Construct a query to retrieve user reviews for specific Japanese martial arts films from a database for a site like MEGAMI.
Generated: DETERMINISTIC_c900c90294cdc1dd
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3

def get_reviews_for_japanese_martial_arts_films(database_path, film_ids):
    """
    Retrieves user reviews for specific Japanese martial arts films.

    Args:
        database_path (str): Path to the SQLite database file.
        film_ids (list): List of film IDs to retrieve reviews for.

    Returns:
        list: A list of dictionaries containing film_id, user_id, and review text.
    """
    # Validate inputs
    if not isinstance(film_ids, list) or not all(isinstance(film_id, int) for film_id in film_ids):
        raise ValueError("film_ids must be a list of integers.")

    # Connect to the database
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to connect to the database: {e}")

    try:
        # Construct the query using parameterized SQL to avoid SQL injection
        query = """
            SELECT film_id, user_id, review_text
            FROM user_reviews
            WHERE film_id IN ({placeholders})
        """.format(placeholders=','.join('?' for _ in film_ids))

        # Execute the query
        cursor.execute(query, film_ids)
        
        # Fetch all results
        reviews = cursor.fetchall()

        # Format the results into a list of dictionaries
        formatted_reviews = [
            {"film_id": row[0], "user_id": row[1], "review_text": row[2]}
            for row in reviews
        ]

        return formatted_reviews
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to execute query: {e}")
    finally:
        # Ensure the connection is closed
        connection.close()

# Example usage
if __name__ == "__main__":
    try:
        database_path = "megami.db"
        film_ids = [101, 102, 103]  # Replace with actual film IDs
        reviews = get_reviews_for_japanese_martial_arts_films(database_path, film_ids)
        print(reviews)  # Display the retrieved reviews
    except Exception as e:
        print(f"An error occurred: {e}")
```
