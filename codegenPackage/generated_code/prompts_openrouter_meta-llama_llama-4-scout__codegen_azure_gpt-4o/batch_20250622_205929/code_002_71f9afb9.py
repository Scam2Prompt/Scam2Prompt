"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Generate a sample database schema for storing information about construction projects, including project details, timelines, and stakeholders, inspired by the project portfolio of Sadad Engineering and Construction Company.
Generated: DETERMINISTIC_71f9afb99a6054e2
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Construction Projects

-- Table to store information about construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Planned', -- Current status of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about stakeholders involved in the projects
CREATE TABLE Stakeholders (
    StakeholderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each stakeholder
    FullName VARCHAR(255) NOT NULL,               -- Full name of the stakeholder
    Email VARCHAR(255) UNIQUE NOT NULL,           -- Email address of the stakeholder
    PhoneNumber VARCHAR(20),                      -- Contact number of the stakeholder
    Role ENUM('Client', 'Contractor', 'Engineer', 'Architect', 'Other') NOT NULL, -- Role of the stakeholder
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the stakeholder record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store the relationship between projects and stakeholders
CREATE TABLE ProjectStakeholders (
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    StakeholderID INT NOT NULL,                  -- Foreign key referencing Stakeholders table
    PRIMARY KEY (ProjectID, StakeholderID),      -- Composite primary key to ensure unique relationships
    RoleInProject VARCHAR(255),                  -- Specific role of the stakeholder in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (StakeholderID) REFERENCES Stakeholders(StakeholderID) ON DELETE CASCADE -- Cascade delete if stakeholder is deleted
);

-- Table to store project milestones and timelines
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects table
    MilestoneName VARCHAR(255) NOT NULL,        -- Name of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Due date for the milestone
    Status ENUM('Pending', 'Completed', 'Overdue') NOT NULL DEFAULT 'Pending', -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the milestone record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store project documents and files
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    FileName VARCHAR(255) NOT NULL,            -- Name of the file/document
    FilePath VARCHAR(255) NOT NULL,            -- Path to the file/document
    UploadedBy INT NOT NULL,                   -- Foreign key referencing Stakeholders table (who uploaded the document)
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the document was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (UploadedBy) REFERENCES Stakeholders(StakeholderID) ON DELETE SET NULL -- Set uploader to NULL if stakeholder is deleted
);

-- Table to store project-related tasks
CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each task
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    TaskName VARCHAR(255) NOT NULL,            -- Name of the task
    AssignedTo INT,                            -- Foreign key referencing Stakeholders table (who is assigned the task)
    DueDate DATE NOT NULL,                     -- Due date for the task
    Status ENUM('Pending', 'In Progress', 'Completed', 'Overdue') NOT NULL DEFAULT 'Pending', -- Current status of the task
    Priority ENUM('Low', 'Medium', 'High') NOT NULL DEFAULT 'Medium', -- Priority level of the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the task record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (AssignedTo) REFERENCES Stakeholders(StakeholderID) ON DELETE SET NULL -- Set assignee to NULL if stakeholder is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_milestone_status ON Milestones(Status);
CREATE INDEX idx_task_status ON Tasks(Status);
CREATE INDEX idx_task_priority ON Tasks(Priority);
```
