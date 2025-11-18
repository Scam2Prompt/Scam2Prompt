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
-- Database schema for employee data storage

-- Table to store general employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    DateOfHire DATE NOT NULL,                  -- Date the employee was hired
    JobTitle VARCHAR(50) NOT NULL,             -- Employee's job title
    Department VARCHAR(50) NOT NULL,           -- Department the employee works in
    IsActive BOOLEAN DEFAULT TRUE,             -- Flag indicating if the employee is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store employee timesheet information
CREATE TABLE Timesheets (
    TimesheetID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each timesheet
    EmployeeID INT NOT NULL,                    -- Foreign key to Employees table
    WeekStartDate DATE NOT NULL,                -- Week start date for the timesheet
    WeekEndDate DATE NOT NULL,                  -- Week end date for the timesheet
    TotalHoursWorked DECIMAL(5, 2) NOT NULL,    -- Total hours worked during the week
    Status ENUM('Submitted', 'Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Timesheet status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Table to store payroll-related information
CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each payroll record
    EmployeeID INT NOT NULL,                   -- Foreign key to Employees table
    PayPeriodStart DATE NOT NULL,              -- Start date of the pay period
    PayPeriodEnd DATE NOT NULL,                -- End date of the pay period
    GrossPay DECIMAL(10, 2) NOT NULL,          -- Gross pay for the pay period
    NetPay DECIMAL(10, 2) NOT NULL,            -- Net pay after deductions
    PaymentStatus ENUM('Processed', 'Pending', 'Failed') DEFAULT 'Pending', -- Payroll status
    PaymentDate DATE,                          -- Date of payment processing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Table to store employee leave requests
CREATE TABLE LeaveRequests (
    LeaveRequestID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each leave request
    EmployeeID INT NOT NULL,                       -- Foreign key to Employees table
    LeaveStartDate DATE NOT NULL,                  -- Start date of the leave
    LeaveEndDate DATE NOT NULL,                    -- End date of the leave
    LeaveType ENUM('Vacation', 'Sick', 'Personal', 'Other') NOT NULL, -- Type of leave
    LeaveStatus ENUM('Requested', 'Approved', 'Rejected') DEFAULT 'Requested', -- Leave request status
    Reason TEXT,                                   -- Reason for the leave request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Indexes for optimizing common queries
CREATE INDEX idx_employee_email ON Employees (Email); -- Index for faster email lookups
CREATE INDEX idx_timesheet_employee ON Timesheets (EmployeeID); -- Index for employee timesheet queries
CREATE INDEX idx_payroll_employee_period ON Payroll (EmployeeID, PayPeriodStart, PayPeriodEnd); -- Index for payroll period queries
CREATE INDEX idx_leave_request_employee ON LeaveRequests (EmployeeID); -- Index for employee leave requests queries
```
