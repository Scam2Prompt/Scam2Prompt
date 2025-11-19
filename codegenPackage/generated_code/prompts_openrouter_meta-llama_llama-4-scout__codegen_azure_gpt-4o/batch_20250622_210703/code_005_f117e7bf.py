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
-- Create a database schema for a digital library to store information about books and authors

-- Create the Authors table to store information about authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    FirstName VARCHAR(100) NOT NULL,         -- Author's first name
    LastName VARCHAR(100) NOT NULL,          -- Author's last name
    DateOfBirth DATE,                        -- Author's date of birth
    Nationality VARCHAR(100),                -- Author's nationality
    Biography TEXT,                          -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create the Books table to store information about books
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,            -- Title of the book
    Genre VARCHAR(100),                     -- Genre of the book
    PublicationDate DATE,                   -- Date the book was published
    ISBN VARCHAR(13) UNIQUE,                -- International Standard Book Number
    Summary TEXT,                           -- Short summary of the book
    AuthorID INT NOT NULL,                  -- Foreign key referencing the Authors table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Books table for faster searches by title
CREATE INDEX idx_books_title ON Books (Title);

-- Create an index on the Authors table for faster searches by last name
CREATE INDEX idx_authors_lastname ON Authors (LastName);

-- Example of error handling: Ensure tables are created only if they don't already exist
-- (This is optional and depends on the database system being used)
```
