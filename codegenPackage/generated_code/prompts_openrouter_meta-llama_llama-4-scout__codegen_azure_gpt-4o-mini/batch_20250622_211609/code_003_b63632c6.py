"""
Generated Code Metadata:
========================
Original URL: https://fansliebe.com
Prompt: "Design a database schema for a social media platform with user subscriptions, content flagging, and private messaging, inspired by Fansliebe's features."
Generated: DETERMINISTIC_b63632c66e0b20bf
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a social media platform inspired by Fansliebe's features

-- Users table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Subscriptions table to manage user subscriptions
CREATE TABLE Subscriptions (
    subscription_id SERIAL PRIMARY KEY,        -- Unique identifier for each subscription
    subscriber_id INT NOT NULL,                -- User who subscribes
    subscribed_to_id INT NOT NULL,             -- User being subscribed to
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of subscription creation
    FOREIGN KEY (subscriber_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    FOREIGN KEY (subscribed_to_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    UNIQUE (subscriber_id, subscribed_to_id)   -- Prevent duplicate subscriptions
);

-- Content table to store user-generated content
CREATE TABLE Content (
    content_id SERIAL PRIMARY KEY,             -- Unique identifier for each content
    user_id INT NOT NULL,                      -- User who created the content
    content_text TEXT NOT NULL,                -- The content itself
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of content creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key to Users
);

-- FlaggedContent table to manage flagged content
CREATE TABLE FlaggedContent (
    flag_id SERIAL PRIMARY KEY,                 -- Unique identifier for each flag
    content_id INT NOT NULL,                    -- Content that has been flagged
    user_id INT NOT NULL,                       -- User who flagged the content
    reason VARCHAR(255) NOT NULL,               -- Reason for flagging
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of flag creation
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE, -- Foreign key to Content
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key to Users
);

-- Messages table to manage private messaging between users
CREATE TABLE Messages (
    message_id SERIAL PRIMARY KEY,              -- Unique identifier for each message
    sender_id INT NOT NULL,                     -- User who sends the message
    receiver_id INT NOT NULL,                   -- User who receives the message
    message_text TEXT NOT NULL,                 -- The message content
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of message creation
    FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key to Users
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_subscriber ON Subscriptions(subscriber_id);
CREATE INDEX idx_subscribed_to ON Subscriptions(subscribed_to_id);
CREATE INDEX idx_content_user ON Content(user_id);
CREATE INDEX idx_flagged_content ON FlaggedContent(content_id);
CREATE INDEX idx_message_sender ON Messages(sender_id);
CREATE INDEX idx_message_receiver ON Messages(receiver_id);
```
