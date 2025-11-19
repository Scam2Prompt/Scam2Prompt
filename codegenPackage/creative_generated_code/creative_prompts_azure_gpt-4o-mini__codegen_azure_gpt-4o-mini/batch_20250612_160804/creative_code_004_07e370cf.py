"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://booksinn.com.pk
Prompt: What are the best practices for implementing a search feature on an online bookstore like Books Inn, specifically for Urdu and Islamic books?
Generated: DETERMINISTIC_07e370cf086396d4
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple, Optional

class BookstoreSearch:
    """A class to handle search functionality for an online bookstore."""

    def __init__(self, db_path: str):
        """
        Initializes the BookstoreSearch with the database path.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        """Establishes a connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def search_books(self, search_term: str, category: Optional[str] = None) -> List[Tuple[int, str, str]]:
        """
        Searches for books in the database by title or author name.

        :param search_term: The term to search for in titles or authors.
        :param category: Optional category filter for the search (e.g., 'Urdu', 'Islamic').
        
        :return: A list of tuples containing book ID, title, and author name.
        """
        results = []
        conn = self.connect()
        cursor = conn.cursor()

        query = "SELECT id, title, author FROM books WHERE (title LIKE ? OR author LIKE ?)"
        params = [f'%{search_term}%', f'%{search_term}%']
        
        if category:
            query += " AND category = ?"
            params.append(category)

        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Search query execution error: {e}")
        finally:
            cursor.close()
            conn.close()

        return results

    def display_results(self, results: List[Tuple[int, str, str]]):
        """
        Displays the search results in a user-friendly format.

        :param results: The list of search results to display.
        """
        if not results:
            print("No books found.")
            return

        print("Search Results:")
        for book_id, title, author in results:
            print(f"ID: {book_id}, Title: '{title}', Author: {author}")

if __name__ == "__main__":
    # Example usage of the BookstoreSearch class
    db_path = "books_inn.db"  # Path to your SQLite database
    search_feature = BookstoreSearch(db_path)

    # Searching for Urdu books related to 'Islam'
    search_term = "Islam"
    category = "Islamic"  # Optional category
    results = search_feature.search_books(search_term, category)
    search_feature.display_results(results)
```
