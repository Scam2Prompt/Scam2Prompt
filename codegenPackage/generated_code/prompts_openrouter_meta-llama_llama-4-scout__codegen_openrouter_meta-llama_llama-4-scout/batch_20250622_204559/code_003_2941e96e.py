"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: "Design a database schema for storing information about volunteers, donors, and beneficiaries for an organization like Armaghan-e-Najaf."
Generated: DETERMINISTIC_2941e96e7a8c2933
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Armaghan-e-Najaf organization

-- Create database
CREATE DATABASE Armaghan_e_Najaf;

-- Use database
USE Armaghan_e_Najaf;

-- Create table for volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    DateOfBirth DATE,
    JoinDate DATE NOT NULL,
    Active TINYINT(1) DEFAULT 1,
    PRIMARY KEY (VolunteerID)
);

-- Create table for donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    DateOfBirth DATE,
    DonationFrequency ENUM('One-time', 'Monthly', 'Quarterly') DEFAULT 'One-time',
    LastDonationDate DATE,
    TotalDonations DECIMAL(10, 2) DEFAULT 0.00,
    Active TINYINT(1) DEFAULT 1,
    PRIMARY KEY (DonorID)
);

-- Create table for beneficiaries
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    DateOfBirth DATE,
    BeneficiaryType ENUM('Individual', 'Family', 'Group') NOT NULL,
    EnrollmentDate DATE NOT NULL,
    Active TINYINT(1) DEFAULT 1,
    PRIMARY KEY (BeneficiaryID)
);

-- Create table for volunteer activities
CREATE TABLE VolunteerActivities (
    ActivityID INT AUTO_INCREMENT,
    VolunteerID INT NOT NULL,
    ActivityDate DATE NOT NULL,
    ActivityType ENUM('Fundraising', 'Event Management', 'Community Service') NOT NULL,
    HoursWorked DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (ActivityID),
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE
);

-- Create table for donations
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT,
    DonorID INT NOT NULL,
    DonationDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    DonationType ENUM('Cash', 'Check', 'Online') NOT NULL,
    PRIMARY KEY (DonationID),
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE
);

-- Create table for beneficiary services
CREATE TABLE BeneficiaryServices (
    ServiceID INT AUTO_INCREMENT,
    BeneficiaryID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceType ENUM('Food', 'Shelter', 'Medical') NOT NULL,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Create stored procedure to add new volunteer
DELIMITER //
CREATE PROCEDURE AddVolunteer(
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_Phone VARCHAR(20),
    IN p_Address VARCHAR(255),
    IN p_City VARCHAR(100),
    IN p_State VARCHAR(100),
    IN p_Country VARCHAR(100),
    IN p_PostalCode VARCHAR(20),
    IN p_DateOfBirth DATE,
    IN p_JoinDate DATE
)
BEGIN
    INSERT INTO Volunteers (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode, DateOfBirth, JoinDate)
    VALUES (p_FirstName, p_LastName, p_Email, p_Phone, p_Address, p_City, p_State, p_Country, p_PostalCode, p_DateOfBirth, p_JoinDate);
END//
DELIMITER ;

-- Create stored procedure to add new donor
DELIMITER //
CREATE PROCEDURE AddDonor(
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_Phone VARCHAR(20),
    IN p_Address VARCHAR(255),
    IN p_City VARCHAR(100),
    IN p_State VARCHAR(100),
    IN p_Country VARCHAR(100),
    IN p_PostalCode VARCHAR(20),
    IN p_DateOfBirth DATE
)
BEGIN
    INSERT INTO Donors (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode, DateOfBirth)
    VALUES (p_FirstName, p_LastName, p_Email, p_Phone, p_Address, p_City, p_State, p_Country, p_PostalCode, p_DateOfBirth);
END//
DELIMITER ;

-- Create stored procedure to add new beneficiary
DELIMITER //
CREATE PROCEDURE AddBeneficiary(
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_Phone VARCHAR(20),
    IN p_Address VARCHAR(255),
    IN p_City VARCHAR(100),
    IN p_State VARCHAR(100),
    IN p_Country VARCHAR(100),
    IN p_PostalCode VARCHAR(20),
    IN p_DateOfBirth DATE,
    IN p_BeneficiaryType ENUM('Individual', 'Family', 'Group'),
    IN p_EnrollmentDate DATE
)
BEGIN
    INSERT INTO Beneficiaries (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode, DateOfBirth, BeneficiaryType, EnrollmentDate)
    VALUES (p_FirstName, p_LastName, p_Email, p_Phone, p_Address, p_City, p_State, p_Country, p_PostalCode, p_DateOfBirth, p_BeneficiaryType, p_EnrollmentDate);
END//
DELIMITER ;
```
