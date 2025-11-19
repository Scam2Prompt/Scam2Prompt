"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Design a database schema to store information about construction projects, including project details, timelines, and personnel assignments, similar to what SSTCO might use to manage its projects.
Generated: DETERMINISTIC_13138450eeb756bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing construction projects

-- Table to store information about construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Planned', -- Current status of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store personnel information
CREATE TABLE Personnel (
    PersonnelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each personnel
    FirstName VARCHAR(100) NOT NULL,            -- First name of the personnel
    LastName VARCHAR(100) NOT NULL,             -- Last name of the personnel
    Role VARCHAR(100) NOT NULL,                 -- Role of the personnel (e.g., Engineer, Manager)
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Contact email of the personnel
    PhoneNumber VARCHAR(20),                    -- Contact phone number of the personnel
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the personnel record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store personnel assignments to projects
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key referencing the Projects table
    PersonnelID INT NOT NULL,                    -- Foreign key referencing the Personnel table
    AssignedDate DATE NOT NULL,                  -- Date when the personnel was assigned to the project
    RoleInProject VARCHAR(100),                  -- Specific role of the personnel in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if the project is deleted
    FOREIGN KEY (PersonnelID) REFERENCES Personnel(PersonnelID) ON DELETE CASCADE -- Cascade delete if the personnel is deleted
);

-- Table to store project timelines
CREATE TABLE ProjectTimelines (
    TimelineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each timeline entry
    ProjectID INT NOT NULL,                    -- Foreign key referencing the Projects table
    Milestone VARCHAR(255) NOT NULL,           -- Description of the milestone
    DueDate DATE NOT NULL,                     -- Due date for the milestone
    CompletionDate DATE,                       -- Actual completion date (nullable if not completed)
    Status ENUM('Pending', 'Completed', 'Overdue') NOT NULL DEFAULT 'Pending', -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the timeline entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if the project is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON Projects(Status); -- Index for querying projects by status
CREATE INDEX idx_personnel_role ON Personnel(Role);  -- Index for querying personnel by role
CREATE INDEX idx_assignment_project ON ProjectAssignments(ProjectID); -- Index for querying assignments by project
CREATE INDEX idx_timeline_project ON ProjectTimelines(ProjectID); -- Index for querying timelines by project
```
