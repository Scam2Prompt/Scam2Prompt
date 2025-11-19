"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Design a database schema to store information about construction projects, including client details, project scope, timelines, and budgets, for a company like ILMAM Construction."
Generated: DETERMINISTIC_ea60fa67707d04a1
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

CREATE DATABASE ILMAM_Construction;

USE ILMAM_Construction;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,                -- Client's name
    ContactEmail VARCHAR(100) NOT NULL UNIQUE, -- Client's contact email
    PhoneNumber VARCHAR(15),                    -- Client's phone number
    Address VARCHAR(255),                        -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    ProjectName VARCHAR(100) NOT NULL,          -- Name of the project
    Scope TEXT NOT NULL,                         -- Description of the project scope
    StartDate DATE NOT NULL,                     -- Project start date
    EndDate DATE NOT NULL,                       -- Project end date
    Budget DECIMAL(15, 2) NOT NULL,             -- Project budget
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project milestones
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    MilestoneName VARCHAR(100) NOT NULL,         -- Name of the milestone
    DueDate DATE NOT NULL,                        -- Due date for the milestone
    Status ENUM('Pending', 'Completed') DEFAULT 'Pending', -- Milestone status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project expenses
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each expense
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    Description VARCHAR(255) NOT NULL,           -- Description of the expense
    Amount DECIMAL(15, 2) NOT NULL,              -- Amount of the expense
    ExpenseDate DATE NOT NULL,                    -- Date of the expense
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project team members
CREATE TABLE TeamMembers (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each team member
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    Name VARCHAR(100) NOT NULL,                   -- Name of the team member
    Role VARCHAR(50) NOT NULL,                    -- Role of the team member in the project
    ContactEmail VARCHAR(100) NOT NULL,          -- Contact email of the team member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_milestone_due_date ON Milestones(DueDate);
CREATE INDEX idx_expense_date ON Expenses(ExpenseDate);
CREATE INDEX idx_team_member_name ON TeamMembers(Name);
```
