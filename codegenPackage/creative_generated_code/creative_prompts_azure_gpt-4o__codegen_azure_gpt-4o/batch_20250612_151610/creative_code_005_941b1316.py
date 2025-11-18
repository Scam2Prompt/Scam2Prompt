"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Create a database schema for tracking the fabrication of custom industrial structures, based on the services offered by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_941b1316b23927da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tracking the Fabrication of Custom Industrial Structures
-- Services offered by Multiservicios Industriales 3L

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                       -- Name of the customer
    Email VARCHAR(100),                               -- Email address of the customer
    PhoneNumber VARCHAR(15),                          -- Contact phone number of the customer
    Address TEXT,                                     -- Physical address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about fabrication projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each project
    CustomerID INT NOT NULL,                          -- Foreign key linking to Customers table
    Name VARCHAR(100) NOT NULL,                       -- Name of the project
    Description TEXT,                                 -- Detailed description of the project
    StartDate DATE NOT NULL,                          -- Project start date
    EndDate DATE,                                     -- Project end date (nullable if ongoing)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete for customer removal
);

-- Table to store information about materials required for each project
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                       -- Name of the material
    Unit VARCHAR(50) NOT NULL,                        -- Unit of measurement (e.g., kg, meters)
    CostPerUnit DECIMAL(10, 2) NOT NULL,              -- Cost per unit of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track materials used in fabrication projects
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project-material relationship
    ProjectID INT NOT NULL,                           -- Foreign key linking to Projects table
    MaterialID INT NOT NULL,                          -- Foreign key linking to Materials table
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of material used
    TotalCost AS (Quantity * (SELECT CostPerUnit FROM Materials WHERE MaterialID = ProjectMaterials.MaterialID)), -- Calculated column for total cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete for project removal
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE RESTRICT -- Restrict deletion of materials
);

-- Table to store information about employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each employee
    Name VARCHAR(100) NOT NULL,                       -- Name of the employee
    Role VARCHAR(50),                                 -- Role or position of the employee
    PhoneNumber VARCHAR(15),                          -- Contact phone number of the employee
    Email VARCHAR(100),                               -- Email address of the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track employees assigned to fabrication projects
CREATE TABLE ProjectEmployees (
    ProjectEmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project-employee relationship
    ProjectID INT NOT NULL,                           -- Foreign key linking to Projects table
    EmployeeID INT NOT NULL,                          -- Foreign key linking to Employees table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the employee was assigned
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete for project removal
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE RESTRICT -- Restrict deletion of employees
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,                       -- Name of the service
    Description TEXT,                                 -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,                     -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track services provided for fabrication projects
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project-service relationship
    ProjectID INT NOT NULL,                           -- Foreign key linking to Projects table
    ServiceID INT NOT NULL,                           -- Foreign key linking to Services table
    Quantity INT NOT NULL,                            -- Quantity of service provided
    TotalCost AS (Quantity * (SELECT Cost FROM Services WHERE ServiceID = ProjectServices.ServiceID)), -- Calculated column for total cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete for project removal
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE RESTRICT -- Restrict deletion of services
);

-- End of schema definition
```
