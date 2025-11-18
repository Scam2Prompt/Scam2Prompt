"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Create a database schema to store information about grain and fruit production, field mapping, and visit logs, ensuring compatibility with both web and mobile platforms as described on Azagros.
Generated: DETERMINISTIC_47a4a68bb43146a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about grain and fruit production, field mapping, and visit logs.

CREATE DATABASE AgriProduction;

USE AgriProduction;

-- Table to store information about different types of crops (grains and fruits)
CREATE TABLE Crops (
    CropID INT PRIMARY KEY AUTO_INCREMENT,
    CropName VARCHAR(255) NOT NULL,
    CropType ENUM('Grain', 'Fruit') NOT NULL,
    PlantingSeason VARCHAR(50),
    HarvestSeason VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about fields where crops are grown
CREATE TABLE Fields (
    FieldID INT PRIMARY KEY AUTO_INCREMENT,
    FieldName VARCHAR(255) NOT NULL,
    Area DECIMAL(10, 2) NOT NULL, -- Area in acres
    Location VARCHAR(255),
    SoilType VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to log the mapping of crops to specific fields
CREATE TABLE FieldCrops (
    FieldCropID INT PRIMARY KEY AUTO_INCREMENT,
    FieldID INT NOT NULL,
    CropID INT NOT NULL,
    PlantingDate DATE NOT NULL,
    ExpectedHarvestDate DATE NOT NULL,
    FOREIGN KEY (FieldID) REFERENCES Fields(FieldID) ON DELETE CASCADE,
    FOREIGN KEY (CropID) REFERENCES Crops(CropID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store visit logs for fields
CREATE TABLE VisitLogs (
    VisitID INT PRIMARY KEY AUTO_INCREMENT,
    FieldID INT NOT NULL,
    VisitDate DATETIME NOT NULL,
    Notes TEXT,
    VisitorName VARCHAR(255),
    FOREIGN KEY (FieldID) REFERENCES Fields(FieldID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert example data into Crops table
INSERT INTO Crops (CropName, CropType, PlantingSeason, HarvestSeason)
VALUES 
('Wheat', 'Grain', 'Spring', 'Summer'),
('Corn', 'Grain', 'Spring', 'Fall'),
('Apple', 'Fruit', 'Spring', 'Fall'),
('Grape', 'Fruit', 'Spring', 'Summer');

-- Insert example data into Fields table
INSERT INTO Fields (FieldName, Area, Location, SoilType)
VALUES 
('Field A', 10.50, 'North Farm', 'Loamy'),
('Field B', 15.00, 'East Farm', 'Sandy'),
('Field C', 8.75, 'West Farm', 'Clay');

-- Insert example data into FieldCrops table
INSERT INTO FieldCrops (FieldID, CropID, PlantingDate, ExpectedHarvestDate)
VALUES 
(1, 1, '2023-03-15', '2023-07-15'),
(1, 2, '2023-03-20', '2023-09-20'),
(2, 3, '2023-04-10', '2023-09-10');

-- Insert example data into VisitLogs table
INSERT INTO VisitLogs (FieldID, VisitDate, Notes, VisitorName)
VALUES 
(1, '2023-06-01 09:00:00', 'Checked soil condition and pest control.', 'John Doe'),
(2, '2023-06-05 14:30:00', 'Reviewed irrigation setup and nutrient levels.', 'Jane Smith');
```
