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
-- SQL Schema for Industrial Construction Projects Database

-- Create a database for industrial construction projects
CREATE DATABASE IndustrialConstructionProjects;

-- Switch to the newly created database
USE IndustrialConstructionProjects;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL,      -- Email address of the client
    ContactPhone VARCHAR(20),                -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Project status
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store material usage details
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(255) NOT NULL,                -- Name of the material
    Unit VARCHAR(50) NOT NULL,                 -- Unit of measurement (e.g., kg, liters, etc.)
    CostPerUnit DECIMAL(10, 2) NOT NULL,       -- Cost per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store material usage in projects
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects table
    MaterialID INT NOT NULL,                          -- Foreign key referencing Materials table
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of material used
    TotalCost DECIMAL(15, 2) GENERATED ALWAYS AS (Quantity * (SELECT CostPerUnit FROM Materials WHERE Materials.MaterialID = ProjectMaterials.MaterialID)) STORED, -- Automatically calculated total cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Cascade delete if material is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_project_name ON Projects(Name);
CREATE INDEX idx_material_name ON Materials(Name);

-- Error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';
```
