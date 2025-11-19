"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: Design a database schema to store patient information and treatment plans for an orthopedic practice like Gelenkzentrum Mönchengladbach.
Generated: DETERMINISTIC_8cb7614a8c3f0c60
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the orthopedic practice
CREATE DATABASE Gelenkzentrum;

-- Use the database
USE Gelenkzentrum;

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    PostalCode VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table to store doctors information
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Specialty VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID)
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    Diagnosis VARCHAR(255) NOT NULL,
    TreatmentDescription TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TreatmentPlanID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE
);

-- Create a table to store medications
CREATE TABLE Medications (
    MedicationID INT AUTO_INCREMENT,
    TreatmentPlanID INT NOT NULL,
    MedicationName VARCHAR(255) NOT NULL,
    Dosage VARCHAR(100) NOT NULL,
    Frequency VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MedicationID),
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE
);

-- Create a table to store surgical procedures
CREATE TABLE SurgicalProcedures (
    ProcedureID INT AUTO_INCREMENT,
    TreatmentPlanID INT NOT NULL,
    ProcedureName VARCHAR(255) NOT NULL,
    ProcedureDate DATE,
    ProcedureDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProcedureID),
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE
);

-- Create a table to store patient medical history
CREATE TABLE MedicalHistory (
    MedicalHistoryID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    Condition VARCHAR(255) NOT NULL,
    DiagnosisDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MedicalHistoryID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);
```

```sql
-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Email, Phone, Address, City, PostalCode)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', '12345');

INSERT INTO Doctors (FirstName, LastName, Email, Phone, Specialty)
VALUES 
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'Orthopedic Surgeon');

INSERT INTO TreatmentPlans (PatientID, DoctorID, Diagnosis, TreatmentDescription, StartDate)
VALUES 
(1, 1, 'Knee injury', 'Physical therapy and pain management', '2022-01-01');

INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2022-01-15', '10:00:00');

INSERT INTO Medications (TreatmentPlanID, MedicationName, Dosage, Frequency)
VALUES 
(1, 'Acetaminophen', '1000mg', 'Every 4-6 hours');

INSERT INTO SurgicalProcedures (TreatmentPlanID, ProcedureName, ProcedureDate, ProcedureDescription)
VALUES 
(1, 'Knee arthroscopy', '2022-02-01', 'Minimally invasive procedure to diagnose and treat knee injury');

INSERT INTO MedicalHistory (PatientID, Condition, DiagnosisDate)
VALUES 
(1, 'Hypertension', '2010-01-01');
```
