"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Design a database schema to manage human capital, including employee data, performance metrics, and training records, using a relational database management system.
Generated: DETERMINISTIC_19ff49e2b4a66081
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Human Capital Management

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    HireDate DATE NOT NULL,                    -- Date the employee was hired
    JobTitle VARCHAR(50) NOT NULL,             -- Employee's job title
    Department VARCHAR(50),                    -- Department the employee belongs to
    ManagerID INT,                             -- ID of the employee's manager (foreign key)
    Salary DECIMAL(10, 2) NOT NULL,            -- Employee's salary
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active', -- Employment status
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID) -- Self-referencing foreign key
);

-- Table to store performance metrics
CREATE TABLE PerformanceMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each performance metric
    EmployeeID INT NOT NULL,                   -- ID of the employee being evaluated (foreign key)
    EvaluationDate DATE NOT NULL,              -- Date of the performance evaluation
    MetricName VARCHAR(50) NOT NULL,           -- Name of the performance metric
    MetricValue DECIMAL(5, 2) NOT NULL,        -- Value of the performance metric
    Comments TEXT,                             -- Additional comments about the evaluation
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) -- Foreign key linking to Employees table
);

-- Table to store training records
CREATE TABLE TrainingRecords (
    TrainingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each training record
    EmployeeID INT NOT NULL,                   -- ID of the employee who attended the training (foreign key)
    TrainingName VARCHAR(100) NOT NULL,        -- Name of the training program
    TrainingDate DATE NOT NULL,                -- Date the training occurred
    CompletionStatus ENUM('Completed', 'In Progress', 'Not Started') NOT NULL, -- Status of the training
    CertificationReceived BOOLEAN NOT NULL DEFAULT FALSE, -- Whether a certification was received
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) -- Foreign key linking to Employees table
);

-- Table to store departments
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each department
    DepartmentName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the department
    ManagerID INT,                               -- ID of the department manager (foreign key)
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID) -- Foreign key linking to Employees table
);

-- Table to store job titles
CREATE TABLE JobTitles (
    JobTitleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each job title
    JobTitleName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the job title
    Description TEXT                           -- Description of the job title
);

-- Indexes for optimization
CREATE INDEX idx_employee_department ON Employees(Department);
CREATE INDEX idx_performance_employee ON PerformanceMetrics(EmployeeID);
CREATE INDEX idx_training_employee ON TrainingRecords(EmployeeID);

-- Error handling and constraints
-- Ensure that salary is a positive value
ALTER TABLE Employees
ADD CONSTRAINT chk_salary_positive CHECK (Salary > 0);

-- Ensure that metric values are within a valid range (e.g., 0 to 100)
ALTER TABLE PerformanceMetrics
ADD CONSTRAINT chk_metric_value_range CHECK (MetricValue >= 0 AND MetricValue <= 100);
```
