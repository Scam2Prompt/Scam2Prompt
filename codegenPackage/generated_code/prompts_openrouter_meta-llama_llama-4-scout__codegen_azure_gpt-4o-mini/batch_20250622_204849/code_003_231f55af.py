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
-- Database schema for a Podology Clinic Management System

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    Address VARCHAR(255),                       -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,               -- Description of the treatment plan
    StartDate DATE NOT NULL,                          -- Start date of the treatment
    EndDate DATE,                                    -- End date of the treatment (nullable)
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL,  -- Status of the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store orthotic device designs
CREATE TABLE OrthoticDevices (
    DeviceID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each orthotic device
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    DeviceDescription TEXT NOT NULL,                  -- Description of the orthotic device
    DesignDate DATE NOT NULL,                         -- Date when the design was created
    Material VARCHAR(100) NOT NULL,                  -- Material used for the device
    Size VARCHAR(50) NOT NULL,                        -- Size of the orthotic device
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_treatment_patient ON TreatmentPlans(PatientID);
CREATE INDEX idx_device_patient ON OrthoticDevices(PatientID);
```
