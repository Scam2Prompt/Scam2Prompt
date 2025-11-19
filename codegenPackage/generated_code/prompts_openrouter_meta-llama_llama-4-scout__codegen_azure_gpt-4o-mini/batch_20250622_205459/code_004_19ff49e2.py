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
-- Database schema for managing human capital

-- Create a table to store employee data
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,           -- Employee's first name
    LastName VARCHAR(50) NOT NULL,            -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Employee's email address
    Phone VARCHAR(15),                        -- Employee's phone number
    HireDate DATE NOT NULL,                   -- Date the employee was hired
    JobTitle VARCHAR(50) NOT NULL,            -- Job title of the employee
    DepartmentID INT,                         -- Foreign key to Departments table
    Salary DECIMAL(10, 2) NOT NULL,           -- Employee's salary
    CONSTRAINT FK_Department FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create a table to store department data
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each department
    DepartmentName VARCHAR(100) NOT NULL UNIQUE  -- Name of the department
);

-- Create a table to store performance metrics
CREATE TABLE PerformanceMetrics (
    MetricID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each performance metric
    EmployeeID INT NOT NULL,                      -- Foreign key to Employees table
    ReviewDate DATE NOT NULL,                     -- Date of the performance review
    Score INT CHECK (Score BETWEEN 1 AND 5),     -- Performance score (1 to 5)
    Comments TEXT,                                -- Additional comments on performance
    CONSTRAINT FK_Employee FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create a table to store training records
CREATE TABLE TrainingRecords (
    TrainingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each training record
    EmployeeID INT NOT NULL,                      -- Foreign key to Employees table
    TrainingDate DATE NOT NULL,                   -- Date of the training
    TrainingProgram VARCHAR(100) NOT NULL,       -- Name of the training program
    CompletionStatus ENUM('Completed', 'In Progress', 'Not Completed') NOT NULL, -- Status of training
    CONSTRAINT FK_TrainingEmployee FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create a table to store employee skills
CREATE TABLE EmployeeSkills (
    SkillID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each skill
    EmployeeID INT NOT NULL,                      -- Foreign key to Employees table
    SkillName VARCHAR(100) NOT NULL,             -- Name of the skill
    ProficiencyLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Proficiency level
    CONSTRAINT FK_SkillEmployee FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create indexes for performance optimization
CREATE INDEX idx_employee_email ON Employees(Email);
CREATE INDEX idx_department_name ON Departments(DepartmentName);
CREATE INDEX idx_performance_employee ON PerformanceMetrics(EmployeeID);
CREATE INDEX idx_training_employee ON TrainingRecords(EmployeeID);
CREATE INDEX idx_skill_employee ON EmployeeSkills(EmployeeID);
```
