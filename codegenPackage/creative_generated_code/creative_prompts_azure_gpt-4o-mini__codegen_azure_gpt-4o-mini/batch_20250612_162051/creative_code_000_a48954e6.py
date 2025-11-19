"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahedabdelmajed.com
Prompt: Generate a code snippet that implements a search function for articles on a personal website similar to Dr. Wahed Abdel Majid's, focusing on user queries about freedom and personal development.
Generated: DETERMINISTIC_a48954e6fdce3d1b
Batch ID: 20250612_162051
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

class ArticleSearch:
    def __init__(self, db_path: str):
        """
        Initialize the ArticleSearch with a path to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = self._create_connection()

    def _create_connection(self) -> sqlite3.Connection:
        """
        Create a database connection to the SQLite database specified by db_path.

        :return: SQLite database connection object.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            print("Connection to SQLite database successful.")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def search_articles(self, query: str) -> List[Tuple[int, str, str]]:
        """
        Search for articles that match the given query.

        :param query: A string containing the search terms.
        :return: A list of tuples containing article ID, title, and content.
        """
        try:
            cursor = self.connection.cursor()
            # Parameterized query to prevent SQL injection
            cursor.execute("SELECT id, title, content FROM articles WHERE content LIKE ? OR title LIKE ?", (f"%{query}%", f"%{query}%"))
            results = cursor.fetchall()
            print(f"Found {len(results)} articles matching the query '{query}'.")
            return results
        except sqlite3.Error as e:
            print(f"Error executing search query: {e}")
            raise
        finally:
            cursor.close()

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    # Please replace 'articles.db' with the actual path to your database
    search = ArticleSearch('articles.db')

    try:
        user_query = input("Enter your search query about freedom or personal development: ")
        articles = search.search_articles(user_query)

        # Display the results
        if articles:
            for article in articles:
                print(f"ID: {article[0]}, Title: {article[1]}\nContent: {article[2][:100]}...\n")  # Display first 100 chars of content
        else:
            print("No articles found.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        search.close_connection()
```
