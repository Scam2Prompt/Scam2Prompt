"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Design a database schema for storing information about paving projects and customer reviews, based on the structure used by Bedford Paving Company.
Generated: DETERMINISTIC_cec7e318c75bc2fe
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about paving projects and customer reviews
-- This is designed to be clean, efficient, and scalable.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- First name of the customer
    LastName VARCHAR(50) NOT NULL,             -- Last name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Unique email address for the customer
    Phone VARCHAR(15),                         -- Contact number for the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Table to store paving project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key linking to the customer
    ProjectName VARCHAR(100) NOT NULL,         -- Name or title of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (null if ongoing)
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store customer reviews related to paving projects
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProjectID INT NOT NULL,                    -- Foreign key linking to the project
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1-5 scale)
    ReviewText TEXT,                           -- Textual review provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store employees assigned to projects
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- First name of the employee
    LastName VARCHAR(50) NOT NULL,             -- Last name of the employee
    JobTitle VARCHAR(100),                     -- Job title or role of the employee
    Phone VARCHAR(15),                         -- Contact number for the employee
    Email VARCHAR(255) UNIQUE,                 -- Unique email address for the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Table to link employees to projects
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key linking to the project
    EmployeeID INT NOT NULL,                     -- Foreign key linking to the employee
    Role VARCHAR(100),                           -- Role of the employee in the project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Indexes for faster data retrieval
CREATE INDEX idx_customer_email ON Customers (Email); -- Index for customer email
CREATE INDEX idx_project_status ON Projects (Status); -- Index for project status
CREATE INDEX idx_review_project ON Reviews (ProjectID); -- Index for reviews linked to projects
CREATE INDEX idx_employee_email ON Employees (Email); -- Index for employee email

-- End of schema
```
