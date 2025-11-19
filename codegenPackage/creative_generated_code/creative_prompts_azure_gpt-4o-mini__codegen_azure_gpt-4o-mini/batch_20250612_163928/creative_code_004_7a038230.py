"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://podologiaenpiura.com
Prompt: Design a database schema for a podiatry clinic that tracks patient treatments, including details on orthotic insoles and the latest non-invasive techniques for foot care.
Generated: DETERMINISTIC_7a03823025590741
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a Podiatry Clinic
CREATE DATABASE PodiatryClinic;

USE PodiatryClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,                -- Patient's first name
    LastName VARCHAR(50) NOT NULL,                  -- Patient's last name
    DateOfBirth DATE NOT NULL,                      -- Patient's date of birth
    Phone VARCHAR(15),                              -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                      -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Record creation timestamp
);

-- Table to store treatment types
CREATE TABLE TreatmentTypes (
    TreatmentTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment type
    TreatmentName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the treatment
    Description TEXT,                                -- Description of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Record creation timestamp
);

-- Table to store treatments applied to each patient
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each treatment record
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    TreatmentTypeID INT NOT NULL,                    -- Foreign key referencing TreatmentTypes
    TreatmentDate DATE NOT NULL,                     -- Date when the treatment was applied
    Notes TEXT,                                      -- Additional notes regarding the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentTypeID) REFERENCES TreatmentTypes(TreatmentTypeID) ON DELETE CASCADE
);

-- Table to store orthotic insoles details
CREATE TABLE OrthoticInsoles (
    InsoleID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each insole record
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    InsoleType VARCHAR(100) NOT NULL,                -- Type of orthotic insole
    PrescriptionDate DATE NOT NULL,                  -- Date when the insole was prescribed
    FitDate DATE,                                    -- Date when the insole was fitted
    Notes TEXT,                                      -- Additional notes about the orthotic insole
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store non-invasive techniques
CREATE TABLE NonInvasiveTechniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each technique
    TechniqueName VARCHAR(100) NOT NULL UNIQUE,      -- Name of the non-invasive technique
    Description TEXT,                                 -- Description of the technique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Record creation timestamp
);
```
