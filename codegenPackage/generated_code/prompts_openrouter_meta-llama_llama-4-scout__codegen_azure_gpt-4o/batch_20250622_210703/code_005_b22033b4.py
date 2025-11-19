"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Design a database schema for storing information about NGO projects, volunteers, and beneficiaries, using Youngistaan Foundation as a case study."
Generated: DETERMINISTIC_b22033b41ef23c36
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for NGO Projects, Volunteers, and Beneficiaries
-- Case Study: Youngistaan Foundation

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Active', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each volunteer
    FullName VARCHAR(255) NOT NULL,             -- Full name of the volunteer
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Email address of the volunteer
    PhoneNumber VARCHAR(15),                    -- Contact number of the volunteer
    Skills TEXT,                                -- Skills or expertise of the volunteer
    Availability ENUM('Full-Time', 'Part-Time', 'Occasional') NOT NULL, -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the volunteer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FullName VARCHAR(255) NOT NULL,               -- Full name of the beneficiary
    Age INT,                                      -- Age of the beneficiary
    Gender ENUM('Male', 'Female', 'Other'),       -- Gender of the beneficiary
    ContactInfo TEXT,                             -- Contact information (if applicable)
    Address TEXT,                                 -- Address of the beneficiary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the beneficiary was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to map volunteers to projects (many-to-many relationship)
CREATE TABLE ProjectVolunteers (
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    VolunteerID INT NOT NULL,                     -- Foreign key referencing Volunteers table
    Role VARCHAR(255),                            -- Role of the volunteer in the project
    AssignedDate DATE NOT NULL,                   -- Date when the volunteer was assigned to the project
    PRIMARY KEY (ProjectID, VolunteerID),         -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to map beneficiaries to projects (many-to-many relationship)
CREATE TABLE ProjectBeneficiaries (
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    BeneficiaryID INT NOT NULL,                   -- Foreign key referencing Beneficiaries table
    AssistanceProvided TEXT,                      -- Description of assistance provided to the beneficiary
    AssistanceDate DATE NOT NULL,                 -- Date when assistance was provided
    PRIMARY KEY (ProjectID, BeneficiaryID),       -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_volunteer_email ON Volunteers(Email);
CREATE INDEX idx_beneficiary_name ON Beneficiaries(FullName);
```
