"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Design a database schema to store information about hair transplantation procedures, including patient data, treatment plans, and post-operative care instructions.
Generated: DETERMINISTIC_a01b46857302603d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for hair transplantation procedures
CREATE DATABASE HairTransplantationDB;

-- Use the created database
USE HairTransplantationDB;

-- Create a table for patients
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

-- Create a table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID)
);

-- Create a table for treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    ProcedureDate DATE NOT NULL,
    ProcedureType VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TreatmentPlanID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Create a table for post-operative care instructions
CREATE TABLE PostOperativeCareInstructions (
    InstructionID INT AUTO_INCREMENT,
    TreatmentPlanID INT NOT NULL,
    InstructionDate DATE NOT NULL,
    Instructions TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InstructionID),
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID)
);

-- Create a table for medication instructions
CREATE TABLE MedicationInstructions (
    MedicationID INT AUTO_INCREMENT,
    TreatmentPlanID INT NOT NULL,
    MedicationName VARCHAR(255) NOT NULL,
    Dosage VARCHAR(255) NOT NULL,
    Frequency VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MedicationID),
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID)
);

-- Create a table for follow-up appointments
CREATE TABLE FollowUpAppointments (
    AppointmentID INT AUTO_INCREMENT,
    TreatmentPlanID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID)
);

-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Email, Phone, Address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO Doctors (FirstName, LastName, Email, Phone)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO TreatmentPlans (PatientID, DoctorID, ProcedureDate, ProcedureType, Description)
VALUES (1, 1, '2022-01-01', 'Hair Transplantation', ' Transplantation of 1000 grafts');

INSERT INTO PostOperativeCareInstructions (TreatmentPlanID, InstructionDate, Instructions)
VALUES (1, '2022-01-02', 'Avoid heavy lifting and bending');

INSERT INTO MedicationInstructions (TreatmentPlanID, MedicationName, Dosage, Frequency)
VALUES (1, 'Pain reliever', '2 tablets', 'Every 4 hours');

INSERT INTO FollowUpAppointments (TreatmentPlanID, AppointmentDate, Description)
VALUES (1, '2022-01-14', 'Check on transplanted area');
```
