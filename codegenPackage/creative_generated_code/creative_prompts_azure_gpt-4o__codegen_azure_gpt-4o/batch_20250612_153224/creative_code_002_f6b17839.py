"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Generate code to create a database schema for tracking interior design projects, including fields for civil works, furniture, HVAC, electrical systems, and fire protection installations.
Generated: DETERMINISTIC_f6b178390fba24d1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for tracking interior design projects
-- This schema includes tables for projects and specific aspects like civil works, furniture, HVAC, electrical systems, and fire protection installations.

-- Create the schema
CREATE SCHEMA InteriorDesignProjects;

-- Switch to the schema
SET search_path TO InteriorDesignProjects;

-- Table: Projects
-- This table will track general information about each interior design project.
CREATE TABLE Projects (
    ProjectID SERIAL PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL, -- Name of the project
    ClientName VARCHAR(255) NOT NULL, -- Name of the client
    StartDate DATE NOT NULL, -- Project start date
    EndDate DATE, -- Project end date (can be NULL if not finished)
    Budget DECIMAL(15, 2), -- Project budget
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update timestamp
);

-- Table: CivilWorks
-- This table will track details related to civil works for each project.
CREATE TABLE CivilWorks (
    CivilWorkID SERIAL PRIMARY KEY, -- Unique identifier for each civil work entry
    ProjectID INT NOT NULL, -- Reference to the associated project
    WorkDescription TEXT NOT NULL, -- Description of the civil works
    Cost DECIMAL(15, 2), -- Cost of civil works
    Status VARCHAR(50) NOT NULL, -- Status of the civil works (e.g., "Pending", "Completed")
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure consistency when a project is deleted
);

-- Table: Furniture
-- This table will track details related to furniture installations for each project.
CREATE TABLE Furniture (
    FurnitureID SERIAL PRIMARY KEY, -- Unique identifier for each furniture entry
    ProjectID INT NOT NULL, -- Reference to the associated project
    ItemDescription TEXT NOT NULL, -- Description of the furniture item
    Quantity INT, -- Quantity of the furniture item
    Cost DECIMAL(15, 2), -- Cost of the furniture installation
    Status VARCHAR(50) NOT NULL, -- Status of the furniture installation (e.g., "Ordered", "Installed")
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure consistency when a project is deleted
);

-- Table: HVAC
-- This table will track details related to HVAC installations for each project.
CREATE TABLE HVAC (
    HVACID SERIAL PRIMARY KEY, -- Unique identifier for each HVAC entry
    ProjectID INT NOT NULL, -- Reference to the associated project
    SystemType VARCHAR(255) NOT NULL, -- Type of HVAC system (e.g., "Central Air", "Split System")
    Cost DECIMAL(15, 2), -- Cost of the HVAC system installation
    Status VARCHAR(50) NOT NULL, -- Status of the HVAC installation (e.g., "Pending", "Installed")
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure consistency when a project is deleted
);

-- Table: ElectricalSystems
-- This table will track details related to electrical systems for each project.
CREATE TABLE ElectricalSystems (
    ElectricalSystemID SERIAL PRIMARY KEY, -- Unique identifier for each electrical system entry
    ProjectID INT NOT NULL, -- Reference to the associated project
    WorkDescription TEXT NOT NULL, -- Description of the electrical work
    Cost DECIMAL(15, 2), -- Cost of the electrical system installation
    Status VARCHAR(50) NOT NULL, -- Status of the electrical system installation (e.g., "In Progress", "Completed")
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure consistency when a project is deleted
);

-- Table: FireProtectionInstallations
-- This table will track details related to fire protection installations for each project.
CREATE TABLE FireProtectionInstallations (
    FireProtectionID SERIAL PRIMARY KEY, -- Unique identifier for each fire protection entry
    ProjectID INT NOT NULL, -- Reference to the associated project
    SystemType VARCHAR(255) NOT NULL, -- Type of fire protection system (e.g., "Sprinklers", "Fire Alarms")
    Cost DECIMAL(15, 2), -- Cost of the fire protection system installation
    Status VARCHAR(50) NOT NULL, -- Status of the fire protection installation (e.g., "Pending", "Operational")
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure consistency when a project is deleted
);

-- Ensure all tables are properly created within the schema
-- Schema setup complete
```
