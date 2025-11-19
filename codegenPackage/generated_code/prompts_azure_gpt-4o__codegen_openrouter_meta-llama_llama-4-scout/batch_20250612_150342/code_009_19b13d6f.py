"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Develop a database schema for managing laboratory data, including results from molecular diagnostics and automated analysis systems, as outlined in the laboratory informatics section.
Generated: DETERMINISTIC_19b13d6fda52d330
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for laboratory data management
CREATE DATABASE LaboratoryData;

-- Use the LaboratoryData database
USE LaboratoryData;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Sex VARCHAR(10) NOT NULL CHECK (Sex IN ('Male', 'Female', 'Other')),
    PRIMARY KEY (PatientID)
);

-- Create a table for samples
CREATE TABLE Samples (
    SampleID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    SampleType VARCHAR(255) NOT NULL,
    CollectionDate DATE NOT NULL,
    CollectionTime TIME NOT NULL,
    PRIMARY KEY (SampleID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- Create a table for molecular diagnostics tests
CREATE TABLE MolecularDiagnostics (
    TestID INT AUTO_INCREMENT,
    SampleID INT NOT NULL,
    TestType VARCHAR(255) NOT NULL,
    TestDate DATE NOT NULL,
    TestTime TIME NOT NULL,
    Result VARCHAR(255),
    PRIMARY KEY (TestID),
    FOREIGN KEY (SampleID) REFERENCES Samples(SampleID)
);

-- Create a table for automated analysis systems
CREATE TABLE AutomatedAnalysis (
    AnalysisID INT AUTO_INCREMENT,
    SampleID INT NOT NULL,
    SystemType VARCHAR(255) NOT NULL,
    AnalysisDate DATE NOT NULL,
    AnalysisTime TIME NOT NULL,
    Result VARCHAR(255),
    PRIMARY KEY (AnalysisID),
    FOREIGN KEY (SampleID) REFERENCES Samples(SampleID)
);

-- Create a table for laboratory equipment
CREATE TABLE LaboratoryEquipment (
    EquipmentID INT AUTO_INCREMENT,
    EquipmentType VARCHAR(255) NOT NULL,
    EquipmentName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (EquipmentID)
);

-- Create a table for quality control data
CREATE TABLE QualityControl (
    QCID INT AUTO_INCREMENT,
    EquipmentID INT NOT NULL,
    TestDate DATE NOT NULL,
    TestTime TIME NOT NULL,
    Result VARCHAR(255) NOT NULL,
    PRIMARY KEY (QCID),
    FOREIGN KEY (EquipmentID) REFERENCES LaboratoryEquipment(EquipmentID)
);

-- Create a table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL CHECK (Role IN ('Admin', 'Technician', 'Viewer')),
    PRIMARY KEY (UserID)
);

-- Create a table for audit logs
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT,
    UserID INT NOT NULL,
    Action VARCHAR(255) NOT NULL,
    LogDate DATE NOT NULL,
    LogTime TIME NOT NULL,
    Details TEXT,
    PRIMARY KEY (LogID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create stored procedure to add new patient
DELIMITER //
CREATE PROCEDURE AddPatient(
    IN pFirstName VARCHAR(255),
    IN pLastName VARCHAR(255),
    IN pDateOfBirth DATE,
    IN pSex VARCHAR(10)
)
BEGIN
    INSERT INTO Patients (FirstName, LastName, DateOfBirth, Sex)
    VALUES (pFirstName, pLastName, pDateOfBirth, pSex);
END//
DELIMITER ;

-- Create stored procedure to add new sample
DELIMITER //
CREATE PROCEDURE AddSample(
    IN pPatientID INT,
    IN pSampleType VARCHAR(255),
    IN pCollectionDate DATE,
    IN pCollectionTime TIME
)
BEGIN
    INSERT INTO Samples (PatientID, SampleType, CollectionDate, CollectionTime)
    VALUES (pPatientID, pSampleType, pCollectionDate, pCollectionTime);
END//
DELIMITER ;

-- Create trigger to log changes to patient data
DELIMITER //
CREATE TRIGGER PatientUpdateTrigger
AFTER UPDATE ON Patients
FOR EACH ROW
BEGIN
    INSERT INTO AuditLogs (UserID, Action, LogDate, LogTime, Details)
    VALUES (USER(), 'Patient updated', CURDATE(), CURTIME(), CONCAT('PatientID: ', OLD.PatientID, ' updated to ', NEW.FirstName, ' ', NEW.LastName));
END//
DELIMITER ;
```
