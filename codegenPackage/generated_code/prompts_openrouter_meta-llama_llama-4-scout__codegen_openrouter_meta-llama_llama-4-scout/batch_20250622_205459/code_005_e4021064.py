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
-- Create a database schema to store information on gemstones
CREATE DATABASE GemstoneDB;

-- Use the GemstoneDB database
USE GemstoneDB;

-- Create a table to store gemstone properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (PropertyID)
);

-- Create a table to store gemstone meanings
CREATE TABLE Meanings (
    MeaningID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (MeaningID)
);

-- Create a table to store gemstone information
CREATE TABLE Gemstones (
    GemstoneID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    PRIMARY KEY (GemstoneID)
);

-- Create a bridge table to store gemstone properties
CREATE TABLE GemstoneProperties (
    GemstoneID INT,
    PropertyID INT,
    Value VARCHAR(255),
    PRIMARY KEY (GemstoneID, PropertyID),
    FOREIGN KEY (GemstoneID) REFERENCES Gemstones(GemstoneID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID)
);

-- Create a bridge table to store gemstone meanings
CREATE TABLE GemstoneMeanings (
    GemstoneID INT,
    MeaningID INT,
    Description TEXT,
    PRIMARY KEY (GemstoneID, MeaningID),
    FOREIGN KEY (GemstoneID) REFERENCES Gemstones(GemstoneID),
    FOREIGN KEY (MeaningID) REFERENCES Meanings(MeaningID)
);

-- Insert data on Amethyst
INSERT INTO Gemstones (Name)
VALUES ('Amethyst');

SET @amethystId = LAST_INSERT_ID();

INSERT INTO Properties (Name, Description)
VALUES 
('Hardness', 'The resistance of a mineral to scratching'),
('Crystal Structure', 'The repeating pattern of a crystal''s atoms');

SET @hardnessId = LAST_INSERT_ID();
SET @crystalStructureId = LAST_INSERT_ID() - 1;

INSERT INTO GemstoneProperties (GemstoneID, PropertyID, Value)
VALUES 
(@amethystId, @hardnessId, '7'),
(@amethystId, @crystalStructureId, 'Trigonal');

INSERT INTO Meanings (Name, Description)
VALUES 
('Calming', 'Promotes peace and calmness'),
('Protection', 'Protects against negative energies');

SET @calmingId = LAST_INSERT_ID();
SET @protectionId = LAST_INSERT_ID() - 1;

INSERT INTO GemstoneMeanings (GemstoneID, MeaningID, Description)
VALUES 
(@amethystId, @calmingId, 'Amethyst is said to calm the mind and emotions'),
(@amethystId, @protectionId, 'Amethyst is believed to protect against negative energies');

-- Insert data on Blue Amethyst
INSERT INTO Gemstones (Name)
VALUES ('Blue Amethyst');

SET @blueAmethystId = LAST_INSERT_ID();

INSERT INTO Properties (Name, Description)
VALUES 
('Rarity', 'The scarcity of a gemstone');

SET @rarityId = LAST_INSERT_ID();

INSERT INTO GemstoneProperties (GemstoneID, PropertyID, Value)
VALUES 
(@blueAmethystId, @hardnessId, '7'),
(@blueAmethystId, @crystalStructureId, 'Trigonal'),
(@blueAmethystId, @rarityId, 'Rare');

INSERT INTO GemstoneMeanings (GemstoneID, MeaningID, Description)
VALUES 
(@blueAmethystId, @calmingId, 'Blue Amethyst is said to have a calming effect on the wearer'),
(@blueAmethystId, @protectionId, 'Blue Amethyst is believed to offer protection against negative energies');
```
