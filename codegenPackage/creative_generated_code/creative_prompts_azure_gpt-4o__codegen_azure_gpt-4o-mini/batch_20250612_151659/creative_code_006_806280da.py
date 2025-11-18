"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Develop a database schema for a platform like HopefulMe, including tables for users, posts, events, group chats, and e-book downloads.
Generated: DETERMINISTIC_806280da24360aa3
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for the HopefulMe platform

-- Drop the existing database if it exists
DROP DATABASE IF EXISTS hopeful_me;

-- Create a new database for the platform
CREATE DATABASE hopeful_me;
USE hopeful_me;

-- Table for users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email for user notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for posts
CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each post
    user_id INT NOT NULL,                      -- Reference to the user who created the post
    content TEXT NOT NULL,                     -- Content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Post creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures user deletion cascades to posts
);

-- Table for events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each event
    user_id INT NOT NULL,                      -- Reference to the user who created the event
    title VARCHAR(100) NOT NULL,               -- Title of the event
    description TEXT,                          -- Description of the event
    event_date DATETIME NOT NULL,              -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Event creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures user deletion cascades to events
);

-- Table for group chats
CREATE TABLE group_chats (
    group_chat_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each group chat
    group_name VARCHAR(100) NOT NULL,            -- Name of the group chat
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Group chat creation timestamp
);

-- Table for group chat members
CREATE TABLE group_chat_members (
    group_chat_id INT NOT NULL,                  -- Reference to the group chat
    user_id INT NOT NULL,                         -- Reference to the user in the group chat
    PRIMARY KEY (group_chat_id, user_id),        -- Composite primary key to ensure unique membership
    FOREIGN KEY (group_chat_id) REFERENCES group_chats(group_chat_id) ON DELETE CASCADE, -- Ensure group chat deletion cascades
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure user deletion cascades to group chat memberships
);

-- Table for e-book downloads
CREATE TABLE ebook_downloads (
    download_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each download
    user_id INT NOT NULL,                         -- Reference to the user who downloaded the e-book
    ebook_title VARCHAR(255) NOT NULL,           -- Title of the downloaded e-book
    download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Download timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure user deletion cascades to downloads
);

-- Ensure all tables are created successfully
SELECT 'All tables created successfully' AS message;
```
