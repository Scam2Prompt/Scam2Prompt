"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Create a database schema for storing advertising locations and formats, referencing WOW MEDIA's offerings like "Medios Exteriores" and "Canales especiales."
Generated: DETERMINISTIC_cede73b2d956f343
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing advertising locations and formats

-- Create the table to store advertising formats
CREATE TABLE AdvertisingFormats (
    FormatID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the advertising format
    FormatName VARCHAR(255) NOT NULL,        -- Name of the advertising format (e.g., "Medios Exteriores", "Canales especiales")
    Description TEXT                         -- Detailed description of the format
);

-- Create the table to store advertising locations
CREATE TABLE AdvertisingLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the advertising location
    LocationName VARCHAR(255) NOT NULL,        -- Name of the advertising location (e.g., "Downtown Billboard")
    Address TEXT,                              -- Address or detailed location of the advertising spot
    City VARCHAR(100),                         -- City of the advertising location
    State VARCHAR(100),                        -- State/region of the advertising location
    Country VARCHAR(100),                      -- Country of the advertising location
    Latitude DECIMAL(9, 6),                    -- Latitude coordinate for mapping
    Longitude DECIMAL(9, 6)                    -- Longitude coordinate for mapping
);

-- Create a junction table to associate advertising formats with locations
CREATE TABLE FormatLocationMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping record
    LocationID INT NOT NULL,                  -- Foreign key referencing AdvertisingLocations
    FormatID INT NOT NULL,                    -- Foreign key referencing AdvertisingFormats
    StartDate DATE NOT NULL,                  -- Start date for the advertising campaign
    EndDate DATE NOT NULL,                    -- End date for the advertising campaign
    Price DECIMAL(10, 2) NOT NULL,            -- Price for the advertising placement

    -- Foreign key constraints to ensure referential integrity
    FOREIGN KEY (LocationID) REFERENCES AdvertisingLocations(LocationID) ON DELETE CASCADE,
    FOREIGN KEY (FormatID) REFERENCES AdvertisingFormats(FormatID) ON DELETE CASCADE
);

-- Additional indexes for optimizing queries
CREATE INDEX idx_LocationName ON AdvertisingLocations(LocationName);
CREATE INDEX idx_FormatName ON AdvertisingFormats(FormatName);
CREATE INDEX idx_StartDate ON FormatLocationMapping(StartDate);
CREATE INDEX idx_EndDate ON FormatLocationMapping(EndDate);
```
