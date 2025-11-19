"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Staffing Agency specializing in Healthcare Professionals

-- Create table for healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for professionals
    FirstName VARCHAR(50) NOT NULL,               -- First name of the professional
    LastName VARCHAR(50) NOT NULL,                -- Last name of the professional
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Contact email (must be unique)
    PhoneNumber VARCHAR(15),                      -- Contact phone number
    RoleID INT NOT NULL,                          -- Foreign key referencing the role
    YearsOfExperience INT DEFAULT 0,              -- Years of experience in the field
    CertificationStatus BOOLEAN NOT NULL,         -- Indicates if certification is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create table for healthcare roles (e.g., nurses, doctors, etc.)
CREATE TABLE HealthcareRoles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for roles 
    RoleName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the role (e.g., "Registered Nurse")
    Description TEXT,                      -- Description of the role
    IsActive BOOLEAN DEFAULT TRUE          -- Indicates if the role is actively used
);

-- Create table for client organizations
CREATE TABLE ClientOrganizations (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for clients
    OrganizationName VARCHAR(100) NOT NULL,  -- Name of the client organization
    ContactPerson VARCHAR(100),              -- Name of the primary contact person
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Contact email (must be unique)
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Address TEXT,                            -- Address of the client organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create table for job placements
CREATE TABLE JobPlacements (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for placements
    ProfessionalID INT NOT NULL,                -- Foreign key referencing HealthcareProfessionals
    ClientID INT NOT NULL,                      -- Foreign key referencing ClientOrganizations
    RoleID INT NOT NULL,                        -- Foreign key referencing HealthcareRoles
    StartDate DATE NOT NULL,                    -- Placement start date
    EndDate DATE,                               -- Placement end date (nullable if ongoing)
    IsActive BOOLEAN DEFAULT TRUE,              -- Indicates if the placement is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    CONSTRAINT FK_Professional FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID),
    CONSTRAINT FK_Client FOREIGN KEY (ClientID) REFERENCES ClientOrganizations(ClientID),
    CONSTRAINT FK_Role FOREIGN KEY (RoleID) REFERENCES HealthcareRoles(RoleID)
);

-- Create table for certifications (optional)
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for certifications
    CertificationName VARCHAR(100) NOT NULL,        -- Name of the certification
    IssuingAuthority VARCHAR(100),                  -- Authority that issued the certification
    DateIssued DATE,                                -- Date when the certification was issued
    ExpiryDate DATE,                                -- Expiry date of the certification
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthcareProfessionals
    CONSTRAINT FK_CertificationProfessional FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID)
);

-- Create indexes to optimize queries
CREATE INDEX idx_RoleName ON HealthcareRoles(RoleName);
CREATE INDEX idx_Email ON HealthcareProfessionals(Email);
CREATE INDEX idx_ClientEmail ON ClientOrganizations(Email);
CREATE INDEX idx_PlacementStatus ON JobPlacements(IsActive);
```
