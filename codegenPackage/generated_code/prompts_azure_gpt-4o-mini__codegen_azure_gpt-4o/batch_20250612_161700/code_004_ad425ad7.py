"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Design a database schema for storing information about new roof installations and re-roofing projects for Coastal Roofing & Waterproofing.
Generated: DETERMINISTIC_ad425ad72dabf9fc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about new roof installations and re-roofing projects
-- for Coastal Roofing & Waterproofing.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    AddressLine1 VARCHAR(255) NOT NULL,        -- Customer's primary address line
    AddressLine2 VARCHAR(255),                 -- Additional address information (optional)
    City VARCHAR(100) NOT NULL,                -- City of the customer
    State VARCHAR(50) NOT NULL,                -- State of the customer
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key referencing the customer
    ProjectType ENUM('New Installation', 'Re-Roofing') NOT NULL, -- Type of project
    RoofType VARCHAR(50) NOT NULL,             -- Type of roof (e.g., asphalt, metal, tile)
    SquareFootage DECIMAL(10, 2) NOT NULL,     -- Size of the roof in square feet
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (nullable for ongoing projects)
    TotalCost DECIMAL(12, 2) NOT NULL,         -- Total cost of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Project status
    Notes TEXT,                                -- Additional notes about the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    Role ENUM('Roofer', 'Supervisor', 'Manager', 'Admin') NOT NULL, -- Employee role
    HireDate DATE NOT NULL,                    -- Date the employee was hired
    IsActive BOOLEAN DEFAULT TRUE,             -- Whether the employee is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the employee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to assign employees to projects
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key referencing the project
    EmployeeID INT NOT NULL,                     -- Foreign key referencing the employee
    RoleInProject ENUM('Roofer', 'Supervisor') NOT NULL, -- Role of the employee in the project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Cascade delete if employee is removed
);

-- Table to store material information
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                 -- Name of the material
    Description TEXT,                           -- Description of the material
    UnitCost DECIMAL(10, 2) NOT NULL,           -- Cost per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to track materials used in projects
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                           -- Foreign key referencing the project
    MaterialID INT NOT NULL,                          -- Foreign key referencing the material
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of the material used
    TotalCost AS (Quantity * (SELECT UnitCost FROM Materials WHERE Materials.MaterialID = ProjectMaterials.MaterialID)) STORED, -- Calculated total cost
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Cascade delete if material is removed
);
```
