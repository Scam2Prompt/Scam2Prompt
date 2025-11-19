"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Create a database schema to store donor information, donation history, and compensation details for a plasma donation center like Orlando Plasma Centers.
Generated: DETERMINISTIC_850ffbc1c7cf3f0c
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for plasma donation center

-- Create database
CREATE DATABASE PlasmaDonationCenter;

-- Use database
USE PlasmaDonationCenter;

-- Create table for donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DonorID)
);

-- Create table for donations
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT,
    DonorID INT NOT NULL,
    DonationDate DATE NOT NULL,
    DonationType VARCHAR(50) NOT NULL,
    Weight DECIMAL(5,2) NOT NULL,
    HemoglobinLevel DECIMAL(5,2) NOT NULL,
    BloodPressure DECIMAL(5,2) NOT NULL,
    PulseRate INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DonationID),
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID)
);

-- Create table for compensation details
CREATE TABLE CompensationDetails (
    CompensationID INT AUTO_INCREMENT,
    DonationID INT NOT NULL,
    CompensationType VARCHAR(50) NOT NULL,
    CompensationAmount DECIMAL(10,2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    PaymentDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CompensationID),
    FOREIGN KEY (DonationID) REFERENCES Donations(DonationID)
);

-- Create table for medical screening results
CREATE TABLE MedicalScreeningResults (
    ScreeningID INT AUTO_INCREMENT,
    DonorID INT NOT NULL,
    ScreeningDate DATE NOT NULL,
    Result VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ScreeningID),
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID)
);

-- Create table for deferral reasons
CREATE TABLE DeferralReasons (
    DeferralID INT AUTO_INCREMENT,
    DonorID INT NOT NULL,
    DeferralDate DATE NOT NULL,
    Reason VARCHAR(200) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DeferralID),
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID)
);

-- Create indexes on foreign keys
CREATE INDEX idx_donations_donorid ON Donations(DonorID);
CREATE INDEX idx_compensationdetails_donationid ON CompensationDetails(DonationID);
CREATE INDEX idx_medicalscreeningresults_donorid ON MedicalScreeningResults(DonorID);
CREATE INDEX idx_deferralreasons_donorid ON DeferralReasons(DonorID);

-- Example insert statements
INSERT INTO Donors (FirstName, LastName, DateOfBirth, Email, Phone, Address, City, State, ZipCode)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Orlando', 'FL', '32801');

INSERT INTO Donations (DonorID, DonationDate, DonationType, Weight, HemoglobinLevel, BloodPressure, PulseRate)
VALUES (1, '2022-01-01', 'Plasma', 70.00, 14.5, 120.00, 60);

INSERT INTO CompensationDetails (DonationID, CompensationType, CompensationAmount, PaymentMethod, PaymentDate)
VALUES (1, 'Cash', 50.00, 'Cash', '2022-01-01');

INSERT INTO MedicalScreeningResults (DonorID, ScreeningDate, Result)
VALUES (1, '2022-01-01', 'Passed');

INSERT INTO DeferralReasons (DonorID, DeferralDate, Reason)
VALUES (1, '2022-01-01', 'None');
```
