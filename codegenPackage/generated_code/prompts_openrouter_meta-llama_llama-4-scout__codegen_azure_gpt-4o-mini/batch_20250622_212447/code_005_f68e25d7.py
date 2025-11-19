"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Design a simple database schema to store employee information and benefits data for a company like Vertiv GmbH.
Generated: DETERMINISTIC_f68e25d7d934ce20
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing employee information and benefits data

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS EmployeeBenefits;
DROP TABLE IF EXISTS Employees;

-- Create a table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,              -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Employee's email address (must be unique)
    PhoneNumber VARCHAR(15),                     -- Employee's phone number (optional)
    HireDate DATE NOT NULL,                      -- Date when the employee was hired
    JobTitle VARCHAR(50) NOT NULL,              -- Job title of the employee
    Department VARCHAR(50) NOT NULL,            -- Department where the employee works
    Salary DECIMAL(10, 2) NOT NULL               -- Employee's salary
);

-- Create a table to store benefits information associated with employees
CREATE TABLE EmployeeBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each benefit
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees table
    BenefitType VARCHAR(50) NOT NULL,           -- Type of benefit (e.g., Health, Retirement)
    BenefitDescription TEXT,                     -- Description of the benefit
    StartDate DATE NOT NULL,                     -- Start date of the benefit
    EndDate DATE,                                -- End date of the benefit (optional)
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (uncomment to use)
-- INSERT INTO Employees (FirstName, LastName, Email, PhoneNumber, HireDate, JobTitle, Department, Salary)
-- VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2023-01-15', 'Software Engineer', 'IT', 75000.00);

-- INSERT INTO EmployeeBenefits (EmployeeID, BenefitType, BenefitDescription, StartDate, EndDate)
-- VALUES (1, 'Health', 'Comprehensive health insurance', '2023-01-15', NULL);
```
