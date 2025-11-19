"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Design a basic database schema to store patient information, treatment plans, and progress tracking for a child developmental centre like Jewel Autism Centre.
Generated: DETERMINISTIC_447edd772814e753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for a child developmental centre

-- Create a database for the Jewel Autism Centre
CREATE DATABASE JewelAutismCentre;

-- Use the created database
USE JewelAutismCentre;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                 -- Patient's contact number
    Address VARCHAR(255),                       -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,              -- Description of the treatment plan
    StartDate DATE NOT NULL,                         -- Start date of the treatment
    EndDate DATE,                                   -- End date of the treatment (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to track patient progress
CREATE TABLE ProgressTracking (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    TreatmentPlanID INT NOT NULL,               -- Foreign key referencing TreatmentPlans table
    ProgressDate DATE NOT NULL,                 -- Date of the progress record
    ProgressNotes TEXT,                         -- Notes on the patient's progress
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_name ON Patients (LastName, FirstName);
CREATE INDEX idx_treatment_patient ON TreatmentPlans (PatientID);
CREATE INDEX idx_progress_patient ON ProgressTracking (PatientID);
CREATE INDEX idx_progress_treatment ON ProgressTracking (TreatmentPlanID);
```
