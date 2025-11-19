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
-- Database schema for storing information about construction projects
CREATE DATABASE ConstructionProjects;

USE ConstructionProjects;

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE NOT NULL,                     -- End date of the project
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store stakeholders involved in projects
CREATE TABLE Stakeholders (
    StakeholderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each stakeholder
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects
    Name VARCHAR(255) NOT NULL,                   -- Name of the stakeholder
    Role VARCHAR(100) NOT NULL,                   -- Role of the stakeholder in the project
    ContactInfo VARCHAR(255),                     -- Contact information for the stakeholder
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project timelines
CREATE TABLE Timelines (
    TimelineID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each timeline entry
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects
    Milestone VARCHAR(255) NOT NULL,              -- Description of the milestone
    DueDate DATE NOT NULL,                         -- Due date for the milestone
    Status ENUM('Pending', 'Completed', 'Delayed') NOT NULL, -- Current status of the milestone
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project documents
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each document
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects
    DocumentName VARCHAR(255) NOT NULL,           -- Name of the document
    DocumentType ENUM('Report', 'Plan', 'Drawing', 'Contract') NOT NULL, -- Type of document
    FilePath VARCHAR(255) NOT NULL,               -- Path to the document file
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the document was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO Projects (ProjectName, Description, StartDate, EndDate, Budget, Status) VALUES
('Bridge Construction', 'Construction of a new bridge over the river.', '2023-01-01', '2023-12-31', 5000000.00, 'In Progress'),
('Highway Expansion', 'Expanding the existing highway to accommodate more traffic.', '2023-02-01', '2024-06-30', 15000000.00, 'Planned');

INSERT INTO Stakeholders (ProjectID, Name, Role, ContactInfo) VALUES
(1, 'John Doe', 'Project Manager', 'john.doe@example.com'),
(1, 'Jane Smith', 'Civil Engineer', 'jane.smith@example.com');

INSERT INTO Timelines (ProjectID, Milestone, DueDate, Status) VALUES
(1, 'Foundation Completion', '2023-06-30', 'Pending'),
(1, 'Bridge Deck Installation', '2023-09-30', 'Pending');

INSERT INTO ProjectDocuments (ProjectID, DocumentName, DocumentType, FilePath) VALUES
(1, 'Project Plan', 'Plan', '/documents/bridge_project_plan.pdf'),
(1, 'Contract Agreement', 'Contract', '/documents/bridge_contract.pdf');
```
