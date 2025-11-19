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
-- Database schema for storing news articles from various sources

CREATE TABLE Sources (
    SourceID INT PRIMARY KEY AUTO_INCREMENT,
    SourceName VARCHAR(255) NOT NULL UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Articles (
    ArticleID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Content TEXT NOT NULL,
    PublishedAt DATETIME NOT NULL,
    SourceID INT,
    CategoryID INT,
    FOREIGN KEY (SourceID) REFERENCES Sources(SourceID) ON DELETE SET NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample SQL query to retrieve articles by specific categories
-- Replace 'Ekonomi dan Bisnis' with the desired category name

SELECT 
    a.ArticleID,
    a.Title,
    a.Content,
    a.PublishedAt,
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
    a.PublishedAt DESC;
```
