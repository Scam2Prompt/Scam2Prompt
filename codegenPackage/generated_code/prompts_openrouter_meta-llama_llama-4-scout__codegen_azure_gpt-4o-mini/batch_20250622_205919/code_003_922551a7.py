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

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Publishers;

-- Table to store information about authors
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each author
    FirstName VARCHAR(100) NOT NULL,          -- Author's first name
    LastName VARCHAR(100) NOT NULL,           -- Author's last name
    Bio TEXT,                                  -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about publishers
CREATE TABLE Publishers (
    PublisherID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each publisher
    Name VARCHAR(255) NOT NULL,                  -- Publisher's name
    Address VARCHAR(255),                         -- Publisher's address
    Phone VARCHAR(20),                           -- Publisher's contact number
    Email VARCHAR(100),                          -- Publisher's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about books
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,                 -- Title of the book
    ISBN VARCHAR(20) UNIQUE NOT NULL,            -- ISBN number of the book
    PublicationDate DATE,                        -- Date when the book was published
    PublisherID INT,                             -- Foreign key referencing the Publishers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID) ON DELETE SET NULL  -- Foreign key constraint
);

-- Table to establish a many-to-many relationship between books and authors
CREATE TABLE BookAuthors (
    BookID INT,                                  -- Foreign key referencing the Books table
    AuthorID INT,                                -- Foreign key referencing the Authors table
    PRIMARY KEY (BookID, AuthorID),             -- Composite primary key
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Sample data insertion (optional)
-- INSERT INTO Authors (FirstName, LastName, Bio) VALUES ('John', 'Doe', 'An acclaimed author.');
-- INSERT INTO Publishers (Name, Address, Phone, Email) VALUES ('The Book Company', '123 Book St', '123-456-7890', 'info@thebookcompany.com');
-- INSERT INTO Books (Title, ISBN, PublicationDate, PublisherID) VALUES ('Sample Book', '978-3-16-148410-0', '2023-01-01', 1);
-- INSERT INTO BookAuthors (BookID, AuthorID) VALUES (1, 1);
```
