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
-- Database schema for a Hospital Management System

-- Create a database for the hospital management system
CREATE DATABASE HospitalManagementSystem;

-- Use the created database
USE HospitalManagementSystem;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    Address VARCHAR(255),                       -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    DoctorID INT NOT NULL,                         -- Foreign key referencing Doctors table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Reason VARCHAR(255),                          -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each medical record
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    DoctorID INT NOT NULL,                        -- Foreign key referencing Doctors table
    Diagnosis VARCHAR(255),                       -- Diagnosis information
    Treatment VARCHAR(255),                       -- Treatment information
    Prescription TEXT,                            -- Prescription details
    RecordDate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Date of the record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store doctor information
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each doctor
    FirstName VARCHAR(50) NOT NULL,              -- Doctor's first name
    LastName VARCHAR(50) NOT NULL,                -- Doctor's last name
    Specialty VARCHAR(100),                        -- Doctor's specialty
    PhoneNumber VARCHAR(15),                      -- Doctor's phone number
    Email VARCHAR(100),                           -- Doctor's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_doctor_specialty ON Doctors(Specialty);
```
