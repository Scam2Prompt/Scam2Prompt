"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: "Design a database schema to store information about boats, including their make, model, horsepower, and rental rates, for a boat rental company in South Africa."
Generated: DETERMINISTIC_e1220614145f6cbc
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the boat rental company
CREATE DATABASE BoatRentalCompany;

-- Use the database
USE BoatRentalCompany;

-- Create a table to store boat manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT,
    ManufacturerName VARCHAR(255) NOT NULL,
    PRIMARY KEY (ManufacturerID)
);

-- Create a table to store boat models
CREATE TABLE Models (
    ModelID INT AUTO_INCREMENT,
    ModelName VARCHAR(255) NOT NULL,
    ManufacturerID INT,
    Horsepower DECIMAL(5,2),
    PRIMARY KEY (ModelID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID)
);

-- Create a table to store boats
CREATE TABLE Boats (
    BoatID INT AUTO_INCREMENT,
    ModelID INT,
    BoatName VARCHAR(255) NOT NULL,
    YearBuilt INT,
    PRIMARY KEY (BoatID),
    FOREIGN KEY (ModelID) REFERENCES Models(ModelID)
);

-- Create a table to store rental rates
CREATE TABLE RentalRates (
    RentalRateID INT AUTO_INCREMENT,
    BoatID INT,
    Rate DECIMAL(10,2) NOT NULL,
    Currency VARCHAR(10) NOT NULL DEFAULT 'ZAR',
    RentalDuration VARCHAR(50) NOT NULL,
    PRIMARY KEY (RentalRateID),
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID)
);

-- Create a table to store boat availability and rental status
CREATE TABLE BoatAvailability (
    AvailabilityID INT AUTO_INCREMENT,
    BoatID INT,
    RentalStatus VARCHAR(50) NOT NULL DEFAULT 'Available',
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AvailabilityID),
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID)
);

-- Create a table to store customer rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT,
    BoatID INT,
    RentalDate DATE NOT NULL,
    ReturnDate DATE,
    CustomerName VARCHAR(255) NOT NULL,
    PRIMARY KEY (RentalID),
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID)
);

-- Insert sample data
INSERT INTO Manufacturers (ManufacturerName)
VALUES 
('Bavaria'),
('Bennington'),
('Boston Whaler');

INSERT INTO Models (ModelName, ManufacturerID, Horsepower)
VALUES 
('Bavaria 40', 1, 200.00),
('Bennington 25SLX', 2, 150.00),
('Boston Whaler Outrage 23', 3, 250.00);

INSERT INTO Boats (ModelID, BoatName, YearBuilt)
VALUES 
(1, 'Sea Breeze', 2020),
(2, 'Lake Life', 2019),
(3, 'Ocean Quest', 2021);

INSERT INTO RentalRates (BoatID, Rate, RentalDuration)
VALUES 
(1, 1500.00, 'Daily'),
(1, 8000.00, 'Weekly'),
(2, 1200.00, 'Daily'),
(2, 6000.00, 'Weekly'),
(3, 1800.00, 'Daily'),
(3, 9000.00, 'Weekly');

INSERT INTO BoatAvailability (BoatID)
VALUES 
(1),
(2),
(3);

-- Example query to retrieve boat information with rental rates
SELECT 
    b.BoatName,
    m.ModelName,
    ma.ManufacturerName,
    b.YearBuilt,
    rr.Rate,
    rr.RentalDuration
FROM 
    Boats b
JOIN 
    Models m ON b.ModelID = m.ModelID
JOIN 
    Manufacturers ma ON m.ManufacturerID = ma.ManufacturerID
JOIN 
    RentalRates rr ON b.BoatID = rr.BoatID;
```
