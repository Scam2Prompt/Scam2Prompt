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
-- Database schema for storing information about orthopedic surgical procedures
-- Focused on foot and ankle surgeries

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for surgeons
CREATE TABLE Surgeons (
    SurgeonID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each surgeon
    FirstName VARCHAR(50) NOT NULL,              -- Surgeon's first name
    LastName VARCHAR(50) NOT NULL,               -- Surgeon's last name
    Specialty VARCHAR(100) NOT NULL,             -- Surgeon's specialty
    PhoneNumber VARCHAR(15),                     -- Surgeon's phone number
    Email VARCHAR(100),                          -- Surgeon's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for procedure types
CREATE TABLE ProcedureTypes (
    ProcedureTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each procedure type
    ProcedureName VARCHAR(100) NOT NULL,             -- Name of the surgical procedure
    Description TEXT,                                 -- Description of the procedure
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for surgical procedures
CREATE TABLE SurgicalProcedures (
    ProcedureID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each surgical procedure
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    SurgeonID INT NOT NULL,                          -- Foreign key referencing Surgeons
    ProcedureTypeID INT NOT NULL,                    -- Foreign key referencing ProcedureTypes
    SurgeryDate DATE NOT NULL,                       -- Date of the surgery
    Notes TEXT,                                     -- Additional notes about the procedure
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (SurgeonID) REFERENCES Surgeons(SurgeonID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProcedureTypeID) REFERENCES ProcedureTypes(ProcedureTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient ON SurgicalProcedures(PatientID);
CREATE INDEX idx_surgeon ON SurgicalProcedures(SurgeonID);
CREATE INDEX idx_procedure_type ON SurgicalProcedures(ProcedureTypeID);
```
