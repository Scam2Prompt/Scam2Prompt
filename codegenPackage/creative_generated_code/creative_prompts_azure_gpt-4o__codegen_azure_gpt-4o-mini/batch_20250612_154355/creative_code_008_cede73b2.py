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
-- Database schema for storing advertising locations and formats for WOW MEDIA
-- This schema includes tables for advertising locations, formats, and their relationships.

-- Drop tables if they already exist (for development purposes)
DROP TABLE IF EXISTS AdvertisingLocations;
DROP TABLE IF EXISTS AdvertisingFormats;
DROP TABLE IF EXISTS LocationFormats;

-- Table to store unique advertising locations
CREATE TABLE AdvertisingLocations (
    LocationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each location
    LocationName VARCHAR(255) NOT NULL,         -- Name of the advertising location
    Description TEXT,                            -- Description of the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was updated
);

-- Table to store unique advertising formats
CREATE TABLE AdvertisingFormats (
    FormatID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each format
    FormatName VARCHAR(255) NOT NULL,            -- Name of the advertising format
    Description TEXT,                            -- Description of the format
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was updated
);

-- Junction table to associate locations with formats
CREATE TABLE LocationFormats (
    LocationFormatID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each location-format pair
    LocationID INT NOT NULL,                         -- Foreign key referencing AdvertisingLocations
    FormatID INT NOT NULL,                           -- Foreign key referencing AdvertisingFormats
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was updated
    FOREIGN KEY (LocationID) REFERENCES AdvertisingLocations(LocationID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (FormatID) REFERENCES AdvertisingFormats(FormatID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert sample data into AdvertisingLocations
INSERT INTO AdvertisingLocations (LocationName, Description) VALUES 
('Medios Exteriores', 'Outdoor advertising locations including billboards and transit ads.'),
('Canales especiales', 'Special channels for targeted advertising.');

-- Insert sample data into AdvertisingFormats
INSERT INTO AdvertisingFormats (FormatName, Description) VALUES 
('Billboard', 'Large outdoor advertisement structure.'),
('Digital Screen', 'Digital format for dynamic advertising.');

-- Insert sample data into LocationFormats
INSERT INTO LocationFormats (LocationID, FormatID) VALUES 
(1, 1),  -- Medios Exteriores with Billboard
(1, 2),  -- Medios Exteriores with Digital Screen
(2, 2);  -- Canales especiales with Digital Screen
```
