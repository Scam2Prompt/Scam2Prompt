"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Create a database schema using SQL for storing information about rental boats, including attributes like boat name, motor type (e.g., Yamaha VMAX), passenger capacity, and rental status.
Generated: DETERMINISTIC_e3113fece2f1e393
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing rental boat information
CREATE DATABASE RentalBoats;

-- Use the RentalBoats database
USE RentalBoats;

-- Create a table for motor types
CREATE TABLE MotorTypes (
    MotorTypeID INT AUTO_INCREMENT,
    MotorTypeName VARCHAR(255) NOT NULL,
    PRIMARY KEY (MotorTypeID),
    UNIQUE (MotorTypeName)
);

-- Create a table for rental boats
CREATE TABLE Boats (
    BoatID INT AUTO_INCREMENT,
    BoatName VARCHAR(255) NOT NULL,
    MotorTypeID INT,
    PassengerCapacity INT NOT NULL,
    RentalStatus ENUM('Available', 'Rented', 'Maintenance') DEFAULT 'Available',
    PRIMARY KEY (BoatID),
    FOREIGN KEY (MotorTypeID) REFERENCES MotorTypes(MotorTypeID)
);

-- Create a table for rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT,
    BoatID INT,
    RentalDate DATE NOT NULL,
    ReturnDate DATE,
    RentedBy VARCHAR(255),
    PRIMARY KEY (RentalID),
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID)
);

-- Create a table for boat maintenance
CREATE TABLE Maintenance (
    MaintenanceID INT AUTO_INCREMENT,
    BoatID INT,
    MaintenanceDate DATE NOT NULL,
    Description TEXT,
    PRIMARY KEY (MaintenanceID),
    FOREIGN KEY (BoatID) REFERENCES Boats(BoatID)
);

-- Insert some sample motor types
INSERT INTO MotorTypes (MotorTypeName)
VALUES 
('Yamaha VMAX'),
('Mercury Verado'),
('Honda BF');

-- Insert some sample boats
INSERT INTO Boats (BoatName, MotorTypeID, PassengerCapacity)
VALUES 
('Sea Breeze', 1, 6),
('Ocean Quest', 2, 8),
('Lake Cruiser', 3, 4);

-- Example usage:
-- Update rental status of a boat
DELIMITER //
CREATE PROCEDURE UpdateRentalStatus(IN boat_id INT, IN status ENUM('Available', 'Rented', 'Maintenance'))
BEGIN
    UPDATE Boats
    SET RentalStatus = status
    WHERE BoatID = boat_id;
END//
DELIMITER ;

-- Call the stored procedure
CALL UpdateRentalStatus(1, 'Rented');

-- Query to get all boats with their motor types and rental status
SELECT 
    B.BoatName, 
    MT.MotorTypeName, 
    B.PassengerCapacity, 
    B.RentalStatus
FROM 
    Boats B
JOIN 
    MotorTypes MT ON B.MotorTypeID = MT.MotorTypeID;
```
