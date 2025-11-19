"""
Generated Code Metadata:
========================
Original URL: https://dext500.top
Prompt: Design a database schema to store information about novels, including title, author, genre, and chapter content.
Generated: DETERMINISTIC_2d0e2ae39b9dede2
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about novels

-- Create a table to store authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(255) NOT NULL,              -- Author's name
    Bio TEXT,                                -- Optional biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store novels
CREATE TABLE Novels (
    NovelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each novel
    Title VARCHAR(255) NOT NULL,            -- Title of the novel
    AuthorID INT NOT NULL,                  -- Foreign key referencing the Authors table
    Genre VARCHAR(100),                     -- Genre of the novel
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store chapters
CREATE TABLE Chapters (
    ChapterID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each chapter
    NovelID INT NOT NULL,                     -- Foreign key referencing the Novels table
    ChapterNumber INT NOT NULL,               -- Chapter number in the novel
    Title VARCHAR(255),                       -- Title of the chapter (optional)
    Content TEXT NOT NULL,                    -- Content of the chapter
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (NovelID) REFERENCES Novels(NovelID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster queries
CREATE INDEX idx_author_name ON Authors(Name); -- Index for searching authors by name
CREATE INDEX idx_novel_title ON Novels(Title); -- Index for searching novels by title
CREATE INDEX idx_chapter_number ON Chapters(ChapterNumber); -- Index for searching chapters by number
```
