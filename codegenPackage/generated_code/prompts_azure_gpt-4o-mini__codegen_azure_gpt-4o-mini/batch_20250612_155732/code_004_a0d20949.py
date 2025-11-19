"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Illustrate how to implement a database schema in SQL to manage healthcare professional records for a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_a0d20949e3805fca
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing healthcare professional records
-- for a placement agency like Seanda Healthcare.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS HealthcareProfessionals;
DROP TABLE IF EXISTS Specializations;
DROP TABLE IF EXISTS Certifications;
DROP TABLE IF EXISTS Placements;

-- Create a table to store healthcare professionals' information
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,               -- First name of the healthcare professional
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the healthcare professional
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                        -- Contact phone number
    DateOfBirth DATE NOT NULL,                      -- Date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store specializations of healthcare professionals
CREATE TABLE Specializations (
    SpecializationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each specialization
    SpecializationName VARCHAR(100) NOT NULL UNIQUE  -- Name of the specialization
);

-- Create a junction table to associate healthcare professionals with their specializations
CREATE TABLE ProfessionalSpecializations (
    ProfessionalID INT,                             -- Foreign key referencing HealthcareProfessionals
    SpecializationID INT,                           -- Foreign key referencing Specializations
    PRIMARY KEY (ProfessionalID, SpecializationID), -- Composite primary key
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (SpecializationID) REFERENCES Specializations(SpecializationID) ON DELETE CASCADE
);

-- Create a table to store certifications of healthcare professionals
CREATE TABLE Certifications (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each certification
    CertificationName VARCHAR(100) NOT NULL UNIQUE, -- Name of the certification
    IssuingOrganization VARCHAR(100) NOT NULL,      -- Organization that issued the certification
    ExpirationDate DATE                             -- Expiration date of the certification
);

-- Create a junction table to associate healthcare professionals with their certifications
CREATE TABLE ProfessionalCertifications (
    ProfessionalID INT,                             -- Foreign key referencing HealthcareProfessionals
    CertificationID INT,                            -- Foreign key referencing Certifications
    PRIMARY KEY (ProfessionalID, CertificationID),  -- Composite primary key
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE
);

-- Create a table to store placement records for healthcare professionals
CREATE TABLE Placements (
    PlacementID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each placement
    ProfessionalID INT,                              -- Foreign key referencing HealthcareProfessionals
    PlacementDate DATE NOT NULL,                     -- Date of placement
    FacilityName VARCHAR(100) NOT NULL,             -- Name of the facility where placed
    Position VARCHAR(100) NOT NULL,                  -- Position held at the facility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE
);

-- Indexes can be added for performance optimization as needed
-- Example: CREATE INDEX idx_email ON HealthcareProfessionals(Email);
```
