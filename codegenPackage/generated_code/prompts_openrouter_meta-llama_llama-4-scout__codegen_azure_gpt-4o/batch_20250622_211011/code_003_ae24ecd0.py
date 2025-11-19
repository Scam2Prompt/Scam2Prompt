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
-- Database Schema for Digital Art Pieces, Anime Series Episodes, and Artist Collaborations

-- Create a table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Name of the artist
    Bio TEXT,                                -- Short biography of the artist
    Website VARCHAR(255),                   -- Website or portfolio link
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store information about digital art pieces
CREATE TABLE DigitalArtPieces (
    ArtID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each art piece
    Title VARCHAR(255) NOT NULL,            -- Title of the art piece
    Description TEXT,                       -- Description of the art piece
    ArtistID INT NOT NULL,                  -- Foreign key referencing the artist who created the art
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE
);

-- Create a table to store information about anime series
CREATE TABLE AnimeSeries (
    SeriesID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each anime series
    Title VARCHAR(255) NOT NULL,             -- Title of the anime series
    Description TEXT,                        -- Description of the anime series
    ReleaseDate DATE,                        -- Release date of the anime series
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store information about anime series episodes
CREATE TABLE AnimeEpisodes (
    EpisodeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each episode
    SeriesID INT NOT NULL,                    -- Foreign key referencing the anime series
    Title VARCHAR(255) NOT NULL,              -- Title of the episode
    EpisodeNumber INT NOT NULL,               -- Episode number within the series
    AirDate DATE,                             -- Air date of the episode
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SeriesID) REFERENCES AnimeSeries(SeriesID) ON DELETE CASCADE
);

-- Create a table to store information about artist collaborations
CREATE TABLE ArtistCollaborations (
    CollaborationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collaboration
    Artist1ID INT NOT NULL,                         -- Foreign key referencing the first artist
    Artist2ID INT NOT NULL,                         -- Foreign key referencing the second artist
    CollaborationDetails TEXT,                     -- Details about the collaboration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (Artist1ID) REFERENCES Artists(ArtistID) ON DELETE CASCADE,
    FOREIGN KEY (Artist2ID) REFERENCES Artists(ArtistID) ON DELETE CASCADE,
    CONSTRAINT UniqueCollaboration UNIQUE (Artist1ID, Artist2ID) -- Ensure unique collaborations
);

-- Create indexes for faster querying
CREATE INDEX idx_artist_name ON Artists(Name);
CREATE INDEX idx_art_title ON DigitalArtPieces(Title);
CREATE INDEX idx_series_title ON AnimeSeries(Title);
CREATE INDEX idx_episode_title ON AnimeEpisodes(Title);
```
