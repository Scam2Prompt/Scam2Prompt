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
-- Database schema for a digital library system
-- Tables for storing book and author information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Authors table
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE,
    nationality TEXT,
    biography TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT name_unique UNIQUE (first_name, last_name)
);

-- Books table
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    isbn TEXT UNIQUE,
    publication_year INTEGER,
    genre TEXT,
    description TEXT,
    page_count INTEGER,
    language TEXT DEFAULT 'English',
    publisher TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for book-author relationship (many-to-many)
CREATE TABLE book_authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

-- Categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Book categories junction table
CREATE TABLE book_categories (
    book_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Users table for library management
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    is_active BOOLEAN DEFAULT 1,
    is_staff BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Book copies table for inventory management
CREATE TABLE book_copies (
    copy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    barcode TEXT UNIQUE,
    acquisition_date DATE DEFAULT CURRENT_DATE,
    condition TEXT CHECK(condition IN ('New', 'Good', 'Fair', 'Poor')),
    is_available BOOLEAN DEFAULT 1,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);

-- Borrow records table
CREATE TABLE borrow_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    copy_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    borrow_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    status TEXT CHECK(status IN ('Borrowed', 'Returned', 'Overdue', 'Lost')) DEFAULT 'Borrowed',
    FOREIGN KEY (copy_id) REFERENCES book_copies(copy_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_author_timestamp
AFTER UPDATE ON authors
FOR EACH ROW
BEGIN
    UPDATE authors SET updated_at = CURRENT_TIMESTAMP WHERE author_id = OLD.author_id;
END;

CREATE TRIGGER update_book_timestamp
AFTER UPDATE ON books
FOR EACH ROW
BEGIN
    UPDATE books SET updated_at = CURRENT_TIMESTAMP WHERE book_id = OLD.book_id;
END;

CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_books_isbn ON books(isbn);
CREATE INDEX idx_authors_name ON authors(last_name, first_name);
CREATE INDEX idx_borrow_records_user ON borrow_records(user_id);
CREATE INDEX idx_borrow_records_copy ON borrow_records(copy_id);
```
