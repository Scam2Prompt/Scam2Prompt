"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Fundación Munasim Kullakita's Beneficiary Management System

-- Table to store beneficiary personal information
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FirstName VARCHAR(100) NOT NULL,             -- First name of the beneficiary
    LastName VARCHAR(100) NOT NULL,              -- Last name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the beneficiary
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    ContactNumber VARCHAR(15),                   -- Contact number of the beneficiary
    Email VARCHAR(255),                          -- Email address of the beneficiary
    Address TEXT,                                -- Address of the beneficiary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment program details
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each treatment record
    BeneficiaryID INT NOT NULL,                  -- Foreign key to the Beneficiaries table
    TreatmentType VARCHAR(100) NOT NULL,         -- Type of treatment (e.g., medical, psychological)
    StartDate DATE NOT NULL,                     -- Start date of the treatment
    EndDate DATE,                                -- End date of the treatment (nullable if ongoing)
    Notes TEXT,                                  -- Additional notes about the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Table to store education program details
CREATE TABLE EducationPrograms (
    EducationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each education record
    BeneficiaryID INT NOT NULL,                  -- Foreign key to the Beneficiaries table
    ProgramName VARCHAR(255) NOT NULL,           -- Name of the education program
    InstitutionName VARCHAR(255),               -- Name of the institution providing the program
    StartDate DATE NOT NULL,                     -- Start date of the education program
    EndDate DATE,                                -- End date of the education program (nullable if ongoing)
    Status ENUM('Enrolled', 'Completed', 'Dropped') NOT NULL, -- Current status of the program
    Notes TEXT,                                  -- Additional notes about the education program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Table to store reintegration program details
CREATE TABLE ReintegrationPrograms (
    ReintegrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reintegration record
    BeneficiaryID INT NOT NULL,                     -- Foreign key to the Beneficiaries table
    ProgramName VARCHAR(255) NOT NULL,              -- Name of the reintegration program
    StartDate DATE NOT NULL,                        -- Start date of the reintegration program
    EndDate DATE,                                   -- End date of the reintegration program (nullable if ongoing)
    Status ENUM('In Progress', 'Completed', 'Terminated') NOT NULL, -- Current status of the program
    Notes TEXT,                                     -- Additional notes about the reintegration program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Table to log program participation history
CREATE TABLE ProgramParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    BeneficiaryID INT NOT NULL,                     -- Foreign key to the Beneficiaries table
    ProgramType ENUM('Treatment', 'Education', 'Reintegration') NOT NULL, -- Type of program
    ProgramID INT NOT NULL,                         -- ID of the specific program (TreatmentID, EducationID, or ReintegrationID)
    ParticipationDate DATE NOT NULL,                -- Date of participation
    Notes TEXT,                                     -- Additional notes about the participation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_beneficiary_id ON Treatments (BeneficiaryID);
CREATE INDEX idx_beneficiary_id_edu ON EducationPrograms (BeneficiaryID);
CREATE INDEX idx_beneficiary_id_reintegration ON ReintegrationPrograms (BeneficiaryID);
CREATE INDEX idx_beneficiary_id_participation ON ProgramParticipation (BeneficiaryID);
```
