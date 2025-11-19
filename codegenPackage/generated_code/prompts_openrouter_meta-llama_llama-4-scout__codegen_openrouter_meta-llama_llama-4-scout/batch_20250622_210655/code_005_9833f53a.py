"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: "Design a database schema to store patient information, health conditions, and treatment plans for a clinic like Green Apples e-Rx Clinic."
Generated: DETERMINISTIC_9833f53aecb77e42
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the clinic
CREATE DATABASE GreenApplesERx;

-- Use the database
USE GreenApplesERx;

-- Create a table to store patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table to store health conditions
CREATE TABLE HealthConditions (
    ConditionID INT AUTO_INCREMENT,
    ConditionName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ConditionID)
);

-- Create a table to store patient health conditions
CREATE TABLE PatientHealthConditions (
    PatientID INT NOT NULL,
    ConditionID INT NOT NULL,
    DiagnosisDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID, ConditionID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (ConditionID) REFERENCES HealthConditions(ConditionID) ON DELETE CASCADE
);

-- Create a table to store medications
CREATE TABLE Medications (
    MedicationID INT AUTO_INCREMENT,
    MedicationName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MedicationID)
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    PlanName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create a table to store treatment plan medications
CREATE TABLE TreatmentPlanMedications (
    PlanID INT NOT NULL,
    MedicationID INT NOT NULL,
    Dosage VARCHAR(255) NOT NULL,
    Frequency VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID, MedicationID),
    FOREIGN KEY (PlanID) REFERENCES TreatmentPlans(PlanID) ON DELETE CASCADE,
    FOREIGN KEY (MedicationID) REFERENCES Medications(MedicationID) ON DELETE CASCADE
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create a table to store doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Specialty VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID)
);

-- Create a table to store appointment doctors
CREATE TABLE AppointmentDoctors (
    AppointmentID INT NOT NULL,
    DoctorID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID, DoctorID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE
);
```
