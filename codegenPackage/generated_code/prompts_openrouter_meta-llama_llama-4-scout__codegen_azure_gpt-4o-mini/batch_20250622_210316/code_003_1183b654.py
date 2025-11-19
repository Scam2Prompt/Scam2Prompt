"""
Generated Code Metadata:
========================
Original URL: https://kashifanwar.com
Prompt: Design a basic database schema for storing and retrieving interviews, articles, and news updates, inspired by the structure of kashifanwar.com.
Generated: DETERMINISTIC_1183b65470ffe4b3
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing interviews, articles, and news updates

-- Create a table for storing users who can create content
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Create a table for storing articles
CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,       -- Unique identifier for each article
    title VARCHAR(255) NOT NULL,        -- Title of the article
    content TEXT NOT NULL,               -- Main content of the article
    author_id INT NOT NULL,              -- Foreign key referencing the user who wrote the article
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of article creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (author_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing interviews
CREATE TABLE interviews (
    interview_id SERIAL PRIMARY KEY,     -- Unique identifier for each interview
    title VARCHAR(255) NOT NULL,         -- Title of the interview
    content TEXT NOT NULL,                -- Main content of the interview
    interviewer_id INT NOT NULL,          -- Foreign key referencing the user who conducted the interview
    interviewee_name VARCHAR(100) NOT NULL, -- Name of the person being interviewed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of interview creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (interviewer_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing news updates
CREATE TABLE news_updates (
    news_id SERIAL PRIMARY KEY,           -- Unique identifier for each news update
    title VARCHAR(255) NOT NULL,          -- Title of the news update
    content TEXT NOT NULL,                 -- Main content of the news update
    author_id INT NOT NULL,                -- Foreign key referencing the user who wrote the news update
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of news update creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (author_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster retrieval
CREATE INDEX idx_articles_author ON articles(author_id);
CREATE INDEX idx_interviews_interviewer ON interviews(interviewer_id);
CREATE INDEX idx_news_updates_author ON news_updates(author_id);
```
