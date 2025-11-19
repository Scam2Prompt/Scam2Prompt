"""
Generated Code Metadata:
========================
Original URL: https://wahedabdelmajed.com
Prompt: Generate a code snippet that implements a search function for articles on a personal website similar to Dr. Wahed Abdel Majid's, focusing on user queries about freedom and personal development.
Generated: DETERMINISTIC_a48954e6fdce3d1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

class ArticleSearch:
    def __init__(self, db_path: str):
        """
        Initializes the ArticleSearch with a database connection.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = self.create_connection()

    def create_connection(self) -> sqlite3.Connection:
        """
        Creates a database connection to the SQLite database.

        :return: SQLite connection object.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def search_articles(self, query: str) -> List[Tuple[int, str, str]]:
        """
        Searches for articles in the database that match the user query.

        :param query: The search term provided by the user.
        :return: A list of tuples containing article ID, title, and content.
        """
        try:
            cursor = self.connection.cursor()
            # Use parameterized queries to prevent SQL injection
            cursor.execute("SELECT id, title, content FROM articles WHERE content LIKE ? OR title LIKE ?", 
                           (f'%{query}%', f'%{query}%'))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Error executing search query: {e}")
            return []
        finally:
            cursor.close()

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    # Initialize the ArticleSearch with the path to the database
    search = ArticleSearch('articles.db')
    
    # User query for searching articles
    user_query = "freedom and personal development"
    
    # Perform the search
    articles = search.search_articles(user_query)
    
    # Display the search results
    if articles:
        for article in articles:
            print(f"ID: {article[0]}, Title: {article[1]}\nContent: {article[2][:100]}...\n")
    else:
        print("No articles found matching your query.")
    
    # Close the database connection
    search.close_connection()
```
