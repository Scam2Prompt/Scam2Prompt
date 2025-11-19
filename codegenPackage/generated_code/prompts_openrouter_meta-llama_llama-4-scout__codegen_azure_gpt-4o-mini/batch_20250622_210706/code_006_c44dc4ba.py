"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Design a database schema for storing anime metadata, user information, and streaming history, suitable for a platform like HiAnime.
Generated: DETERMINISTIC_c44dc4ba2d573cc6
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for HiAnime platform

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store anime metadata
CREATE TABLE Anime (
    anime_id SERIAL PRIMARY KEY, -- Unique identifier for each anime
    title VARCHAR(255) NOT NULL, -- Title of the anime
    description TEXT, -- Description of the anime
    genre VARCHAR(100), -- Genre of the anime
    release_date DATE, -- Release date of the anime
    rating DECIMAL(3, 2), -- Rating of the anime (0.00 to 10.00)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of anime entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store streaming history for users
CREATE TABLE StreamingHistory (
    history_id SERIAL PRIMARY KEY, -- Unique identifier for each streaming record
    user_id INT NOT NULL, -- Foreign key referencing Users table
    anime_id INT NOT NULL, -- Foreign key referencing Anime table
    watch_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the anime was watched
    progress INT DEFAULT 0, -- Progress in percentage (0-100)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures user data integrity
    FOREIGN KEY (anime_id) REFERENCES Anime(anime_id) ON DELETE CASCADE -- Ensures anime data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_anime_title ON Anime(title);
CREATE INDEX idx_streaming_user ON StreamingHistory(user_id);
CREATE INDEX idx_streaming_anime ON StreamingHistory(anime_id);
```
