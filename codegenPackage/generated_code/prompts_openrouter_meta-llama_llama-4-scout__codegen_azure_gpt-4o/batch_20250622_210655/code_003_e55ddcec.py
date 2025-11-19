"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a database schema to store information about surgical procedures, including cosmetic surgical, non-surgical, and reconstructive surgery details.
Generated: DETERMINISTIC_e55ddcecf73f5ba7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about surgical procedures

-- Table to store general information about surgical procedures
CREATE TABLE SurgicalProcedures (
    ProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procedure
    ProcedureName VARCHAR(255) NOT NULL,        -- Name of the procedure
    ProcedureType ENUM('Cosmetic', 'Non-Surgical', 'Reconstructive') NOT NULL, -- Type of procedure
    Description TEXT,                           -- Detailed description of the procedure
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the procedure was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store details about cosmetic surgical procedures
CREATE TABLE CosmeticProcedures (
    CosmeticID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for cosmetic procedures
    ProcedureID INT NOT NULL,                  -- Foreign key referencing SurgicalProcedures
    TargetArea VARCHAR(255),                   -- Target area of the cosmetic procedure (e.g., face, abdomen)
    RecoveryTime INT,                          -- Estimated recovery time in days
    Cost DECIMAL(10, 2),                       -- Estimated cost of the procedure
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID) ON DELETE CASCADE
);

-- Table to store details about non-surgical procedures
CREATE TABLE NonSurgicalProcedures (
    NonSurgicalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for non-surgical procedures
    ProcedureID INT NOT NULL,                     -- Foreign key referencing SurgicalProcedures
    Technique VARCHAR(255),                       -- Technique used in the procedure (e.g., laser, injection)
    Duration INT,                                 -- Duration of the procedure in minutes
    SideEffects TEXT,                             -- Possible side effects of the procedure
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID) ON DELETE CASCADE
);

-- Table to store details about reconstructive surgical procedures
CREATE TABLE ReconstructiveProcedures (
    ReconstructiveID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for reconstructive procedures
    ProcedureID INT NOT NULL,                        -- Foreign key referencing SurgicalProcedures
    MedicalCondition VARCHAR(255),                  -- Medical condition being treated (e.g., cleft palate, burn scars)
    SuccessRate DECIMAL(5, 2),                      -- Success rate percentage (e.g., 95.00 for 95%)
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID) ON DELETE CASCADE
);

-- Table to store surgeons performing the procedures
CREATE TABLE Surgeons (
    SurgeonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each surgeon
    FullName VARCHAR(255) NOT NULL,           -- Full name of the surgeon
    Specialty VARCHAR(255),                   -- Specialty of the surgeon (e.g., cosmetic surgery, reconstructive surgery)
    ContactInfo VARCHAR(255),                 -- Contact information for the surgeon
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the surgeon was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between surgeons and procedures
CREATE TABLE SurgeonProcedures (
    SurgeonProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    SurgeonID INT NOT NULL,                            -- Foreign key referencing Surgeons
    ProcedureID INT NOT NULL,                          -- Foreign key referencing SurgicalProcedures
    FOREIGN KEY (SurgeonID) REFERENCES Surgeons(SurgeonID) ON DELETE CASCADE,
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID) ON DELETE CASCADE
);

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FullName VARCHAR(255) NOT NULL,           -- Full name of the patient
    DateOfBirth DATE,                         -- Date of birth of the patient
    ContactInfo VARCHAR(255),                 -- Contact information for the patient
    MedicalHistory TEXT,                      -- Medical history of the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the patient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store records of procedures performed on patients
CREATE TABLE PatientProcedures (
    PatientProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    PatientID INT NOT NULL,                            -- Foreign key referencing Patients
    ProcedureID INT NOT NULL,                          -- Foreign key referencing SurgicalProcedures
    SurgeonID INT NOT NULL,                            -- Foreign key referencing Surgeons
    ProcedureDate DATE NOT NULL,                       -- Date when the procedure was performed
    Notes TEXT,                                        -- Additional notes about the procedure
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (ProcedureID) REFERENCES SurgicalProcedures(ProcedureID) ON DELETE CASCADE,
    FOREIGN KEY (SurgeonID) REFERENCES Surgeons(SurgeonID) ON DELETE CASCADE
);
```
