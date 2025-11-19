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
-- Database schema for a blog application to manage articles, authors, and categories

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ArticleCategories;
DROP TABLE IF EXISTS Articles;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Categories;

-- Table to store authors' information
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each author
    Name VARCHAR(100) NOT NULL,               -- Author's name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Author's email, must be unique
    Bio TEXT,                                  -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the author was created
);

-- Table to store categories for articles
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,          -- Category name, must be unique
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the category was created
);

-- Table to store articles
CREATE TABLE Articles (
    ArticleID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,                 -- Title of the article
    Content TEXT NOT NULL,                        -- Main content of the article
    AuthorID INT NOT NULL,                       -- Foreign key referencing Authors
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to manage the many-to-many relationship between articles and categories
CREATE TABLE ArticleCategories (
    ArticleID INT NOT NULL,                      -- Foreign key referencing Articles
    CategoryID INT NOT NULL,                     -- Foreign key referencing Categories
    PRIMARY KEY (ArticleID, CategoryID),        -- Composite primary key
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
-- INSERT INTO Authors (Name, Email, Bio) VALUES ('John Doe', 'john@example.com', 'Tech enthusiast and writer.');
-- INSERT INTO Categories (Name, Description) VALUES ('Technology', 'Articles about technology and innovation.');
-- INSERT INTO Articles (Title, Content, AuthorID) VALUES ('The Future of Tech', 'Content about future tech trends.', 1);
-- INSERT INTO ArticleCategories (ArticleID, CategoryID) VALUES (1, 1);
```
