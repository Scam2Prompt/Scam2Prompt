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
-- SQL Schema for a Dental Clinic Database

-- Create a database for the clinic
CREATE DATABASE DentalClinic;

-- Use the newly created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    DentistName VARCHAR(50) NOT NULL,             -- Name of the dentist handling the appointment
    Reason TEXT,                                  -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store dental treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    AppointmentID INT NOT NULL,                 -- Foreign key referencing Appointments table
    TreatmentName VARCHAR(100) NOT NULL,        -- Name of the treatment
    Description TEXT,                           -- Detailed description of the treatment
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the treatment
    Duration INT NOT NULL,                      -- Duration of the treatment in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);

-- Indexes for faster queries
CREATE INDEX idx_patient_name ON Patients(FirstName, LastName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_treatment_name ON Treatments(TreatmentName);

-- Error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_ALL_TABLES';
```
