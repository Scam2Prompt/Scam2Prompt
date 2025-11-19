"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: "Design a database schema for a blog using MySQL, considering WebServicesIndia's experience in WordPress Development and custom web design services."
Generated: DETERMINISTIC_6a316e5faf4099b4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a blog

-- Create a database for the blog
CREATE DATABASE IF NOT EXISTS blog_db;

-- Use the created database
USE blog_db;

-- Table to store users
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email for user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store blog posts
CREATE TABLE IF NOT EXISTS posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each post
    user_id INT NOT NULL,                      -- Foreign key referencing the user who created the post
    title VARCHAR(255) NOT NULL,               -- Title of the blog post
    content TEXT NOT NULL,                      -- Content of the blog post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of post creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store comments on posts
CREATE TABLE IF NOT EXISTS comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each comment
    post_id INT NOT NULL,                       -- Foreign key referencing the post
    user_id INT NOT NULL,                       -- Foreign key referencing the user who made the comment
    content TEXT NOT NULL,                      -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of comment creation
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store categories for posts
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,           -- Unique name for the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of category creation
);

-- Table to associate posts with categories (Many-to-Many relationship)
CREATE TABLE IF NOT EXISTS post_categories (
    post_id INT NOT NULL,                        -- Foreign key referencing the post
    category_id INT NOT NULL,                    -- Foreign key referencing the category
    PRIMARY KEY (post_id, category_id),         -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store tags for posts
CREATE TABLE IF NOT EXISTS tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each tag
    name VARCHAR(100) NOT NULL UNIQUE,           -- Unique name for the tag
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of tag creation
);

-- Table to associate posts with tags (Many-to-Many relationship)
CREATE TABLE IF NOT EXISTS post_tags (
    post_id INT NOT NULL,                        -- Foreign key referencing the post
    tag_id INT NOT NULL,                         -- Foreign key referencing the tag
    PRIMARY KEY (post_id, tag_id),              -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE  -- Ensures referential integrity
);
```
