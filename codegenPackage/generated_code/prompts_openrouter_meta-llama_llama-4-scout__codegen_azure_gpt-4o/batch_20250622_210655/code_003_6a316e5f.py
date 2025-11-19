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
-- Database Schema for a Blog

-- Create a table for storing user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE,     -- Email address of the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    role ENUM('admin', 'author', 'subscriber') DEFAULT 'subscriber', -- User role
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for storing blog posts
CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    user_id INT NOT NULL,                   -- Foreign key referencing the author of the post
    title VARCHAR(255) NOT NULL,            -- Title of the blog post
    content TEXT NOT NULL,                  -- Content of the blog post
    status ENUM('draft', 'published') DEFAULT 'draft', -- Status of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Post creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table for storing comments on blog posts
CREATE TABLE comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    post_id INT NOT NULL,                      -- Foreign key referencing the post
    user_id INT NOT NULL,                      -- Foreign key referencing the user who made the comment
    content TEXT NOT NULL,                     -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Comment creation timestamp
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table for storing categories
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,          -- Name of the category
    description TEXT DEFAULT NULL,              -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Category creation timestamp
);

-- Create a table for associating posts with categories (many-to-many relationship)
CREATE TABLE post_categories (
    post_id INT NOT NULL,                       -- Foreign key referencing the post
    category_id INT NOT NULL,                   -- Foreign key referencing the category
    PRIMARY KEY (post_id, category_id),         -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Cascade delete if category is deleted
);

-- Create a table for storing tags
CREATE TABLE tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    name VARCHAR(100) NOT NULL UNIQUE,     -- Name of the tag
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Tag creation timestamp
);

-- Create a table for associating posts with tags (many-to-many relationship)
CREATE TABLE post_tags (
    post_id INT NOT NULL,                       -- Foreign key referencing the post
    tag_id INT NOT NULL,                        -- Foreign key referencing the tag
    PRIMARY KEY (post_id, tag_id),              -- Composite primary key
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE -- Cascade delete if tag is deleted
);

-- Create a table for storing likes on posts
CREATE TABLE post_likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each like
    post_id INT NOT NULL,                   -- Foreign key referencing the post
    user_id INT NOT NULL,                   -- Foreign key referencing the user who liked the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Like creation timestamp
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table for storing media files (e.g., images, videos)
CREATE TABLE media (
    media_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media file
    user_id INT NOT NULL,                    -- Foreign key referencing the uploader
    file_path VARCHAR(255) NOT NULL,         -- Path to the media file
    file_type ENUM('image', 'video', 'audio', 'document') NOT NULL, -- Type of media file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Media upload timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);
```
