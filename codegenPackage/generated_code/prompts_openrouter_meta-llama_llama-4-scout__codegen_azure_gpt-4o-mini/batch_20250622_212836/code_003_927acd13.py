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
-- Database schema for a simple blog

-- Create a table for users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for categories (e.g., games, technology)
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,       -- Unique identifier for each category
    name VARCHAR(50) NOT NULL UNIQUE,     -- Name of the category
    description TEXT,                     -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for blog posts
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,            -- Unique identifier for each post
    user_id INT NOT NULL,                  -- Foreign key referencing the user who created the post
    category_id INT NOT NULL,              -- Foreign key referencing the category of the post
    title VARCHAR(255) NOT NULL,           -- Title of the post
    content TEXT NOT NULL,                  -- Content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of post creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for comments on posts
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,         -- Unique identifier for each comment
    post_id INT NOT NULL,                  -- Foreign key referencing the post being commented on
    user_id INT NOT NULL,                  -- Foreign key referencing the user who made the comment
    content TEXT NOT NULL,                  -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of comment creation
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for tags to allow for post tagging
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,             -- Unique identifier for each tag
    name VARCHAR(50) NOT NULL UNIQUE,      -- Name of the tag
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of tag creation
);

-- Create a junction table for many-to-many relationship between posts and tags
CREATE TABLE post_tags (
    post_id INT NOT NULL,                  -- Foreign key referencing the post
    tag_id INT NOT NULL,                   -- Foreign key referencing the tag
    PRIMARY KEY (post_id, tag_id),        -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
