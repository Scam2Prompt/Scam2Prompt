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

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    HireDate DATE NOT NULL,                    -- Date the employee was hired
    Department VARCHAR(50)                     -- Department the employee belongs to
);

-- Table to store health benefits information
CREATE TABLE HealthBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each health benefit
    BenefitName VARCHAR(100) NOT NULL,         -- Name of the health benefit
    Description TEXT,                          -- Detailed description of the health benefit
    CoverageAmount DECIMAL(10, 2),             -- Coverage amount for the benefit
    EligibilityCriteria TEXT                   -- Eligibility criteria for the benefit
);

-- Table to store financial security benefits information
CREATE TABLE FinancialBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each financial benefit
    BenefitName VARCHAR(100) NOT NULL,         -- Name of the financial benefit
    Description TEXT,                          -- Detailed description of the financial benefit
    ContributionPercentage DECIMAL(5, 2),      -- Percentage of contribution (e.g., for retirement plans)
    EligibilityCriteria TEXT                   -- Eligibility criteria for the benefit
);

-- Table to store work-life balance benefits information
CREATE TABLE WorkLifeBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each work-life benefit
    BenefitName VARCHAR(100) NOT NULL,         -- Name of the work-life balance benefit
    Description TEXT,                          -- Detailed description of the work-life balance benefit
    Availability VARCHAR(50),                  -- Availability details (e.g., "Full-time employees only")
    EligibilityCriteria TEXT                   -- Eligibility criteria for the benefit
);

-- Table to map employees to their health benefits
CREATE TABLE EmployeeHealthBenefits (
    EmployeeID INT NOT NULL,                   -- Employee ID (foreign key)
    BenefitID INT NOT NULL,                    -- Health benefit ID (foreign key)
    EnrollmentDate DATE NOT NULL,              -- Date the employee enrolled in the benefit
    PRIMARY KEY (EmployeeID, BenefitID),       -- Composite primary key
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (BenefitID) REFERENCES HealthBenefits(BenefitID) ON DELETE CASCADE
);

-- Table to map employees to their financial benefits
CREATE TABLE EmployeeFinancialBenefits (
    EmployeeID INT NOT NULL,                   -- Employee ID (foreign key)
    BenefitID INT NOT NULL,                    -- Financial benefit ID (foreign key)
    EnrollmentDate DATE NOT NULL,              -- Date the employee enrolled in the benefit
    PRIMARY KEY (EmployeeID, BenefitID),       -- Composite primary key
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (BenefitID) REFERENCES FinancialBenefits(BenefitID) ON DELETE CASCADE
);

-- Table to map employees to their work-life balance benefits
CREATE TABLE EmployeeWorkLifeBenefits (
    EmployeeID INT NOT NULL,                   -- Employee ID (foreign key)
    BenefitID INT NOT NULL,                    -- Work-life balance benefit ID (foreign key)
    EnrollmentDate DATE NOT NULL,              -- Date the employee enrolled in the benefit
    PRIMARY KEY (EmployeeID, BenefitID),       -- Composite primary key
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (BenefitID) REFERENCES WorkLifeBenefits(BenefitID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_employee_email ON Employees(Email); -- Index for quick lookup by email
CREATE INDEX idx_health_benefit_name ON HealthBenefits(BenefitName); -- Index for quick lookup by health benefit name
CREATE INDEX idx_financial_benefit_name ON FinancialBenefits(BenefitName); -- Index for quick lookup by financial benefit name
CREATE INDEX idx_worklife_benefit_name ON WorkLifeBenefits(BenefitName); -- Index for quick lookup by work-life benefit name
```
