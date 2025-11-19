"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Create a SQL database schema for storing patient information, treatment plans, and appointment schedules for a dental clinic like Odontoclinic Suzano.
Generated: DETERMINISTIC_dcf723483126006f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Dental Clinic Database

-- Create a database for the dental clinic
CREATE DATABASE DentalClinic;

-- Use the created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,            -- Description of the treatment plan
    Cost DECIMAL(10, 2) NOT NULL,                  -- Cost of the treatment plan
    StartDate DATE NOT NULL,                       -- Start date of the treatment plan
    EndDate DATE,                                  -- End date of the treatment plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    DentistName VARCHAR(50) NOT NULL,             -- Name of the dentist handling the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate); -- Index for appointment date search

-- Error handling: Ensure foreign key constraints are enforced
SET FOREIGN_KEY_CHECKS = 1;
```
