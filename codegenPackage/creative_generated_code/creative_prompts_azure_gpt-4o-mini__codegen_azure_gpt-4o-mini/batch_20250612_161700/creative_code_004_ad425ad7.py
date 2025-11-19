"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoastalroofing.com
Prompt: Design a database schema for storing information about new roof installations and re-roofing projects for Coastal Roofing & Waterproofing.
Generated: DETERMINISTIC_ad425ad72dabf9fc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about new roof installations and re-roofing projects

CREATE DATABASE CoastalRoofing;

USE CoastalRoofing;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Unique email address for the customer
    Phone VARCHAR(15),                         -- Contact phone number
    Address VARCHAR(255),                       -- Customer's address
    City VARCHAR(100),                          -- City of residence
    State VARCHAR(50),                          -- State of residence
    ZipCode VARCHAR(10),                        -- Postal code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store information about roofing projects
CREATE TABLE RoofingProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    CustomerID INT NOT NULL,                     -- Foreign key to the Customers table
    ProjectType ENUM('New Installation', 'Re-Roofing') NOT NULL, -- Type of roofing project
    ProjectStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the project
    StartDate DATE NOT NULL,                     -- Start date of the project
    EndDate DATE,                                -- End date of the project
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store details of materials used in roofing projects
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,           -- Name of the material
    CostPerUnit DECIMAL(10, 2) NOT NULL,          -- Cost per unit of the material
    Unit VARCHAR(50) NOT NULL                       -- Unit of measurement (e.g., square feet, bundles)
);

-- Table to associate materials with roofing projects
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    ProjectID INT NOT NULL,                            -- Foreign key to the RoofingProjects table
    MaterialID INT NOT NULL,                           -- Foreign key to the Materials table
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of the material used
    FOREIGN KEY (ProjectID) REFERENCES RoofingProjects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,              -- Employee's first name
    LastName VARCHAR(50) NOT NULL,               -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Unique email address for the employee
    Phone VARCHAR(15),                           -- Contact phone number
    HireDate DATE NOT NULL,                      -- Date when the employee was hired
    Position VARCHAR(50) NOT NULL,               -- Job position of the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to log project assignments to employees
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the assignment
    ProjectID INT NOT NULL,                        -- Foreign key to the RoofingProjects table
    EmployeeID INT NOT NULL,                       -- Foreign key to the Employees table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was assigned
    FOREIGN KEY (ProjectID) REFERENCES RoofingProjects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensures referential integrity
);
```
