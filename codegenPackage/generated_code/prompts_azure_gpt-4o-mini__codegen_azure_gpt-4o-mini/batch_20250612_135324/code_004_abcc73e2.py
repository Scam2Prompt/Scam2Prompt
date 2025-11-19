"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about completed renovation projects

-- Create a table for storing client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the renovation project
    ProjectScope TEXT NOT NULL,                -- Description of the project scope
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE NOT NULL,                     -- End date of the project
    TotalCost DECIMAL(10, 2) NOT NULL,        -- Total cost of the project
    Status ENUM('Completed', 'In Progress', 'Cancelled') DEFAULT 'Completed',  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing project costs breakdown
CREATE TABLE ProjectCosts (
    CostID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each cost entry
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects table
    CostDescription VARCHAR(255) NOT NULL,     -- Description of the cost
    CostAmount DECIMAL(10, 2) NOT NULL,        -- Amount of the cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing project milestones
CREATE TABLE ProjectMilestones (
    MilestoneID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects table
    MilestoneDescription VARCHAR(255) NOT NULL, -- Description of the milestone
    MilestoneDate DATE NOT NULL,                 -- Date of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_client ON Projects(ClientID);
CREATE INDEX idx_project_cost_project ON ProjectCosts(ProjectID);
CREATE INDEX idx_project_milestone_project ON ProjectMilestones(ProjectID);
```
