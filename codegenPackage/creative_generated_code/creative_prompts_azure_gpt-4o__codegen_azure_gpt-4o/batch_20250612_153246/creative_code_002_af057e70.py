"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Create a database schema for storing information about ENAFO's academic programs, including monitorías, modules, and seasonal offerings, along with student enrollment details.
Generated: DETERMINISTIC_af057e70c64c2fc8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for ENAFO's academic programs

-- Table: Programs
-- Stores information about academic programs offered by ENAFO
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the academic program
    Description TEXT,                         -- Description of the program
    DurationMonths INT NOT NULL,             -- Duration of the program in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Modules
-- Stores information about modules within each academic program
CREATE TABLE Modules (
    ModuleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each module
    ProgramID INT NOT NULL,                  -- Foreign key referencing Programs table
    ModuleName VARCHAR(255) NOT NULL,        -- Name of the module
    ModuleDescription TEXT,                  -- Description of the module
    DurationWeeks INT NOT NULL,              -- Duration of the module in weeks
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade deletion if program is deleted
);

-- Table: SeasonalOfferings
-- Stores information about seasonal offerings of programs
CREATE TABLE SeasonalOfferings (
    OfferingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each offering
    ProgramID INT NOT NULL,                    -- Foreign key referencing Programs table
    Season VARCHAR(50) NOT NULL,               -- Season (e.g., Spring, Summer, Fall, Winter)
    Year INT NOT NULL,                         -- Year of the offering
    StartDate DATE NOT NULL,                   -- Start date of the offering
    EndDate DATE NOT NULL,                     -- End date of the offering
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade deletion if program is deleted
);

-- Table: Monitorias
-- Stores information about monitorías (mentorships or guided sessions) for modules
CREATE TABLE Monitorias (
    MonitoriaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each monitoría
    ModuleID INT NOT NULL,                      -- Foreign key referencing Modules table
    MentorName VARCHAR(255) NOT NULL,           -- Name of the mentor
    SessionDate DATE NOT NULL,                  -- Date of the monitoría session
    DurationHours INT NOT NULL,                 -- Duration of the monitoría session in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ModuleID) REFERENCES Modules(ModuleID) ON DELETE CASCADE -- Cascade deletion if module is deleted
);

-- Table: Students
-- Stores information about students enrolled in ENAFO
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,           -- First name of the student
    LastName VARCHAR(100) NOT NULL,            -- Last name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the student
    PhoneNumber VARCHAR(15),                   -- Phone number of the student
    EnrollmentDate DATE NOT NULL,              -- Date the student enrolled
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Enrollments
-- Stores information about student enrollments in seasonal offerings
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    OfferingID INT NOT NULL,                     -- Foreign key referencing SeasonalOfferings table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade deletion if student is deleted
    FOREIGN KEY (OfferingID) REFERENCES SeasonalOfferings(OfferingID) ON DELETE CASCADE -- Cascade deletion if offering is deleted
);

-- Ensure all tables use UTF-8 encoding for international support
SET NAMES utf8mb4;
```
