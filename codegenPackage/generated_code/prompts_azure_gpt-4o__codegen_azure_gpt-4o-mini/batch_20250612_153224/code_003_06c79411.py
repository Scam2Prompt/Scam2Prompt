"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a database schema in SQL to manage client information, project details, and consulting costs for an architectural firm like TWM Associates.
Generated: DETERMINISTIC_06c794114f408b2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information, project details, and consulting costs
CREATE DATABASE TWM_Associates;

USE TWM_Associates;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactPerson VARCHAR(255),                -- Name of the contact person
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the client
    Phone VARCHAR(20),                         -- Phone number of the client
    Address VARCHAR(255),                      -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store consulting costs associated with projects
CREATE TABLE ConsultingCosts (
    CostID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each cost entry
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects
    CostDescription VARCHAR(255) NOT NULL,     -- Description of the cost
    CostAmount DECIMAL(10, 2) NOT NULL,        -- Amount of the cost
    CostDate DATE NOT NULL,                     -- Date when the cost was incurred
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_cost_description ON ConsultingCosts(CostDescription);
```
