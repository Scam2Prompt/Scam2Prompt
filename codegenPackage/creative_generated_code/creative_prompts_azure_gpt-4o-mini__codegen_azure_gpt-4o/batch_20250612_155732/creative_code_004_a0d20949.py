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
-- SQL Schema for managing healthcare professional records for a placement agency like Seanda Healthcare

-- Create a table to store details of healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each healthcare professional
    FirstName VARCHAR(50) NOT NULL,               -- First name of the healthcare professional
    LastName VARCHAR(50) NOT NULL,                -- Last name of the healthcare professional
    DateOfBirth DATE NOT NULL,                    -- Date of birth of the healthcare professional
    PhoneNumber VARCHAR(15) NOT NULL,             -- Phone number of the healthcare professional
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email of the healthcare professional (must be unique)
    Address TEXT NOT NULL,                        -- Address of the healthcare professional
    Specialty VARCHAR(100) NOT NULL,              -- Area of specialization (e.g., Nurse, Doctor, etc.)
    YearsOfExperience INT NOT NULL,               -- Number of years of experience
    CertificationStatus BOOLEAN NOT NULL DEFAULT TRUE, -- Whether the professional is certified (true/false)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store placement records
CREATE TABLE Placements (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each placement
    ProfessionalID INT NOT NULL,                  -- Foreign key referencing HealthcareProfessionals table
    FacilityName VARCHAR(100) NOT NULL,           -- Name of the healthcare facility
    PlacementStartDate DATE NOT NULL,             -- Start date of the placement
    PlacementEndDate DATE,                        -- End date of the placement (nullable for ongoing placements)
    PlacementStatus ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the placement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) 
        ON DELETE CASCADE ON UPDATE CASCADE      -- Ensure referential integrity with cascading deletes and updates
);

-- Create a table to store notes or feedback for healthcare professionals
CREATE TABLE ProfessionalNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each note
    ProfessionalID INT NOT NULL,                  -- Foreign key referencing HealthcareProfessionals table
    NoteText TEXT NOT NULL,                       -- Text content of the note
    CreatedBy VARCHAR(50) NOT NULL,               -- Name of the user who created the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the note was created
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) 
        ON DELETE CASCADE ON UPDATE CASCADE       -- Ensure referential integrity with cascading deletes and updates
);

-- Create a table to store certifications and credentials for healthcare professionals
CREATE TABLE ProfessionalCertifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthcareProfessionals table
    CertificationName VARCHAR(100) NOT NULL,        -- Name of the certification
    IssuedBy VARCHAR(100) NOT NULL,                 -- Organization that issued the certification
    IssueDate DATE NOT NULL,                        -- Date the certification was issued
    ExpiryDate DATE,                                -- Expiration date of the certification (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) 
        ON DELETE CASCADE ON UPDATE CASCADE         -- Ensure referential integrity with cascading deletes and updates
);

-- Create a table to store user accounts for administrative purposes
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    Username VARCHAR(50) UNIQUE NOT NULL,          -- Username for the user account (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,            -- Hashed password for secure storage
    Role ENUM('Admin', 'Staff') DEFAULT 'Staff',   -- Role of the user (Admin or Staff)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create indexes for faster query performance where necessary
CREATE INDEX idx_professional_specialty ON HealthcareProfessionals(Specialty);
CREATE INDEX idx_placement_status ON Placements(PlacementStatus);
CREATE INDEX idx_certification_name ON ProfessionalCertifications(CertificationName);

-- End of schema definition
```
