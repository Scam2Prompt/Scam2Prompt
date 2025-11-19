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
-- Database schema for storing employee information and benefits data

-- Create a table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    HireDate DATE NOT NULL,                    -- Date the employee was hired
    JobTitle VARCHAR(50),                      -- Employee's job title
    Department VARCHAR(50),                    -- Department the employee belongs to
    Salary DECIMAL(10, 2) NOT NULL,            -- Employee's salary
    IsActive BOOLEAN DEFAULT TRUE              -- Indicates if the employee is currently active
);

-- Create a table to store benefits information
CREATE TABLE Benefits (
    BenefitID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each benefit
    BenefitName VARCHAR(100) NOT NULL,         -- Name of the benefit (e.g., Health Insurance)
    Description TEXT,                          -- Detailed description of the benefit
    IsMandatory BOOLEAN DEFAULT FALSE          -- Indicates if the benefit is mandatory
);

-- Create a junction table to associate employees with their benefits
CREATE TABLE EmployeeBenefits (
    EmployeeBenefitID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    EmployeeID INT NOT NULL,                          -- Foreign key referencing Employees table
    BenefitID INT NOT NULL,                           -- Foreign key referencing Benefits table
    EnrollmentDate DATE NOT NULL,                     -- Date the employee enrolled in the benefit
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (BenefitID) REFERENCES Benefits(BenefitID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_employee_email ON Employees (Email); -- Index for quick lookup by email
CREATE INDEX idx_benefit_name ON Benefits (BenefitName); -- Index for quick lookup by benefit name
CREATE INDEX idx_employee_benefit ON EmployeeBenefits (EmployeeID, BenefitID); -- Composite index for associations
```
