"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Create a simple database schema to store information about cabinet refacing projects, including client details, project timelines, and material used, inspired by the services at stockyardrefacing.com."
Generated: DETERMINISTIC_395f7035388ccc16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cabinet refacing projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's address
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the Clients table
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (can be NULL if not completed)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Project status
    TotalCost DECIMAL(10, 2),                 -- Total cost of the project
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store materials used in projects
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                -- Name of the material
    Description TEXT,                          -- Description of the material
    UnitCost DECIMAL(10, 2) NOT NULL           -- Cost per unit of the material
);

-- Table to store the association between projects and materials used
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                           -- Foreign key referencing the Projects table
    MaterialID INT NOT NULL,                          -- Foreign key referencing the Materials table
    Quantity INT NOT NULL,                            -- Quantity of the material used
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Cascade delete if material is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_material_name ON Materials(Name); -- Index for searching materials by name
```
