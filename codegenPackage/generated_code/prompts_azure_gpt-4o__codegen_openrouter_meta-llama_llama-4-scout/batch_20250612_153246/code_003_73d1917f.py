"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Develop a database schema for storing information about surgical instruments, including fields for product categories like "Amputating Knives," "Micro Scissors," and "Plaster Scissors," as outlined on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_73d1917ff81b90dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for surgical instruments
CREATE DATABASE SurgicalInstrumentsDB;

-- Use the database
USE SurgicalInstrumentsDB;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for surgical instruments
CREATE TABLE SurgicalInstruments (
    InstrumentID INT AUTO_INCREMENT,
    CategoryID INT NOT NULL,
    InstrumentName VARCHAR(255) NOT NULL,
    Description TEXT,
    Material VARCHAR(100) NOT NULL,
    SterilizationMethod VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InstrumentID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Create a table for instrument specifications
CREATE TABLE InstrumentSpecifications (
    SpecificationID INT AUTO_INCREMENT,
    InstrumentID INT NOT NULL,
    Length DECIMAL(5,2) NOT NULL,
    Weight DECIMAL(5,2) NOT NULL,
    UnitOfMeasurement VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SpecificationID),
    FOREIGN KEY (InstrumentID) REFERENCES SurgicalInstruments(InstrumentID)
);

-- Insert product categories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Amputating Knives', 'Instruments used for amputating limbs or digits'),
('Micro Scissors', 'Instruments used for precise cutting in microsurgery'),
('Plaster Scissors', 'Instruments used for cutting plaster casts');

-- Insert surgical instruments
INSERT INTO SurgicalInstruments (CategoryID, InstrumentName, Description, Material, SterilizationMethod)
VALUES 
(1, 'Boyd Amputating Knife', 'A knife used for amputating limbs', 'Stainless Steel', 'Autoclaving'),
(1, 'Gigli Amputating Knife', 'A wire saw used for amputating limbs', 'Stainless Steel', 'Autoclaving'),
(2, 'Micro Scissors Curved', 'Curved micro scissors for precise cutting', 'Titanium', 'Ultrasonic Cleaning'),
(3, 'Plaster Scissors Straight', 'Straight scissors for cutting plaster casts', 'Stainless Steel', 'Autoclaving');

-- Insert instrument specifications
INSERT INTO InstrumentSpecifications (InstrumentID, Length, Weight, UnitOfMeasurement)
VALUES 
(1, 15.00, 20.00, 'cm'),
(2, 20.00, 30.00, 'cm'),
(3, 10.00, 5.00, 'cm'),
(4, 25.00, 40.00, 'cm');

-- Create views for easy data retrieval
CREATE VIEW InstrumentDetails AS
SELECT 
    si.InstrumentName,
    pc.CategoryName,
    si.Description,
    si.Material,
    si.SterilizationMethod,
    ispec.Length,
    ispec.Weight,
    ispec.UnitOfMeasurement
FROM 
    SurgicalInstruments si
JOIN 
    ProductCategories pc ON si.CategoryID = pc.CategoryID
JOIN 
    InstrumentSpecifications ispec ON si.InstrumentID = ispec.InstrumentID;

-- Create stored procedure to add new instrument
DELIMITER //
CREATE PROCEDURE AddNewInstrument(
    IN categoryID INT,
    IN instrumentName VARCHAR(255),
    IN description TEXT,
    IN material VARCHAR(100),
    IN sterilizationMethod VARCHAR(100),
    IN length DECIMAL(5,2),
    IN weight DECIMAL(5,2),
    IN unitOfMeasurement VARCHAR(50)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO SurgicalInstruments (CategoryID, InstrumentName, Description, Material, SterilizationMethod)
    VALUES (categoryID, instrumentName, description, material, sterilizationMethod);

    SET @instrumentID = LAST_INSERT_ID();

    INSERT INTO InstrumentSpecifications (InstrumentID, Length, Weight, UnitOfMeasurement)
    VALUES (@instrumentID, length, weight, unitOfMeasurement);

    COMMIT;
END//
DELIMITER ;
```
