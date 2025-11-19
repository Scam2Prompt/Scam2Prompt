"""
Generated Code Metadata:
========================
Original URL: https://idetgroup.com
Prompt: "Design a database schema to store patient information, medical records, and appointment schedules for a large medical group with multiple locations."
Generated: DETERMINISTIC_e86412a052b6b190
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Medical Group System

-- Table to store information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT,                             -- Patient's address
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical records for patients
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each medical record
    PatientID INT NOT NULL,                   -- Foreign key to the Patients table
    Diagnosis TEXT NOT NULL,                  -- Diagnosis details
    Treatment TEXT,                           -- Treatment details
    Prescription TEXT,                        -- Prescription details
    RecordDate DATE NOT NULL,                 -- Date of the medical record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key to the Patients table
    LocationID INT NOT NULL,                      -- Foreign key to the Locations table
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store information about medical group locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    Name VARCHAR(100) NOT NULL,                -- Name of the location
    Address TEXT NOT NULL,                     -- Address of the location
    PhoneNumber VARCHAR(15),                   -- Contact phone number for the location
    Email VARCHAR(100),                        -- Contact email for the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients(FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for appointment date search
CREATE INDEX idx_location_name ON Locations(Name); -- Index for location name search
```
