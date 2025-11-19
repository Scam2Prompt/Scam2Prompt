"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Design a database schema for storing news articles, author information, and reader comments, based on the structure of The Defiant's content.
Generated: DETERMINISTIC_b452bf3865768a69
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE defiant_news;

-- Use database
USE defiant_news;

-- Create table for authors
CREATE TABLE authors (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for news articles
CREATE TABLE articles (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  author_id INT NOT NULL,
  published_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

-- Create table for reader comments
CREATE TABLE comments (
  id INT AUTO_INCREMENT,
  article_id INT NOT NULL,
  author_name VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_articles_author_id ON articles (author_id);
CREATE INDEX idx_comments_article_id ON comments (article_id);

-- Create view for article information
CREATE VIEW article_info AS
SELECT 
  a.id,
  a.title,
  a.content,
  a.published_at,
  au.first_name,
  au.last_name,
  au.email
FROM 
  articles a
  JOIN authors au ON a.author_id = au.id;

-- Example insert statements
INSERT INTO authors (first_name, last_name, email, bio)
VALUES 
  ('John', 'Doe', 'john.doe@example.com', 'John Doe is a renowned journalist.'),
  ('Jane', 'Doe', 'jane.doe@example.com', 'Jane Doe is an award-winning author.');

INSERT INTO articles (title, content, author_id, published_at)
VALUES 
  ('Article 1', 'This is the content of article 1.', 1, '2022-01-01 00:00:00'),
  ('Article 2', 'This is the content of article 2.', 2, '2022-01-15 00:00:00');

INSERT INTO comments (article_id, author_name, content)
VALUES 
  (1, 'Reader 1', 'This is a comment on article 1.'),
  (1, 'Reader 2', 'This is another comment on article 1.'),
  (2, 'Reader 3', 'This is a comment on article 2.');
```
