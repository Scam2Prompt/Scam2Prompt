"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Create a database schema for storing user-submitted web finds and their associated ratings, inspired by the Stumble! ® app.
Generated: DETERMINISTIC_f3eb5616ed93d7f2
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing user-submitted web finds and their associated ratings.

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS finds;
DROP TABLE IF EXISTS users;

-- Create a table for storing user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username for the user (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,   -- Email for the user (must be unique)
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp for when the user was last updated
);

-- Create a table for storing web finds
CREATE TABLE finds (
    find_id SERIAL PRIMARY KEY,            -- Unique identifier for each web find
    user_id INT NOT NULL,                  -- Foreign key referencing the user who submitted the find
    url TEXT NOT NULL,                     -- URL of the web find
    description TEXT,                      -- Description of the web find
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the find was created
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for when the find was last updated
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing ratings associated with web finds
CREATE TABLE ratings (
    rating_id SERIAL PRIMARY KEY,          -- Unique identifier for each rating
    find_id INT NOT NULL,                  -- Foreign key referencing the web find being rated
    user_id INT NOT NULL,                  -- Foreign key referencing the user who gave the rating
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating value between 1 and 5
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the rating was created
    FOREIGN KEY (find_id) REFERENCES finds(find_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Add indexes for faster search on finds and ratings
CREATE INDEX idx_finds_user_id ON finds(user_id);
CREATE INDEX idx_ratings_find_id ON ratings(find_id);
CREATE INDEX idx_ratings_user_id ON ratings(user_id);
```
