"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuki.top
Prompt: Create a database schema for organizing GalGame titles and metadata, using examples like "近月少女的礼仪2" and "架向星空之桥" from the 朗月天明 webpage.
Generated: DETERMINISTIC_08226510a9c5cced
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for GalGame Titles and Metadata
-- This schema is designed to organize and store metadata for GalGame titles.

CREATE DATABASE IF NOT EXISTS GalGameLibrary;

USE GalGameLibrary;

-- Table to store information about GalGame titles
CREATE TABLE IF NOT EXISTS GalGames (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each GalGame
    title VARCHAR(255) NOT NULL,              -- Game title
    original_title VARCHAR(255),              -- Original title (if different)
    release_date DATE,                        -- Release date of the game
    developer VARCHAR(255),                   -- Name of the developer/company
    publisher VARCHAR(255),                   -- Name of the publisher/company
    genre VARCHAR(255),                       -- Genre of the game (e.g., romance, fantasy)
    language VARCHAR(50) DEFAULT 'Japanese',  -- Language of the game (default is Japanese)
    description TEXT,                         -- Short description or summary of the game
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store tags associated with GalGame titles
CREATE TABLE IF NOT EXISTS Tags (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each tag
    name VARCHAR(50) NOT NULL UNIQUE          -- Tag name (e.g., 'romance', 'comedy')
);

-- Junction table to associate tags with GalGame titles (many-to-many relationship)
CREATE TABLE IF NOT EXISTS GalGameTags (
    galgame_id INT NOT NULL,                  -- Foreign key referencing GalGames table
    tag_id INT NOT NULL,                      -- Foreign key referencing Tags table
    PRIMARY KEY (galgame_id, tag_id),         -- Composite primary key
    FOREIGN KEY (galgame_id) REFERENCES GalGames(id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (tag_id) REFERENCES Tags(id) ON DELETE CASCADE          -- Cascade delete
);

-- Table to store ratings for GalGame titles
CREATE TABLE IF NOT EXISTS Ratings (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each rating
    galgame_id INT NOT NULL,                  -- Foreign key referencing GalGames table
    rating FLOAT CHECK (rating >= 0 AND rating <= 10), -- Rating value (0-10 scale)
    reviewer VARCHAR(255),                    -- Name of the reviewer (optional)
    review_date DATE,                         -- Date of the review
    FOREIGN KEY (galgame_id) REFERENCES GalGames(id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store images associated with GalGame titles
CREATE TABLE IF NOT EXISTS GalGameImages (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each image
    galgame_id INT NOT NULL,                  -- Foreign key referencing GalGames table
    image_url VARCHAR(2083) NOT NULL,         -- URL/link to the image
    description VARCHAR(255),                 -- Description of the image (e.g., cover art, screenshot)
    FOREIGN KEY (galgame_id) REFERENCES GalGames(id) ON DELETE CASCADE -- Cascade delete
);

-- Sample insertions for demonstration purposes
INSERT INTO GalGames (title, original_title, release_date, developer, publisher, genre, description)
VALUES
('近月少女的礼仪2', '近月少女的礼儀2', '2018-07-27', 'Navel', 'Navel', 'Romance', 'A romantic visual novel set in an elite academy.'),
('架向星空之桥', '星空へ架かる橋', '2010-10-15', 'feng', 'feng', 'Romance', 'A story about building relationships and healing wounds.');

INSERT INTO Tags (name)
VALUES
('Romance'), ('School'), ('Comedy'), ('Drama'), ('Fantasy');

INSERT INTO GalGameTags (galgame_id, tag_id)
VALUES
(1, 1), (1, 2), (2, 1), (2, 3);
```
