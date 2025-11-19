"""
Generated Code Metadata:
========================
Original URL: https://filmdailyweb.com
Prompt: Design a database schema for a blog platform that handles various categories like business, lifestyle, and tech, similar to Film Daily Web's structure.
Generated: DETERMINISTIC_f7d2d1e99e302efe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a blog platform

-- Create a table for categories
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,    -- Name of the category, must be unique
    description TEXT,                      -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the user was last updated
);

-- Create a table for blog posts
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each post
    title VARCHAR(255) NOT NULL,           -- Title of the blog post
    content TEXT NOT NULL,                  -- Content of the blog post
    user_id INT NOT NULL,                   -- Foreign key referencing the user who created the post
    category_id INT NOT NULL,               -- Foreign key referencing the category of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the post was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the post was last updated
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for comments
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each comment
    post_id INT NOT NULL,                  -- Foreign key referencing the post being commented on
    user_id INT NOT NULL,                   -- Foreign key referencing the user who made the comment
    content TEXT NOT NULL,                  -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the comment was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the comment was last updated
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for tags
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each tag
    name VARCHAR(50) NOT NULL UNIQUE,      -- Unique name for the tag
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the tag was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the tag was last updated
);

-- Create a junction table for post tags (many-to-many relationship)
CREATE TABLE post_tags (
    post_id INT NOT NULL,                  -- Foreign key referencing the post
    tag_id INT NOT NULL,                   -- Foreign key referencing the tag
    PRIMARY KEY (post_id, tag_id),        -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE   -- Ensure referential integrity
);
```
