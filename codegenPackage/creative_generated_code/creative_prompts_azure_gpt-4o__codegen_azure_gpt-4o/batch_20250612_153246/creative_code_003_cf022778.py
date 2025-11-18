"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkcs.org
Prompt: Suggest a database schema for storing information about Morahs and their placement options, as described by ZKCS.
Generated: DETERMINISTIC_cf022778168eb17c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing Morahs and their placement options
-- Based on ZKCS requirements

-- Table to store information about Morahs
CREATE TABLE Morahs (
    MorahID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each Morah
    FirstName VARCHAR(50) NOT NULL,         -- First name of the Morah
    LastName VARCHAR(50) NOT NULL,          -- Last name of the Morah
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                -- Phone number of the Morah
    Specialization VARCHAR(100),            -- Area of expertise or specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update timestamp
);

-- Table to store placement options for Morahs
CREATE TABLE PlacementOptions (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for placement option
    LocationName VARCHAR(100) NOT NULL,         -- Name of the placement location
    Address VARCHAR(255),                       -- Address of the placement location
    City VARCHAR(50) NOT NULL,                  -- City where the placement is located
    State VARCHAR(50),                          -- State where the placement is located
    ZipCode VARCHAR(10),                        -- Zip code for the placement location
    ContactPerson VARCHAR(100),                 -- Name of the contact person at the location
    ContactEmail VARCHAR(100),                  -- Email of the contact person
    ContactPhone VARCHAR(15),                   -- Phone number for the contact person
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update timestamp
);

-- Table to link Morahs with their placement options (many-to-many relationship)
CREATE TABLE MorahPlacements (
    MorahPlacementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for Morah placement
    MorahID INT NOT NULL,                            -- Foreign key referencing Morahs table
    PlacementID INT NOT NULL,                        -- Foreign key referencing PlacementOptions table
    PlacementDate DATE,                              -- Date when the placement was assigned
    Notes TEXT,                                      -- Additional notes about the placement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update timestamp
    FOREIGN KEY (MorahID) REFERENCES Morahs(MorahID) ON DELETE CASCADE, -- Cascade delete for Morahs
    FOREIGN KEY (PlacementID) REFERENCES PlacementOptions(PlacementID) ON DELETE CASCADE -- Cascade delete for placement options
);

-- Indexes for optimizing queries
CREATE INDEX idx_MorahName ON Morahs (FirstName, LastName);
CREATE INDEX idx_PlacementLocation ON PlacementOptions (City, State);
CREATE INDEX idx_MorahPlacement ON MorahPlacements (MorahID, PlacementID);
```
