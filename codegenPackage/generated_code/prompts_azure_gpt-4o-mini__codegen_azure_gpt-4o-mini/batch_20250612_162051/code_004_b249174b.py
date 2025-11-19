"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Construct a database schema for managing information on various types of construction projects, including underground and engineering works, as highlighted by URANPRES.
Generated: DETERMINISTIC_b249174bea685afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing construction projects
CREATE DATABASE ConstructionProjects;

USE ConstructionProjects;

-- Table to store information about different types of construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    ProjectType ENUM('Underground', 'Engineering', 'Other') NOT NULL, -- Type of project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable)
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the project was last updated
);

-- Table to store information about project teams
CREATE TABLE ProjectTeams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each team
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects
    TeamName VARCHAR(255) NOT NULL,            -- Name of the team
    TeamLead VARCHAR(255) NOT NULL,            -- Name of the team lead
    MembersCount INT NOT NULL,                  -- Number of members in the team
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about project tasks
CREATE TABLE ProjectTasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each task
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    TaskName VARCHAR(255) NOT NULL,             -- Name of the task
    AssignedTo VARCHAR(255),                     -- Name of the person assigned to the task
    DueDate DATE NOT NULL,                       -- Due date for the task
    Status ENUM('Not Started', 'In Progress', 'Completed') NOT NULL, -- Current status of the task
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about project materials
CREATE TABLE ProjectMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each material
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    MaterialName VARCHAR(255) NOT NULL,         -- Name of the material
    Quantity DECIMAL(10, 2) NOT NULL,           -- Quantity of the material
    Unit VARCHAR(50) NOT NULL,                  -- Unit of measurement (e.g., kg, m3)
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about project locations
CREATE TABLE ProjectLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each location
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    Address VARCHAR(255) NOT NULL,               -- Address of the project location
    Latitude DECIMAL(9, 6),                      -- Latitude for geolocation
    Longitude DECIMAL(9, 6),                     -- Longitude for geolocation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project-related documents
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each document
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    DocumentName VARCHAR(255) NOT NULL,         -- Name of the document
    DocumentPath VARCHAR(255) NOT NULL,         -- Path to the document file
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the document was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_type ON Projects(ProjectType);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_task_status ON ProjectTasks(Status);
CREATE INDEX idx_material_project ON ProjectMaterials(ProjectID);
CREATE INDEX idx_location_project ON ProjectLocations(ProjectID);
CREATE INDEX idx_document_project ON ProjectDocuments(ProjectID);
```
