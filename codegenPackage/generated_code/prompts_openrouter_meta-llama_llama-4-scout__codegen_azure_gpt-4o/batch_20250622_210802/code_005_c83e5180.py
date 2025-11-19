"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Design a database schema for storing information about construction projects, clients, and teams, inspired by the data presented on the INARO S.A.S. website."
Generated: DETERMINISTIC_c83e518066c98c89
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Construction Projects, Clients, and Teams

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE,               -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store information about teams
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    Name VARCHAR(255) NOT NULL,            -- Name of the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about team members
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    Name VARCHAR(255) NOT NULL,              -- Name of the team member
    Role VARCHAR(255),                       -- Role of the team member (e.g., Engineer, Architect)
    Email VARCHAR(255) UNIQUE,               -- Email address of the team member
    PhoneNumber VARCHAR(20),                 -- Phone number of the team member
    TeamID INT NOT NULL,                     -- Foreign key referencing the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Table to associate projects with teams
CREATE TABLE ProjectTeams (
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    TeamID INT NOT NULL,    -- Foreign key referencing the team
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the team was assigned to the project
    PRIMARY KEY (ProjectID, TeamID), -- Composite primary key to ensure unique associations
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Table to track project milestones
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,                 -- Name of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Due date for the milestone
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Table to track expenses related to projects
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each expense
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Description TEXT NOT NULL,                -- Description of the expense
    Amount DECIMAL(15, 2) NOT NULL,           -- Amount of the expense
    IncurredAt DATE NOT NULL,                 -- Date the expense was incurred
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);
```
