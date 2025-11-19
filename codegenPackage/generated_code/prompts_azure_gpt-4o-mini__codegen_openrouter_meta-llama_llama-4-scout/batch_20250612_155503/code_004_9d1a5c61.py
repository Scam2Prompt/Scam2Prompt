"""
Generated Code Metadata:
========================
Original URL: https://livesupportdesks.live
Prompt: How do I set up a knowledge base for a live support desk, inspired by the content on livesupportdesks.live?
Generated: DETERMINISTIC_9d1a5c61f89aae07
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# knowledge_base.py

import sqlite3
from typing import Dict, List

class KnowledgeBase:
    """
    A simple knowledge base implementation using SQLite.
    """

    def __init__(self, db_name: str = "knowledge_base.db"):
        """
        Initializes the knowledge base.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the 'articles' table if it doesn't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT NOT NULL
            );
        """)
        self.conn.commit()

    def add_article(self, title: str, content: str, category: str):
        """
        Adds a new article to the knowledge base.

        Args:
            title (str): The title of the article.
            content (str): The content of the article.
            category (str): The category of the article.
        """
        try:
            self.cursor.execute("""
                INSERT INTO articles (title, content, category)
                VALUES (?, ?, ?);
            """, (title, content, category))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding article: {e}")

    def get_articles(self, category: str = None) -> List[Dict]:
        """
        Retrieves a list of articles.

        Args:
            category (str): The category of articles to retrieve.

        Returns:
            List[Dict]: A list of articles, where each article is a dictionary.
        """
        try:
            if category:
                self.cursor.execute("""
                    SELECT * FROM articles
                    WHERE category = ?;
                """, (category,))
            else:
                self.cursor.execute("""
                    SELECT * FROM articles;
                """)
            rows = self.cursor.fetchall()
            articles = []
            for row in rows:
                article = {
                    "id": row[0],
                    "title": row[1],
                    "content": row[2],
                    "category": row[3]
                }
                articles.append(article)
            return articles
        except sqlite3.Error as e:
            print(f"Error retrieving articles: {e}")
            return []

    def get_article(self, article_id: int) -> Dict:
        """
        Retrieves a single article by ID.

        Args:
            article_id (int): The ID of the article.

        Returns:
            Dict: The article, or None if not found.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM articles
                WHERE id = ?;
            """, (article_id,))
            row = self.cursor.fetchone()
            if row:
                article = {
                    "id": row[0],
                    "title": row[1],
                    "content": row[2],
                    "category": row[3]
                }
                return article
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error retrieving article: {e}")
            return None

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()


def main():
    kb = KnowledgeBase()

    # Add some sample articles
    kb.add_article("Article 1", "This is the content of article 1.", "Category A")
    kb.add_article("Article 2", "This is the content of article 2.", "Category B")

    # Retrieve all articles
    articles = kb.get_articles()
    for article in articles:
        print(article["title"])

    # Retrieve a single article
    article = kb.get_article(1)
    if article:
        print(article["title"])
        print(article["content"])

    kb.close()


if __name__ == "__main__":
    main()
```
