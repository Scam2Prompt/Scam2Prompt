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
import datetime
from typing import List, Dict

# Define a class for the database query
class NewsQuery:
    def __init__(self, db_connection):
        """
        Initialize the NewsQuery class.

        Args:
        db_connection: A connection object to the database.
        """
        self.db_connection = db_connection

    def get_most_viewed_articles(self, 
                               start_date: datetime.date = None, 
                               end_date: datetime.date = None, 
                               category: str = None, 
                               limit: int = 10) -> List[Dict]:
        """
        Retrieve the most viewed articles from the database.

        Args:
        start_date (datetime.date): The start date for filtering articles. Defaults to None.
        end_date (datetime.date): The end date for filtering articles. Defaults to None.
        category (str): The category for filtering articles. Defaults to None.
        limit (int): The number of articles to retrieve. Defaults to 10.

        Returns:
        List[Dict]: A list of dictionaries containing the article information.
        """

        # Create a cursor object to execute SQL queries
        cursor = self.db_connection.cursor()

        # Define the base query
        query = """
            SELECT 
                a.id, 
                a.title, 
                a.content, 
                a.category, 
                a.views, 
                a.publish_date
            FROM 
                articles a
            """

        # Define conditions for the query
        conditions = []
        params = []

        # Add date filter if provided
        if start_date:
            conditions.append("a.publish_date >= ?")
            params.append(start_date)
        if end_date:
            conditions.append("a.publish_date <= ?")
            params.append(end_date)

        # Add category filter if provided
        if category:
            conditions.append("a.category = ?")
            params.append(category)

        # Add conditions to the query
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Order by views in descending order and limit the results
        query += " ORDER BY a.views DESC LIMIT ?"
        params.append(limit)

        try:
            # Execute the query
            cursor.execute(query, params)

            # Fetch all rows from the query
            rows = cursor.fetchall()

            # Create a list of dictionaries with article information
            articles = [
                {
                    "id": row[0],
                    "title": row[1],
                    "content": row[2],
                    "category": row[3],
                    "views": row[4],
                    "publish_date": row[5]
                } for row in rows
            ]

            return articles

        except Exception as e:
            # Handle any exceptions that occur during query execution
            print(f"An error occurred: {e}")
            return []

        finally:
            # Close the cursor object
            cursor.close()


# Example usage
if __name__ == "__main__":
    import sqlite3

    # Establish a connection to the database
    connection = sqlite3.connect("news.db")

    # Create a NewsQuery object
    news_query = NewsQuery(connection)

    # Retrieve the most viewed articles
    articles = news_query.get_most_viewed_articles(
        start_date=datetime.date(2022, 1, 1), 
        end_date=datetime.date(2022, 12, 31), 
        category="politics", 
        limit=5
    )

    # Print the articles
    for article in articles:
        print(article)

    # Close the database connection
    connection.close()
```
