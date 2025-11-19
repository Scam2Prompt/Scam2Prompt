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
-- Database schema for a library of movies and TV shows

-- Create a table to store genres
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each genre
    GenreName VARCHAR(100) NOT NULL UNIQUE    -- Name of the genre
);

-- Create a table to store streaming qualities
CREATE TABLE StreamingQualities (
    QualityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each streaming quality
    QualityName VARCHAR(50) NOT NULL UNIQUE     -- Name of the streaming quality (e.g., 720p, 1080p, 4K)
);

-- Create a table to store movies and TV shows
CREATE TABLE Media (
    MediaID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each media item
    Title VARCHAR(255) NOT NULL,                -- Title of the movie or TV show
    Description TEXT,                            -- Description of the media item
    ReleaseYear INT,                            -- Year the media was released
    Type ENUM('Movie', 'TV Show') NOT NULL,    -- Type of media (Movie or TV Show)
    Duration INT,                                -- Duration in minutes (for movies) or number of episodes (for TV shows)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the media was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a junction table to associate media with genres (many-to-many relationship)
CREATE TABLE MediaGenres (
    MediaID INT,                                -- Foreign key referencing Media
    GenreID INT,                                -- Foreign key referencing Genres
    PRIMARY KEY (MediaID, GenreID),            -- Composite primary key
    FOREIGN KEY (MediaID) REFERENCES Media(MediaID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Create a junction table to associate media with streaming qualities (many-to-many relationship)
CREATE TABLE MediaStreamingQualities (
    MediaID INT,                                -- Foreign key referencing Media
    QualityID INT,                              -- Foreign key referencing StreamingQualities
    PRIMARY KEY (MediaID, QualityID),          -- Composite primary key
    FOREIGN KEY (MediaID) REFERENCES Media(MediaID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (QualityID) REFERENCES StreamingQualities(QualityID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for Genres
INSERT INTO Genres (GenreName) VALUES 
('Action'), 
('Comedy'), 
('Drama'), 
('Horror'), 
('Sci-Fi'), 
('Documentary');

-- Sample data insertion for StreamingQualities
INSERT INTO StreamingQualities (QualityName) VALUES 
('720p'), 
('1080p'), 
('4K');

-- Sample data insertion for Media
INSERT INTO Media (Title, Description, ReleaseYear, Type, Duration) VALUES 
('Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology.', 2010, 'Movie', 148),
('Breaking Bad', 'A high school chemistry teacher turned methamphetamine manufacturer.', 2008, 'TV Show', 62);

-- Sample data insertion for MediaGenres
INSERT INTO MediaGenres (MediaID, GenreID) VALUES 
(1, 1),  -- Inception is Action
(2, 3);  -- Breaking Bad is Drama

-- Sample data insertion for MediaStreamingQualities
INSERT INTO MediaStreamingQualities (MediaID, QualityID) VALUES 
(1, 2),  -- Inception is available in 1080p
(2, 1);  -- Breaking Bad is available in 720p
```
