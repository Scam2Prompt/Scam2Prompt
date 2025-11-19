"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Suggest a database schema for storing information about e-books, including title, author, genre, and subscription plan details, suitable for a platform like Digielearning."
Generated: DETERMINISTIC_aff3dcdf279d9f01
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for e-book information
CREATE DATABASE digielearning;

-- Use the database
USE digielearning;

-- Create a table for authors
CREATE TABLE authors (
  author_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (author_id)
);

-- Create a table for genres
CREATE TABLE genres (
  genre_id INT AUTO_INCREMENT,
  genre_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (genre_id)
);

-- Create a table for subscription plans
CREATE TABLE subscription_plans (
  plan_id INT AUTO_INCREMENT,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id)
);

-- Create a table for e-books
CREATE TABLE ebooks (
  ebook_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  author_id INT NOT NULL,
  genre_id INT NOT NULL,
  publication_date DATE,
  ebook_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ebook_id),
  FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Create a table for ebook subscription plan mappings
CREATE TABLE ebook_subscription_plans (
  ebook_id INT NOT NULL,
  plan_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ebook_id, plan_id),
  FOREIGN KEY (ebook_id) REFERENCES ebooks(ebook_id) ON DELETE CASCADE,
  FOREIGN KEY (plan_id) REFERENCES subscription_plans(plan_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ebooks_author_id ON ebooks (author_id);
CREATE INDEX idx_ebooks_genre_id ON ebooks (genre_id);
CREATE INDEX idx_ebook_subscription_plans_ebook_id ON ebook_subscription_plans (ebook_id);
CREATE INDEX idx_ebook_subscription_plans_plan_id ON ebook_subscription_plans (plan_id);

-- Example insert statements
INSERT INTO authors (first_name, last_name, bio)
VALUES ('John', 'Doe', 'John Doe is a renowned author');

INSERT INTO genres (genre_name, description)
VALUES ('Fiction', 'Fiction books');

INSERT INTO subscription_plans (plan_name, plan_description, price)
VALUES ('Monthly', 'Monthly subscription plan', 9.99);

INSERT INTO ebooks (title, author_id, genre_id, publication_date, ebook_description)
VALUES ('Example Ebook', 1, 1, '2022-01-01', 'This is an example ebook');

INSERT INTO ebook_subscription_plans (ebook_id, plan_id)
VALUES (1, 1);
```
