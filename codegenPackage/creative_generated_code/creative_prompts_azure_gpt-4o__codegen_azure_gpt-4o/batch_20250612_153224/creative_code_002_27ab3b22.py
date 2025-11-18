"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Create a database schema for storing information about beneficiaries of social programs, including fields for personal details, program participation, and reintegration status, inspired by Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_27ab3b22b83065fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema Design for Social Program Beneficiaries

-- Create a table to store beneficiary information
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FirstName VARCHAR(100) NOT NULL,             -- First name of the beneficiary
    LastName VARCHAR(100) NOT NULL,              -- Last name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender
    NationalID VARCHAR(50) UNIQUE,               -- National ID (optional but unique identifier)
    ContactNumber VARCHAR(15),                   -- Contact number of the beneficiary
    Address TEXT,                                -- Residential address
    Email VARCHAR(150),                          -- Email address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store social program participation information
CREATE TABLE ProgramParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    BeneficiaryID INT NOT NULL,                     -- Foreign key referencing Beneficiaries table
    ProgramName VARCHAR(255) NOT NULL,              -- Name of the social program
    StartDate DATE NOT NULL,                        -- Start date of program participation
    EndDate DATE,                                   -- End date of program participation (optional)
    Status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Participation status
    Remarks TEXT DEFAULT NULL,                     -- Additional remarks (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table to store reintegration status information
CREATE TABLE ReintegrationStatus (
    ReintegrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for reintegration record
    BeneficiaryID INT NOT NULL,                     -- Foreign key referencing Beneficiaries table
    ReintegrationDate DATE NOT NULL,                -- Date of reintegration
    ReintegrationDetails TEXT NOT NULL,             -- Details of reintegration process
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- Reintegration status
    SupportServicesProvided TEXT DEFAULT NULL,      -- List of support services provided (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Additional indexes for faster querying where necessary
CREATE INDEX idx_beneficiary_dob ON Beneficiaries(DateOfBirth); -- Index for querying by date of birth
CREATE INDEX idx_program_status ON ProgramParticipation(Status); -- Index for querying by program status
CREATE INDEX idx_reintegration_status ON ReintegrationStatus(Status); -- Index for querying by reintegration status
```
