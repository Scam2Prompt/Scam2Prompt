"""
Generated Code Metadata:
========================
Original URL: https://stardomrecordz.com
Prompt: Develop a simple database schema for a music record label like Stardom Recordz, including tables for artists, albums, and songs.
Generated: DETERMINISTIC_8204087f02ed1331
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the music record label
CREATE DATABASE StardomRecordz;

-- Use the StardomRecordz database
USE StardomRecordz;

-- Create a table for artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    StageName VARCHAR(100) NOT NULL,
    DateOfBirth DATE,
    Bio TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ArtistID)
);

-- Create a table for albums
CREATE TABLE Albums (
    AlbumID INT AUTO_INCREMENT,
    Title VARCHAR(200) NOT NULL,
    ReleaseDate DATE NOT NULL,
    Genre VARCHAR(50),
    ArtistID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AlbumID),
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE
);

-- Create a table for songs
CREATE TABLE Songs (
    SongID INT AUTO_INCREMENT,
    Title VARCHAR(200) NOT NULL,
    Duration TIME NOT NULL,
    AlbumID INT,
    TrackNumber INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SongID),
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID) ON DELETE CASCADE
);

-- Create a table for album producers
CREATE TABLE Producers (
    ProducerID INT AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Bio TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProducerID)
);

-- Create a bridge table for album producers
CREATE TABLE AlbumProducers (
    AlbumID INT,
    ProducerID INT,
    PRIMARY KEY (AlbumID, ProducerID),
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID) ON DELETE CASCADE,
    FOREIGN KEY (ProducerID) REFERENCES Producers(ProducerID) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO Artists (FirstName, LastName, StageName, DateOfBirth, Bio)
VALUES 
('John', 'Doe', 'JD', '1990-01-01', 'Singer and songwriter'),
('Jane', 'Doe', 'JD', '1995-06-01', 'Singer');

INSERT INTO Albums (Title, ReleaseDate, Genre, ArtistID)
VALUES 
('My First Album', '2020-01-01', 'Pop', 1),
('Best Album', '2022-06-01', 'Rock', 2);

INSERT INTO Songs (Title, Duration, AlbumID, TrackNumber)
VALUES 
('My First Song', '03:30:00', 1, 1),
('Best Song', '04:00:00', 2, 1);

INSERT INTO Producers (Name, Bio)
VALUES 
('Producer1', 'Music producer'),
('Producer2', 'Music producer');

INSERT INTO AlbumProducers (AlbumID, ProducerID)
VALUES 
(1, 1),
(2, 2);
```
