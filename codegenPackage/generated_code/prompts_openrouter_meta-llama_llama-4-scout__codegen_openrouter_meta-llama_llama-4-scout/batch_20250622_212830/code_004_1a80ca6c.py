"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Write a SQL query to store and retrieve information about different types of stones and pebbles, including their certification and quality.
Generated: DETERMINISTIC_1a80ca6c22ff88e3
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing stone and pebble information
CREATE DATABASE StoneDatabase;

-- Use the StoneDatabase
USE StoneDatabase;

-- Create a table for stone types
CREATE TABLE StoneTypes (
    StoneTypeID INT AUTO_INCREMENT,
    StoneTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (StoneTypeID)
);

-- Create a table for pebble types
CREATE TABLE PebbleTypes (
    PebbleTypeID INT AUTO_INCREMENT,
    PebbleTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (PebbleTypeID)
);

-- Create a table for certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT,
    CertificationName VARCHAR(255) NOT NULL,
    IssuingOrganization VARCHAR(255) NOT NULL,
    PRIMARY KEY (CertificationID)
);

-- Create a table for stone quality
CREATE TABLE StoneQuality (
    StoneQualityID INT AUTO_INCREMENT,
    StoneQualityName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (StoneQualityID)
);

-- Create a table for stones
CREATE TABLE Stones (
    StoneID INT AUTO_INCREMENT,
    StoneTypeID INT NOT NULL,
    CertificationID INT,
    StoneQualityID INT NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Dimensions VARCHAR(255) NOT NULL,
    PRIMARY KEY (StoneID),
    FOREIGN KEY (StoneTypeID) REFERENCES StoneTypes(StoneTypeID),
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID),
    FOREIGN KEY (StoneQualityID) REFERENCES StoneQuality(StoneQualityID)
);

-- Create a table for pebbles
CREATE TABLE Pebbles (
    PebbleID INT AUTO_INCREMENT,
    PebbleTypeID INT NOT NULL,
    CertificationID INT,
    StoneQualityID INT NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Dimensions VARCHAR(255) NOT NULL,
    PRIMARY KEY (PebbleID),
    FOREIGN KEY (PebbleTypeID) REFERENCES PebbleTypes(PebbleTypeID),
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID),
    FOREIGN KEY (StoneQualityID) REFERENCES StoneQuality(StoneQualityID)
);

-- Insert sample data into StoneTypes table
INSERT INTO StoneTypes (StoneTypeName, Description)
VALUES 
('Marble', 'A metamorphic rock'),
('Granite', 'A type of igneous rock'),
('Limestone', 'A sedimentary rock');

-- Insert sample data into PebbleTypes table
INSERT INTO PebbleTypes (PebbleTypeName, Description)
VALUES 
('River Rock', 'Smooth rocks found in rivers'),
('Sea Stone', 'Pebbles found in the ocean'),
('Polished Pebble', 'Man-made polished pebbles');

-- Insert sample data into Certifications table
INSERT INTO Certifications (CertificationName, IssuingOrganization)
VALUES 
('GIA', 'Gemological Institute of America'),
('AGL', 'American Gem Laboratory');

-- Insert sample data into StoneQuality table
INSERT INTO StoneQuality (StoneQualityName, Description)
VALUES 
('High', 'Exceptional quality'),
('Medium', 'Average quality'),
('Low', 'Poor quality');

-- Insert sample data into Stones table
INSERT INTO Stones (StoneTypeID, CertificationID, StoneQualityID, Weight, Dimensions)
VALUES 
(1, 1, 1, 5.00, '10cm x 5cm x 2cm'),
(2, 2, 2, 10.00, '20cm x 10cm x 5cm'),
(3, NULL, 3, 2.00, '5cm x 2cm x 1cm');

-- Insert sample data into Pebbles table
INSERT INTO Pebbles (PebbleTypeID, CertificationID, StoneQualityID, Weight, Dimensions)
VALUES 
(1, NULL, 2, 0.50, '2cm x 1cm x 0.5cm'),
(2, 1, 1, 1.00, '5cm x 2cm x 1cm'),
(3, NULL, 3, 0.25, '1cm x 0.5cm x 0.25cm');

-- Retrieve all stone information
SELECT 
    s.StoneID,
    st.StoneTypeName,
    c.CertificationName,
    sq.StoneQualityName,
    s.Weight,
    s.Dimensions
FROM 
    Stones s
INNER JOIN 
    StoneTypes st ON s.StoneTypeID = st.StoneTypeID
LEFT JOIN 
    Certifications c ON s.CertificationID = c.CertificationID
INNER JOIN 
    StoneQuality sq ON s.StoneQualityID = sq.StoneQualityID;

-- Retrieve all pebble information
SELECT 
    p.PebbleID,
    pt.PebbleTypeName,
    c.CertificationName,
    sq.StoneQualityName,
    p.Weight,
    p.Dimensions
FROM 
    Pebbles p
INNER JOIN 
    PebbleTypes pt ON p.PebbleTypeID = pt.PebbleTypeID
LEFT JOIN 
    Certifications c ON p.CertificationID = c.CertificationID
INNER JOIN 
    StoneQuality sq ON p.StoneQualityID = sq.StoneQualityID;
```
