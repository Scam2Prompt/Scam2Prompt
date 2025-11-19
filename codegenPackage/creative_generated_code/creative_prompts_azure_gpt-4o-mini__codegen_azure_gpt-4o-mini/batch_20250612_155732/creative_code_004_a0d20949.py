"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seandahealthcare.co.za
Prompt: Illustrate how to implement a database schema in SQL to manage healthcare professional records for a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_a0d20949e3805fca
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing healthcare professional records
-- for a placement agency like Seanda Healthcare.

-- Drop the database if it exists (for development purposes)
DROP DATABASE IF EXISTS SeandaHealthcare;
CREATE DATABASE SeandaHealthcare;
USE SeandaHealthcare;

-- Table to store healthcare professionals' information
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,                 -- First name of the healthcare professional
    LastName VARCHAR(50) NOT NULL,                   -- Last name of the healthcare professional
    Email VARCHAR(100) NOT NULL UNIQUE,              -- Email address, must be unique
    PhoneNumber VARCHAR(15),                         -- Contact number
    Specialty VARCHAR(100),                          -- Area of specialization (e.g., Nursing, Physiotherapy)
    LicenseNumber VARCHAR(50),                       -- Professional license number
    DateOfBirth DATE NOT NULL,                       -- Date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Date and time of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Date and time of last update
);

-- Table to store healthcare facilities
CREATE TABLE HealthcareFacilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each facility
    FacilityName VARCHAR(100) NOT NULL,              -- Name of the healthcare facility
    Address VARCHAR(255),                             -- Address of the facility
    PhoneNumber VARCHAR(15),                         -- Contact number
    Email VARCHAR(100) UNIQUE,                        -- Email address, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Date and time of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Date and time of last update
);

-- Table to establish a relationship between healthcare professionals and facilities
CREATE TABLE ProfessionalFacility (
    ProfessionalFacilityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each record
    ProfessionalID INT,                                     -- Foreign key referencing HealthcareProfessionals
    FacilityID INT,                                        -- Foreign key referencing HealthcareFacilities
    PlacementDate DATE NOT NULL,                           -- Date of placement in the facility
    EndDate DATE,                                         -- Date of end of placement
    Status ENUM('Active', 'Inactive', 'Terminated') NOT NULL,  -- Status of the placement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Date and time of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Date and time of last update
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (FacilityID) REFERENCES HealthcareFacilities(FacilityID) ON DELETE CASCADE
);

-- Index to speed up queries for professionals by specialty
CREATE INDEX idx_specialty ON HealthcareProfessionals(Specialty);

-- Index to speed up lookups for facilities by name
CREATE INDEX idx_facility_name ON HealthcareFacilities(FacilityName);

-- Sample data insertion (commented out for production)
-- INSERT INTO HealthcareProfessionals (FirstName, LastName, Email, PhoneNumber, Specialty, LicenseNumber, DateOfBirth) VALUES
-- ('John', 'Doe', 'john.doe@example.com', '1234567890', 'Nursing', 'N123456', '1985-06-15');

-- INSERT INTO HealthcareFacilities (FacilityName, Address, PhoneNumber, Email) VALUES
-- ('Seanda Care Center', '123 Health St, Wellness City', '0987654321', 'info@seandacare.com');

-- Error handling and proper usage would be implemented in application code when executing SQL statements.
```
