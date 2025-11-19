"""
Generated Code Metadata:
========================
Original URL: https://app-gala-games-online-world.blogspot.com
Prompt: Design a simple database schema for a blog, taking into account the types of posts (e.g., games, technology) seen on https://app-gala-games-online-world.blogspot.com.
Generated: DETERMINISTIC_927acd13fe947d66
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a blog platform

-- Table to store information about blog posts
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    Title VARCHAR(255) NOT NULL,           -- Title of the blog post
    Content TEXT NOT NULL,                 -- Content of the blog post
    AuthorID INT NOT NULL,                 -- Foreign key referencing the author of the post
    CategoryID INT NOT NULL,               -- Foreign key referencing the category of the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the post was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the post was last updated
);

-- Table to store information about authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(100) NOT NULL,              -- Name of the author
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email of the author (must be unique)
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the author was added
);

-- Table to store categories for blog posts
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category (must be unique)
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the category was added
);

-- Table to store comments on blog posts
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    PostID INT NOT NULL,                      -- Foreign key referencing the post
    AuthorName VARCHAR(100) NOT NULL,         -- Name of the person who commented
    Content TEXT NOT NULL,                    -- Content of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE -- Cascade delete if the post is deleted
);

-- Table to store tags for blog posts
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    Name VARCHAR(100) NOT NULL UNIQUE,    -- Name of the tag (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the tag was added
);

-- Many-to-Many relationship between Posts and Tags
CREATE TABLE PostTags (
    PostID INT NOT NULL,                  -- Foreign key referencing the post
    TagID INT NOT NULL,                   -- Foreign key referencing the tag
    PRIMARY KEY (PostID, TagID),          -- Composite primary key
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE, -- Cascade delete if the post is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE     -- Cascade delete if the tag is deleted
);

-- Indexes for optimization
CREATE INDEX idx_posts_category ON Posts(CategoryID); -- Index for faster category-based queries
CREATE INDEX idx_posts_author ON Posts(AuthorID);     -- Index for faster author-based queries
CREATE INDEX idx_comments_post ON Comments(PostID);   -- Index for faster post-based comment queries
```
