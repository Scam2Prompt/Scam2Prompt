"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Design a database schema for storing information about local government projects and initiatives in Khao Luang Subdistrict, including tables for project details, funding, and responsible agencies.
Generated: DETERMINISTIC_563c040e62422d5b
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Local Government Projects in Khao Luang Subdistrict

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store funding details for each project
CREATE TABLE Funding (
    FundingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each funding record
    ProjectID INT NOT NULL,                   -- Foreign key referencing the Projects table
    Amount DECIMAL(15, 2) NOT NULL,           -- Amount of funding allocated
    Source VARCHAR(255) NOT NULL,             -- Source of funding (e.g., government, private, NGO)
    AllocatedDate DATE NOT NULL,              -- Date when the funding was allocated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the funding record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store information about responsible agencies
CREATE TABLE Agencies (
    AgencyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each agency
    AgencyName VARCHAR(255) NOT NULL,         -- Name of the agency
    ContactPerson VARCHAR(255),               -- Name of the contact person in the agency
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(255),                       -- Contact email address
    Address TEXT,                             -- Address of the agency
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the agency record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to map projects to responsible agencies
CREATE TABLE ProjectAgencies (
    ProjectID INT NOT NULL,                   -- Foreign key referencing the Projects table
    AgencyID INT NOT NULL,                    -- Foreign key referencing the Agencies table
    Role VARCHAR(255) NOT NULL,               -- Role of the agency in the project (e.g., Lead, Support)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the mapping record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    PRIMARY KEY (ProjectID, AgencyID),        -- Composite primary key to ensure unique mapping
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (AgencyID) REFERENCES Agencies(AgencyID) ON DELETE CASCADE -- Cascade delete if agency is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON Projects(Status); -- Index for querying projects by status
CREATE INDEX idx_funding_project ON Funding(ProjectID); -- Index for querying funding by project
CREATE INDEX idx_agency_name ON Agencies(AgencyName); -- Index for querying agencies by name
```
