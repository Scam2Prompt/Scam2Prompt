"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Design a database schema for storing architectural project data using Études' comprehensive suite of professional services."
Generated: DETERMINISTIC_2ebf3f4ebd1ff942
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing architectural project data

CREATE DATABASE ArchitecturalProjects;

USE ArchitecturalProjects;

-- Table to store information about architectural projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    ClientName VARCHAR(255) NOT NULL,          -- Name of the client
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Budget DECIMAL(15, 2) NOT NULL,            -- Budget allocated for the project
    Status ENUM('Planning', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp when the project was last updated
);

-- Table to store information about project team members
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each team member
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    MemberName VARCHAR(255) NOT NULL,          -- Name of the team member
    Role VARCHAR(100) NOT NULL,                 -- Role of the team member in the project
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Email of the team member (must be unique)
    Phone VARCHAR(15),                          -- Phone number of the team member (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the team member was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp when the team member was last updated
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store project milestones
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    MilestoneName VARCHAR(255) NOT NULL,        -- Name of the milestone
    DueDate DATE NOT NULL,                       -- Due date for the milestone
    Status ENUM('Pending', 'Completed', 'Delayed') NOT NULL,  -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the milestone was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp when the milestone was last updated
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store project documents
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each document
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    DocumentName VARCHAR(255) NOT NULL,         -- Name of the document
    DocumentPath VARCHAR(255) NOT NULL,         -- Path to the document file
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the document was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store project notes
CREATE TABLE ProjectNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each note
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects
    NoteText TEXT NOT NULL,                      -- Content of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the note was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_client_name ON Projects(ClientName);
CREATE INDEX idx_member_email ON TeamMembers(Email);
CREATE INDEX idx_milestone_due_date ON Milestones(DueDate);
```
