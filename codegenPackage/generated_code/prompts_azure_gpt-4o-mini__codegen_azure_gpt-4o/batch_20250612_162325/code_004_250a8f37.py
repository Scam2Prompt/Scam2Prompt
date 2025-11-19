"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Client Projects in a Cosmetic Manufacturing Business

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services offered for each project
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store raw materials used in projects
CREATE TABLE RawMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(255) NOT NULL,                -- Name of the raw material
    Description TEXT,                          -- Detailed description of the material
    Unit VARCHAR(50) NOT NULL,                 -- Unit of measurement (e.g., kg, liters)
    CostPerUnit DECIMAL(10, 2) NOT NULL,       -- Cost per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track raw materials used in specific projects
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                           -- Foreign key referencing the project
    MaterialID INT NOT NULL,                          -- Foreign key referencing the raw material
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of the material used
    TotalCost DECIMAL(10, 2) GENERATED ALWAYS AS (Quantity * (SELECT CostPerUnit FROM RawMaterials WHERE RawMaterials.MaterialID = MaterialID)) STORED, -- Calculated total cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (MaterialID) REFERENCES RawMaterials(MaterialID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store employees assigned to projects
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    Name VARCHAR(255) NOT NULL,                -- Name of the employee
    Role VARCHAR(255) NOT NULL,                -- Role of the employee (e.g., chemist, designer)
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the employee
    PhoneNumber VARCHAR(20),                   -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track employee assignments to projects
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key referencing the project
    EmployeeID INT NOT NULL,                     -- Foreign key referencing the employee
    Role VARCHAR(255) NOT NULL,                  -- Role of the employee in the project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Assignment timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensure referential integrity
);
```
