"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Create a database schema for storing metadata about e-books, including genre, title, author, and live preview links, inspired by Digielearning's e-book organization.
Generated: DETERMINISTIC_4fd8db0f49a0c8b6
Batch ID: 20250612_150116
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://preview-link.com/1984": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://preview-link.com/hp1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Define the database schema for storing e-book metadata

-- Create table to store authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(255) NOT NULL,              -- Name of the author
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create table to store genres
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    GenreName VARCHAR(255) NOT NULL UNIQUE, -- Name of the genre
    Description TEXT,                       -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create table to store e-book metadata
CREATE TABLE EBooks (
    EBookID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each e-book
    Title VARCHAR(255) NOT NULL,                -- Title of the e-book
    AuthorID INT NOT NULL,                      -- Foreign key reference to Authors table
    GenreID INT NOT NULL,                       -- Foreign key reference to Genres table
    LivePreviewLink VARCHAR(2083),             -- URL for live preview of the e-book
    PublishedDate DATE,                         -- Date when the e-book was published
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE, -- Cascade deletion for associated author
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE -- Cascade deletion for associated genre
);

-- Indexing for performance optimization
CREATE INDEX idx_author ON EBooks(AuthorID); -- Index on AuthorID for faster lookup
CREATE INDEX idx_genre ON EBooks(GenreID);   -- Index on GenreID for faster lookup

-- Sample data insertion for demonstration

-- Insert demo authors
INSERT INTO Authors (Name, Bio) VALUES 
('J.K. Rowling', 'British author best known for the Harry Potter series.'),
('George Orwell', 'English novelist, essayist, and critic famous for works like 1984 and Animal Farm.');

-- Insert demo genres
INSERT INTO Genres (GenreName, Description) VALUES 
('Fantasy', 'A genre of speculative fiction involving magical elements.'),
('Dystopian', 'A genre depicting an imagined society under oppression or authoritarian rule.');

-- Insert demo e-books
INSERT INTO EBooks (Title, AuthorID, GenreID, LivePreviewLink, PublishedDate) VALUES 
('Harry Potter and the Sorcerer\'s Stone', 1, 1, 'https://preview-link.com/hp1', '1997-06-26'),
('1984', 2, 2, 'https://preview-link.com/1984', '1949-06-08');
```
