"""
Generated Code Metadata:
========================
Original URL: https://gaflancoin.com
Prompt: Create a SQL database schema for a tech news website, with tables for articles, categories (e.g., technology, lifestyle), and tags, reflecting the structure of content on Gaflan Coin.
Generated: DETERMINISTIC_03fb1f1a218dd491
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Tech News Website

-- Create a table for categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., Technology, Lifestyle)
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for articles
CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,              -- Title of the article
    Content TEXT NOT NULL,                    -- Main content of the article
    Author VARCHAR(255) NOT NULL,             -- Author of the article
    CategoryID INT NOT NULL,                  -- Foreign key linking to the Categories table
    PublishedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the article was published
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the article was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for tags
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    Name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the tag (e.g., Blockchain, AI)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the tag was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the tag was last updated
);

-- Create a junction table for article-tag relationships (many-to-many)
CREATE TABLE ArticleTags (
    ArticleID INT NOT NULL, -- Foreign key linking to the Articles table
    TagID INT NOT NULL,     -- Foreign key linking to the Tags table
    PRIMARY KEY (ArticleID, TagID), -- Composite primary key to ensure uniqueness of the relationship
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_articles_category ON Articles(CategoryID); -- Index for faster lookups by category
CREATE INDEX idx_article_tags_tag ON ArticleTags(TagID);    -- Index for faster lookups by tag
CREATE INDEX idx_article_tags_article ON ArticleTags(ArticleID); -- Index for faster lookups by article
```
