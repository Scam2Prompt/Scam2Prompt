"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Create a SQL database schema to store patient information, care plans, and service records for a hospice care provider like Amalfi Hospice Care, Inc.
Generated: DETERMINISTIC_6e5ffc9b6620fd69
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Hospice Care Provider Database

-- Create a database for the hospice care provider
CREATE DATABASE HospiceCareDB;

-- Switch to the newly created database
USE HospiceCareDB;

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
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store care plans for patients
CREATE TABLE CarePlans (
    CarePlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each care plan
    PatientID INT NOT NULL,                    -- Foreign key to the Patients table
    Diagnosis TEXT NOT NULL,                   -- Patient's diagnosis
    TreatmentPlan TEXT NOT NULL,               -- Detailed treatment plan
    StartDate DATE NOT NULL,                   -- Start date of the care plan
    EndDate DATE,                              -- End date of the care plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store service records for patients
CREATE TABLE ServiceRecords (
    ServiceRecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    PatientID INT NOT NULL,                         -- Foreign key to the Patients table
    ServiceDate DATE NOT NULL,                      -- Date of the service
    ServiceType VARCHAR(100) NOT NULL,              -- Type of service provided (e.g., nursing, therapy)
    Notes TEXT,                                     -- Additional notes about the service
    ProviderName VARCHAR(100) NOT NULL,             -- Name of the service provider
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (LastName, FirstName); -- Index for patient name search
CREATE INDEX idx_careplan_patient ON CarePlans (PatientID);      -- Index for care plan lookups by patient
CREATE INDEX idx_service_patient ON ServiceRecords (PatientID);  -- Index for service record lookups by patient

-- Error handling and constraints
-- Ensure that email addresses are unique
ALTER TABLE Patients ADD CONSTRAINT unique_email UNIQUE (Email);

-- Ensure that service types are not empty
ALTER TABLE ServiceRecords ADD CONSTRAINT chk_service_type CHECK (ServiceType <> '');

-- Ensure that care plan start date is before end date
ALTER TABLE CarePlans ADD CONSTRAINT chk_dates CHECK (StartDate <= EndDate OR EndDate IS NULL);
```
