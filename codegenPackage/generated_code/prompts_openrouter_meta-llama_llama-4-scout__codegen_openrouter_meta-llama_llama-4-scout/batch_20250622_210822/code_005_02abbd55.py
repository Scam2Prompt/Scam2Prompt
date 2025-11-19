"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Design a database schema to store and manage a large collection of articles, quizzes, and trending posts.
Generated: DETERMINISTIC_02abbd55e54a2320
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the application
CREATE DATABASE content_management;

-- Use the created database
USE content_management;

-- Create a table for articles
CREATE TABLE articles (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  author_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for authors
CREATE TABLE authors (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for quizzes
CREATE TABLE quizzes (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for quiz questions
CREATE TABLE quiz_questions (
  id INT AUTO_INCREMENT,
  quiz_id INT NOT NULL,
  question TEXT NOT NULL,
  option_a VARCHAR(100),
  option_b VARCHAR(100),
  option_c VARCHAR(100),
  option_d VARCHAR(100),
  answer VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);

-- Create a table for trending posts
CREATE TABLE trending_posts (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for article authors (many-to-many relationship)
CREATE TABLE article_authors (
  article_id INT NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY (article_id, author_id),
  FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

-- Create indexes for faster querying
CREATE INDEX idx_articles_author_id ON articles (author_id);
CREATE INDEX idx_quiz_questions_quiz_id ON quiz_questions (quiz_id);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "content_management", "root", "password")
    db.connect()

    # Create tables
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    db.close_connection()
```
