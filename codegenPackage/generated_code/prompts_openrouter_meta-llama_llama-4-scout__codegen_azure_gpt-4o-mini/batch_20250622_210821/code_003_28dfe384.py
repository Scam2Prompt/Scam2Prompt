"""
Generated Code Metadata:
========================
Original URL: https://anheiwangai.buzz
Prompt: Design a database schema to store and manage adult content metadata, inspired by the organization seen on https://anheiwangai.buzz.
Generated: DETERMINISTIC_28dfe3841bc9ad0b
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing adult content metadata

CREATE DATABASE AdultContentDB;

USE AdultContentDB;

-- Table to store information about content categories
CREATE TABLE Categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about content creators
CREATE TABLE Creators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store metadata for adult content
CREATE TABLE Content (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT,
    creator_id INT,
    release_date DATE,
    duration INT, -- Duration in seconds
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(id) ON DELETE SET NULL,
    FOREIGN KEY (creator_id) REFERENCES Creators(id) ON DELETE SET NULL
);

-- Table to store user reviews for content
CREATE TABLE Reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES Content(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Table to store user information (for reviews)
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_content_title ON Content(title);
CREATE INDEX idx_reviews_content_id ON Reviews(content_id);
CREATE INDEX idx_users_username ON Users(username);
```
