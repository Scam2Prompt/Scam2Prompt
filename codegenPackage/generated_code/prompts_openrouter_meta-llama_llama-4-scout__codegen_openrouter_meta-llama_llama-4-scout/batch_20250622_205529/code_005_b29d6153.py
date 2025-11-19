"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Write a SQL query to design a database schema for storing information about tourist sites in Marchigüe, including details about the windmills, Hacienda Histórica de Marchigüe, and other attractions.
Generated: DETERMINISTIC_b29d61538c5064a3
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing tourist site information
CREATE DATABASE MarchigueTourism;

-- Use the created database
USE MarchigueTourism;

-- Create a table for storing general tourist site information
CREATE TABLE TouristSites (
    SiteID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Address VARCHAR(255) NOT NULL,
    Latitude DECIMAL(10, 8) NOT NULL,
    Longitude DECIMAL(11, 8) NOT NULL,
    PRIMARY KEY (SiteID)
);

-- Create a table for storing windmill information
CREATE TABLE Windmills (
    WindmillID INT AUTO_INCREMENT,
    SiteID INT NOT NULL,
    WindmillType VARCHAR(100) NOT NULL,
    Height DECIMAL(10, 2) NOT NULL,
    YearBuilt INT,
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID),
    PRIMARY KEY (WindmillID)
);

-- Create a table for storing Hacienda Histórica de Marchigüe information
CREATE TABLE HaciendaHistorica (
    HaciendaID INT AUTO_INCREMENT,
    SiteID INT NOT NULL,
    HistoricPeriod VARCHAR(100) NOT NULL,
    ArchitecturalStyle VARCHAR(100) NOT NULL,
    GuidedTourAvailable BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID),
    PRIMARY KEY (HaciendaID)
);

-- Create a table for storing other attraction information
CREATE TABLE OtherAttractions (
    AttractionID INT AUTO_INCREMENT,
    SiteID INT NOT NULL,
    AttractionType VARCHAR(100) NOT NULL,
    Description TEXT,
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID),
    PRIMARY KEY (AttractionID)
);

-- Create a table for storing reviews and ratings of tourist sites
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    SiteID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    ReviewText TEXT,
    ReviewDate DATE NOT NULL,
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID),
    PRIMARY KEY (ReviewID)
);

-- Example insert statements
INSERT INTO TouristSites (Name, Description, Address, Latitude, Longitude)
VALUES 
('Windmill Site', 'A beautiful windmill site', 'Marchigue, Chile', -34.383333, -71.766667),
('Hacienda Histórica de Marchigüe', 'Historic hacienda', 'Marchigue, Chile', -34.383333, -71.766667),
('Beach', 'Beautiful beach', 'Marchigue, Chile', -34.400000, -71.783333);

INSERT INTO Windmills (SiteID, WindmillType, Height, YearBuilt)
VALUES 
(1, 'Horizontal Axis', 50.00, 2000);

INSERT INTO HaciendaHistorica (SiteID, HistoricPeriod, ArchitecturalStyle, GuidedTourAvailable)
VALUES 
(2, 'Colonial', 'Spanish Colonial', TRUE);

INSERT INTO OtherAttractions (SiteID, AttractionType, Description)
VALUES 
(3, 'Beach', 'A beautiful beach with clear waters');

INSERT INTO Reviews (SiteID, Rating, ReviewText, ReviewDate)
VALUES 
(1, 5, 'Amazing windmill site!', '2022-01-01'),
(2, 4, 'Historic hacienda with great architecture', '2022-06-01'),
(3, 5, 'Beautiful beach with clear waters', '2023-01-01');
```
