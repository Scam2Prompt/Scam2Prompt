"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Design a database schema for storing client information and project details for an experiential marketing agency with operations in Uganda, Mozambique, and South Africa."
Generated: DETERMINISTIC_0a652fce223dcbfa
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an Experiential Marketing Agency
-- This schema is designed to store client information and project details
-- for operations in Uganda, Mozambique, and South Africa.

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    Address TEXT,                            -- Physical address of the client
    Country ENUM('Uganda', 'Mozambique', 'South Africa') NOT NULL, -- Country of operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    Country ENUM('Uganda', 'Mozambique', 'South Africa') NOT NULL, -- Country where the project is executed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store team members assigned to projects
CREATE TABLE TeamMembers (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    ProjectID INT NOT NULL,                      -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,                  -- Name of the team member
    Role VARCHAR(100) NOT NULL,                  -- Role of the team member in the project
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Email address of the team member
    PhoneNumber VARCHAR(20),                     -- Phone number of the team member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project milestones
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key referencing the project
    Title VARCHAR(255) NOT NULL,                -- Title of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Due date for the milestone
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store expenses related to projects
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each expense
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Description TEXT NOT NULL,                -- Description of the expense
    Amount DECIMAL(15, 2) NOT NULL,           -- Amount spent
    ExpenseDate DATE NOT NULL,                -- Date of the expense
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_country ON Clients(Country);
CREATE INDEX idx_projects_country ON Projects(Country);
CREATE INDEX idx_milestones_status ON Milestones(Status);
```
