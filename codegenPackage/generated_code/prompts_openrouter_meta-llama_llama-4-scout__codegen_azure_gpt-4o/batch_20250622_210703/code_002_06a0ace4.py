"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Generate a SQL database schema for a music label management system inspired by Comet Records, including tables for artists, albums, and music genres like progressive house.
Generated: DETERMINISTIC_06a0ace48ddf7ae3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Music Label Management System

-- Table: Artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Name of the artist
    Country VARCHAR(100),                    -- Country of origin
    DateOfBirth DATE,                        -- Date of birth of the artist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Genres
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    Name VARCHAR(100) NOT NULL UNIQUE,      -- Name of the genre (e.g., Progressive House)
    Description TEXT,                       -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Albums
CREATE TABLE Albums (
    AlbumID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each album
    Title VARCHAR(255) NOT NULL,            -- Title of the album
    ReleaseDate DATE,                       -- Release date of the album
    ArtistID INT NOT NULL,                  -- Foreign key referencing the artist
    GenreID INT NOT NULL,                   -- Foreign key referencing the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE, -- Cascade delete if artist is removed
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE SET NULL -- Set genre to NULL if genre is removed
);

-- Table: Tracks
CREATE TABLE Tracks (
    TrackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each track
    Title VARCHAR(255) NOT NULL,            -- Title of the track
    Duration TIME,                          -- Duration of the track (HH:MM:SS)
    AlbumID INT NOT NULL,                   -- Foreign key referencing the album
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID) ON DELETE CASCADE -- Cascade delete if album is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_artist_name ON Artists(Name); -- Index for quick lookup of artist by name
CREATE INDEX idx_genre_name ON Genres(Name);   -- Index for quick lookup of genre by name
CREATE INDEX idx_album_title ON Albums(Title); -- Index for quick lookup of album by title
CREATE INDEX idx_track_title ON Tracks(Title); -- Index for quick lookup of track by title
```
