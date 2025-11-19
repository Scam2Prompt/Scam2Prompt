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
-- Database schema for a digital library to store information about books and authors

-- Create a table to store author information
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each author
    FirstName VARCHAR(100) NOT NULL,          -- Author's first name
    LastName VARCHAR(100) NOT NULL,           -- Author's last name
    Bio TEXT,                                  -- Short biography of the author
    DateOfBirth DATE,                          -- Author's date of birth
    Nationality VARCHAR(50)                    -- Author's nationality
);

-- Create a table to store book information
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,               -- Title of the book
    Genre VARCHAR(100),                         -- Genre of the book
    PublishDate DATE,                           -- Date the book was published
    ISBN VARCHAR(20) UNIQUE NOT NULL,          -- International Standard Book Number
    AuthorID INT,                               -- Foreign key referencing the Authors table
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store reviews for books
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each review
    BookID INT,                                 -- Foreign key referencing the Books table
    ReviewerName VARCHAR(100) NOT NULL,        -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given to the book (1 to 5)
    ReviewText TEXT,                            -- Text of the review
    ReviewDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the review
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store book availability in the library
CREATE TABLE BookAvailability (
    AvailabilityID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for availability record
    BookID INT,                                    -- Foreign key referencing the Books table
    IsAvailable BOOLEAN DEFAULT TRUE,              -- Availability status of the book
    Location VARCHAR(100),                         -- Location of the book in the library
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster search queries
CREATE INDEX idx_author_lastname ON Authors(LastName);
CREATE INDEX idx_book_title ON Books(Title);
CREATE INDEX idx_review_rating ON Reviews(Rating);
```
