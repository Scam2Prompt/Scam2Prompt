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
-- SQL Database Schema for a Music Label Management System

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Genres;

-- Table to store information about music genres
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each genre
    GenreName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the genre, must be unique
    Description TEXT                          -- Optional description of the genre
);

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each artist
    ArtistName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the artist, must be unique
    Bio TEXT,                                  -- Optional biography of the artist
    DateOfBirth DATE,                          -- Optional date of birth
    Country VARCHAR(100)                       -- Optional country of origin
);

-- Table to store information about albums
CREATE TABLE Albums (
    AlbumID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each album
    AlbumTitle VARCHAR(100) NOT NULL,          -- Title of the album
    ReleaseDate DATE NOT NULL,                 -- Release date of the album
    ArtistID INT NOT NULL,                     -- Foreign key referencing the artist
    GenreID INT NOT NULL,                      -- Foreign key referencing the genre
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE      -- Ensures referential integrity
);

-- Sample data insertion for Genres
INSERT INTO Genres (GenreName, Description) VALUES
('Progressive House', 'A subgenre of house music characterized by a progressive build-up and melodic elements.'),
('Techno', 'A genre of electronic dance music that emerged in Detroit in the 1980s.'),
('Trance', 'A genre of electronic music that emphasizes melody and builds up to a climax.');

-- Sample data insertion for Artists
INSERT INTO Artists (ArtistName, Bio, DateOfBirth, Country) VALUES
('DJ Example', 'An influential DJ and producer in the progressive house scene.', '1985-05-15', 'USA'),
('Artist One', 'Known for their unique sound and energetic performances.', '1990-08-20', 'UK');

-- Sample data insertion for Albums
INSERT INTO Albums (AlbumTitle, ReleaseDate, ArtistID, GenreID) VALUES
('Progressive Vibes', '2023-01-01', 1, 1),
('Techno Beats', '2022-06-15', 2, 2);
```
