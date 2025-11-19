"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Design a database schema to store information about dental education programs, including program duration, accreditation details, and course schedules, inspired by the offerings of INESO."
Generated: DETERMINISTIC_b2a5375f37e917ef
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about dental education programs

-- Table to store information about dental education programs
CREATE TABLE DentalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the dental education program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    AccreditationDetails TEXT NOT NULL,       -- Accreditation information for the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store course schedules for each program
CREATE TABLE CourseSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ProgramID INT NOT NULL,                    -- Foreign key referencing DentalPrograms
    CourseName VARCHAR(255) NOT NULL,          -- Name of the course
    StartDate DATE NOT NULL,                   -- Start date of the course
    EndDate DATE NOT NULL,                     -- End date of the course
    InstructorName VARCHAR(255),               -- Name of the instructor for the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the schedule was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProgramID) REFERENCES DentalPrograms(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store accreditation organizations
CREATE TABLE AccreditationOrganizations (
    OrganizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organization
    OrganizationName VARCHAR(255) NOT NULL,        -- Name of the accreditation organization
    ContactInfo TEXT,                              -- Contact information for the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the organization was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to link programs with accreditation organizations
CREATE TABLE ProgramAccreditations (
    AccreditationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accreditation record
    ProgramID INT NOT NULL,                         -- Foreign key referencing DentalPrograms
    OrganizationID INT NOT NULL,                    -- Foreign key referencing AccreditationOrganizations
    AccreditationDate DATE NOT NULL,                -- Date when the program was accredited
    ExpiryDate DATE,                                 -- Expiry date of the accreditation (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the accreditation record was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProgramID) REFERENCES DentalPrograms(ProgramID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (OrganizationID) REFERENCES AccreditationOrganizations(OrganizationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_program_name ON DentalPrograms(ProgramName);
CREATE INDEX idx_course_name ON CourseSchedules(CourseName);
CREATE INDEX idx_organization_name ON AccreditationOrganizations(OrganizationName);
CREATE INDEX idx_accreditation_date ON ProgramAccreditations(AccreditationDate);

-- Error handling and constraints
-- Ensure that course schedules have valid dates
ALTER TABLE CourseSchedules
ADD CONSTRAINT chk_dates CHECK (StartDate < EndDate);

-- Ensure that accreditation expiry dates are valid
ALTER TABLE ProgramAccreditations
ADD CONSTRAINT chk_expiry_date CHECK (AccreditationDate < ExpiryDate OR ExpiryDate IS NULL);
```
