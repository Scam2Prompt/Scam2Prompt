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
-- Database schema for a Podiatry Clinic to track patient treatments
-- Includes information on orthotic insoles and non-invasive techniques for foot care

-- Create a table for storing patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for a patient
    FirstName VARCHAR(50) NOT NULL,             -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender (limited options)
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    Email VARCHAR(100),                         -- Contact email
    Address TEXT                                -- Patient's address
);

-- Create a table for storing treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a treatment
    PatientID INT NOT NULL,                     -- Foreign key to the Patients table
    TreatmentDate DATE NOT NULL,                -- Date of the treatment
    TreatmentType ENUM('Orthotic Insoles', 'Non-Invasive Technique') NOT NULL, -- Type of treatment provided
    TreatmentDescription TEXT NOT NULL,         -- Description of the treatment
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the treatment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create a table for storing orthotic insoles details
CREATE TABLE OrthoticInsoles (
    InsoleID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for an orthotic insole
    TreatmentID INT NOT NULL,                   -- Foreign key to the Treatments table
    Material VARCHAR(50) NOT NULL,              -- Material used for the insole
    Size VARCHAR(10) NOT NULL,                  -- Size of the insole
    CustomMade BOOLEAN NOT NULL,                -- Indicates whether the insole is custom-made
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE
);

-- Create a table for storing non-invasive techniques details
CREATE TABLE NonInvasiveTechniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a technique
    TreatmentID INT NOT NULL,                   -- Foreign key to the Treatments table
    TechniqueName VARCHAR(100) NOT NULL,        -- Name of the non-invasive technique
    EquipmentUsed VARCHAR(100),                 -- Equipment used (if applicable)
    SessionDuration INT NOT NULL,               -- Duration of the session in minutes
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE
);

-- Create indexes to improve query performance
CREATE INDEX idx_patient_name ON Patients(LastName, FirstName); -- Index for faster searching by patient name
CREATE INDEX idx_treatment_date ON Treatments(TreatmentDate);   -- Index for faster filtering by treatment date
```
