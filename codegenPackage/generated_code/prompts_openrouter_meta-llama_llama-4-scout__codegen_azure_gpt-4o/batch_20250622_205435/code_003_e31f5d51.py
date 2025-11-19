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

-- Table to store artist information
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Name of the artist
    Bio TEXT,                                -- Short biography of the artist
    Country VARCHAR(100),                    -- Country of origin
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store music genres
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    Name VARCHAR(100) NOT NULL UNIQUE,      -- Name of the genre (e.g., Techno, House)
    Description TEXT,                       -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store album information
CREATE TABLE Albums (
    AlbumID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each album
    Title VARCHAR(255) NOT NULL,            -- Title of the album
    ReleaseDate DATE,                       -- Release date of the album
    ArtistID INT NOT NULL,                  -- Foreign key referencing the artist
    CoverImageURL VARCHAR(2083),            -- URL to the album cover image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Cascade delete if artist is removed
);

-- Table to store tracks within albums
CREATE TABLE Tracks (
    TrackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each track
    Title VARCHAR(255) NOT NULL,            -- Title of the track
    Duration TIME,                          -- Duration of the track (HH:MM:SS)
    AlbumID INT NOT NULL,                   -- Foreign key referencing the album
    GenreID INT NOT NULL,                   -- Foreign key referencing the genre
    TrackNumber INT NOT NULL,               -- Track number in the album
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID) ON DELETE CASCADE, -- Cascade delete if album is removed
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE SET NULL -- Set genre to NULL if genre is removed
);

-- Table to store collaborations between artists
CREATE TABLE ArtistCollaborations (
    CollaborationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collaboration
    ArtistID1 INT NOT NULL,                         -- First artist in the collaboration
    ArtistID2 INT NOT NULL,                         -- Second artist in the collaboration
    CollaborationDetails TEXT,                     -- Details about the collaboration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ArtistID1) REFERENCES Artists(ArtistID) ON DELETE CASCADE, -- Cascade delete if artist is removed
    FOREIGN KEY (ArtistID2) REFERENCES Artists(ArtistID) ON DELETE CASCADE  -- Cascade delete if artist is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_artist_name ON Artists(Name); -- Index for quick lookup of artists by name
CREATE INDEX idx_album_title ON Albums(Title); -- Index for quick lookup of albums by title
CREATE INDEX idx_track_title ON Tracks(Title); -- Index for quick lookup of tracks by title
CREATE INDEX idx_genre_name ON Genres(Name);   -- Index for quick lookup of genres by name
```
