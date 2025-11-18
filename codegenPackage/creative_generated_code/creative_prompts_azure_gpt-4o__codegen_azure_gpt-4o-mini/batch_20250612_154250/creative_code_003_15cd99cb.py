"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tari.ee
Prompt: Create a database schema for managing architectural projects, including fields for client needs and rational solutions, as outlined on Tari.ee.
Generated: DETERMINISTIC_15cd99cba158f819
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing architectural projects

CREATE DATABASE ArchitecturalProjects;

USE ArchitecturalProjects;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Name of the client
    ContactEmail VARCHAR(100) NOT NULL,       -- Email address for client communication
    Phone VARCHAR(15),                        -- Phone number for client communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store architectural projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key linking to Clients table
    ProjectName VARCHAR(200) NOT NULL,        -- Name of the project
    Description TEXT NOT NULL,                 -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project, can be NULL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures integrity
);

-- Table to manage client needs
CREATE TABLE ClientNeeds (
    NeedID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each need
    ProjectID INT NOT NULL,                     -- Foreign key linking to Projects table
    NeedDescription TEXT NOT NULL,              -- Description of the client's needs
    Priority ENUM('Low', 'Medium', 'High') NOT NULL, -- Priority of the need
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures integrity
);

-- Table to store rational solutions proposed to clients
CREATE TABLE RationalSolutions (
    SolutionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each solution
    ProjectID INT NOT NULL,                      -- Foreign key linking to Projects table
    SolutionDescription TEXT NOT NULL,           -- Description of the proposed solution
    Benefits TEXT,                               -- Benefits of the proposed solution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures integrity
);

-- Index for faster querying of projects by client
CREATE INDEX idx_client_projects ON Projects(ClientID);

-- Index for faster querying of client needs by project
CREATE INDEX idx_project_needs ON ClientNeeds(ProjectID);

-- Index for faster querying of rational solutions by project
CREATE INDEX idx_project_solutions ON RationalSolutions(ProjectID);
```
