"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Create a SQL database schema for storing information about industrial construction projects, including client details, project timelines, and material usage, similar to what Tether SARL might use."
Generated: DETERMINISTIC_5d94ca79189a3ec6
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Industrial Construction Projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS MaterialUsage;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactPerson VARCHAR(255),                -- Name of the contact person
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    Email VARCHAR(255),                        -- Contact email address
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE NOT NULL,                     -- Project end date
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store material usage details for each project
CREATE TABLE MaterialUsage (
    UsageID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each material usage record
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects
    MaterialName VARCHAR(255) NOT NULL,       -- Name of the material
    Quantity DECIMAL(10, 2) NOT NULL,         -- Quantity of the material used
    Unit VARCHAR(50) NOT NULL,                 -- Unit of measurement (e.g., kg, m3)
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the material used
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_material_name ON MaterialUsage(MaterialName);
```
