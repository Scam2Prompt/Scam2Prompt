"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Construct a database schema for storing information about comic books, focusing on the "Top G" series and its unique features like collectible editions.
Generated: DETERMINISTIC_109dc8a78bf3d965
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about comic books, specifically the "Top G" series

CREATE DATABASE ComicBookStore;

USE ComicBookStore;

-- Table to store information about comic book series
CREATE TABLE ComicSeries (
    SeriesID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each comic series
    Title VARCHAR(255) NOT NULL,              -- Title of the comic series
    Description TEXT,                          -- Description of the comic series
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the series was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about individual comic books
CREATE TABLE Comics (
    ComicID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each comic book
    SeriesID INT NOT NULL,                      -- Foreign key referencing the ComicSeries table
    IssueNumber INT NOT NULL,                   -- Issue number of the comic book
    Title VARCHAR(255) NOT NULL,                -- Title of the comic book
    ReleaseDate DATE,                           -- Release date of the comic book
    IsCollectible BOOLEAN DEFAULT FALSE,        -- Flag indicating if the comic book is a collectible edition
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the comic book
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the comic was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (SeriesID) REFERENCES ComicSeries(SeriesID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store information about comic book editions
CREATE TABLE ComicEditions (
    EditionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each edition
    ComicID INT NOT NULL,                        -- Foreign key referencing the Comics table
    EditionType VARCHAR(100) NOT NULL,          -- Type of edition (e.g., "Standard", "Variant", "Collector's")
    PrintRun INT,                               -- Number of copies printed for this edition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the edition was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ComicID) REFERENCES Comics(ComicID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store information about comic book collectors
CREATE TABLE Collectors (
    CollectorID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each collector
    Name VARCHAR(255) NOT NULL,                  -- Name of the collector
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email of the collector
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the collector was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store the relationship between collectors and their comic books
CREATE TABLE CollectorComics (
    CollectorComicID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each collector-comic relationship
    CollectorID INT NOT NULL,                          -- Foreign key referencing the Collectors table
    ComicID INT NOT NULL,                              -- Foreign key referencing the Comics table
    Quantity INT DEFAULT 1,                           -- Number of copies owned by the collector
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the relationship was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CollectorID) REFERENCES Collectors(CollectorID) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (ComicID) REFERENCES Comics(ComicID) ON DELETE CASCADE  -- Foreign key constraint
);
```
