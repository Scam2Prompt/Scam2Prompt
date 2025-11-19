"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: "Design a database schema to store information about various Buddhist art pieces, including the พระพุทธรูปประจําวันเกิดวันพฤหัสบดี พระปางตรัสรู้หรือปางสมาธิ."
Generated: DETERMINISTIC_20f2866787d1ed31
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Buddhist art pieces

-- Create a table to store information about Buddhist art pieces
CREATE TABLE BuddhistArtPieces (
    ArtPieceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each art piece
    Name VARCHAR(255) NOT NULL,                -- Name of the art piece
    Description TEXT,                          -- Detailed description of the art piece
    OriginCountry VARCHAR(100),                -- Country of origin
    CreationDate DATE,                         -- Approximate creation date
    ArtType VARCHAR(100),                      -- Type of art (e.g., sculpture, painting)
    AssociatedDay VARCHAR(50),                 -- Associated day (e.g., Thursday for พระพุทธรูปประจําวันเกิดวันพฤหัสบดี)
    BuddhaPosture VARCHAR(100),                -- Buddha posture (e.g., ปางตรัสรู้ or ปางสมาธิ)
    ImageURL VARCHAR(255),                     -- URL to an image of the art piece
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store additional metadata or tags for Buddhist art pieces
CREATE TABLE ArtPieceTags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tag
    ArtPieceID INT NOT NULL,                   -- Foreign key referencing BuddhistArtPieces
    Tag VARCHAR(100) NOT NULL,                 -- Tag or keyword associated with the art piece
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the tag was created
    FOREIGN KEY (ArtPieceID) REFERENCES BuddhistArtPieces(ArtPieceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store information about artists or creators (if known)
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,                -- Name of the artist
    Biography TEXT,                            -- Short biography of the artist
    BirthDate DATE,                            -- Birth date of the artist
    DeathDate DATE,                            -- Death date of the artist (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to associate Buddhist art pieces with artists
CREATE TABLE ArtPieceArtists (
    ArtPieceID INT NOT NULL,                   -- Foreign key referencing BuddhistArtPieces
    ArtistID INT NOT NULL,                     -- Foreign key referencing Artists
    Role VARCHAR(100),                         -- Role of the artist (e.g., sculptor, painter)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the association was created
    PRIMARY KEY (ArtPieceID, ArtistID),        -- Composite primary key
    FOREIGN KEY (ArtPieceID) REFERENCES BuddhistArtPieces(ArtPieceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store information about exhibitions or locations where the art pieces are displayed
CREATE TABLE Exhibitions (
    ExhibitionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each exhibition
    Name VARCHAR(255) NOT NULL,                  -- Name of the exhibition or location
    Address TEXT,                                -- Address of the exhibition or location
    StartDate DATE,                              -- Start date of the exhibition
    EndDate DATE,                                -- End date of the exhibition (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to associate Buddhist art pieces with exhibitions
CREATE TABLE ArtPieceExhibitions (
    ArtPieceID INT NOT NULL,                   -- Foreign key referencing BuddhistArtPieces
    ExhibitionID INT NOT NULL,                 -- Foreign key referencing Exhibitions
    DisplayDate DATE,                          -- Date when the art piece was displayed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the association was created
    PRIMARY KEY (ArtPieceID, ExhibitionID),    -- Composite primary key
    FOREIGN KEY (ArtPieceID) REFERENCES BuddhistArtPieces(ArtPieceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions(ExhibitionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Example indexes for optimizing queries
CREATE INDEX idx_art_type ON BuddhistArtPieces(ArtType); -- Index for querying by art type
CREATE INDEX idx_associated_day ON BuddhistArtPieces(AssociatedDay); -- Index for querying by associated day
CREATE INDEX idx_buddha_posture ON BuddhistArtPieces(BuddhaPosture); -- Index for querying by Buddha posture
```
