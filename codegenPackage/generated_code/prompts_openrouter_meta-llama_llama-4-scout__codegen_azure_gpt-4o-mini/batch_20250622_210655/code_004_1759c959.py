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

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS InstitutionalSupport;
DROP TABLE IF EXISTS Programs;

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Description TEXT,                           -- Description of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store institutional support information
CREATE TABLE InstitutionalSupport (
    SupportID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each support entry
    SupportName VARCHAR(255) NOT NULL,         -- Name of the institutional support
    Description TEXT,                           -- Description of the support
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the support was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store program information
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the program
    SupportID INT,                              -- Foreign key referencing InstitutionalSupport
    Description TEXT,                           -- Description of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (SupportID) REFERENCES InstitutionalSupport(SupportID) ON DELETE SET NULL  -- Foreign key constraint
);

-- Sample data insertion (optional)
INSERT INTO InstitutionalSupport (SupportName, Description) VALUES
('NAPREDUJEM UZ PODRŠKU- MROSP', 'Support program for project advancement.'),
('TEMELJNE SUSTAVNE PODRŠKE- NZZRCD', 'Basic systemic support program.');

INSERT INTO Projects (ProjectName, StartDate, EndDate, Description) VALUES
('Project A', '2023-01-01', '2023-12-31', 'Description for Project A.'),
('Project B', '2023-02-01', NULL, 'Description for Project B.');

INSERT INTO Programs (ProgramName, SupportID, Description) VALUES
('Program 1', 1, 'Description for Program 1.'),
('Program 2', 2, 'Description for Program 2.');
```
