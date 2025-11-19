"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Staffing Agency Specializing in Healthcare Professionals

-- Create a table for healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,                -- First name of the professional
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the professional
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    DateOfBirth DATE,                              -- Date of birth
    Gender ENUM('Male', 'Female', 'Other'),        -- Gender of the professional
    Address TEXT,                                  -- Address of the professional
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for roles (e.g., Nurse, Doctor, etc.)
CREATE TABLE Roles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each role
    RoleName VARCHAR(100) UNIQUE NOT NULL,         -- Name of the role (e.g., Nurse, Doctor)
    Description TEXT,                              -- Description of the role
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for job placements
CREATE TABLE JobPlacements (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each placement
    ProfessionalID INT NOT NULL,                   -- Foreign key referencing HealthcareProfessionals
    RoleID INT NOT NULL,                           -- Foreign key referencing Roles
    EmployerName VARCHAR(100) NOT NULL,            -- Name of the employer
    StartDate DATE NOT NULL,                       -- Start date of the placement
    EndDate DATE,                                  -- End date of the placement (nullable for ongoing placements)
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the placement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID) ON DELETE CASCADE
);

-- Create a table for certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthcareProfessionals
    CertificationName VARCHAR(100) NOT NULL,        -- Name of the certification
    IssuedBy VARCHAR(100),                          -- Issuing organization
    IssueDate DATE NOT NULL,                        -- Date the certification was issued
    ExpiryDate DATE,                                -- Expiry date of the certification (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE
);

-- Create a table for availability of professionals
CREATE TABLE Availability (
    AvailabilityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each availability record
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthcareProfessionals
    AvailableFrom DATE NOT NULL,                    -- Start date of availability
    AvailableTo DATE,                               -- End date of availability (nullable for open-ended availability)
    Notes TEXT,                                     -- Additional notes about availability
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE
);

-- Create a table for timesheets
CREATE TABLE Timesheets (
    TimesheetID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each timesheet
    PlacementID INT NOT NULL,                       -- Foreign key referencing JobPlacements
    WorkDate DATE NOT NULL,                         -- Date of work
    HoursWorked DECIMAL(5, 2) NOT NULL,             -- Number of hours worked
    Notes TEXT,                                     -- Additional notes about the work
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PlacementID) REFERENCES JobPlacements(PlacementID) ON DELETE CASCADE
);

-- Insert sample roles based on Amazing Grace Medical Recruitment's site
INSERT INTO Roles (RoleName, Description) VALUES
('Registered Nurse', 'A healthcare professional who provides patient care and coordinates treatment.'),
('Enrolled Nurse', 'A nurse who works under the supervision of a registered nurse.'),
('Assistant in Nursing', 'A healthcare worker who assists nurses in providing care.'),
('Midwife', 'A healthcare professional specializing in pregnancy, childbirth, and postpartum care.'),
('Doctor', 'A licensed medical practitioner.'),
('Allied Health Professional', 'A professional providing diagnostic, technical, and therapeutic services.');

-- End of schema
```
