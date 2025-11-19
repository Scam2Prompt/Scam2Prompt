"""
Generated Code Metadata:
========================
Original URL: https://azuki-2o2.pages.dev
Prompt: "Design a basic database schema for storing information about digital art pieces, anime series episodes, and artist collaborations, using a SQL database like MySQL."
Generated: DETERMINISTIC_ae24ecd0ebf5bfe1
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about digital art pieces, anime series episodes, and artist collaborations

-- Create a database for the digital art and anime series
CREATE DATABASE IF NOT EXISTS DigitalArtDB;
USE DigitalArtDB;

-- Table to store information about artists
CREATE TABLE IF NOT EXISTS Artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL,                 -- Name of the artist
    bio TEXT,                                   -- Biography of the artist
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the artist was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about digital art pieces
CREATE TABLE IF NOT EXISTS ArtPieces (
    art_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each art piece
    title VARCHAR(255) NOT NULL,                -- Title of the art piece
    artist_id INT NOT NULL,                      -- Foreign key referencing the artist
    creation_date DATE,                         -- Date the art piece was created
    medium VARCHAR(100),                        -- Medium used for the art piece (e.g., digital, painting)
    description TEXT,                           -- Description of the art piece
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the art piece was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about anime series
CREATE TABLE IF NOT EXISTS AnimeSeries (
    series_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each anime series
    title VARCHAR(255) NOT NULL,                 -- Title of the anime series
    genre VARCHAR(100),                          -- Genre of the anime series
    release_date DATE,                          -- Release date of the anime series
    description TEXT,                           -- Description of the anime series
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the series was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about episodes of anime series
CREATE TABLE IF NOT EXISTS Episodes (
    episode_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each episode
    series_id INT NOT NULL,                       -- Foreign key referencing the anime series
    episode_number INT NOT NULL,                  -- Episode number in the series
    title VARCHAR(255) NOT NULL,                  -- Title of the episode
    air_date DATE,                               -- Air date of the episode
    description TEXT,                            -- Description of the episode
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the episode was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (series_id) REFERENCES AnimeSeries(series_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about artist collaborations
CREATE TABLE IF NOT EXISTS Collaborations (
    collaboration_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each collaboration
    artist_id1 INT NOT NULL,                          -- First artist in the collaboration
    artist_id2 INT NOT NULL,                          -- Second artist in the collaboration
    project_title VARCHAR(255) NOT NULL,             -- Title of the collaboration project
    description TEXT,                                 -- Description of the collaboration
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the collaboration was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (artist_id1) REFERENCES Artists(artist_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (artist_id2) REFERENCES Artists(artist_id) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
```
