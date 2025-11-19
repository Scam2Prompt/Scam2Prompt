"""
Generated Code Metadata:
========================
Original URL: https://456movie.click
Prompt: Design a database schema to store a vast library of movies and TV shows with multiple genres and streaming qualities.
Generated: DETERMINISTIC_1bb64dfcb738f878
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing a vast library of movies and TV shows

-- Table to store information about movies and TV shows
CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media item
    title VARCHAR(255) NOT NULL,             -- Title of the movie or TV show
    description TEXT,                        -- Description or synopsis
    release_date DATE,                       -- Release date of the media
    type ENUM('Movie', 'TV Show') NOT NULL,  -- Type of media (Movie or TV Show)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store genres
CREATE TABLE Genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    name VARCHAR(100) NOT NULL UNIQUE        -- Name of the genre (e.g., Action, Comedy, Drama)
);

-- Junction table to associate media with multiple genres
CREATE TABLE MediaGenres (
    media_id INT NOT NULL,                   -- Foreign key referencing Media table
    genre_id INT NOT NULL,                   -- Foreign key referencing Genres table
    PRIMARY KEY (media_id, genre_id),        -- Composite primary key
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store streaming qualities
CREATE TABLE StreamingQualities (
    quality_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each quality
    name VARCHAR(50) NOT NULL UNIQUE           -- Name of the quality (e.g., 720p, 1080p, 4K)
);

-- Junction table to associate media with multiple streaming qualities
CREATE TABLE MediaStreamingQualities (
    media_id INT NOT NULL,                      -- Foreign key referencing Media table
    quality_id INT NOT NULL,                    -- Foreign key referencing StreamingQualities table
    PRIMARY KEY (media_id, quality_id),         -- Composite primary key
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (quality_id) REFERENCES StreamingQualities(quality_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store additional metadata for media (e.g., runtime, language, etc.)
CREATE TABLE MediaMetadata (
    media_id INT PRIMARY KEY,                  -- Foreign key referencing Media table
    runtime_minutes INT,                       -- Runtime in minutes
    language VARCHAR(50),                      -- Language of the media
    country VARCHAR(50),                       -- Country of origin
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_media_title ON Media(title); -- Index for quick search by title
CREATE INDEX idx_genre_name ON Genres(name);  -- Index for quick search by genre name
CREATE INDEX idx_quality_name ON StreamingQualities(name); -- Index for quick search by quality name
```
