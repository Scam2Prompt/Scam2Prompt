"""
Generated Code Metadata:
========================
Original URL: https://moviebox9.click
Prompt: Design a database schema to store MovieBox's extensive library of movies and TV shows, including metadata like titles, genres, directors, and release dates.
Generated: DETERMINISTIC_b7829f1136d389e4
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for MovieBox's library of movies and TV shows

-- Table to store information about movies and TV shows
CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media item
    title VARCHAR(255) NOT NULL,             -- Title of the movie or TV show
    type ENUM('Movie', 'TV Show') NOT NULL,  -- Type of media (Movie or TV Show)
    release_date DATE,                       -- Release date of the media
    description TEXT,                        -- Brief description or synopsis
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store genres
CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    name VARCHAR(100) NOT NULL UNIQUE        -- Name of the genre (e.g., Action, Comedy)
);

-- Table to store directors
CREATE TABLE Director (
    director_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each director
    name VARCHAR(255) NOT NULL UNIQUE,          -- Name of the director
    birth_date DATE,                             -- Birth date of the director
    nationality VARCHAR(100)                    -- Nationality of the director
);

-- Table to associate media with genres (many-to-many relationship)
CREATE TABLE MediaGenre (
    media_id INT NOT NULL,                      -- Foreign key referencing Media table
    genre_id INT NOT NULL,                      -- Foreign key referencing Genre table
    PRIMARY KEY (media_id, genre_id),           -- Composite primary key
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE CASCADE  -- Cascade delete
);

-- Table to associate media with directors (many-to-many relationship)
CREATE TABLE MediaDirector (
    media_id INT NOT NULL,                      -- Foreign key referencing Media table
    director_id INT NOT NULL,                   -- Foreign key referencing Director table
    PRIMARY KEY (media_id, director_id),        -- Composite primary key
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (director_id) REFERENCES Director(director_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store user ratings for media
CREATE TABLE MediaRating (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each rating
    media_id INT NOT NULL,                     -- Foreign key referencing Media table
    user_id INT NOT NULL,                      -- Identifier for the user (can be linked to a User table)
    rating TINYINT CHECK (rating BETWEEN 1 AND 10), -- Rating value (1-10)
    review TEXT,                               -- Optional user review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store cast members (actors/actresses)
CREATE TABLE Cast (
    cast_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each cast member
    name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the cast member
    birth_date DATE,                           -- Birth date of the cast member
    nationality VARCHAR(100)                   -- Nationality of the cast member
);

-- Table to associate media with cast members (many-to-many relationship)
CREATE TABLE MediaCast (
    media_id INT NOT NULL,                     -- Foreign key referencing Media table
    cast_id INT NOT NULL,                      -- Foreign key referencing Cast table
    role VARCHAR(255),                         -- Role played by the cast member (e.g., character name)
    PRIMARY KEY (media_id, cast_id),           -- Composite primary key
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (cast_id) REFERENCES Cast(cast_id) ON DELETE CASCADE     -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_media_title ON Media(title); -- Index for quick search by title
CREATE INDEX idx_genre_name ON Genre(name);   -- Index for quick search by genre name
CREATE INDEX idx_director_name ON Director(name); -- Index for quick search by director name
CREATE INDEX idx_cast_name ON Cast(name);     -- Index for quick search by cast name
```
