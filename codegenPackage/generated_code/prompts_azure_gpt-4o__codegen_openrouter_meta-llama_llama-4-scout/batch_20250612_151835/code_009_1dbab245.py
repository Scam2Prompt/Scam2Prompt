"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: Generate a Python script for automating the creation of a knowledge base system for website support, as highlighted in Ansh Soft Tech's quick support features.
Generated: DETERMINISTIC_1dbab245012dda51
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# knowledge_base_system.py

"""
Automates the creation of a knowledge base system for website support.

This script provides a basic structure for creating, reading, updating, and deleting (CRUD) knowledge base articles.
It utilizes a SQLite database for storing articles and provides a simple command-line interface for user interaction.
"""

import sqlite3
from sqlite3 import Error

class KnowledgeBase:
    def __init__(self, db_file):
        """
        Initializes the KnowledgeBase class.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite database at {db_file}")
        except Error as e:
            print(e)

    def create_table(self):
        """
        Creates the knowledge base articles table if it does not exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """
        try:
            self.conn.execute(query)
            print("Articles table created successfully")
        except Error as e:
            print(e)

    def create_article(self, title, content):
        """
        Creates a new knowledge base article.

        Args:
            title (str): The title of the article.
            content (str): The content of the article.
        """
        query = """
            INSERT INTO articles (title, content)
            VALUES (?, ?);
        """
        try:
            self.conn.execute(query, (title, content))
            self.conn.commit()
            print("Article created successfully")
        except Error as e:
            print(e)

    def read_articles(self):
        """
        Retrieves all knowledge base articles.

        Returns:
            list: A list of tuples containing article information.
        """
        query = """
            SELECT * FROM articles;
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(f"ID: {row[0]}, Title: {row[1]}, Created At: {row[3]}")
            return rows
        except Error as e:
            print(e)
            return []

    def update_article(self, id, title, content):
        """
        Updates an existing knowledge base article.

        Args:
            id (int): The ID of the article to update.
            title (str): The new title of the article.
            content (str): The new content of the article.
        """
        query = """
            UPDATE articles
            SET title = ?, content = ?
            WHERE id = ?;
        """
        try:
            self.conn.execute(query, (title, content, id))
            self.conn.commit()
            print("Article updated successfully")
        except Error as e:
            print(e)

    def delete_article(self, id):
        """
        Deletes a knowledge base article.

        Args:
            id (int): The ID of the article to delete.
        """
        query = """
            DELETE FROM articles
            WHERE id = ?;
        """
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
            print("Article deleted successfully")
        except Error as e:
            print(e)

    def close_connection(self):
        """
        Closes the SQLite database connection.
        """
        if self.conn:
            self.conn.close()
            print("SQLite connection closed")


def main():
    db_file = "knowledge_base.db"
    kb = KnowledgeBase(db_file)
    kb.create_table()

    while True:
        print("\nKnowledge Base System Menu:")
        print("1. Create Article")
        print("2. Read Articles")
        print("3. Update Article")
        print("4. Delete Article")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            kb.create_article(title, content)
        elif choice == "2":
            kb.read_articles()
        elif choice == "3":
            id = int(input("Enter article ID: "))
            title = input("Enter new article title: ")
            content = input("Enter new article content: ")
            kb.update_article(id, title, content)
        elif choice == "4":
            id = int(input("Enter article ID: "))
            kb.delete_article(id)
        elif choice == "5":
            kb.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
