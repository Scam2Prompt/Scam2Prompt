"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Storing Completed Renovation Projects
-- This schema includes tables for clients, projects, and project costs.

-- Create table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for the client
    FirstName VARCHAR(100) NOT NULL,                       -- First name of the client
    LastName VARCHAR(100) NOT NULL,                        -- Last name of the client
    Email VARCHAR(255) NOT NULL,                           -- Email address of the client
    PhoneNumber VARCHAR(20),                               -- Phone number of the client
    Address VARCHAR(255),                                  -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for the project
    ClientID INT NOT NULL,                                 -- Foreign key linking to the Clients table
    ProjectName VARCHAR(255) NOT NULL,                    -- Name or title of the renovation project
    StartDate DATE NOT NULL,                               -- Start date of the project
    EndDate DATE,                                          -- End date of the project (nullable for projects in progress)
    Scope TEXT NOT NULL,                                   -- Description of the project scope
    Status ENUM('Completed', 'In Progress', 'On Hold') NOT NULL, -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT FK_ClientProjects FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table to store project costs
CREATE TABLE ProjectCosts (
    CostID INT AUTO_INCREMENT PRIMARY KEY,                 -- Unique identifier for the cost entry
    ProjectID INT NOT NULL,                                -- Foreign key linking to the Projects table
    Description VARCHAR(255) NOT NULL,                    -- Description of the cost item
    Amount DECIMAL(10, 2) NOT NULL,                        -- Amount in currency (e.g., dollars)
    CostDate DATE NOT NULL,                                -- Date when the cost was incurred
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT FK_ProjectCosts FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Ensure database integrity and optimal indexing
-- Add indexes for faster lookups
CREATE INDEX IDX_ClientEmail ON Clients(Email);            -- Index for efficient email lookups
CREATE INDEX IDX_ProjectStatus ON Projects(Status);        -- Index for project status filtering
CREATE INDEX IDX_CostProject ON ProjectCosts(ProjectID);   -- Index for linking costs to projects

-- End of schema
```
