"""
Generated Code Metadata:
========================
Original URL: https://claim-originether.org
Prompt: Design a database schema for a multi-language news website.
Generated: DETERMINISTIC_619aa1ba9521bda9
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for multi-language news website
CREATE DATABASE news_website;

-- Use the database
USE news_website;

-- Create table for languages
CREATE TABLE languages (
  id INT AUTO_INCREMENT,
  code VARCHAR(5) NOT NULL,  -- e.g., 'en', 'fr', 'es'
  name VARCHAR(50) NOT NULL,  -- e.g., 'English', 'Français', 'Español'
  PRIMARY KEY (id),
  UNIQUE KEY (code)
);

-- Create table for news categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,  -- e.g., 'Politics', 'Sports', 'Entertainment'
  slug VARCHAR(100) NOT NULL,  -- e.g., 'politics', 'sports', 'entertainment'
  PRIMARY KEY (id),
  UNIQUE KEY (slug)
);

-- Create table for news articles
CREATE TABLE articles (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  category_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for article translations
CREATE TABLE article_translations (
  id INT AUTO_INCREMENT,
  article_id INT NOT NULL,
  language_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE,
  FOREIGN KEY (language_id) REFERENCES languages(id) ON DELETE CASCADE,
  UNIQUE KEY (article_id, language_id)
);

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'moderator', 'user') DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create table for comments
CREATE TABLE comments (
  id INT AUTO_INCREMENT,
  article_id INT NOT NULL,
  user_id INT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for comment translations
CREATE TABLE comment_translations (
  id INT AUTO_INCREMENT,
  comment_id INT NOT NULL,
  language_id INT NOT NULL,
  content TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (comment_id) REFERENCES comments(id) ON DELETE CASCADE,
  FOREIGN KEY (language_id) REFERENCES languages(id) ON DELETE CASCADE,
  UNIQUE KEY (comment_id, language_id)
);
```

```sql
-- example_data.sql

-- Insert example data into languages table
INSERT INTO languages (code, name) VALUES
  ('en', 'English'),
  ('fr', 'Français'),
  ('es', 'Español');

-- Insert example data into categories table
INSERT INTO categories (name, slug) VALUES
  ('Politics', 'politics'),
  ('Sports', 'sports'),
  ('Entertainment', 'entertainment');

-- Insert example data into articles table
INSERT INTO articles (title, content, category_id) VALUES
  ('Example Article', 'This is an example article.', 1);

-- Insert example data into article_translations table
INSERT INTO article_translations (article_id, language_id, title, content) VALUES
  (1, 1, 'Example Article (English)', 'This is an example article in English.'),
  (1, 2, 'Article Exemple (Français)', 'Ceci est un article exemple en Français.'),
  (1, 3, 'Artículo de Ejemplo (Español)', 'Este es un artículo de ejemplo en Español.');

-- Insert example data into users table
INSERT INTO users (username, email, password, role) VALUES
  ('admin', 'admin@example.com', 'password', 'admin'),
  ('moderator', 'moderator@example.com', 'password', 'moderator'),
  ('user', 'user@example.com', 'password', 'user');

-- Insert example data into comments table
INSERT INTO comments (article_id, user_id, content) VALUES
  (1, 1, 'This is an example comment.');

-- Insert example data into comment_translations table
INSERT INTO comment_translations (comment_id, language_id, content) VALUES
  (1, 1, 'This is an example comment in English.'),
  (1, 2, 'Ceci est un commentaire exemple en Français.'),
  (1, 3, 'Este es un comentario de ejemplo en Español.');
```
