"""
Generated Code Metadata:
========================
Original URL: https://baycarepatientportal.net
Prompt: Design a database schema to store patient health information, including test results, diagnoses, and treatment plans, with secure access controls.
Generated: DETERMINISTIC_c8e77cebe4672a19
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient health information
-- Includes tables for patients, test results, diagnoses, treatment plans, and access controls

-- Create table for storing patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),               -- Patient's contact number
    Email VARCHAR(100),                      -- Patient's email address
    Address TEXT,                            -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for storing test results
CREATE TABLE TestResults (
    TestID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each test result
    PatientID INT NOT NULL,                  -- Foreign key referencing Patients table
    TestName VARCHAR(100) NOT NULL,          -- Name of the test
    TestDate DATE NOT NULL,                  -- Date the test was conducted
    Result TEXT NOT NULL,                    -- Test result details
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is deleted
);

-- Create table for storing diagnoses
CREATE TABLE Diagnoses (
    DiagnosisID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each diagnosis
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    DiagnosisDate DATE NOT NULL,                -- Date of diagnosis
    DiagnosisDescription TEXT NOT NULL,         -- Description of the diagnosis
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is deleted
);

-- Create table for storing treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,         -- Description of the treatment plan
    StartDate DATE NOT NULL,                    -- Start date of the treatment
    EndDate DATE,                               -- End date of the treatment (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is deleted
);

-- Create table for storing access controls
CREATE TABLE AccessControls (
    AccessID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each access control record
    UserID INT NOT NULL,                       -- Identifier for the user (e.g., doctor, nurse, admin)
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    AccessLevel ENUM('Read', 'Write', 'Admin') NOT NULL, -- Access level for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is deleted
);

-- Ensure secure access controls by restricting direct access to sensitive data
-- Application-level authentication and authorization should be implemented
```
