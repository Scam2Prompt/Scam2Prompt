"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema to store information about beneficiaries, volunteers, and projects for an organization like Rakhshanda Memorial, focusing on psychological health and financial independence initiatives.
Generated: DETERMINISTIC_514619b18bc5a19f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Rakhshanda Memorial Organization

-- Table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FullName VARCHAR(100) NOT NULL,              -- Full name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the beneficiary
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    ContactNumber VARCHAR(15),                   -- Contact number of the beneficiary
    Email VARCHAR(100),                          -- Email address of the beneficiary
    Address TEXT,                                -- Address of the beneficiary
    PsychologicalHealthStatus TEXT,              -- Details about psychological health status
    FinancialIndependenceStatus TEXT,            -- Details about financial independence status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each volunteer
    FullName VARCHAR(100) NOT NULL,              -- Full name of the volunteer
    ContactNumber VARCHAR(15),                   -- Contact number of the volunteer
    Email VARCHAR(100) NOT NULL,                 -- Email address of the volunteer
    Skills TEXT,                                 -- Skills or expertise of the volunteer
    Availability ENUM('Full-Time', 'Part-Time') NOT NULL, -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    ProjectName VARCHAR(100) NOT NULL,           -- Name of the project
    Description TEXT,                            -- Description of the project
    StartDate DATE NOT NULL,                     -- Start date of the project
    EndDate DATE,                                -- End date of the project (nullable for ongoing projects)
    Budget DECIMAL(10, 2),                       -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between beneficiaries and projects
CREATE TABLE BeneficiaryProjects (
    BeneficiaryProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    BeneficiaryID INT NOT NULL,                          -- Foreign key referencing Beneficiaries table
    ProjectID INT NOT NULL,                              -- Foreign key referencing Projects table
    Role ENUM('Participant', 'Recipient') NOT NULL,      -- Role of the beneficiary in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store the relationship between volunteers and projects
CREATE TABLE VolunteerProjects (
    VolunteerProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the relationship
    VolunteerID INT NOT NULL,                            -- Foreign key referencing Volunteers table
    ProjectID INT NOT NULL,                              -- Foreign key referencing Projects table
    Role ENUM('Coordinator', 'Support') NOT NULL,        -- Role of the volunteer in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store logs for error tracking and auditing
CREATE TABLE Logs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,                -- Unique identifier for each log entry
    LogType ENUM('Error', 'Info', 'Warning') NOT NULL,   -- Type of log entry
    Message TEXT NOT NULL,                               -- Log message
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP        -- Timestamp of log creation
);
```
