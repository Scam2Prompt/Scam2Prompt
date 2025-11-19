"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: "Design a database schema to store patient information, health conditions, and treatment plans for a clinic like Green Apples e-Rx Clinic."
Generated: DETERMINISTIC_9833f53aecb77e42
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Green Apples e-Rx Clinic

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    Address TEXT,                             -- Residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store health conditions
CREATE TABLE HealthConditions (
    ConditionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each health condition
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    ConditionName VARCHAR(100) NOT NULL,        -- Name of the health condition
    DiagnosisDate DATE NOT NULL,                -- Date of diagnosis
    Notes TEXT,                                 -- Additional notes about the condition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    ConditionID INT NOT NULL,                   -- Foreign key referencing HealthConditions table
    TreatmentDescription TEXT NOT NULL,         -- Description of the treatment plan
    StartDate DATE NOT NULL,                    -- Start date of the treatment
    EndDate DATE,                               -- End date of the treatment (nullable)
    PrescribedBy VARCHAR(100) NOT NULL,         -- Name of the doctor prescribing the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (ConditionID) REFERENCES HealthConditions(ConditionID) ON DELETE CASCADE -- Cascade delete if condition is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_condition_patient ON HealthConditions (PatientID); -- Index for patient-condition relationship
CREATE INDEX idx_treatment_condition ON TreatmentPlans (ConditionID); -- Index for condition-treatment relationship
```
