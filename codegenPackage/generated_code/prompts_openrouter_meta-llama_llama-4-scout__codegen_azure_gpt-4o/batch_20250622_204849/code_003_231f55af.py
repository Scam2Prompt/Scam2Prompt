"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Design a database schema for a podology clinic management system, including tables for patient information, treatment plans, and orthotic device designs.
Generated: DETERMINISTIC_231f55af53c45dac
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Podology Clinic Management System

-- Table: Patients
-- Stores information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: TreatmentPlans
-- Stores treatment plans for patients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    Diagnosis TEXT NOT NULL,                        -- Diagnosis details
    TreatmentDescription TEXT NOT NULL,            -- Description of the treatment plan
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE,                                   -- End date of the treatment plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table: OrthoticDeviceDesigns
-- Stores designs for orthotic devices
CREATE TABLE OrthoticDeviceDesigns (
    DesignID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each orthotic device design
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    DesignName VARCHAR(100) NOT NULL,             -- Name of the orthotic device design
    Material VARCHAR(100) NOT NULL,               -- Material used for the orthotic device
    Dimensions TEXT NOT NULL,                     -- Dimensions of the orthotic device
    Notes TEXT,                                   -- Additional notes about the design
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_id_treatment_plans ON TreatmentPlans(PatientID);
CREATE INDEX idx_patient_id_orthotic_designs ON OrthoticDeviceDesigns(PatientID);

-- End of schema definition
```
