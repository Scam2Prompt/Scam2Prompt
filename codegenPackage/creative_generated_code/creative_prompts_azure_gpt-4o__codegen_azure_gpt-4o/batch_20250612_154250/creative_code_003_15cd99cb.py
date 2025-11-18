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

-- Create the table for storing clients' information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL,             -- Email address of the client
    Phone VARCHAR(20),                       -- Phone number of the client
    Address TEXT,                            -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create the table for storing architectural projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Description of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project
    Budget DECIMAL(15, 2),                    -- Budget for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Create the table for storing client needs
CREATE TABLE ClientNeeds (
    NeedID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each need
    ProjectID INT NOT NULL,                  -- Foreign key referencing Projects table
    NeedDescription TEXT NOT NULL,           -- Detailed description of the client's need
    Priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium', -- Priority level for the need
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Create the table for storing rational solutions
CREATE TABLE RationalSolutions (
    SolutionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each solution
    NeedID INT NOT NULL,                       -- Foreign key referencing ClientNeeds table
    SolutionDescription TEXT NOT NULL,         -- Detailed description of the solution
    Feasibility ENUM('Low', 'Medium', 'High') DEFAULT 'Medium', -- Feasibility assessment of the solution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (NeedID) REFERENCES ClientNeeds(NeedID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Indexes for faster search
CREATE INDEX idx_ClientEmail ON Clients(Email); -- Index on Email for quick lookup
CREATE INDEX idx_ProjectName ON Projects(ProjectName); -- Index on ProjectName for quick lookup
CREATE INDEX idx_ClientNeedsPriority ON ClientNeeds(Priority); -- Index on Priority for filtering needs
CREATE INDEX idx_RationalSolutionsFeasibility ON RationalSolutions(Feasibility); -- Index on Feasibility for filtering solutions
```
