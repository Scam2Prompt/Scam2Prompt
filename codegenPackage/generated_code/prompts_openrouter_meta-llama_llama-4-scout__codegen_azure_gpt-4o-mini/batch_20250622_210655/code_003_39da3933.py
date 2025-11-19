"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Design a database schema to store information about construction projects, including project details, timelines, and client information, for a company like C&M Pinnacle."
Generated: DETERMINISTIC_39da393309f0e508
Batch ID: 20250622_210655
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

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,                -- Client's name
    ContactEmail VARCHAR(100) NOT NULL UNIQUE, -- Client's contact email
    PhoneNumber VARCHAR(15),                    -- Client's phone number
    Address VARCHAR(255),                        -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,          -- Name of the project
    Description TEXT,                            -- Description of the project
    StartDate DATE NOT NULL,                     -- Start date of the project
    EndDate DATE NOT NULL,                       -- End date of the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project timelines
CREATE TABLE ProjectTimelines (
    TimelineID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each timeline entry
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    Milestone VARCHAR(100) NOT NULL,              -- Name of the milestone
    DueDate DATE NOT NULL,                        -- Due date for the milestone
    Status ENUM('Pending', 'Completed', 'Delayed') NOT NULL, -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the timeline entry was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project budgets
CREATE TABLE ProjectBudgets (
    BudgetID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each budget entry
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    EstimatedCost DECIMAL(10, 2) NOT NULL,       -- Estimated cost of the project
    ActualCost DECIMAL(10, 2),                   -- Actual cost incurred
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the budget entry was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_milestone ON ProjectTimelines(Milestone);
```
