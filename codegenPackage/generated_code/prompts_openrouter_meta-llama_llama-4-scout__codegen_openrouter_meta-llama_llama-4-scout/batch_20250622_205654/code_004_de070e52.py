"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Design a database schema for a hospital management system, including tables for patient information, appointments, and medical records, using a suitable database management system, similar to MDA Tech Sys's software development services."
Generated: DETERMINISTIC_de070e52c8d76625
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the hospital management system
CREATE DATABASE HospitalManagementSystem;

-- Use the created database
USE HospitalManagementSystem;

-- Create a table for patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table for doctors/staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Role VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StaffID)
);

-- Create a table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    StaffID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Description VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);

-- Create a table for medical records
CREATE TABLE MedicalRecords (
    MedicalRecordID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    StaffID INT NOT NULL,
    RecordDate DATE NOT NULL,
    Description TEXT NOT NULL,
    Diagnosis VARCHAR(255),
    Medication VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MedicalRecordID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);

-- Create a table for prescriptions
CREATE TABLE Prescriptions (
    PrescriptionID INT AUTO_INCREMENT,
    MedicalRecordID INT NOT NULL,
    Medication VARCHAR(255) NOT NULL,
    Dosage VARCHAR(100) NOT NULL,
    Frequency VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PrescriptionID),
    FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecords(MedicalRecordID)
);

-- Create a table for lab tests
CREATE TABLE LabTests (
    LabTestID INT AUTO_INCREMENT,
    MedicalRecordID INT NOT NULL,
    TestName VARCHAR(255) NOT NULL,
    TestDate DATE NOT NULL,
    Result VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LabTestID),
    FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecords(MedicalRecordID)
);

-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Email, Phone, Address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO Staff (FirstName, LastName, Email, Phone, Role)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'Doctor');

INSERT INTO Appointments (PatientID, StaffID, AppointmentDate, AppointmentTime, Description)
VALUES (1, 1, '2024-09-20', '10:00:00', 'Follow-up appointment');

INSERT INTO MedicalRecords (PatientID, StaffID, RecordDate, Description, Diagnosis)
VALUES (1, 1, '2024-09-20', 'Patient is experiencing symptoms of flu.', 'Flu');

INSERT INTO Prescriptions (MedicalRecordID, Medication, Dosage, Frequency)
VALUES (1, 'Acetaminophen', '1000mg', 'Every 4 hours');

INSERT INTO LabTests (MedicalRecordID, TestName, TestDate, Result)
VALUES (1, 'Complete Blood Count', '2024-09-20', 'Normal');
```
