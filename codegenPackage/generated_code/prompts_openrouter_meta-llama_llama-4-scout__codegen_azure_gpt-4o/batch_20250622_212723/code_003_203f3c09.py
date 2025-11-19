"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Design a database schema for storing patient medical records and information, inspired by the features and functionality of myLoyola.
Generated: DETERMINISTIC_203f3c09b357dcbe
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Patient Medical Records and Information

-- Table to store patient personal information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Address TEXT,                             -- Patient's address
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical records for patients
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each medical record
    PatientID INT NOT NULL,                   -- Foreign key linking to Patients table
    Diagnosis TEXT NOT NULL,                  -- Diagnosis details
    TreatmentPlan TEXT,                       -- Treatment plan details
    Prescription TEXT,                        -- Prescription details
    DoctorName VARCHAR(100) NOT NULL,         -- Name of the doctor who created the record
    VisitDate DATE NOT NULL,                  -- Date of the medical visit
    Notes TEXT,                               -- Additional notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure records are deleted if patient is deleted
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key linking to Patients table
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor for the appointment
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Reason TEXT,                                  -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure appointments are deleted if patient is deleted
);

-- Table to store patient login credentials for accessing their records
CREATE TABLE PatientCredentials (
    CredentialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each credential record
    PatientID INT NOT NULL,                      -- Foreign key linking to Patients table
    Username VARCHAR(50) NOT NULL UNIQUE,        -- Unique username for the patient
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure credentials are deleted if patient is deleted
);

-- Table to store audit logs for tracking changes and access
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    PatientID INT,                               -- Foreign key linking to Patients table (if applicable)
    Action VARCHAR(255) NOT NULL,                -- Description of the action performed
    PerformedBy VARCHAR(100) NOT NULL,           -- Name or ID of the user who performed the action
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE SET NULL -- Allow logs to persist even if patient is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for searching patients by name
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate); -- Index for searching appointments by date
CREATE INDEX idx_medical_record_date ON MedicalRecords (VisitDate); -- Index for searching medical records by visit date
```
