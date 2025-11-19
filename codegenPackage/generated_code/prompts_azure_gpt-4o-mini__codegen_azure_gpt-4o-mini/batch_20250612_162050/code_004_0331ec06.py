"""
Generated Code Metadata:
========================
Original URL: https://365onlinenews.com
Prompt: Construct a query for a database that retrieves the most viewed articles from a news site similar to 365 Online News, including filters for date and category.
Generated: DETERMINISTIC_0331ec061f636981
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

def get_most_viewed_articles(db_path, start_date, end_date, category, limit=10):
    """
    Retrieve the most viewed articles from the news database.

    Parameters:
    db_path (str): Path to the SQLite database.
    start_date (str): Start date for filtering articles (YYYY-MM-DD).
    end_date (str): End date for filtering articles (YYYY-MM-DD).
    category (str): Category to filter articles.
    limit (int): Maximum number of articles to retrieve (default is 10).

    Returns:
    list: A list of tuples containing article data.
    """
    # Validate date format
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Date format should be YYYY-MM-DD") from e

    # Establish a connection to the database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL query to retrieve the most viewed articles
        query = """
        SELECT title, views, publication_date, category
        FROM articles
        WHERE publication_date BETWEEN ? AND ?
        AND category = ?
        ORDER BY views DESC
        LIMIT ?;
        """

        # Execute the query with parameters
        cursor.execute(query, (start_date, end_date, category, limit))
        articles = cursor.fetchall()

        return articles

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    db_path = 'news_database.db'
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    category = 'Technology'
    
    articles = get_most_viewed_articles(db_path, start_date, end_date, category)
    for article in articles:
        print(article)
```
