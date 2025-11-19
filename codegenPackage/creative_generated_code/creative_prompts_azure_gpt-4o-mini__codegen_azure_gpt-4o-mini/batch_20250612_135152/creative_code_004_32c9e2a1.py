"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ullivis.blogspot.com
Prompt: Suggest a library for managing blog posts and user profiles in a web application, similar to features found in Blogger.
Generated: DETERMINISTIC_32c9e2a19ec4366d
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blog_manager.py

import sqlite3
from sqlite3 import Error

class BlogManager:
    """A class to manage blog posts and user profiles."""

    def __init__(self, db_file):
        """Initialize the BlogManager with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            return connection
        except Error as e:
            print(f"Error creating connection: {e}")
        return connection

    def create_tables(self):
        """Create the necessary tables for users and blog posts."""
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""

        create_posts_table = """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_users_table)
            cursor.execute(create_posts_table)
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_user(self, username, email):
        """Add a new user to the database."""
        sql = '''INSERT INTO users (username, email) VALUES (?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (username, email))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding user: {e}")

    def add_post(self, user_id, title, content):
        """Add a new post for a user."""
        sql = '''INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (user_id, title, content))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding post: {e}")

    def get_user_posts(self, user_id):
        """Retrieve all posts for a specific user."""
        sql = '''SELECT * FROM posts WHERE user_id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (user_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving posts: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    db = "blog.db"
    blog_manager = BlogManager(db)

    # Add a user
    user_id = blog_manager.add_user("john_doe", "john@example.com")
    
    # Add a post
    if user_id:
        blog_manager.add_post(user_id, "My First Post", "This is the content of my first post.")

    # Retrieve user's posts
    posts = blog_manager.get_user_posts(user_id)
    print(posts)

    # Close the connection
    blog_manager.close_connection()
```
