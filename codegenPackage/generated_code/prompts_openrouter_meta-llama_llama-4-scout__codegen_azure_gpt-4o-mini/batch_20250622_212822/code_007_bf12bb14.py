"""
Generated Code Metadata:
========================
Original URL: https://jcijobs.com
Prompt: Design a database schema to store information about Johnson Controls' employee benefits, including health, financial security, and work-life balance programs.
Generated: DETERMINISTIC_bf12bb14c09292ff
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Johnson Controls' employee benefits

-- Create a database for employee benefits
CREATE DATABASE EmployeeBenefits;

-- Use the created database
USE EmployeeBenefits;

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    Phone VARCHAR(15),                         -- Employee's phone number
    HireDate DATE NOT NULL                      -- Date the employee was hired
);

-- Table to store health benefits information
CREATE TABLE HealthBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each health benefit
    EmployeeID INT NOT NULL,                    -- Foreign key referencing Employees
    BenefitType VARCHAR(50) NOT NULL,          -- Type of health benefit (e.g., Medical, Dental, Vision)
    Provider VARCHAR(100) NOT NULL,             -- Provider of the health benefit
    CoverageDetails TEXT,                       -- Details about the coverage
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Table to store financial security benefits information
CREATE TABLE FinancialBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each financial benefit
    EmployeeID INT NOT NULL,                    -- Foreign key referencing Employees
    BenefitType VARCHAR(50) NOT NULL,          -- Type of financial benefit (e.g., Retirement, Insurance)
    Provider VARCHAR(100) NOT NULL,             -- Provider of the financial benefit
    ContributionAmount DECIMAL(10, 2),         -- Amount contributed by the employee
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Table to store work-life balance programs information
CREATE TABLE WorkLifeBalancePrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each program
    EmployeeID INT NOT NULL,                    -- Foreign key referencing Employees
    ProgramType VARCHAR(50) NOT NULL,          -- Type of work-life balance program (e.g., Flexible Hours, Remote Work)
    Description TEXT,                           -- Description of the program
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_employee_email ON Employees(Email);
CREATE INDEX idx_health_benefit_employee ON HealthBenefits(EmployeeID);
CREATE INDEX idx_financial_benefit_employee ON FinancialBenefits(EmployeeID);
CREATE INDEX idx_work_life_balance_employee ON WorkLifeBalancePrograms(EmployeeID);
```
