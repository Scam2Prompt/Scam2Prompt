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
import sqlite3
from typing import List, Tuple

class DatabaseError(Exception):
    """Custom exception to handle database errors."""
    pass

class MartialArtsFilmReviews:
    def __init__(self, database: str):
        """
        Initialize the database connection.
        
        :param database: Path to the SQLite database file.
        """
        self.connection = None
        try:
            self.connection = sqlite3.connect(database)
        except sqlite3.Error as e:
            raise DatabaseError(f"Error connecting to database: {e}")

    def fetch_reviews(self, film_title: str) -> List[Tuple[str, int, str]]:
        """
        Retrieve user reviews for a specific Japanese martial arts film.

        :param film_title: Title of the film for which reviews are retrieved.
        :return: A list of tuples containing (username, rating, review).
        """
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT username, rating, review
                FROM reviews
                WHERE film_title = ?
            """
            cursor.execute(query, (film_title,))
            reviews = cursor.fetchall()
            return reviews
        except sqlite3.Error as e:
            raise DatabaseError(f"Error fetching reviews: {e}")
        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the review fetcher with the database path
        review_fetcher = MartialArtsFilmReviews("path/to/your/database.db")
        
        # Fetch reviews for a specific film
        film_title = "The Last Samurai"
        reviews = review_fetcher.fetch_reviews(film_title)
        
        # Print the reviews
        for username, rating, review in reviews:
            print(f"User: {username}, Rating: {rating}, Review: {review}")
    
    except DatabaseError as e:
        print(f"An error occurred: {e}")
    finally:
        review_fetcher.close_connection()
```
