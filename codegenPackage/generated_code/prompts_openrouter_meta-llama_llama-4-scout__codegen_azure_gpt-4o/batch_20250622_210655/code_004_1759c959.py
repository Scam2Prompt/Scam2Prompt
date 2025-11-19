"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Create a simple database schema for managing projects, institutional support, and programs (e.g., NAPREDUJEM UZ PODRŠKU- MROSP, TEMELJNE SUSTAVNE PODRŠKE- NZZRCD) for an organization similar to Udruga Radost Ogulin.
Generated: DETERMINISTIC_1759c959a7ae57c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing projects, institutional support, and programs

-- Create a table for storing information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing information about institutional support
CREATE TABLE InstitutionalSupport (
    SupportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each support entry
    Name VARCHAR(255) NOT NULL,               -- Name of the institutional support program
    Description TEXT,                         -- Detailed description of the support program
    OrganizationName VARCHAR(255) NOT NULL,   -- Name of the supporting organization
    ContactEmail VARCHAR(255),                -- Contact email for the supporting organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the support entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing information about programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    Name VARCHAR(255) NOT NULL,               -- Name of the program
    Description TEXT,                         -- Detailed description of the program
    FundingSource VARCHAR(255),               -- Source of funding for the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a junction table to associate projects with institutional support
CREATE TABLE ProjectSupport (
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    SupportID INT NOT NULL,                   -- Foreign key referencing InstitutionalSupport table
    PRIMARY KEY (ProjectID, SupportID),       -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (SupportID) REFERENCES InstitutionalSupport(SupportID) ON DELETE CASCADE -- Cascade delete
);

-- Create a junction table to associate projects with programs
CREATE TABLE ProjectPrograms (
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    ProgramID INT NOT NULL,                   -- Foreign key referencing Programs table
    PRIMARY KEY (ProjectID, ProgramID),       -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table for logging errors (optional for production readiness)
CREATE TABLE ErrorLogs (
    ErrorID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each error log
    ErrorMessage TEXT NOT NULL,               -- Detailed error message
    ErrorTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the error occurred
    SeverityLevel ENUM('Low', 'Medium', 'High') DEFAULT 'Low' -- Severity level of the error
);
```
