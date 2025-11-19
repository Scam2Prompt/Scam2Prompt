"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate a sample database schema for storing information about orthopedic surgical procedures, including tables for patients, surgeons, and procedure types, with a focus on foot and ankle surgeries.
Generated: DETERMINISTIC_ad18a1f0f6dd81ea
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Orthopedic Surgical Procedures (Foot and Ankle Focus)

-- Table: Patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),               -- Patient's contact number
    Email VARCHAR(100),                      -- Patient's email address
    Address TEXT                             -- Patient's residential address
);

-- Table: Surgeons
CREATE TABLE Surgeons (
    SurgeonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each surgeon
    FirstName VARCHAR(50) NOT NULL,           -- Surgeon's first name
    LastName VARCHAR(50) NOT NULL,            -- Surgeon's last name
    Specialty VARCHAR(100) NOT NULL,          -- Surgeon's specialty (e.g., Orthopedics)
    ContactNumber VARCHAR(15),               -- Surgeon's contact number
    Email VARCHAR(100),                      -- Surgeon's email address
    YearsOfExperience INT NOT NULL,          -- Surgeon's years of experience
    LicenseNumber VARCHAR(50) NOT NULL       -- Surgeon's medical license number
);

-- Table: ProcedureTypes
CREATE TABLE ProcedureTypes (
    ProcedureTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procedure type
    Name VARCHAR(100) NOT NULL,                     -- Name of the procedure (e.g., "Bunionectomy")
    Description TEXT,                               -- Detailed description of the procedure
    FocusArea ENUM('Foot', 'Ankle') NOT NULL        -- Focus area of the procedure
);

-- Table: Procedures
CREATE TABLE Procedures (
    ProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procedure
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    SurgeonID INT NOT NULL,                     -- Foreign key referencing Surgeons table
    ProcedureTypeID INT NOT NULL,               -- Foreign key referencing ProcedureTypes table
    ProcedureDate DATE NOT NULL,                -- Date the procedure was performed
    Notes TEXT,                                 -- Additional notes about the procedure
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (SurgeonID) REFERENCES Surgeons(SurgeonID) ON DELETE CASCADE,
    FOREIGN KEY (ProcedureTypeID) REFERENCES ProcedureTypes(ProcedureTypeID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_surgeon_name ON Surgeons (FirstName, LastName);
CREATE INDEX idx_procedure_date ON Procedures (ProcedureDate);

-- Error handling and constraints
-- Ensure that email addresses are unique for both Patients and Surgeons
ALTER TABLE Patients ADD CONSTRAINT unique_patient_email UNIQUE (Email);
ALTER TABLE Surgeons ADD CONSTRAINT unique_surgeon_email UNIQUE (Email);

-- Ensure that LicenseNumber is unique for Surgeons
ALTER TABLE Surgeons ADD CONSTRAINT unique_license_number UNIQUE (LicenseNumber);
```
