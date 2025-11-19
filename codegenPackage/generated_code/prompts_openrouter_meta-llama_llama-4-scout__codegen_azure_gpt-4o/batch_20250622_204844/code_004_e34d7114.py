"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Design a database schema for storing information about Japanese female martial arts movies, including titles, descriptions, genres, and technical requirements for streaming on various devices.
Generated: DETERMINISTIC_e34d7114b05207b5
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Japanese female martial arts movies

-- Table to store movie information
CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each movie
    Title VARCHAR(255) NOT NULL,            -- Title of the movie
    Description TEXT,                       -- Description of the movie
    ReleaseDate DATE,                       -- Release date of the movie
    Duration INT,                           -- Duration of the movie in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store genres associated with movies
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    Name VARCHAR(100) NOT NULL UNIQUE       -- Name of the genre (e.g., Action, Drama, etc.)
);

-- Junction table to associate movies with multiple genres
CREATE TABLE MovieGenres (
    MovieID INT NOT NULL,                   -- Foreign key referencing Movies table
    GenreID INT NOT NULL,                   -- Foreign key referencing Genres table
    PRIMARY KEY (MovieID, GenreID),         -- Composite primary key
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE  -- Cascade delete
);

-- Table to store technical requirements for streaming
CREATE TABLE StreamingRequirements (
    RequirementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each requirement
    MovieID INT NOT NULL,                         -- Foreign key referencing Movies table
    DeviceType VARCHAR(100) NOT NULL,             -- Type of device (e.g., Smartphone, TV, etc.)
    Resolution VARCHAR(50) NOT NULL,              -- Required resolution (e.g., 1080p, 4K, etc.)
    Bandwidth VARCHAR(50) NOT NULL,               -- Required bandwidth (e.g., 5 Mbps, 10 Mbps, etc.)
    PRIMARY KEY (RequirementID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_movie_title ON Movies(Title); -- Index for quick search by movie title
CREATE INDEX idx_genre_name ON Genres(Name);   -- Index for quick search by genre name
CREATE INDEX idx_device_type ON StreamingRequirements(DeviceType); -- Index for quick search by device type
```
