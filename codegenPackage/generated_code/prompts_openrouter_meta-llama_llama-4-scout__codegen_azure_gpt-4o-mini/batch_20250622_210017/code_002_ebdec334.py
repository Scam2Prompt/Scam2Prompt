"""
Generated Code Metadata:
========================
Original URL: https://sushiswap.andy.cx
Prompt: Design a simple database schema to store and manage blog posts, including metadata like title, date, category, and tags.
Generated: DETERMINISTIC_ebdec334db83671b
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for managing blog posts

-- Create a database for the blog
CREATE DATABASE BlogDB;

-- Use the created database
USE BlogDB;

-- Table to store blog posts
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each post
    Title VARCHAR(255) NOT NULL,            -- Title of the blog post
    Content TEXT NOT NULL,                   -- Content of the blog post
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the post was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Date and time when the post was last updated
    CategoryID INT,                          -- Foreign key to the Categories table
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)  -- Ensures referential integrity
);

-- Table to store categories for blog posts
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE   -- Name of the category, must be unique
);

-- Table to store tags for blog posts
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each tag
    TagName VARCHAR(100) NOT NULL UNIQUE         -- Name of the tag, must be unique
);

-- Junction table to associate posts with tags (many-to-many relationship)
CREATE TABLE PostTags (
    PostID INT,                                  -- Foreign key to the Posts table
    TagID INT,                                   -- Foreign key to the Tags table
    PRIMARY KEY (PostID, TagID),                 -- Composite primary key
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE       -- Ensures referential integrity
);

-- Sample data insertion for Categories
INSERT INTO Categories (CategoryName) VALUES 
('Technology'),
('Lifestyle'),
('Travel'),
('Food');

-- Sample data insertion for Tags
INSERT INTO Tags (TagName) VALUES 
('Programming'),
('Health'),
('Adventure'),
('Cooking');

-- Note: Ensure to handle errors during data insertion and retrieval in application code.
-- Use transactions where necessary to maintain data integrity.
```
