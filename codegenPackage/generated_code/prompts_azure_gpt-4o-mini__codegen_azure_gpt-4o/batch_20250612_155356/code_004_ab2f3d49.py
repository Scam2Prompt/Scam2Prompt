"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Design a database schema for storing artist profiles and performance history for Tree House Sessions, ensuring it captures unique attributes mentioned in the content.
Generated: DETERMINISTIC_ab2f3d4907d1c0d9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing artist profiles and performance history for Tree House Sessions

-- Table: Artists
-- This table stores information about artists.
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Full name of the artist
    StageName VARCHAR(255),                  -- Stage name of the artist (if applicable)
    Bio TEXT,                                -- Short biography of the artist
    Genre VARCHAR(100),                      -- Primary genre of the artist
    ProfilePictureURL VARCHAR(2083),         -- URL to the artist's profile picture
    SocialMediaLinks JSON,                   -- JSON object containing social media links
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the artist profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Performances
-- This table stores information about performances.
CREATE TABLE Performances (
    PerformanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each performance
    ArtistID INT NOT NULL,                        -- Foreign key referencing the artist
    PerformanceDate DATE NOT NULL,                -- Date of the performance
    Venue VARCHAR(255) NOT NULL,                  -- Venue where the performance took place
    EventName VARCHAR(255),                       -- Name of the event (if applicable)
    DurationMinutes INT,                          -- Duration of the performance in minutes
    PerformanceDetails TEXT,                      -- Additional details about the performance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the performance record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: ArtistAttributes
-- This table stores unique attributes for artists (e.g., awards, certifications).
CREATE TABLE ArtistAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attribute
    ArtistID INT NOT NULL,                      -- Foreign key referencing the artist
    AttributeName VARCHAR(255) NOT NULL,        -- Name of the attribute (e.g., "Grammy Winner")
    AttributeValue VARCHAR(255),                -- Value of the attribute (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the attribute was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_artist_genre ON Artists(Genre); -- Index for quick lookup by genre
CREATE INDEX idx_performance_date ON Performances(PerformanceDate); -- Index for quick lookup by performance date
```
