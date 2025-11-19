"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate a sample database schema for storing information about orthopedic surgical procedures, including tables for patients, surgeons, and procedure types, with a focus on foot and ankle surgeries.
Generated: DETERMINISTIC_ad18a1f0f6dd81ea
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for orthopedic surgical procedures
CREATE DATABASE OrthopedicProcedures;

-- Use the database
USE OrthopedicProcedures;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactNumber VARCHAR(20),
    Email VARCHAR(255) UNIQUE,
    Address VARCHAR(255),
    PRIMARY KEY (PatientID)
);

-- Create a table for surgeons
CREATE TABLE Surgeons (
    SurgeonID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    MedicalLicenseNumber VARCHAR(50) NOT NULL,
    Specialty VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(20),
    Email VARCHAR(255) UNIQUE,
    PRIMARY KEY (SurgeonID)
);

-- Create a table for procedure types
CREATE TABLE ProcedureTypes (
    ProcedureTypeID INT AUTO_INCREMENT,
    ProcedureName VARCHAR(255) NOT NULL,
    ProcedureDescription TEXT,
    PRIMARY KEY (ProcedureTypeID)
);

-- Create a table for foot and ankle procedure types
CREATE TABLE FootAnkleProcedures (
    ProcedureTypeID INT,
    SpecificProcedureName VARCHAR(255) NOT NULL,
    PRIMARY KEY (ProcedureTypeID),
    FOREIGN KEY (ProcedureTypeID) REFERENCES ProcedureTypes(ProcedureTypeID)
);

-- Create a table for surgical procedures
CREATE TABLE SurgicalProcedures (
    ProcedureID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    SurgeonID INT NOT NULL,
    ProcedureTypeID INT NOT NULL,
    ProcedureDate DATE NOT NULL,
    ProcedureDescription TEXT,
    PRIMARY KEY (ProcedureID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (SurgeonID) REFERENCES Surgeons(SurgeonID),
    FOREIGN KEY (ProcedureTypeID) REFERENCES ProcedureTypes(ProcedureTypeID)
);

-- Create a table for procedure outcomes
CREATE TABLE ProcedureOutcomes (
    OutcomeID INT AUTO_INCREMENT,
    ProcedureID INT NOT NULL,
    OutcomeDescription TEXT NOT NULL,
    FollowUpDate DATE,
    PRIMARY KEY (OutcomeID),
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Patients_LastName ON Patients (LastName);
CREATE INDEX idx_Surgeons_LastName ON Surgeons (LastName);
CREATE INDEX idx_SurgicalProcedures_ProcedureDate ON SurgicalProcedures (ProcedureDate);
```

```sql
-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, ContactNumber, Email, Address)
VALUES 
('John', 'Doe', '1990-01-01', '123-456-7890', 'john.doe@example.com', '123 Main St');

INSERT INTO Surgeons (FirstName, LastName, MedicalLicenseNumber, Specialty, ContactNumber, Email)
VALUES 
('Jane', 'Smith', 'MD12345', 'Orthopedic Surgery', '987-654-3210', 'jane.smith@example.com');

INSERT INTO ProcedureTypes (ProcedureName, ProcedureDescription)
VALUES 
('Foot Reconstruction', 'Surgical reconstruction of the foot');

INSERT INTO FootAnkleProcedures (ProcedureTypeID, SpecificProcedureName)
VALUES 
(1, 'Toe realignment');

INSERT INTO SurgicalProcedures (PatientID, SurgeonID, ProcedureTypeID, ProcedureDate, ProcedureDescription)
VALUES 
(1, 1, 1, '2022-01-01', 'Performed foot reconstruction');

INSERT INTO ProcedureOutcomes (ProcedureID, OutcomeDescription, FollowUpDate)
VALUES 
(1, 'Patient recovering well', '2022-02-01');
```
