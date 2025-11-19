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
-- Database schema for The Book Company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    nationality TEXT,
    biography TEXT,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create publishing_services table
CREATE TABLE IF NOT EXISTS publishing_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) CHECK(base_price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create books table
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    isbn TEXT UNIQUE NOT NULL CHECK(LENGTH(isbn) = 13 OR LENGTH(isbn) = 10),
    publication_date DATE,
    genre TEXT,
    page_count INTEGER CHECK(page_count > 0),
    price DECIMAL(10, 2) CHECK(price >= 0),
    author_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES publishing_services(service_id) ON DELETE RESTRICT
);

-- Create book_revisions table for versioning
CREATE TABLE IF NOT EXISTS book_revisions (
    revision_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    revision_number INTEGER NOT NULL CHECK(revision_number > 0),
    changes TEXT NOT NULL,
    revised_by TEXT NOT NULL,
    revision_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    UNIQUE(book_id, revision_number)
);

-- Create index for faster author lookups
CREATE INDEX IF NOT EXISTS idx_author_name ON authors(last_name, first_name);

-- Create index for faster book searches
CREATE INDEX IF NOT EXISTS idx_book_title ON books(title);
CREATE INDEX IF NOT EXISTS idx_book_genre ON books(genre);
CREATE INDEX IF NOT EXISTS idx_book_author ON books(author_id);

-- Create trigger to update timestamps on row modification
CREATE TRIGGER IF NOT EXISTS update_authors_timestamp
AFTER UPDATE ON authors
BEGIN
    UPDATE authors SET updated_at = CURRENT_TIMESTAMP WHERE author_id = NEW.author_id;
END;

CREATE TRIGGER IF NOT EXISTS update_books_timestamp
AFTER UPDATE ON books
BEGIN
    UPDATE books SET updated_at = CURRENT_TIMESTAMP WHERE book_id = NEW.book_id;
END;

CREATE TRIGGER IF NOT EXISTS update_services_timestamp
AFTER UPDATE ON publishing_services
BEGIN
    UPDATE publishing_services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = NEW.service_id;
END;
```
