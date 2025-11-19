"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Design a database schema for storing news articles, author information, and reader comments, based on the structure of The Defiant's content.
Generated: DETERMINISTIC_b452bf3865768a69
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing news articles, author information, and reader comments

-- Table to store author information
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(255) NOT NULL,              -- Full name of the author
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the author
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the author was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store news articles
CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,              -- Title of the article
    Content TEXT NOT NULL,                    -- Full content of the article
    PublishedAt TIMESTAMP NOT NULL,           -- Timestamp when the article was published
    AuthorID INT NOT NULL,                    -- Foreign key referencing the author of the article
    Category VARCHAR(100),                    -- Category of the article (e.g., Politics, Technology)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE -- Cascade delete if author is removed
);

-- Table to store reader comments
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    ArticleID INT NOT NULL,                   -- Foreign key referencing the article being commented on
    ReaderName VARCHAR(255) NOT NULL,         -- Name of the reader who posted the comment
    ReaderEmail VARCHAR(255),                 -- Email of the reader (optional)
    Content TEXT NOT NULL,                    -- Content of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE -- Cascade delete if article is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_author_email ON Authors(Email); -- Index for quick lookup of authors by email
CREATE INDEX idx_article_category ON Articles(Category); -- Index for filtering articles by category
CREATE INDEX idx_comment_article ON Comments(ArticleID); -- Index for retrieving comments for a specific article
```
