"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate a SQL database schema to store information about construction projects, including project type (e.g., pole construction, electrical and civil engineering), location, and project status, for a company like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_82e85303a5f33780
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Construction Projects Database

-- Table to store information about project types
CREATE TABLE ProjectTypes (
    ProjectTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project type
    TypeName VARCHAR(255) NOT NULL UNIQUE,        -- Name of the project type (e.g., Pole Construction, Electrical Engineering)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about project statuses
CREATE TABLE ProjectStatuses (
    StatusID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each project status
    StatusName VARCHAR(255) NOT NULL UNIQUE,      -- Name of the project status (e.g., In Progress, Completed, On Hold)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,            -- Name of the project
    ProjectTypeID INT NOT NULL,                   -- Foreign key referencing ProjectTypes
    Location VARCHAR(255) NOT NULL,               -- Location of the project
    StatusID INT NOT NULL,                        -- Foreign key referencing ProjectStatuses
    StartDate DATE,                               -- Start date of the project
    EndDate DATE,                                 -- End date of the project (nullable for ongoing projects)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE CASCADE ON UPDATE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (StatusID) REFERENCES ProjectStatuses(StatusID) ON DELETE CASCADE ON UPDATE CASCADE -- Enforce referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_project_type ON ConstructionProjects(ProjectTypeID);
CREATE INDEX idx_project_status ON ConstructionProjects(StatusID);
CREATE INDEX idx_project_location ON ConstructionProjects(Location);

-- Example data insertion for ProjectTypes
INSERT INTO ProjectTypes (TypeName) VALUES 
('Pole Construction'),
('Electrical Engineering'),
('Civil Engineering');

-- Example data insertion for ProjectStatuses
INSERT INTO ProjectStatuses (StatusName) VALUES 
('Not Started'),
('In Progress'),
('Completed'),
('On Hold');
```
