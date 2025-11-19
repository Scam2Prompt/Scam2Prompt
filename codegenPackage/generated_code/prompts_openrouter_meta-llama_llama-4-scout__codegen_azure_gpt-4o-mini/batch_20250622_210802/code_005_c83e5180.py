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
-- Database schema for storing information about construction projects, clients, and teams

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS TeamMembers;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,               -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Email address of the client
    PhoneNumber VARCHAR(20),                   -- Phone number of the client
    Address VARCHAR(255),                       -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store team information
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each team
    TeamName VARCHAR(255) NOT NULL,           -- Name of the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the team was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store team members
CREATE TABLE TeamMembers (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each team member
    TeamID INT NOT NULL,                       -- Foreign key referencing Teams
    Name VARCHAR(255) NOT NULL,                -- Name of the team member
    Role VARCHAR(100),                         -- Role of the team member in the team
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the team member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the member was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    TeamID INT NOT NULL,                       -- Foreign key referencing Teams
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable)
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Clients (Name, ContactEmail, PhoneNumber, Address) VALUES
('Client A', 'clientA@example.com', '123-456-7890', '123 Main St, City, Country'),
('Client B', 'clientB@example.com', '098-765-4321', '456 Elm St, City, Country');

INSERT INTO Teams (TeamName) VALUES
('Team Alpha'),
('Team Beta');

INSERT INTO TeamMembers (TeamID, Name, Role, Email) VALUES
(1, 'Alice Smith', 'Project Manager', 'alice@example.com'),
(1, 'Bob Johnson', 'Engineer', 'bob@example.com'),
(2, 'Charlie Brown', 'Architect', 'charlie@example.com');

INSERT INTO Projects (ClientID, TeamID, ProjectName, StartDate, EndDate, Budget, Status) VALUES
(1, 1, 'Project X', '2023-01-01', '2023-12-31', 100000.00, 'In Progress'),
(2, 2, 'Project Y', '2023-02-01', NULL, 150000.00, 'Planned');
```
