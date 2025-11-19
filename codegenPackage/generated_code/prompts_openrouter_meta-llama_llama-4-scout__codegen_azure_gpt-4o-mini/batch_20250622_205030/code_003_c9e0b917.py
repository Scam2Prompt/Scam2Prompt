"""
Generated Code Metadata:
========================
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Design a basic database schema for storing information about digital characters (e.g., Palio) and their respective voting counts in an event, using SQL.
Generated: DETERMINISTIC_c9e0b91783e6b53a
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing digital character information and voting counts
CREATE DATABASE DigitalCharacterVoting;

-- Use the created database
USE DigitalCharacterVoting;

-- Create a table to store information about digital characters
CREATE TABLE Characters (
    CharacterID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each character
    CharacterName VARCHAR(100) NOT NULL,          -- Name of the character
    Description TEXT,                              -- Description of the character
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the character was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store voting information
CREATE TABLE Votes (
    VoteID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each vote
    CharacterID INT NOT NULL,                      -- Foreign key referencing the character
    VoteCount INT DEFAULT 0,                       -- Number of votes for the character
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the vote was recorded
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on CharacterID in Votes table for faster lookups
CREATE INDEX idx_character_votes ON Votes(CharacterID);

-- Sample insert statements for testing
INSERT INTO Characters (CharacterName, Description) VALUES 
('Palio', 'A brave digital character known for its agility.'),
('Zyra', 'A mystical character with magical powers.');

INSERT INTO Votes (CharacterID, VoteCount) VALUES 
(1, 100),  -- Votes for Palio
(2, 150);  -- Votes for Zyra

-- Query to retrieve all characters and their vote counts
SELECT c.CharacterName, c.Description, COALESCE(v.VoteCount, 0) AS VoteCount
FROM Characters c
LEFT JOIN Votes v ON c.CharacterID = v.CharacterID;
```
