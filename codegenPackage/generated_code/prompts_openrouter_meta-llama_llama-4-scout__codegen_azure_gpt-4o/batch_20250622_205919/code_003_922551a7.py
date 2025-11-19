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
-- Database schema for storing information about books, authors, and publishing services

-- Table to store information about authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    FirstName VARCHAR(100) NOT NULL,         -- Author's first name
    LastName VARCHAR(100) NOT NULL,          -- Author's last name
    DateOfBirth DATE,                        -- Author's date of birth
    Nationality VARCHAR(100),               -- Author's nationality
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about publishing services
CREATE TABLE Publishers (
    PublisherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each publisher
    Name VARCHAR(255) NOT NULL,                 -- Publisher's name
    Address VARCHAR(255),                       -- Publisher's address
    ContactEmail VARCHAR(255),                  -- Publisher's contact email
    ContactPhone VARCHAR(20),                   -- Publisher's contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about books
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,               -- Book title
    Genre VARCHAR(100),                        -- Book genre
    PublicationDate DATE,                      -- Date the book was published
    ISBN VARCHAR(13) UNIQUE NOT NULL,          -- Unique ISBN for the book
    AuthorID INT NOT NULL,                     -- Foreign key referencing the Authors table
    PublisherID INT NOT NULL,                  -- Foreign key referencing the Publishers table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the book
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE, -- Cascade delete for author
    FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID) ON DELETE CASCADE -- Cascade delete for publisher
);

-- Table to store information about book reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    BookID INT NOT NULL,                       -- Foreign key referencing the Books table
    ReviewerName VARCHAR(255),                 -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the book (1 to 5)
    ReviewText TEXT,                           -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE -- Cascade delete for book
);

-- Indexes for optimizing queries
CREATE INDEX idx_author_name ON Authors (LastName, FirstName); -- Index for author name
CREATE INDEX idx_publisher_name ON Publishers (Name);         -- Index for publisher name
CREATE INDEX idx_book_title ON Books (Title);                 -- Index for book title
CREATE INDEX idx_review_rating ON Reviews (Rating);           -- Index for review rating
```
