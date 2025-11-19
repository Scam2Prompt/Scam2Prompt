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
-- Database schema for a child developmental center to store patient information, treatment plans, and progress tracking.

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),               -- Contact number of the patient or guardian
    Email VARCHAR(100),                       -- Email address of the patient or guardian
    Address TEXT,                             -- Address of the patient
    GuardianName VARCHAR(100),                -- Name of the guardian
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                  -- Foreign key referencing Patients table
    Diagnosis TEXT NOT NULL,                 -- Diagnosis details
    Goals TEXT NOT NULL,                     -- Treatment goals
    StartDate DATE NOT NULL,                 -- Start date of the treatment plan
    EndDate DATE,                            -- End date of the treatment plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to track progress
CREATE TABLE ProgressTracking (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    PlanID INT NOT NULL,                       -- Foreign key referencing TreatmentPlans table
    SessionDate DATE NOT NULL,                 -- Date of the session
    Notes TEXT,                                -- Notes about the session
    ProgressLevel ENUM('Poor', 'Average', 'Good', 'Excellent') NOT NULL, -- Progress level assessment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (PlanID) REFERENCES TreatmentPlans(PlanID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster queries
CREATE INDEX idx_patient_id ON TreatmentPlans(PatientID);
CREATE INDEX idx_progress_patient_id ON ProgressTracking(PatientID);
CREATE INDEX idx_progress_plan_id ON ProgressTracking(PlanID);
```
