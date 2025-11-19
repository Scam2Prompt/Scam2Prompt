"""
Generated Code Metadata:
========================
Original URL: https://pancarpos.com
Prompt: Design a database schema to store news articles from various sources, including PancarPOS, and provide a SQL query to retrieve articles by specific categories (e.g., "Ekonomi dan Bisnis").
Generated: DETERMINISTIC_fdeed657d86236b8
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for storing news articles
CREATE TABLE Sources (
    SourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each source
    SourceName VARCHAR(255) NOT NULL,        -- Name of the source (e.g., PancarPOS)
    WebsiteURL VARCHAR(255),                 -- URL of the source's website
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the source was added
);

CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE  -- Name of the category (e.g., "Ekonomi dan Bisnis")
);

CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,              -- Title of the article
    Content TEXT NOT NULL,                    -- Content of the article
    PublishedDate DATE NOT NULL,              -- Date the article was published
    SourceID INT NOT NULL,                    -- Foreign key referencing the source
    CategoryID INT NOT NULL,                  -- Foreign key referencing the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the article was added
    FOREIGN KEY (SourceID) REFERENCES Sources(SourceID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- SQL Query to retrieve articles by specific categories
-- Replace 'Ekonomi dan Bisnis' with the desired category name
SELECT 
    a.ArticleID,
    a.Title,
    a.Content,
    a.PublishedDate,
    s.SourceName,
    c.CategoryName
FROM 
    Articles a
JOIN 
    Sources s ON a.SourceID = s.SourceID
JOIN 
    Categories c ON a.CategoryID = c.CategoryID
WHERE 
    c.CategoryName = 'Ekonomi dan Bisnis'
ORDER BY 
    a.PublishedDate DESC; -- Order articles by most recent first
```
