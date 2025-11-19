"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Develop a database schema for managing construction projects and their statuses, inspired by the project categories mentioned on the Sadad Engineering site.
Generated: DETERMINISTIC_84c6000cc50a5178
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Construction Projects and Their Statuses

-- Create a table to store information about construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the construction project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Category VARCHAR(100) NOT NULL,           -- Category of the project (e.g., Residential, Commercial, Industrial)
    Status VARCHAR(50) NOT NULL,              -- Current status of the project (e.g., Planned, In Progress, Completed)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the project record was last updated
);

-- Create a table to store project categories
CREATE TABLE ProjectCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the category (e.g., Residential, Commercial, Industrial)
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the category record was last updated
);

-- Create a table to store project statuses
CREATE TABLE ProjectStatuses (
    StatusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each status
    StatusName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the status (e.g., Planned, In Progress, Completed)
    Description TEXT,                        -- Description of the status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the status record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the status record was last updated
);

-- Add foreign key constraints to ensure data integrity
ALTER TABLE ConstructionProjects
ADD CONSTRAINT FK_ProjectCategory FOREIGN KEY (Category) REFERENCES ProjectCategories(CategoryName)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE ConstructionProjects
ADD CONSTRAINT FK_ProjectStatus FOREIGN KEY (Status) REFERENCES ProjectStatuses(StatusName)
ON DELETE SET NULL ON UPDATE CASCADE;

-- Example indexes for optimizing queries
CREATE INDEX idx_project_category ON ConstructionProjects(Category);
CREATE INDEX idx_project_status ON ConstructionProjects(Status);

-- Example data insertion for categories
INSERT INTO ProjectCategories (CategoryName, Description)
VALUES 
('Residential', 'Projects related to residential buildings and housing.'),
('Commercial', 'Projects related to commercial buildings such as offices and malls.'),
('Industrial', 'Projects related to industrial facilities and factories.');

-- Example data insertion for statuses
INSERT INTO ProjectStatuses (StatusName, Description)
VALUES 
('Planned', 'Project is in the planning phase.'),
('In Progress', 'Project is currently under construction.'),
('Completed', 'Project has been completed.');
```
