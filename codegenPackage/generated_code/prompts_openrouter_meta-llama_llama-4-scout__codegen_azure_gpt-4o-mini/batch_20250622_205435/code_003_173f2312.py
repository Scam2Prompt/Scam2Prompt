"""
Generated Code Metadata:
========================
Original URL: https://sallysui.com
Prompt: Design a basic database schema to store user-generated content and community interactions for a platform like Sally.
Generated: DETERMINISTIC_173f2312535a7b46
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a user-generated content platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for each user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store posts created by users
CREATE TABLE Posts (
    post_id SERIAL PRIMARY KEY,            -- Unique identifier for each post
    user_id INT NOT NULL,                  -- Foreign key referencing the user who created the post
    content TEXT NOT NULL,                 -- Content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of post creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store comments on posts
CREATE TABLE Comments (
    comment_id SERIAL PRIMARY KEY,         -- Unique identifier for each comment
    post_id INT NOT NULL,                  -- Foreign key referencing the post being commented on
    user_id INT NOT NULL,                  -- Foreign key referencing the user who made the comment
    content TEXT NOT NULL,                 -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of comment creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (post_id) REFERENCES Posts(post_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store likes on posts
CREATE TABLE Likes (
    like_id SERIAL PRIMARY KEY,            -- Unique identifier for each like
    post_id INT NOT NULL,                  -- Foreign key referencing the liked post
    user_id INT NOT NULL,                  -- Foreign key referencing the user who liked the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of like creation
    UNIQUE (post_id, user_id),             -- Ensure a user can like a post only once
    FOREIGN KEY (post_id) REFERENCES Posts(post_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store user interactions (e.g., follows)
CREATE TABLE Follows (
    follow_id SERIAL PRIMARY KEY,          -- Unique identifier for each follow relationship
    follower_id INT NOT NULL,              -- Foreign key referencing the user who follows
    followed_id INT NOT NULL,              -- Foreign key referencing the user being followed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of follow creation
    UNIQUE (follower_id, followed_id),     -- Ensure a user can follow another user only once
    FOREIGN KEY (follower_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (followed_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
