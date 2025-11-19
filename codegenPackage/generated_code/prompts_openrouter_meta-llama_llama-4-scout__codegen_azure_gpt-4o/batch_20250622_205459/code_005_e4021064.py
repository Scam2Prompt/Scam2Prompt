"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: "Design a database schema to store information on gemstones, including their names, properties, and meanings, and provide SQL queries to insert data on Amethyst and Blue Amethyst from the Wonderino articles."
Generated: DETERMINISTIC_e402106497f3170d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for storing information about gemstones
-- This schema includes tables for gemstones and their properties and meanings.

-- Create a table to store gemstone information
CREATE TABLE Gemstones (
    GemstoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gemstone
    Name VARCHAR(100) NOT NULL,               -- Name of the gemstone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store gemstone properties
CREATE TABLE GemstoneProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    GemstoneID INT NOT NULL,                   -- Foreign key referencing Gemstones table
    PropertyName VARCHAR(100) NOT NULL,        -- Name of the property (e.g., color, hardness)
    PropertyValue VARCHAR(255) NOT NULL,       -- Value of the property (e.g., purple, 7 on Mohs scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (GemstoneID) REFERENCES Gemstones(GemstoneID) ON DELETE CASCADE
);

-- Create a table to store gemstone meanings
CREATE TABLE GemstoneMeanings (
    MeaningID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each meaning
    GemstoneID INT NOT NULL,                   -- Foreign key referencing Gemstones table
    MeaningDescription TEXT NOT NULL,          -- Description of the gemstone's meaning
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (GemstoneID) REFERENCES Gemstones(GemstoneID) ON DELETE CASCADE
);

-- Insert data for Amethyst
INSERT INTO Gemstones (Name) VALUES ('Amethyst');

-- Retrieve the GemstoneID for Amethyst
SET @AmethystID = (SELECT GemstoneID FROM Gemstones WHERE Name = 'Amethyst');

-- Insert properties for Amethyst
INSERT INTO GemstoneProperties (GemstoneID, PropertyName, PropertyValue)
VALUES
(@AmethystID, 'Color', 'Purple'),
(@AmethystID, 'Hardness', '7 on Mohs scale');

-- Insert meanings for Amethyst
INSERT INTO GemstoneMeanings (GemstoneID, MeaningDescription)
VALUES
(@AmethystID, 'Amethyst is believed to promote calmness and clarity.');

-- Insert data for Blue Amethyst
INSERT INTO Gemstones (Name) VALUES ('Blue Amethyst');

-- Retrieve the GemstoneID for Blue Amethyst
SET @BlueAmethystID = (SELECT GemstoneID FROM Gemstones WHERE Name = 'Blue Amethyst');

-- Insert properties for Blue Amethyst
INSERT INTO GemstoneProperties (GemstoneID, PropertyName, PropertyValue)
VALUES
(@BlueAmethystID, 'Color', 'Blue'),
(@BlueAmethystID, 'Hardness', '7 on Mohs scale');

-- Insert meanings for Blue Amethyst
INSERT INTO GemstoneMeanings (GemstoneID, MeaningDescription)
VALUES
(@BlueAmethystID, 'Blue Amethyst is thought to enhance intuition and spiritual growth.');
```
