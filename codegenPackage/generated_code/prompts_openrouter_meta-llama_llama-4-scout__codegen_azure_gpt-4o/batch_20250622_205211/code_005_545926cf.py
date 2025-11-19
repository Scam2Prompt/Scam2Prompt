"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Create a database schema to store information about the artists, exhibitions, and events organized by the Predaia Arte e Natura project.
Generated: DETERMINISTIC_545926cfb72c263c
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Predaia Arte e Natura project

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Full name of the artist
    Bio TEXT,                                -- Short biography of the artist
    Website VARCHAR(255),                   -- Website or portfolio link
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about exhibitions
CREATE TABLE Exhibitions (
    ExhibitionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each exhibition
    Title VARCHAR(255) NOT NULL,                 -- Title of the exhibition
    Description TEXT,                            -- Description of the exhibition
    StartDate DATE NOT NULL,                     -- Start date of the exhibition
    EndDate DATE NOT NULL,                       -- End date of the exhibition
    Location VARCHAR(255) NOT NULL,             -- Location of the exhibition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,            -- Name of the event
    Description TEXT,                      -- Description of the event
    EventDate DATETIME NOT NULL,           -- Date and time of the event
    Location VARCHAR(255) NOT NULL,       -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate artists with exhibitions
CREATE TABLE ArtistExhibitions (
    ArtistExhibitionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ArtistID INT NOT NULL,                             -- Foreign key referencing Artists table
    ExhibitionID INT NOT NULL,                         -- Foreign key referencing Exhibitions table
    Role VARCHAR(255),                                 -- Role of the artist in the exhibition (e.g., "Curator", "Participant")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE, -- Cascade delete for artist
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions(ExhibitionID) ON DELETE CASCADE -- Cascade delete for exhibition
);

-- Table to associate exhibitions with events
CREATE TABLE ExhibitionEvents (
    ExhibitionEventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ExhibitionID INT NOT NULL,                        -- Foreign key referencing Exhibitions table
    EventID INT NOT NULL,                             -- Foreign key referencing Events table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions(ExhibitionID) ON DELETE CASCADE, -- Cascade delete for exhibition
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete for event
);

-- Indexes for optimizing queries
CREATE INDEX idx_artist_name ON Artists(Name); -- Index for artist name
CREATE INDEX idx_exhibition_title ON Exhibitions(Title); -- Index for exhibition title
CREATE INDEX idx_event_name ON Events(Name); -- Index for event name
```
