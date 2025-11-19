"""
Generated Code Metadata:
========================
Original URL: https://www.rararaibar.com
Prompt: Write code to create a database schema for storing news articles from the "Rara Raibar" website, including fields for title, date, category, and content.
Generated: DETERMINISTIC_5880541cc2c16550
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- rara_raibar_db_schema.sql

-- Create database for storing news articles
CREATE DATABASE IF NOT EXISTS rara_raibar_db;

-- Use the created database
USE rara_raibar_db;

-- Create table for news articles
CREATE TABLE IF NOT EXISTS news_articles (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    article_date DATE NOT NULL,
    category ENUM('politics', 'sports', 'entertainment', 'technology', 'business') NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create index on category for efficient querying
CREATE INDEX idx_category ON news_articles (category);

-- Create index on article_date for efficient querying
CREATE INDEX idx_article_date ON news_articles (article_date);

-- Stored procedure to insert new news article
DELIMITER //
CREATE PROCEDURE insert_news_article(
    IN p_title VARCHAR(255),
    IN p_article_date DATE,
    IN p_category ENUM('politics', 'sports', 'entertainment', 'technology', 'business'),
    IN p_content TEXT
)
BEGIN
    INSERT INTO news_articles (title, article_date, category, content)
    VALUES (p_title, p_article_date, p_category, p_content);
END//
DELIMITER ;

-- Stored procedure to update existing news article
DELIMITER //
CREATE PROCEDURE update_news_article(
    IN p_id INT,
    IN p_title VARCHAR(255),
    IN p_article_date DATE,
    IN p_category ENUM('politics', 'sports', 'entertainment', 'technology', 'business'),
    IN p_content TEXT
)
BEGIN
    UPDATE news_articles
    SET title = p_title,
        article_date = p_article_date,
        category = p_category,
        content = p_content
    WHERE id = p_id;
END//
DELIMITER ;

-- Stored procedure to delete news article by id
DELIMITER //
CREATE PROCEDURE delete_news_article(
    IN p_id INT
)
BEGIN
    DELETE FROM news_articles
    WHERE id = p_id;
END//
DELIMITER ;
```

```python
# rara_raibar_db_client.py

import mysql.connector
from mysql.connector import Error

class RaraRaibarDBClient:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def insert_news_article(self, title, article_date, category, content):
        try:
            cursor = self.connection.cursor()
            query = "CALL insert_news_article(%s, %s, %s, %s)"
            cursor.execute(query, (title, article_date, category, content))
            self.connection.commit()
            print("News article inserted successfully")
        except Error as e:
            print(f"Error inserting news article: {e}")

    def update_news_article(self, id, title, article_date, category, content):
        try:
            cursor = self.connection.cursor()
            query = "CALL update_news_article(%s, %s, %s, %s, %s)"
            cursor.execute(query, (id, title, article_date, category, content))
            self.connection.commit()
            print("News article updated successfully")
        except Error as e:
            print(f"Error updating news article: {e}")

    def delete_news_article(self, id):
        try:
            cursor = self.connection.cursor()
            query = "CALL delete_news_article(%s)"
            cursor.execute(query, (id,))
            self.connection.commit()
            print("News article deleted successfully")
        except Error as e:
            print(f"Error deleting news article: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    client = RaraRaibarDBClient("localhost", "rara_raibar_db", "username", "password")
    client.connect()
    client.insert_news_article("Example Title", "2022-01-01", "politics", "Example content")
    client.close_connection()
```
