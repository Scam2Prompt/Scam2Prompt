"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate code to create a database schema for tracking interior design projects, including fields for civil works, furniture, HVAC, electrical systems, and fire protection installations.
Generated: DETERMINISTIC_f6b178390fba24d1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for tracking interior design projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FireProtectionInstallations;
DROP TABLE IF EXISTS ElectricalSystems;
DROP TABLE IF EXISTS HVACSystems;
DROP TABLE IF EXISTS Furniture;
DROP TABLE IF EXISTS CivilWorks;
DROP TABLE IF EXISTS DesignProjects;

-- Create a table for design projects
CREATE TABLE DesignProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    ClientName VARCHAR(255) NOT NULL,          -- Name of the client
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Status ENUM('Planning', 'In Progress', 'Completed', 'On Hold') NOT NULL  -- Current status of the project
);

-- Create a table for civil works associated with design projects
CREATE TABLE CivilWorks (
    CivilWorkID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each civil work
    ProjectID INT NOT NULL,                      -- Foreign key referencing DesignProjects
    Description TEXT NOT NULL,                   -- Description of the civil work
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the civil work
    FOREIGN KEY (ProjectID) REFERENCES DesignProjects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for furniture associated with design projects
CREATE TABLE Furniture (
    FurnitureID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each furniture item
    ProjectID INT NOT NULL,                      -- Foreign key referencing DesignProjects
    ItemName VARCHAR(255) NOT NULL,             -- Name of the furniture item
    Quantity INT NOT NULL,                       -- Quantity of the furniture item
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the furniture item
    FOREIGN KEY (ProjectID) REFERENCES DesignProjects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for HVAC systems associated with design projects
CREATE TABLE HVACSystems (
    HVACSystemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each HVAC system
    ProjectID INT NOT NULL,                       -- Foreign key referencing DesignProjects
    SystemType VARCHAR(255) NOT NULL,            -- Type of HVAC system
    InstallationDate DATE NOT NULL,               -- Date of installation
    Cost DECIMAL(10, 2) NOT NULL,                 -- Cost of the HVAC system
    FOREIGN KEY (ProjectID) REFERENCES DesignProjects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for electrical systems associated with design projects
CREATE TABLE ElectricalSystems (
    ElectricalSystemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each electrical system
    ProjectID INT NOT NULL,                             -- Foreign key referencing DesignProjects
    SystemDescription TEXT NOT NULL,                    -- Description of the electrical system
    InstallationDate DATE NOT NULL,                     -- Date of installation
    Cost DECIMAL(10, 2) NOT NULL,                       -- Cost of the electrical system
    FOREIGN KEY (ProjectID) REFERENCES DesignProjects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for fire protection installations associated with design projects
CREATE TABLE FireProtectionInstallations (
    FireProtectionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each fire protection installation
    ProjectID INT NOT NULL,                           -- Foreign key referencing DesignProjects
    InstallationType VARCHAR(255) NOT NULL,          -- Type of fire protection installation
    InstallationDate DATE NOT NULL,                   -- Date of installation
    Cost DECIMAL(10, 2) NOT NULL,                     -- Cost of the fire protection installation
    FOREIGN KEY (ProjectID) REFERENCES DesignProjects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Commit the transaction to save changes
COMMIT;
```
