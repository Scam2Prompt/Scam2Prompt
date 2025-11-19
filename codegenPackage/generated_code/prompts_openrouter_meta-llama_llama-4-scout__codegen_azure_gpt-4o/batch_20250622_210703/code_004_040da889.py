"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Design a database schema to store information about construction projects, clients, and team members for a design-build and turnkey construction services company, and provide an example of how to query the database."
Generated: DETERMINISTIC_040da88968a618df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Construction Projects, Clients, and Team Members

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    Phone VARCHAR(20),                       -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store team member information
CREATE TABLE TeamMembers (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    Name VARCHAR(255) NOT NULL,                  -- Name of the team member
    Role VARCHAR(100) NOT NULL,                  -- Role of the team member (e.g., Architect, Engineer)
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the team member
    Phone VARCHAR(20),                           -- Phone number of the team member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store construction project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Description of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project
    Budget DECIMAL(15, 2),                    -- Budget for the project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store the association between projects and team members
CREATE TABLE ProjectTeam (
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    TeamMemberID INT NOT NULL,                -- Foreign key referencing TeamMembers table
    AssignedRole VARCHAR(100),                -- Role assigned to the team member for the project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for assignment
    PRIMARY KEY (ProjectID, TeamMemberID),    -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (TeamMemberID) REFERENCES TeamMembers(TeamMemberID) ON DELETE CASCADE
);

-- Example Query: Retrieve all projects along with their client information and assigned team members
SELECT 
    p.ProjectID,
    p.Name AS ProjectName,
    p.Description,
    p.StartDate,
    p.EndDate,
    p.Budget,
    c.Name AS ClientName,
    c.Email AS ClientEmail,
    tm.Name AS TeamMemberName,
    tm.Role AS TeamMemberRole,
    pt.AssignedRole AS ProjectRole
FROM 
    Projects p
JOIN 
    Clients c ON p.ClientID = c.ClientID
LEFT JOIN 
    ProjectTeam pt ON p.ProjectID = pt.ProjectID
LEFT JOIN 
    TeamMembers tm ON pt.TeamMemberID = tm.TeamMemberID
ORDER BY 
    p.ProjectID, tm.Name;
```
