"""
Generated Code Metadata:
========================
Original URL: https://daddys-universitys.com
Prompt: "Generate a sample database schema for storing information about traditional buildings and their restoration projects, similar to those handled by Inaka Revive Solutions."
Generated: DETERMINISTIC_946a7a3bf886736e
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about traditional buildings and their restoration projects

CREATE DATABASE TraditionalBuildingsDB;

USE TraditionalBuildingsDB;

-- Table to store information about traditional buildings
CREATE TABLE Buildings (
    BuildingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each building
    Name VARCHAR(255) NOT NULL,                  -- Name of the building
    Location VARCHAR(255) NOT NULL,              -- Location of the building
    YearBuilt INT,                                -- Year the building was constructed
    Style VARCHAR(100),                           -- Architectural style of the building
    Description TEXT,                             -- Description of the building
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about restoration projects
CREATE TABLE RestorationProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each restoration project
    BuildingID INT NOT NULL,                       -- Foreign key referencing the Buildings table
    StartDate DATE NOT NULL,                       -- Start date of the restoration project
    EndDate DATE,                                  -- End date of the restoration project (NULL if ongoing)
    Budget DECIMAL(10, 2),                        -- Budget allocated for the restoration project
    Description TEXT,                              -- Description of the restoration project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (BuildingID) REFERENCES Buildings(BuildingID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about restoration teams
CREATE TABLE RestorationTeams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each restoration team
    TeamName VARCHAR(255) NOT NULL,               -- Name of the restoration team
    ContactPerson VARCHAR(255),                    -- Contact person for the team
    Phone VARCHAR(20),                            -- Phone number for the team
    Email VARCHAR(255),                           -- Email address for the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link restoration projects with restoration teams
CREATE TABLE ProjectTeams (
    ProjectTeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the project-team link
    ProjectID INT NOT NULL,                        -- Foreign key referencing the RestorationProjects table
    TeamID INT NOT NULL,                           -- Foreign key referencing the RestorationTeams table
    Role VARCHAR(100),                             -- Role of the team in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES RestorationProjects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TeamID) REFERENCES RestorationTeams(TeamID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Buildings (Name, Location, YearBuilt, Style, Description) VALUES
('Old Town Hall', 'Springfield', 1800, 'Federal', 'A historic town hall with classic federal architecture.'),
('Heritage House', 'Greenwood', 1850, 'Victorian', 'A beautifully preserved Victorian house.');

INSERT INTO RestorationProjects (BuildingID, StartDate, EndDate, Budget, Description, Status) VALUES
(1, '2023-01-01', NULL, 50000.00, 'Restoration of the Old Town Hall facade.', 'In Progress'),
(2, '2023-06-01', '2023-12-01', 75000.00, 'Complete restoration of Heritage House.', 'Planned');

INSERT INTO RestorationTeams (TeamName, ContactPerson, Phone, Email) VALUES
('Heritage Restorers', 'Alice Johnson', '555-1234', 'alice@heritagerestorers.com'),
('Classic Builders', 'Bob Smith', '555-5678', 'bob@classicbuilders.com');

INSERT INTO ProjectTeams (ProjectID, TeamID, Role) VALUES
(1, 1, 'Lead Contractor'),
(2, 2, 'Consultant');
```
