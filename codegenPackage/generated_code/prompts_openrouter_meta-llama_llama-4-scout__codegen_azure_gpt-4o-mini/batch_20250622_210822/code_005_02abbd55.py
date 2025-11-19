"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Design a database schema to store and manage a large collection of articles, quizzes, and trending posts.
Generated: DETERMINISTIC_02abbd55e54a2320
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing articles, quizzes, and trending posts

-- Create a database named 'content_management'
CREATE DATABASE content_management;

-- Use the created database
USE content_management;

-- Table to store articles
CREATE TABLE articles (
    article_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each article
    title VARCHAR(255) NOT NULL,                 -- Title of the article
    content TEXT NOT NULL,                        -- Main content of the article
    author_id INT NOT NULL,                       -- Foreign key referencing authors
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of article creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (author_id) REFERENCES authors(author_id) -- Ensure referential integrity
);

-- Table to store quizzes
CREATE TABLE quizzes (
    quiz_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each quiz
    title VARCHAR(255) NOT NULL,                 -- Title of the quiz
    description TEXT,                             -- Description of the quiz
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of quiz creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store questions for quizzes
CREATE TABLE quiz_questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each question
    quiz_id INT NOT NULL,                          -- Foreign key referencing quizzes
    question_text TEXT NOT NULL,                   -- The question text
    correct_answer VARCHAR(255) NOT NULL,         -- The correct answer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of question creation
    FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id) -- Ensure referential integrity
);

-- Table to store trending posts
CREATE TABLE trending_posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each post
    title VARCHAR(255) NOT NULL,                   -- Title of the post
    content TEXT NOT NULL,                         -- Main content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of post creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store authors
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each author
    name VARCHAR(255) NOT NULL,                    -- Name of the author
    email VARCHAR(255) UNIQUE NOT NULL,            -- Email of the author
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of author creation
);

-- Indexes for performance optimization
CREATE INDEX idx_article_title ON articles(title);
CREATE INDEX idx_quiz_title ON quizzes(title);
CREATE INDEX idx_trending_post_title ON trending_posts(title);
```
