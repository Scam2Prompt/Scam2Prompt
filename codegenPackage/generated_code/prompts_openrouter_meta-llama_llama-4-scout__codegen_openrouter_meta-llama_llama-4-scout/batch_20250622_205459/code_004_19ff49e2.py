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
-- Create a database for human capital management
CREATE DATABASE HumanCapitalManagement;

-- Use the database
USE HumanCapitalManagement;

-- Create a table for departments
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT,
    DepartmentName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (DepartmentID)
);

-- Create a table for job titles
CREATE TABLE JobTitles (
    JobTitleID INT AUTO_INCREMENT,
    JobTitle VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (JobTitleID)
);

-- Create a table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateOfBirth DATE NOT NULL,
    HireDate DATE NOT NULL,
    DepartmentID INT,
    JobTitleID INT,
    ManagerID INT,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (JobTitleID) REFERENCES JobTitles(JobTitleID),
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);

-- Create a table for performance metrics
CREATE TABLE PerformanceMetrics (
    PerformanceMetricID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    MetricName VARCHAR(255) NOT NULL,
    MetricValue DECIMAL(10, 2) NOT NULL,
    EvaluationDate DATE NOT NULL,
    PRIMARY KEY (PerformanceMetricID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create a table for training programs
CREATE TABLE TrainingPrograms (
    TrainingProgramID INT AUTO_INCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (TrainingProgramID)
);

-- Create a table for employee training records
CREATE TABLE EmployeeTrainingRecords (
    EmployeeTrainingRecordID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    TrainingProgramID INT NOT NULL,
    TrainingDate DATE NOT NULL,
    CompletionStatus BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (EmployeeTrainingRecordID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (TrainingProgramID) REFERENCES TrainingPrograms(TrainingProgramID)
);

-- Create a table for performance reviews
CREATE TABLE PerformanceReviews (
    PerformanceReviewID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    ReviewDate DATE NOT NULL,
    OverallPerformanceRating DECIMAL(3, 2) NOT NULL,
    ReviewComments TEXT,
    PRIMARY KEY (PerformanceReviewID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create a table for employee skills
CREATE TABLE EmployeeSkills (
    EmployeeSkillID INT AUTO_INCREMENT,
    EmployeeID INT NOT NULL,
    SkillName VARCHAR(255) NOT NULL,
    ProficiencyLevel VARCHAR(255) NOT NULL,
    PRIMARY KEY (EmployeeSkillID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_DepartmentID ON Employees (DepartmentID);
CREATE INDEX idx_JobTitleID ON Employees (JobTitleID);
CREATE INDEX idx_ManagerID ON Employees (ManagerID);
CREATE INDEX idx_EmployeeID ON PerformanceMetrics (EmployeeID);
CREATE INDEX idx_EmployeeID ON EmployeeTrainingRecords (EmployeeID);
CREATE INDEX idx_TrainingProgramID ON EmployeeTrainingRecords (TrainingProgramID);
CREATE INDEX idx_EmployeeID ON PerformanceReviews (EmployeeID);
CREATE INDEX idx_EmployeeID ON EmployeeSkills (EmployeeID);
```

```sql
-- Example data insertion
INSERT INTO Departments (DepartmentName, Description)
VALUES 
('HR', 'Human Resources Department'),
('IT', 'Information Technology Department'),
('Marketing', 'Marketing Department');

INSERT INTO JobTitles (JobTitle, Description)
VALUES 
('Software Engineer', 'Develops software applications'),
('Marketing Manager', 'Manages marketing campaigns'),
('HR Generalist', 'Provides HR support');

INSERT INTO Employees (FirstName, LastName, Email, DateOfBirth, HireDate, DepartmentID, JobTitleID, ManagerID)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1990-01-01', '2020-01-01', 1, 1, NULL),
('Jane', 'Doe', 'jane.doe@example.com', '1995-01-01', '2022-01-01', 2, 2, 1),
('Bob', 'Smith', 'bob.smith@example.com', '1980-01-01', '2018-01-01', 3, 3, 1);

INSERT INTO PerformanceMetrics (EmployeeID, MetricName, MetricValue, EvaluationDate)
VALUES 
(1, 'Code Quality', 90.00, '2022-01-01'),
(2, 'Marketing Campaign Success', 85.00, '2022-06-01'),
(3, 'Employee Satisfaction', 95.00, '2022-12-01');

INSERT INTO TrainingPrograms (ProgramName, Description)
VALUES 
('Software Development', 'Develops software development skills'),
('Marketing Strategy', 'Develops marketing strategy skills'),
('HR Best Practices', 'Develops HR best practices skills');

INSERT INTO EmployeeTrainingRecords (EmployeeID, TrainingProgramID, TrainingDate, CompletionStatus)
VALUES 
(1, 1, '2022-01-15', TRUE),
(2, 2, '2022-07-01', FALSE),
(3, 3, '2022-12-15', TRUE);

INSERT INTO PerformanceReviews (EmployeeID, ReviewDate, OverallPerformanceRating, ReviewComments)
VALUES 
(1, '2022-06-01', 4.50, 'Excellent performance'),
(2, '2022-12-01', 4.00, 'Good performance'),
(3, '2023-01-01', 4.75, 'Outstanding performance');

INSERT INTO EmployeeSkills (EmployeeID, SkillName, ProficiencyLevel)
VALUES 
(1, 'Java', 'Advanced'),
(2, 'Marketing Automation', 'Intermediate'),
(3, 'HR Compliance', 'Expert');
```
