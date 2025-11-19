"""
Generated Code Metadata:
========================
Original URL: https://pumpx.me
Prompt: "Design a database schema to store information about industrial equipment, including the BriX, Grautex, and PanelX series, and their applications in various industries."
Generated: DETERMINISTIC_054b71d97586e8b7
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for industrial equipment

CREATE DATABASE IndustrialEquipment;

USE IndustrialEquipment;

-- Define a table for equipment manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT,
    ManufacturerName VARCHAR(255) NOT NULL,
    PRIMARY KEY (ManufacturerID)
);

-- Define a table for equipment series
CREATE TABLE EquipmentSeries (
    SeriesID INT AUTO_INCREMENT,
    ManufacturerID INT NOT NULL,
    SeriesName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (SeriesID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID)
);

-- Define a table for equipment models
CREATE TABLE EquipmentModels (
    ModelID INT AUTO_INCREMENT,
    SeriesID INT NOT NULL,
    ModelName VARCHAR(255) NOT NULL,
    ModelDescription TEXT,
    PRIMARY KEY (ModelID),
    FOREIGN KEY (SeriesID) REFERENCES EquipmentSeries(SeriesID)
);

-- Define a table for industries
CREATE TABLE Industries (
    IndustryID INT AUTO_INCREMENT,
    IndustryName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (IndustryID)
);

-- Define a table for equipment applications
CREATE TABLE EquipmentApplications (
    ApplicationID INT AUTO_INCREMENT,
    ModelID INT NOT NULL,
    IndustryID INT NOT NULL,
    ApplicationDescription TEXT,
    PRIMARY KEY (ApplicationID),
    FOREIGN KEY (ModelID) REFERENCES EquipmentModels(ModelID),
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID)
);

-- Insert sample data for manufacturers
INSERT INTO Manufacturers (ManufacturerName)
VALUES 
('BriX'),
('Grautex'),
('PanelX');

-- Insert sample data for equipment series
INSERT INTO EquipmentSeries (ManufacturerID, SeriesName, Description)
VALUES 
(1, 'BriX Series', 'BriX series equipment'),
(2, 'Grautex Series', 'Grautex series equipment'),
(3, 'PanelX Series', 'PanelX series equipment');

-- Insert sample data for equipment models
INSERT INTO EquipmentModels (SeriesID, ModelName, ModelDescription)
VALUES 
(1, 'BriX-1000', 'BriX-1000 model description'),
(1, 'BriX-2000', 'BriX-2000 model description'),
(2, 'Grautex-500', 'Grautex-500 model description'),
(3, 'PanelX-100', 'PanelX-100 model description');

-- Insert sample data for industries
INSERT INTO Industries (IndustryName, Description)
VALUES 
('Manufacturing', 'Manufacturing industry'),
('Construction', 'Construction industry'),
('Energy', 'Energy industry');

-- Insert sample data for equipment applications
INSERT INTO EquipmentApplications (ModelID, IndustryID, ApplicationDescription)
VALUES 
(1, 1, 'BriX-1000 used in manufacturing'),
(1, 2, 'BriX-1000 used in construction'),
(2, 1, 'BriX-2000 used in manufacturing'),
(3, 3, 'Grautex-500 used in energy'),
(4, 1, 'PanelX-100 used in manufacturing');

-- Create views for easier data retrieval
CREATE VIEW EquipmentInformation AS
SELECT 
    M.ManufacturerName,
    ES.SeriesName,
    EM.ModelName,
    EM.ModelDescription
FROM 
    EquipmentModels EM
JOIN 
    EquipmentSeries ES ON EM.SeriesID = ES.SeriesID
JOIN 
    Manufacturers M ON ES.ManufacturerID = M.ManufacturerID;

CREATE VIEW EquipmentApplicationsView AS
SELECT 
    EM.ModelName,
    I.IndustryName,
    EA.ApplicationDescription
FROM 
    EquipmentApplications EA
JOIN 
    EquipmentModels EM ON EA.ModelID = EM.ModelID
JOIN 
    Industries I ON EA.IndustryID = I.IndustryID;

-- Create stored procedures for common operations
DELIMITER //
CREATE PROCEDURE GetEquipmentInformation()
BEGIN
    SELECT * FROM EquipmentInformation;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetEquipmentApplications()
BEGIN
    SELECT * FROM EquipmentApplicationsView;
END//
DELIMITER ;

-- Call stored procedures
CALL GetEquipmentInformation();
CALL GetEquipmentApplications();
```
