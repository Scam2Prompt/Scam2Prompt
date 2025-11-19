"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: "Design a database schema to store patient information, medical records, and appointment schedules for a large medical clinic with multiple locations, like Grupo Clínico IDET."
Generated: DETERMINISTIC_a76d959ac82b95f5
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a medical clinic to store patient information, medical records, and appointment schedules

-- Create a database for the clinic
CREATE DATABASE ClinicDB;

-- Use the created database
USE ClinicDB;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    Address VARCHAR(255),                       -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each medical record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    RecordDate DATE NOT NULL,                   -- Date of the medical record
    Diagnosis VARCHAR(255),                     -- Diagnosis details
    Treatment VARCHAR(255),                     -- Treatment details
    Notes TEXT,                                 -- Additional notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Location VARCHAR(100) NOT NULL,               -- Location of the appointment
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store clinic locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each location
    LocationName VARCHAR(100) NOT NULL,           -- Name of the clinic location
    Address VARCHAR(255) NOT NULL,                 -- Address of the clinic location
    PhoneNumber VARCHAR(15),                       -- Phone number of the clinic location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link appointments to specific locations
ALTER TABLE Appointments
ADD COLUMN LocationID INT NOT NULL,              -- Foreign key referencing Locations table
ADD FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE;  -- Ensure referential integrity
```
