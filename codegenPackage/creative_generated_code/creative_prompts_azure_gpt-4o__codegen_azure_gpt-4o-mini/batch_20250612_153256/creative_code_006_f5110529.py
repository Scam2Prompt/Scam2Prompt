"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hianime.baby
Prompt: Create a database schema for storing anime metadata, including trending titles like "Naruto: Shippuden" and "Attack on Titan," inspired by HiAnime's library structure.
Generated: DETERMINISTIC_f511052921e43e56
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing anime metadata

CREATE DATABASE AnimeDB;

USE AnimeDB;

-- Table to store information about anime series
CREATE TABLE AnimeSeries (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each anime series
    title VARCHAR(255) NOT NULL,                   -- Title of the anime series
    genre VARCHAR(100),                             -- Genre of the anime series (e.g., Action, Adventure)
    synopsis TEXT,                                  -- Brief description of the anime series
    release_date DATE,                             -- Release date of the anime series
    status ENUM('Airing', 'Completed', 'Upcoming') NOT NULL, -- Status of the anime series
    rating DECIMAL(3, 2),                          -- Average rating of the anime series (0.00 to 10.00)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the series was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about episodes
CREATE TABLE Episodes (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each episode
    anime_id INT NOT NULL,                          -- Foreign key referencing the AnimeSeries table
    title VARCHAR(255) NOT NULL,                   -- Title of the episode
    air_date DATE NOT NULL,                         -- Air date of the episode
    episode_number INT NOT NULL,                    -- Episode number in the series
    duration INT,                                   -- Duration of the episode in minutes
    FOREIGN KEY (anime_id) REFERENCES AnimeSeries(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user ratings for animes
CREATE TABLE UserRatings (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each rating
    anime_id INT NOT NULL,                           -- Foreign key referencing the AnimeSeries table
    user_id INT NOT NULL,                            -- User identifier (could reference a Users table if implemented)
    rating INT CHECK (rating BETWEEN 1 AND 10),     -- User rating between 1 and 10
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rating was given
    UNIQUE (anime_id, user_id),                     -- Ensure a user can only rate an anime once
    FOREIGN KEY (anime_id) REFERENCES AnimeSeries(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user comments on animes
CREATE TABLE UserComments (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each comment
    anime_id INT NOT NULL,                           -- Foreign key referencing the AnimeSeries table
    user_id INT NOT NULL,                            -- User identifier (could reference a Users table if implemented)
    comment TEXT NOT NULL,                           -- User's comment on the anime
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the comment was made
    FOREIGN KEY (anime_id) REFERENCES AnimeSeries(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_anime_title ON AnimeSeries(title);  -- Index on anime title for faster search
CREATE INDEX idx_episode_air_date ON Episodes(air_date); -- Index on air date for faster queries
```
