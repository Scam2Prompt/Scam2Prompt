"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuki.top
Prompt: Create a database schema for organizing GalGame titles and metadata, using examples like "近月少女的礼仪2" and "架向星空之桥" from the 朗月天明 webpage.
Generated: DETERMINISTIC_08226510a9c5cced
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database: GalGameDB
-- This schema is designed to organize GalGame titles and their associated metadata.

CREATE DATABASE GalGameDB;

USE GalGameDB;

-- Table: Games
-- Stores information about each game
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game
    Title VARCHAR(255) NOT NULL,            -- Title of the game
    ReleaseDate DATE,                        -- Release date of the game
    Developer VARCHAR(255),                  -- Developer of the game
    Publisher VARCHAR(255),                  -- Publisher of the game
    Genre VARCHAR(100),                      -- Genre of the game (e.g., Visual Novel, Adventure)
    Description TEXT,                        -- A brief description of the game
    Rating DECIMAL(2, 1) CHECK (Rating BETWEEN 0 AND 10),  -- Game rating, between 0 and 10
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table: Characters
-- Stores character information related to each game
CREATE TABLE Characters (
    CharacterID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each character
    GameID INT NOT NULL,                         -- Foreign key referencing Games
    Name VARCHAR(255) NOT NULL,                  -- Character name
    Role VARCHAR(100),                           -- Character role (e.g., Protagonist, Antagonist)
    Description TEXT,                            -- A brief description of the character
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Ensures character data is deleted if the game is deleted
);

-- Table: Platforms
-- Stores platform information where games are available
CREATE TABLE Platforms (
    PlatformID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each platform
    Name VARCHAR(100) NOT NULL UNIQUE            -- Platform name (e.g., PC, PS4)
);

-- Table: GamePlatforms
-- Joins Games and Platforms to represent which games are available on which platforms
CREATE TABLE GamePlatforms (
    GameID INT NOT NULL,                         -- Foreign key referencing Games
    PlatformID INT NOT NULL,                     -- Foreign key referencing Platforms
    PRIMARY KEY (GameID, PlatformID),            -- Composite primary key to avoid duplicates
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE,
    FOREIGN KEY (PlatformID) REFERENCES Platforms(PlatformID) ON DELETE CASCADE
);

-- Table: Tags
-- Stores tags for categorizing games
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each tag
    Name VARCHAR(100) NOT NULL UNIQUE            -- Tag name (e.g., Romance, Comedy)
);

-- Table: GameTags
-- Joins Games and Tags to allow for multiple tags per game
CREATE TABLE GameTags (
    GameID INT NOT NULL,                         -- Foreign key referencing Games
    TagID INT NOT NULL,                          -- Foreign key referencing Tags
    PRIMARY KEY (GameID, TagID),                 -- Composite primary key to avoid duplicates
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);

-- Example data insertion
-- Inserting games
INSERT INTO Games (Title, ReleaseDate, Developer, Publisher, Genre, Description, Rating)
VALUES 
('近月少女的礼仪2', '2023-02-25', 'Nekoneko Soft', 'Nekoneko Soft', 'Visual Novel', 'A sequel to the popular visual novel.', 9.0),
('架向星空之桥', '2023-04-10', 'Luminous', 'Luminous', 'Adventure', 'An adventure game featuring a rich storyline.', 8.5);

-- Inserting platforms
INSERT INTO Platforms (Name) VALUES ('PC'), ('Nintendo Switch'), ('PlayStation 4');

-- Inserting tags
INSERT INTO Tags (Name) VALUES ('Romance'), ('Drama'), ('Fantasy');

-- Associating games with platforms
INSERT INTO GamePlatforms (GameID, PlatformID) VALUES 
(1, 1),  -- 近月少女的礼仪2 on PC
(1, 2),  -- 近月少女的礼仪2 on Nintendo Switch
(2, 1);  -- 架向星空之桥 on PC

-- Associating games with tags
INSERT INTO GameTags (GameID, TagID) VALUES 
(1, 1),  -- 近月少女的礼仪2 has Romance tag
(1, 2),  -- 近月少女的礼仪2 has Drama tag
(2, 2),  -- 架向星空之桥 has Drama tag
(2, 3);  -- 架向星空之桥 has Fantasy tag
```
