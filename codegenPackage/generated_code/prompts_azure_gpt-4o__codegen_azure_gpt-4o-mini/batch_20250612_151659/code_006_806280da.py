"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Develop a database schema for a platform like HopefulMe, including tables for users, posts, events, group chats, and e-book downloads.
Generated: DETERMINISTIC_806280da24360aa3
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for the HopefulMe platform

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store posts made by users
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,           -- Unique identifier for each post
    user_id INT NOT NULL,                 -- Foreign key referencing the user who made the post
    content TEXT NOT NULL,                 -- Content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of post creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures posts are deleted if the user is deleted
);

-- Table to store events created by users
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,          -- Unique identifier for each event
    user_id INT NOT NULL,                 -- Foreign key referencing the user who created the event
    title VARCHAR(100) NOT NULL,          -- Title of the event
    description TEXT,                     -- Description of the event
    event_date TIMESTAMP NOT NULL,        -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of event creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures events are deleted if the user is deleted
);

-- Table to store group chats
CREATE TABLE group_chats (
    chat_id SERIAL PRIMARY KEY,           -- Unique identifier for each group chat
    chat_name VARCHAR(100) NOT NULL,      -- Name of the group chat
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of chat creation
);

-- Table to store messages in group chats
CREATE TABLE chat_messages (
    message_id SERIAL PRIMARY KEY,        -- Unique identifier for each message
    chat_id INT NOT NULL,                 -- Foreign key referencing the group chat
    user_id INT NOT NULL,                 -- Foreign key referencing the user who sent the message
    message TEXT NOT NULL,                -- Content of the message
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of message creation
    FOREIGN KEY (chat_id) REFERENCES group_chats(chat_id) ON DELETE CASCADE, -- Ensures messages are deleted if the chat is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures messages are deleted if the user is deleted
);

-- Table to store e-book downloads
CREATE TABLE ebook_downloads (
    download_id SERIAL PRIMARY KEY,       -- Unique identifier for each download
    user_id INT NOT NULL,                 -- Foreign key referencing the user who downloaded the e-book
    ebook_title VARCHAR(100) NOT NULL,    -- Title of the e-book
    download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of download
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures downloads are deleted if the user is deleted
);
```
