"""
Generated Code Metadata:
========================
Original URL: https://sonic-lab.net
Prompt: Design a database schema to manage music metadata for an electronic music label like Soniculture, including artist information, music genres, and album tracks.
Generated: DETERMINISTIC_e31f5d51cfc4ce03
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing music metadata for an electronic music label

-- Create a table to store artist information
CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,               -- Name of the artist
    Bio TEXT,                                  -- Biography of the artist
    Website VARCHAR(255),                      -- Artist's official website
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store music genres
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each genre
    GenreName VARCHAR(100) NOT NULL UNIQUE,    -- Name of the genre
    Description TEXT,                           -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store albums
CREATE TABLE Albums (
    AlbumID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each album
    Title VARCHAR(255) NOT NULL,                -- Title of the album
    ReleaseDate DATE,                           -- Release date of the album
    ArtistID INT,                               -- Foreign key referencing the artist
    GenreID INT,                                -- Foreign key referencing the genre
    CoverArt VARCHAR(255),                      -- URL or path to the album cover art
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE SET NULL  -- Ensure referential integrity
);

-- Create a table to store tracks within albums
CREATE TABLE Tracks (
    TrackID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each track
    Title VARCHAR(255) NOT NULL,                -- Title of the track
    Duration TIME NOT NULL,                      -- Duration of the track
    AlbumID INT,                                 -- Foreign key referencing the album
    TrackNumber INT NOT NULL,                   -- Track number in the album
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store user playlists
CREATE TABLE Playlists (
    PlaylistID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each playlist
    UserID INT NOT NULL,                         -- Identifier for the user who owns the playlist
    PlaylistName VARCHAR(255) NOT NULL,         -- Name of the playlist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store tracks in playlists
CREATE TABLE PlaylistTracks (
    PlaylistID INT,                              -- Foreign key referencing the playlist
    TrackID INT,                                 -- Foreign key referencing the track
    PRIMARY KEY (PlaylistID, TrackID),          -- Composite primary key
    FOREIGN KEY (PlaylistID) REFERENCES Playlists(PlaylistID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (TrackID) REFERENCES Tracks(TrackID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
