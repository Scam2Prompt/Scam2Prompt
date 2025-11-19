"""
Generated Code Metadata:
========================
Original URL: https://www.superstep.org
Prompt: Design a database schema for storing and managing articles, authors, and categories on a blog like Super Step, and provide SQL code for implementation.
Generated: DETERMINISTIC_ab00890a4c068d22
Batch ID: 20250622_205604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for a blog system

-- Table to store authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(100) NOT NULL,              -- Author's name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Author's email (must be unique)
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the author was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) UNIQUE NOT NULL,         -- Category name (must be unique)
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store articles
CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,              -- Title of the article
    Content TEXT NOT NULL,                    -- Content of the article
    AuthorID INT NOT NULL,                    -- Foreign key referencing the author
    CategoryID INT NOT NULL,                  -- Foreign key referencing the category
    PublishedAt TIMESTAMP DEFAULT NULL,       -- Timestamp when the article was published
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE, -- Cascade delete if author is removed
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Set category to NULL if removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_author_id ON Articles (AuthorID); -- Index for author ID in Articles table
CREATE INDEX idx_category_id ON Articles (CategoryID); -- Index for category ID in Articles table
CREATE INDEX idx_published_at ON Articles (PublishedAt); -- Index for published timestamp in Articles table
```
