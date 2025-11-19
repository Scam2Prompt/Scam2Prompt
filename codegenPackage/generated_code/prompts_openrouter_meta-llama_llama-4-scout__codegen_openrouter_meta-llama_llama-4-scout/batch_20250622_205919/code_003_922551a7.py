"""
Generated Code Metadata:
========================
Original URL: https://thebookcompany.org
Prompt: "Design a database schema to store information about books, authors, and publishing services for a company like The Book Company."
Generated: DETERMINISTIC_922551a7a679ed02
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for The Book Company
CREATE DATABASE the_book_company;

-- Use the database
USE the_book_company;

-- Create table for authors
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

-- Create table for publishing services
CREATE TABLE publishing_services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for books
CREATE TABLE books (
  book_id INT AUTO_INCREMENT,
  title VARCHAR(200) NOT NULL,
  subtitle VARCHAR(200),
  author_id INT,
  publication_date DATE,
  isbn VARCHAR(20) UNIQUE,
  price DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id),
  FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

-- Create table for book publishing services
CREATE TABLE book_publishing_services (
  book_id INT,
  service_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id, service_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES publishing_services(service_id) ON DELETE CASCADE
);

-- Create table for book genres
CREATE TABLE genres (
  genre_id INT AUTO_INCREMENT,
  genre_name VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (genre_id)
);

-- Create table for book genres mapping
CREATE TABLE book_genres (
  book_id INT,
  genre_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (book_id, genre_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_books_author_id ON books (author_id);
CREATE INDEX idx_book_publishing_services_book_id ON book_publishing_services (book_id);
CREATE INDEX idx_book_publishing_services_service_id ON book_publishing_services (service_id);
CREATE INDEX idx_book_genres_book_id ON book_genres (book_id);
CREATE INDEX idx_book_genres_genre_id ON book_genres (genre_id);
```

```sql
-- sample_data.sql

-- Insert sample data into authors table
INSERT INTO authors (first_name, last_name, date_of_birth, bio)
VALUES 
('John', 'Doe', '1990-01-01', 'Sample author bio'),
('Jane', 'Doe', '1995-01-01', 'Sample author bio');

-- Insert sample data into publishing_services table
INSERT INTO publishing_services (service_name, service_description)
VALUES 
('Print', 'Print publishing service'),
('Digital', 'Digital publishing service');

-- Insert sample data into books table
INSERT INTO books (title, subtitle, author_id, publication_date, isbn, price)
VALUES 
('Sample Book', 'Sample subtitle', 1, '2020-01-01', '1234567890', 19.99),
('Another Book', 'Another subtitle', 2, '2021-01-01', '9876543210', 14.99);

-- Insert sample data into book_publishing_services table
INSERT INTO book_publishing_services (book_id, service_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

-- Insert sample data into genres table
INSERT INTO genres (genre_name)
VALUES 
('Fiction'),
('Non-Fiction');

-- Insert sample data into book_genres table
INSERT INTO book_genres (book_id, genre_id)
VALUES 
(1, 1),
(2, 2);
```
