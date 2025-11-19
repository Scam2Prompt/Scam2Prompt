"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Design a basic database schema to store patient information, treatment plans, and progress tracking for a child developmental centre like Jewel Autism Centre.
Generated: DETERMINISTIC_447edd772814e753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the child developmental centre
CREATE DATABASE JewelAutismCentre;

-- Use the database
USE JewelAutismCentre;

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    PlanName VARCHAR(255) NOT NULL,
    Description TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create a table to store progress tracking
CREATE TABLE ProgressTracking (
    ProgressID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    PlanID INT,
    ProgressDate DATE NOT NULL,
    Description TEXT,
    ProgressScore DECIMAL(3,2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProgressID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (PlanID) REFERENCES TreatmentPlans(PlanID) ON DELETE SET NULL
);

-- Create a table to store therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TherapistID)
);

-- Create a table to store patient-therapist assignments
CREATE TABLE PatientTherapistAssignments (
    AssignmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    TherapistID INT NOT NULL,
    AssignedDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new patient
DELIMITER //
CREATE PROCEDURE InsertPatient(
    IN pFirstName VARCHAR(255),
    IN pLastName VARCHAR(255),
    IN pDateOfBirth DATE,
    IN pContactNumber VARCHAR(20),
    IN pAddress VARCHAR(255)
)
BEGIN
    INSERT INTO Patients (FirstName, LastName, DateOfBirth, ContactNumber, Address)
    VALUES (pFirstName, pLastName, pDateOfBirth, pContactNumber, pAddress);
END//
DELIMITER ;

-- Create a stored procedure to insert a new treatment plan
DELIMITER //
CREATE PROCEDURE InsertTreatmentPlan(
    IN pPatientID INT,
    IN pPlanName VARCHAR(255),
    IN pDescription TEXT,
    IN pStartDate DATE,
    IN pEndDate DATE
)
BEGIN
    INSERT INTO TreatmentPlans (PatientID, PlanName, Description, StartDate, EndDate)
    VALUES (pPatientID, pPlanName, pDescription, pStartDate, pEndDate);
END//
DELIMITER ;

-- Create a stored procedure to insert a new progress tracking entry
DELIMITER //
CREATE PROCEDURE InsertProgressTracking(
    IN pPatientID INT,
    IN pPlanID INT,
    IN pProgressDate DATE,
    IN pDescription TEXT,
    IN pProgressScore DECIMAL(3,2)
)
BEGIN
    INSERT INTO ProgressTracking (PatientID, PlanID, ProgressDate, Description, ProgressScore)
    VALUES (pPatientID, pPlanID, pProgressDate, pDescription, pProgressScore);
END//
DELIMITER ;
```
