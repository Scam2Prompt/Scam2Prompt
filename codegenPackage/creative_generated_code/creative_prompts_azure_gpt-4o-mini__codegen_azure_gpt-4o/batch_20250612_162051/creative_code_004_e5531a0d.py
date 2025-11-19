"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Fundación Munasim Kullakita's Beneficiary Management

-- Table to store beneficiaries' personal information
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FullName VARCHAR(255) NOT NULL,              -- Full name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    ContactInfo VARCHAR(255),                    -- Contact information (phone/email)
    Address TEXT,                                -- Residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment-related information
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each treatment record
    BeneficiaryID INT NOT NULL,                  -- Foreign key linking to Beneficiaries table
    TreatmentType VARCHAR(255) NOT NULL,         -- Type of treatment (e.g., therapy, medical)
    StartDate DATE NOT NULL,                     -- Start date of the treatment
    EndDate DATE,                                -- End date of the treatment (NULL if ongoing)
    Notes TEXT,                                  -- Additional notes about the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Table to store education-related information
CREATE TABLE EducationPrograms (
    EducationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each education record
    BeneficiaryID INT NOT NULL,                  -- Foreign key linking to Beneficiaries table
    ProgramName VARCHAR(255) NOT NULL,           -- Name of the educational program
    Institution VARCHAR(255) NOT NULL,           -- Institution offering the program
    StartDate DATE NOT NULL,                     -- Start date of the program
    EndDate DATE,                                -- End date of the program (NULL if ongoing)
    CertificationReceived BOOLEAN DEFAULT FALSE, -- Whether certification was received
    Notes TEXT,                                  -- Additional notes about the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Table to store reintegration-related information
CREATE TABLE ReintegrationEfforts (
    ReintegrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reintegration record
    BeneficiaryID INT NOT NULL,                     -- Foreign key linking to Beneficiaries table
    EffortType VARCHAR(255) NOT NULL,               -- Type of reintegration effort (e.g., job placement)
    Organization VARCHAR(255),                      -- Organization involved in the effort
    StartDate DATE NOT NULL,                        -- Start date of the reintegration effort
    EndDate DATE,                                   -- End date of the reintegration effort (NULL if ongoing)
    Outcome VARCHAR(255),                           -- Outcome of the effort
    Notes TEXT,                                     -- Additional notes about the effort
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Ensure database integrity with necessary indices
CREATE INDEX idx_Beneficiaries_FullName ON Beneficiaries(FullName); -- Index for quick search on beneficiary names
CREATE INDEX idx_Treatments_BeneficiaryID ON Treatments(BeneficiaryID); -- Index for quick lookup of treatments by beneficiary
CREATE INDEX idx_EducationPrograms_BeneficiaryID ON EducationPrograms(BeneficiaryID); -- Index for quick lookup of education programs by beneficiary
CREATE INDEX idx_ReintegrationEfforts_BeneficiaryID ON ReintegrationEfforts(BeneficiaryID); -- Index for quick lookup of reintegration efforts by beneficiary
```
