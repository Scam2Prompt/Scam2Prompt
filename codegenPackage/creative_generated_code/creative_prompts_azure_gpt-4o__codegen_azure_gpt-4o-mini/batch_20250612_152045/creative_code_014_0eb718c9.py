"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Design a database schema in SQL to store employee data retrieved from the Socrates GM portal, including timesheets, payroll status, and leave requests.
Generated: DETERMINISTIC_0eb718c910eab7a7
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for the Socrates GM portal employee data
CREATE DATABASE SocratesGM;

USE SocratesGM;

-- Table to store employee details
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,              -- Employee's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Employee's email address
    PhoneNumber VARCHAR(15),                     -- Employee's phone number
    HireDate DATE NOT NULL,                      -- Date of hire
    Position VARCHAR(50) NOT NULL,               -- Job position
    Department VARCHAR(50) NOT NULL,             -- Department where the employee works
    Status ENUM('Active', 'Inactive', 'On Leave') NOT NULL  -- Employment status
);

-- Table to store timesheet entries
CREATE TABLE Timesheets (
    TimesheetID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each timesheet entry
    EmployeeID INT NOT NULL,                      -- Foreign key referencing Employees table
    WorkDate DATE NOT NULL,                       -- Date of work
    HoursWorked DECIMAL(5,2) NOT NULL,           -- Total hours worked on the specified date
    Description TEXT,                             -- Description of work done
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE  -- Ensure integrity
);

-- Table to store payroll status
CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each payroll record
    EmployeeID INT NOT NULL,                      -- Foreign key referencing Employees table
    PayPeriodStart DATE NOT NULL,                 -- Start date of the pay period
    PayPeriodEnd DATE NOT NULL,                   -- End date of the pay period
    GrossPay DECIMAL(10,2) NOT NULL,             -- Total gross pay for the period
    NetPay DECIMAL(10,2) NOT NULL,               -- Total net pay after deductions
    Status ENUM('Paid', 'Pending', 'Failed') NOT NULL, -- Payment status
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE  -- Ensure integrity
);

-- Table to store leave requests
CREATE TABLE LeaveRequests (
    LeaveRequestID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each leave request
    EmployeeID INT NOT NULL,                        -- Foreign key referencing Employees table
    LeaveType ENUM('Sick', 'Vacation', 'Personal', 'Maternity', 'Paternity') NOT NULL,  -- Type of leave
    StartDate DATE NOT NULL,                        -- Start date of leave
    EndDate DATE NOT NULL,                          -- End date of leave
    RequestDate DATE NOT NULL,                      -- Date when the leave was requested
    Status ENUM('Approved', 'Denied', 'Pending') NOT NULL, -- Status of the leave request
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE  -- Ensure integrity
);

-- Indexes to improve query performance
CREATE INDEX idx_employee_email ON Employees(Email);
CREATE INDEX idx_timesheet_employee ON Timesheets(EmployeeID);
CREATE INDEX idx_payroll_employee ON Payroll(EmployeeID);
CREATE INDEX idx_leave_employee ON LeaveRequests(EmployeeID);
```
