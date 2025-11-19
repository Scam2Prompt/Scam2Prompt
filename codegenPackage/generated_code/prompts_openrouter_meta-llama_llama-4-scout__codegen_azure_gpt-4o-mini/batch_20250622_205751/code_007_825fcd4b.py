"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Design a simple database schema to store patient data, treatment plans, and outcomes for obesity and metabolic surgery patients at Dr. Utku Tantoğlu's clinic.
Generated: DETERMINISTIC_825fcd4b5b1e9a08
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient data, treatment plans, and outcomes
-- for obesity and metabolic surgery patients at Dr. Utku Tantoğlu's clinic

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Patient's email address
    Phone VARCHAR(15),                          -- Patient's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    TreatmentDate DATE NOT NULL,                      -- Date of the treatment plan
    PlanDescription TEXT NOT NULL,                    -- Description of the treatment plan
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL,  -- Status of the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store treatment outcomes
CREATE TABLE TreatmentOutcomes (
    OutcomeID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each outcome
    TreatmentPlanID INT NOT NULL,                     -- Foreign key referencing TreatmentPlans table
    OutcomeDate DATE NOT NULL,                        -- Date of the outcome assessment
    OutcomeDescription TEXT NOT NULL,                 -- Description of the outcome
    WeightLoss DECIMAL(5,2),                         -- Weight loss in kilograms
    Complications TEXT,                               -- Any complications experienced
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_email ON Patients(Email);
CREATE INDEX idx_treatment_patient ON TreatmentPlans(PatientID);
CREATE INDEX idx_outcome_treatment ON TreatmentOutcomes(TreatmentPlanID);
```
