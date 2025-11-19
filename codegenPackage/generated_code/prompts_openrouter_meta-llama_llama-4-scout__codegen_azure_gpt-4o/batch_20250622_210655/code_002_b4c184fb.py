"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Generate a sample database schema for storing information about construction projects, including underground construction, geological surveys, and client details, similar to what URANPRES, s.r.o. might use."
Generated: DETERMINISTIC_b4c184fb22988bf2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects, 
-- including underground construction, geological surveys, and client details.

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL,      -- Email address of the client
    ContactPhone VARCHAR(20),                -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table for storing construction project details
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the construction project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for storing geological survey details
CREATE TABLE GeologicalSurveys (
    SurveyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each survey
    ProjectID INT NOT NULL,                  -- Foreign key referencing the construction project
    SurveyDate DATE NOT NULL,                -- Date of the geological survey
    SurveyType ENUM('Seismic', 'Geotechnical', 'Hydrological', 'Other') NOT NULL, -- Type of survey
    Findings TEXT,                           -- Detailed findings of the survey
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE
);

-- Create a table for storing underground construction details
CREATE TABLE UndergroundConstructions (
    UndergroundID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each underground construction
    ProjectID INT NOT NULL,                       -- Foreign key referencing the construction project
    ConstructionType ENUM('Tunnel', 'Pipeline', 'Mine', 'Other') NOT NULL, -- Type of underground construction
    Depth INT NOT NULL,                           -- Depth of the construction in meters
    Length DECIMAL(10, 2),                        -- Length of the construction in meters
    Description TEXT,                             -- Description of the construction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE
);

-- Create indexes for faster querying
CREATE INDEX idx_ClientID ON ConstructionProjects(ClientID);
CREATE INDEX idx_ProjectID ON GeologicalSurveys(ProjectID);
CREATE INDEX idx_ProjectID_Underground ON UndergroundConstructions(ProjectID);

-- Ensure proper error handling and data integrity
-- Use appropriate constraints and foreign keys to maintain relationships between tables.
```
