"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Develop a basic SQL database schema to store patient data, appointment schedules, and medical records for a gastroenterology clinic that offers services such as endocrinologia, motilidade digestiva, and proctologia.
Generated: DETERMINISTIC_96e78c93bc4e5fc3
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Gastroenterology Clinic Database

-- Create a database for the clinic
CREATE DATABASE GastroClinic;

-- Use the created database
USE GastroClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    Address TEXT                              -- Residential address
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    ServiceType ENUM('Endocrinologia', 'Motilidade Digestiva', 'Proctologia') NOT NULL, -- Type of service
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor handling the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Additional notes for the appointment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medical record
    PatientID INT NOT NULL,                  -- Foreign key referencing Patients table
    RecordDate DATE NOT NULL,                -- Date of the medical record
    Diagnosis TEXT NOT NULL,                 -- Diagnosis details
    Treatment TEXT,                          -- Treatment details
    DoctorName VARCHAR(100) NOT NULL,        -- Name of the doctor who created the record
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate); -- Index for appointment date search
CREATE INDEX idx_record_date ON MedicalRecords (RecordDate); -- Index for medical record date search

-- Error handling and constraints
-- Ensure no duplicate email addresses for patients
ALTER TABLE Patients ADD CONSTRAINT unique_email UNIQUE (Email);

-- Ensure appointment date is in the future
ALTER TABLE Appointments ADD CONSTRAINT chk_appointment_date CHECK (AppointmentDate > NOW());

-- Ensure medical record date is not in the future
ALTER TABLE MedicalRecords ADD CONSTRAINT chk_record_date CHECK (RecordDate <= CURDATE());
```
