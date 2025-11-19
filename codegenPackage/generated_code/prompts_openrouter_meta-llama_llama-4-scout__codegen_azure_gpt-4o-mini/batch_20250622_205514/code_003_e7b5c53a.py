"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Design a database schema to store patient information, medical records, and home healthcare services provided by a company like Payidar Evde Sağlık Hizmetleri.
Generated: DETERMINISTIC_e7b5c53aea9a3036
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient information, medical records, and home healthcare services

-- Create a database for the healthcare services
CREATE DATABASE HealthcareServices;

-- Use the created database
USE HealthcareServices;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Email VARCHAR(100),                        -- Patient's email address
    Address VARCHAR(255),                      -- Patient's home address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each medical record
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    RecordDate DATE NOT NULL,                  -- Date of the medical record
    Diagnosis VARCHAR(255),                    -- Diagnosis information
    Treatment VARCHAR(255),                    -- Treatment details
    Notes TEXT,                                -- Additional notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store home healthcare services
CREATE TABLE HomeHealthcareServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    ServiceDate DATE NOT NULL,                 -- Date when the service was provided
    ServiceType VARCHAR(100) NOT NULL,         -- Type of service provided
    ProviderName VARCHAR(100) NOT NULL,        -- Name of the healthcare provider
    Duration INT NOT NULL,                      -- Duration of the service in minutes
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_record_patient ON MedicalRecords(PatientID);
CREATE INDEX idx_service_patient ON HomeHealthcareServices(PatientID);
```
