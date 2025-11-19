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
-- Database Schema for Coastal Roofing & Waterproofing
-- This schema stores information related to new roof installations and re-roofing projects.

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer first name
    LastName VARCHAR(50) NOT NULL,              -- Customer last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer email
    PhoneNumber VARCHAR(15),                    -- Customer contact number
    AddressLine1 VARCHAR(100) NOT NULL,         -- Customer address line 1
    AddressLine2 VARCHAR(100),                  -- Customer address line 2 (optional)
    City VARCHAR(50) NOT NULL,                  -- City of the customer
    State VARCHAR(50) NOT NULL,                 -- State of the customer
    ZipCode VARCHAR(10) NOT NULL,               -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create table for roof types
CREATE TABLE RoofTypes (
    RoofTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each roof type
    Name VARCHAR(50) NOT NULL,                  -- Name of the roof type (e.g., Metal, Shingle, Tile)
    Description TEXT,                           -- Optional description of the roof type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    RoofTypeID INT NOT NULL,                    -- Foreign key referencing RoofTypes table
    ProjectType ENUM('New Installation', 'Re-Roofing') NOT NULL, -- Type of project
    StartDate DATE NOT NULL,                    -- Project start date
    EndDate DATE,                               -- Project end date (optional)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Current status of the project
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the project
    Notes TEXT,                                 -- Optional notes about the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Delete projects if customer is deleted
    FOREIGN KEY (RoofTypeID) REFERENCES RoofTypes(RoofTypeID) ON DELETE SET NULL -- Set roof type to NULL if deleted
);

-- Create table for employees (optional)
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee first name
    LastName VARCHAR(50) NOT NULL,              -- Employee last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Employee email
    PhoneNumber VARCHAR(15),                    -- Employee contact number
    JobTitle VARCHAR(50) NOT NULL,              -- Job title (e.g., Installer, Foreman, Supervisor)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create table for project assignments
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects table
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees table
    AssignedDate DATE NOT NULL,                  -- Date the employee was assigned to the project
    Role ENUM('Installer', 'Foreman', 'Supervisor') NOT NULL, -- Role of the employee in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Delete assignment if project is deleted
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Delete assignment if employee is deleted
);

-- Indexes for optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for faster customer email lookups
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_employee_email ON Employees(Email); -- Index for faster employee email lookups
```
