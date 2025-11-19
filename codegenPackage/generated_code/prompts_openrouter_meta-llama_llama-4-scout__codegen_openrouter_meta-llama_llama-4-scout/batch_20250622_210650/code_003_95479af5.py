"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Develop a simple database schema for storing information on dental treatments, including fields for treatment type, patient ID, and dentist notes, based on Tiziano Testori's clinical activities.
Generated: DETERMINISTIC_95479af5908dce49
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for dental treatments
CREATE DATABASE DentalTreatments;

-- Use the DentalTreatments database
USE DentalTreatments;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (PatientID)
);

-- Create a table for dentists
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (DentistID)
);

-- Create a table for treatment types
CREATE TABLE TreatmentTypes (
    TreatmentTypeID INT AUTO_INCREMENT,
    TreatmentType VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (TreatmentTypeID)
);

-- Create a table for dental treatments
CREATE TABLE DentalTreatments (
    TreatmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DentistID INT NOT NULL,
    TreatmentTypeID INT NOT NULL,
    TreatmentDate DATE NOT NULL,
    DentistNotes TEXT,
    PRIMARY KEY (TreatmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentTypeID) REFERENCES TreatmentTypes(TreatmentTypeID) ON DELETE CASCADE
);

-- Create a trigger to prevent null values in required fields
DELIMITER $$
CREATE TRIGGER PreventNullValues
BEFORE INSERT ON DentalTreatments
FOR EACH ROW
BEGIN
    IF NEW.PatientID IS NULL OR NEW.DentistID IS NULL OR NEW.TreatmentTypeID IS NULL OR NEW.TreatmentDate IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Required fields cannot be null';
    END IF;
END$$
DELIMITER ;

-- Example usage:
INSERT INTO Patients (Name, DateOfBirth, ContactInformation)
VALUES ('John Doe', '1990-01-01', '123 Main St');

INSERT INTO Dentists (Name, Specialty, ContactInformation)
VALUES ('Tiziano Testori', 'Dentist', 'testori@example.com');

INSERT INTO TreatmentTypes (TreatmentType, Description)
VALUES ('Extraction', 'Tooth extraction procedure');

INSERT INTO DentalTreatments (PatientID, DentistID, TreatmentTypeID, TreatmentDate, DentistNotes)
VALUES (1, 1, 1, '2022-01-01', 'Patient tolerated procedure well');
```
