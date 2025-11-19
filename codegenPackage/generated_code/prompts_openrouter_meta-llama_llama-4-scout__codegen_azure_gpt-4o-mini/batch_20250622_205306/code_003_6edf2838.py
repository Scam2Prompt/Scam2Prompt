"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Create a SQL database schema to store patient information, appointments, and dental treatments for a clinic like Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_6edf2838bc415c0a
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Dental Clinic

-- Create a database for the clinic
CREATE DATABASE IF NOT EXISTS DentalClinic;

-- Use the created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE IF NOT EXISTS Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,          -- Patient's first name
    LastName VARCHAR(50) NOT NULL,           -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    PhoneNumber VARCHAR(15),                  -- Patient's phone number
    Email VARCHAR(100),                       -- Patient's email address
    Address VARCHAR(255),                     -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE IF NOT EXISTS Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    TreatmentType VARCHAR(100) NOT NULL,         -- Type of treatment scheduled
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store dental treatments
CREATE TABLE IF NOT EXISTS Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients
    TreatmentDate DATETIME NOT NULL,            -- Date of the treatment
    Description TEXT NOT NULL,                   -- Description of the treatment
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_name ON Patients (LastName, FirstName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);
CREATE INDEX idx_treatment_date ON Treatments (TreatmentDate);
```
