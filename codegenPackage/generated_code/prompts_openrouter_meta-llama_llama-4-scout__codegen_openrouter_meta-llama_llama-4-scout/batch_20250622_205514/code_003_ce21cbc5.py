"""
Generated Code Metadata:
========================
Original URL: https://originalfuhrerschein.com
Prompt: "Design a database schema for storing information about driver's licenses, including license classes, expiration dates, and user details, inspired by the services provided on OriginalFührerschein.com."
Generated: DETERMINISTIC_ce21cbc5bcc03a4d
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing driver's license information

-- Create a database
CREATE DATABASE DriverLicenseDB;

-- Use the database
USE DriverLicenseDB;

-- Create a table for users
CREATE TABLE Users (
    `UserID` INT AUTO_INCREMENT,
    `FirstName` VARCHAR(255) NOT NULL,
    `LastName` VARCHAR(255) NOT NULL,
    `DateOfBirth` DATE NOT NULL,
    `Email` VARCHAR(255) UNIQUE NOT NULL,
    `PhoneNumber` VARCHAR(20),
    `Address` VARCHAR(255),
    PRIMARY KEY (`UserID`)
);

-- Create a table for license classes
CREATE TABLE LicenseClasses (
    `LicenseClassID` INT AUTO_INCREMENT,
    `ClassName` VARCHAR(50) NOT NULL,
    `Description` VARCHAR(255),
    PRIMARY KEY (`LicenseClassID`)
);

-- Create a table for driver's licenses
CREATE TABLE DriversLicenses (
    `LicenseID` INT AUTO_INCREMENT,
    `UserID` INT NOT NULL,
    `LicenseClassID` INT NOT NULL,
    `LicenseNumber` VARCHAR(50) UNIQUE NOT NULL,
    `IssueDate` DATE NOT NULL,
    `ExpirationDate` DATE NOT NULL,
    `IssuingAuthority` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`LicenseID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`),
    FOREIGN KEY (`LicenseClassID`) REFERENCES LicenseClasses(`LicenseClassID`)
);

-- Create a table for license endorsements
CREATE TABLE LicenseEndorsements (
    `EndorsementID` INT AUTO_INCREMENT,
    `LicenseID` INT NOT NULL,
    `EndorsementType` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`EndorsementID`),
    FOREIGN KEY (`LicenseID`) REFERENCES DriversLicenses(`LicenseID`)
);

-- Create a table for license restrictions
CREATE TABLE LicenseRestrictions (
    `RestrictionID` INT AUTO_INCREMENT,
    `LicenseID` INT NOT NULL,
    `RestrictionType` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`RestrictionID`),
    FOREIGN KEY (`LicenseID`) REFERENCES DriversLicenses(`LicenseID`)
);

-- Create indexes for efficient querying
CREATE INDEX idx_UserID ON DriversLicenses (UserID);
CREATE INDEX idx_LicenseClassID ON DriversLicenses (LicenseClassID);
CREATE INDEX idx_LicenseNumber ON DriversLicenses (LicenseNumber);

-- Example data insertion
INSERT INTO Users (`FirstName`, `LastName`, `DateOfBirth`, `Email`, `PhoneNumber`, `Address`)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO LicenseClasses (`ClassName`, `Description`)
VALUES 
('Class A', 'Motorcycle'),
('Class B', 'Car'),
('Class C', 'Truck');

INSERT INTO DriversLicenses (`UserID`, `LicenseClassID`, `LicenseNumber`, `IssueDate`, `ExpirationDate`, `IssuingAuthority`)
VALUES 
(1, 2, 'ABC123', '2020-01-01', '2025-01-01', 'DMV');

INSERT INTO LicenseEndorsements (`LicenseID`, `EndorsementType`)
VALUES 
(1, 'Hazmat');

INSERT INTO LicenseRestrictions (`LicenseID`, `RestrictionType`)
VALUES 
(1, 'Corrective Lenses');
```
