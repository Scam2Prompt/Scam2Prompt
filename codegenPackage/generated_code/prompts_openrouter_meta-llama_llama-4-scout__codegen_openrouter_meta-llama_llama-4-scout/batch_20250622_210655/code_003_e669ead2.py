"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Design a simple database schema to store information about fishing reels, including models like Old School 1, Trout 2, and Salmon, with their respective line classes and prices."
Generated: DETERMINISTIC_e669ead2cc872023
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for fishing reels
CREATE DATABASE FishingReels;

-- Use the FishingReels database
USE FishingReels;

-- Create a table for fishing reel models
CREATE TABLE ReelModels (
    ModelID INT AUTO_INCREMENT,
    ModelName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ModelID)
);

-- Create a table for line classes
CREATE TABLE LineClasses (
    LineClassID INT AUTO_INCREMENT,
    LineClass VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (LineClassID)
);

-- Create a table for fishing reels
CREATE TABLE FishingReels (
    ReelID INT AUTO_INCREMENT,
    ModelID INT NOT NULL,
    LineClassID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ReelID),
    FOREIGN KEY (ModelID) REFERENCES ReelModels(ModelID),
    FOREIGN KEY (LineClassID) REFERENCES LineClasses(LineClassID)
);

-- Insert data into ReelModels table
INSERT INTO ReelModels (ModelName, Description)
VALUES 
('Old School1', 'A vintage fishing reel'),
('Trout2', 'A medium-light action fishing reel'),
('Salmon', 'A heavy action fishing reel');

-- Insert data into LineClasses table
INSERT INTO LineClasses (LineClass, Description)
VALUES 
('Light', 'For small fish and light lines'),
('Medium', 'For medium-sized fish and lines'),
('Heavy', 'For large fish and heavy lines');

-- Insert data into FishingReels table
INSERT INTO FishingReels (ModelID, LineClassID, Price)
VALUES 
(1, 1, 99.99),
(1, 2, 109.99),
(2, 2, 129.99),
(2, 3, 149.99),
(3, 3, 199.99);

-- Create a view to display fishing reels with model and line class information
CREATE VIEW ReelDetails AS
SELECT 
    fr.ReelID,
    rm.ModelName,
    lc.LineClass,
    fr.Price
FROM 
    FishingReels fr
INNER JOIN 
    ReelModels rm ON fr.ModelID = rm.ModelID
INNER JOIN 
    LineClasses lc ON fr.LineClassID = lc.LineClassID;

-- Select data from ReelDetails view
SELECT * FROM ReelDetails;
```
