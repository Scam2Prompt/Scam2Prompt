"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Design a database schema for storing artist profiles and performance history for Tree House Sessions, ensuring it captures unique attributes mentioned in the content.
Generated: DETERMINISTIC_ab2f3d4907d1c0d9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tree House Sessions

-- Table: Artists
-- This table stores information about artists participating in Tree House Sessions.
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,                     -- Artist's name
    Bio TEXT,                                       -- Short biography of the artist
    Genre VARCHAR(100),                             -- Musical genre(s) the artist specializes in
    ProfilePictureURL VARCHAR(2083),                -- URL for the artist's profile picture
    SocialMediaLinks JSON,                          -- Social media links (stored as JSON for flexibility)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the artist profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the profile was last updated
);

-- Table: Performances
-- This table stores information about past performances in Tree House Sessions.
CREATE TABLE Performances (
    PerformanceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each performance
    ArtistID INT NOT NULL,                          -- Foreign key referencing the artist who performed
    PerformanceDate DATE NOT NULL,                  -- Date of the performance
    Venue VARCHAR(255) NOT NULL,                    -- Venue where the performance took place
    SetList JSON,                                   -- List of songs performed (stored as JSON)
    VideoURL VARCHAR(2083),                         -- URL to performance video recording (if available)
    Notes TEXT,                                     -- Additional notes about the performance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the performance record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    CONSTRAINT FK_Performance_Artist FOREIGN KEY (ArtistID) 
        REFERENCES Artists(ArtistID) 
        ON DELETE CASCADE                            -- Delete performances if the associated artist is deleted
);

-- Indexing to improve query performance
CREATE INDEX IDX_Artist_Genre ON Artists(Genre);    -- Index on Genre for efficient queries
CREATE INDEX IDX_Performance_Date ON Performances(PerformanceDate); -- Index on PerformanceDate

-- Example error handling in SQL scripts (not runnable, but good practice):
-- Ensure the database supports JSON datatype (e.g., MySQL 5.7+)
-- Add a TRY-CATCH block or equivalent error handling mechanism in application code where SQL queries are executed.
```
