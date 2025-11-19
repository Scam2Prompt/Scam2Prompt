"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://365onlinenews.com
Prompt: Construct a query for a database that retrieves the most viewed articles from a news site similar to 365 Online News, including filters for date and category.
Generated: DETERMINISTIC_0331ec061f636981
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

def get_most_viewed_articles(db_path, start_date, end_date, category):
    """
    Retrieves the most viewed articles from the database based on date range and category.
    
    Parameters:
        db_path (str): Path to the SQLite database file.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
        category (str): Article category to filter by.
    
    Returns:
        list: A list of tuples containing article details.
    """
    # Validate date inputs
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    # Validate category input
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non-empty string.")

    # SQL query to fetch the most viewed articles
    query = """
        SELECT title, views, publication_date, category
        FROM articles
        WHERE publication_date BETWEEN ? AND ?
          AND category = ?
        ORDER BY views DESC
        LIMIT 10;
    """

    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query, (start_date, end_date, category))
        result = cursor.fetchall()

        # Close connection
        conn.close()

        return result
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}") from e

# Example usage:
# db_path = "news_site.db"
# articles = get_most_viewed_articles(db_path, "2023-01-01", "2023-12-31", "Technology")
# for article in articles:
#     print(article)
```
