"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Develop a database schema for managing laboratory data, including results from molecular diagnostics and automated analysis systems, as outlined in the laboratory informatics section.
Generated: DETERMINISTIC_19b13d6fda52d330
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing laboratory data
-- This schema includes tables for managing molecular diagnostics and automated analysis results

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS TestResults;
DROP TABLE IF EXISTS Tests;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Laboratories;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,          -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,       -- Patient's first name
    LastName VARCHAR(50) NOT NULL,        -- Patient's last name
    DateOfBirth DATE NOT NULL,             -- Patient's date of birth
    Gender VARCHAR(10),                    -- Patient's gender
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store laboratory information
CREATE TABLE Laboratories (
    LaboratoryID SERIAL PRIMARY KEY,       -- Unique identifier for each laboratory
    Name VARCHAR(100) NOT NULL,            -- Laboratory name
    Location VARCHAR(255),                  -- Laboratory location
    ContactNumber VARCHAR(15),              -- Laboratory contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store tests that can be performed
CREATE TABLE Tests (
    TestID SERIAL PRIMARY KEY,              -- Unique identifier for each test
    TestName VARCHAR(100) NOT NULL,         -- Name of the test
    Description TEXT,                       -- Description of the test
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store test results
CREATE TABLE TestResults (
    ResultID SERIAL PRIMARY KEY,            -- Unique identifier for each result
    PatientID INT NOT NULL,                 -- Foreign key referencing Patients
    TestID INT NOT NULL,                    -- Foreign key referencing Tests
    LaboratoryID INT NOT NULL,              -- Foreign key referencing Laboratories
    ResultValue VARCHAR(255),                -- Result value of the test
    ResultDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the result was recorded
    Comments TEXT,                          -- Additional comments about the result
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensures patient data integrity
    FOREIGN KEY (TestID) REFERENCES Tests(TestID) ON DELETE CASCADE,           -- Ensures test data integrity
    FOREIGN KEY (LaboratoryID) REFERENCES Laboratories(LaboratoryID) ON DELETE CASCADE -- Ensures laboratory data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient ON TestResults(PatientID);
CREATE INDEX idx_test ON TestResults(TestID);
CREATE INDEX idx_laboratory ON TestResults(LaboratoryID);
```
