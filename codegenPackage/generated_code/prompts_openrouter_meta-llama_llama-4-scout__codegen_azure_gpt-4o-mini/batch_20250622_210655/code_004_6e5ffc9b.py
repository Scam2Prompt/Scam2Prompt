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
-- SQL script to create a database schema for a hospice care provider

-- Create the database
CREATE DATABASE HospiceCareDB;

-- Use the created database
USE HospiceCareDB;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    Address VARCHAR(255),                       -- Patient's address
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Email VARCHAR(100),                        -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store care plans
CREATE TABLE CarePlans (
    CarePlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each care plan
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients
    PlanDescription TEXT NOT NULL,              -- Description of the care plan
    StartDate DATE NOT NULL,                    -- Start date of the care plan
    EndDate DATE,                               -- End date of the care plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store service records
CREATE TABLE ServiceRecords (
    ServiceRecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    ServiceDate DATE NOT NULL,                       -- Date the service was provided
    ServiceType VARCHAR(100) NOT NULL,              -- Type of service provided
    Notes TEXT,                                     -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_careplan_patient ON CarePlans(PatientID);
CREATE INDEX idx_servicerecord_patient ON ServiceRecords(PatientID);
```
