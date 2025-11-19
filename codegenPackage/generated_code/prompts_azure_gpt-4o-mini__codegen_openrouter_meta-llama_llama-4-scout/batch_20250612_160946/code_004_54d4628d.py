"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema in SQL to manage the records of beneficiaries receiving support from the Rakhshanda Memorial's medical camps and psychological health services.
Generated: DETERMINISTIC_54d4628dca4aeffc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Rakhshanda Memorial's medical camps and psychological health services
CREATE DATABASE RakhshandaMemorial;

-- Use the created database
USE RakhshandaMemorial;

-- Create table for beneficiaries
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BeneficiaryID)
);

-- Create table for medical camps
CREATE TABLE MedicalCamps (
    CampID INT AUTO_INCREMENT,
    CampName VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CampID)
);

-- Create table for psychological health services
CREATE TABLE PsychologicalServices (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for beneficiary medical camp records
CREATE TABLE BeneficiaryMedicalCamps (
    RecordID INT AUTO_INCREMENT,
    BeneficiaryID INT NOT NULL,
    CampID INT NOT NULL,
    VisitDate DATE NOT NULL,
    Diagnosis TEXT,
    Treatment TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RecordID),
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (CampID) REFERENCES MedicalCamps(CampID) ON DELETE CASCADE
);

-- Create table for beneficiary psychological service records
CREATE TABLE BeneficiaryPsychologicalServices (
    RecordID INT AUTO_INCREMENT,
    BeneficiaryID INT NOT NULL,
    ServiceID INT NOT NULL,
    SessionDate DATE NOT NULL,
    SessionNotes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RecordID),
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES PsychologicalServices(ServiceID) ON DELETE CASCADE
);

-- Create table for medical camp staff
CREATE TABLE MedicalCampStaff (
    StaffID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StaffID)
);

-- Create table for medical camp staff attendance
CREATE TABLE MedicalCampStaffAttendance (
    AttendanceID INT AUTO_INCREMENT,
    StaffID INT NOT NULL,
    CampID INT NOT NULL,
    AttendanceDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AttendanceID),
    FOREIGN KEY (StaffID) REFERENCES MedicalCampStaff(StaffID) ON DELETE CASCADE,
    FOREIGN KEY (CampID) REFERENCES MedicalCamps(CampID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_beneficiaries_lastname ON Beneficiaries (LastName);
CREATE INDEX idx_beneficiarymedicalcamps_beneficiaryid ON BeneficiaryMedicalCamps (BeneficiaryID);
CREATE INDEX idx_beneficiarypsychologicalservices_beneficiaryid ON BeneficiaryPsychologicalServices (BeneficiaryID);
CREATE INDEX idx_medicalcamps_startdate ON MedicalCamps (StartDate);
```

```sql
-- Example usage:
-- Insert a new beneficiary
INSERT INTO Beneficiaries (FirstName, LastName, DateOfBirth, ContactNumber, Email, Address)
VALUES ('John', 'Doe', '1990-01-01', '1234567890', 'john.doe@example.com', '123 Main St');

-- Insert a new medical camp
INSERT INTO MedicalCamps (CampName, Location, StartDate, EndDate, Description)
VALUES ('Medical Camp 1', 'New York', '2022-01-01', '2022-01-05', 'A medical camp providing free health check-ups');

-- Insert a new beneficiary medical camp record
INSERT INTO BeneficiaryMedicalCamps (BeneficiaryID, CampID, VisitDate, Diagnosis, Treatment)
VALUES (1, 1, '2022-01-03', 'Hypertension', 'Medication and lifestyle changes');

-- Retrieve all beneficiaries
SELECT * FROM Beneficiaries;

-- Retrieve all medical camps
SELECT * FROM MedicalCamps;

-- Retrieve all beneficiary medical camp records
SELECT * FROM BeneficiaryMedicalCamps;
```
