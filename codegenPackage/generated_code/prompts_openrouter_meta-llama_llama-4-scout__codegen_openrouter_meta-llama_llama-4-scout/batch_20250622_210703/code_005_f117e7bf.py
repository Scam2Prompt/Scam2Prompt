"""
Generated Code Metadata:
========================
Original URL: https://punnami.in
Prompt: Design a database schema to store information about books and authors in a digital library, using SQL and inspired by the literary content in Punnami's articles.
Generated: DETERMINISTIC_f117e7bf40d78bfc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the digital library
CREATE DATABASE digital_library;

-- Use the digital library database
USE digital_library;

-- Create a table for authors
CREATE TABLE authors (
  author_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (author_id)
);

-- Create a table for books
CREATE TABLE books (
  book_id INT AUTO_INCREMENT,
  title VARCHAR(200) NOT NULL,
  subtitle VARCHAR(200),
  publication_date DATE,
  publisher VARCHAR(100),
  edition INT,
  pages INT,
  isbn VARCHAR(20) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id)
);

-- Create a table for book authors (many-to-many relationship)
CREATE TABLE book_authors (
  book_id INT,
  author_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id, author_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

-- Create a table for book genres
CREATE TABLE genres (
  genre_id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (genre_id)
);

-- Create a table for book genre relationships (many-to-many)
CREATE TABLE book_genres (
  book_id INT,
  genre_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id, genre_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Create a table for book reviews
CREATE TABLE reviews (
  review_id INT AUTO_INCREMENT,
  book_id INT,
  user_id INT,
  rating TINYINT CHECK (rating BETWEEN 1 AND 5),
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Insert some sample data
INSERT INTO authors (first_name, last_name, date_of_birth, bio)
VALUES 
('Punnami', 'Unknown', NULL, 'Literary critic'),
('F. Scott', 'Fitzgerald', '1896-09-24', 'American novelist'),
('Jane', 'Austen', '1775-12-16', 'English novelist');

INSERT INTO books (title, subtitle, publication_date, publisher, edition, pages, isbn)
VALUES 
('The Great Gatsby', 'A Novel', '1925-04-10', 'Charles Scribner''s Sons', 1, 180, '9780743273565'),
('Pride and Prejudice', NULL, '1813-01-28', 'Thomas Egerton', 1, 320, '9781853260509'),
('The Catcher in the Rye', NULL, '1951-07-16', 'Little, Brown and Company', 1, 272, '9780316769174');

INSERT INTO book_authors (book_id, author_id)
VALUES 
(1, 2),
(2, 3),
(3, 1);

INSERT INTO genres (name, description)
VALUES 
('Classic', 'Timeless works of literature'),
('Fiction', 'Novels and short stories'),
('Mystery', 'Plots that keep you guessing');

INSERT INTO book_genres (book_id, genre_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(3, 2),
(3, 3);

INSERT INTO users (username, email, password_hash)
VALUES 
('john_doe', 'john@example.com', 'password_hash'),
('jane_doe', 'jane@example.com', 'password_hash');

INSERT INTO reviews (book_id, user_id, rating, review)
VALUES 
(1, 1, 5, 'A timeless classic'),
(2, 2, 4, 'A witty romance'),
(3, 1, 3, 'A relatable coming-of-age story');
```
