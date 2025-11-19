"""
Generated Code Metadata:
========================
Original URL: https://reyesaluminio.com
Prompt: "Design a database schema to store information about aluminum carpentry projects, including client details, project types, and materials used."
Generated: DETERMINISTIC_4d477323df56b5a2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for aluminum carpentry projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's address
);

-- Table to store project types
CREATE TABLE ProjectTypes (
    ProjectTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project type
    TypeName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the project type (e.g., "Window Installation", "Door Fabrication")
    Description TEXT                              -- Description of the project type
);

-- Table to store materials used in projects
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL UNIQUE, -- Name of the material (e.g., "Aluminum Frame", "Glass Panel")
    Unit VARCHAR(50) NOT NULL,                 -- Unit of measurement (e.g., "meters", "pieces")
    CostPerUnit DECIMAL(10, 2) NOT NULL        -- Cost per unit of the material
);

-- Table to store aluminum carpentry projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectTypeID INT NOT NULL,               -- Foreign key referencing ProjectTypes table
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    TotalCost DECIMAL(10, 2),                 -- Total cost of the project
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Project status
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE SET NULL -- Set project type to NULL if removed
);

-- Table to store materials used in each project
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects table
    MaterialID INT NOT NULL,                          -- Foreign key referencing Materials table
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of the material used
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE SET NULL -- Set material to NULL if removed
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for faster lookups
CREATE INDEX idx_project_status ON Projects(Status); -- Index on project status for filtering
CREATE INDEX idx_material_name ON Materials(MaterialName); -- Index on material name for faster lookups
```
