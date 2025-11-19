"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Design a database schema for managing construction projects, clients, and materials, reflecting the operational structure of ECOLUX, which includes residential and commercial projects.
Generated: DETERMINISTIC_73c04a6622ce8759
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Construction Projects, Clients, and Materials

-- Table for Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email of the client (must be unique)
    Phone VARCHAR(15),                       -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table for Projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,                      -- Project name
    Type ENUM('Residential', 'Commercial') NOT NULL, -- Type of project: Residential or Commercial
    StartDate DATE,                                  -- Start date of the project
    EndDate DATE,                                    -- Estimated end date of the project
    Budget DECIMAL(15, 2) NOT NULL,                  -- Project budget
    ClientID INT NOT NULL,                           -- Client associated with the project
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL DEFAULT 'Planned', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Foreign key linking to Clients
);

-- Table for Materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(255) NOT NULL,                -- Name of the material
    Type VARCHAR(255),                         -- Type/category of the material
    Unit VARCHAR(50) NOT NULL,                 -- Unit of measurement (e.g., kg, meters)
    PricePerUnit DECIMAL(10, 2) NOT NULL,      -- Price per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table for Project Materials (many-to-many relationship between Projects and Materials)
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each entry
    ProjectID INT NOT NULL,                           -- Project associated with the material
    MaterialID INT NOT NULL,                          -- Material associated with the project
    Quantity DECIMAL(15, 2) NOT NULL,                 -- Quantity of the material used for the project
    TotalCost DECIMAL(15, 2) GENERATED ALWAYS AS (Quantity * PricePerUnit) STORED, -- Auto-calculated total cost
    PricePerUnit DECIMAL(10, 2) NOT NULL,             -- Price per unit of the material (stored for reference)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Foreign key linking to Projects
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Foreign key linking to Materials
);

-- Indexes for better query performance
CREATE INDEX idx_ClientName ON Clients(Name);        -- Index for querying clients by name
CREATE INDEX idx_ProjectName ON Projects(Name);      -- Index for querying projects by name
CREATE INDEX idx_MaterialName ON Materials(Name);    -- Index for querying materials by name
CREATE INDEX idx_ProjectType ON Projects(Type);      -- Index for querying projects by type
```
