"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Design a database schema to store information about plumbing and fire fighting services provided by a company like ERA ENGINEERING."
Generated: DETERMINISTIC_69453f7e3bb13dde
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Plumbing and Fire Fighting Services

-- Table to store information about services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service (e.g., Plumbing, Fire Fighting)
    Description TEXT,                         -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(255) NOT NULL,            -- Full name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Contact number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service request
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    RequestDate DATE NOT NULL,                -- Date when the service was requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                               -- Additional notes or instructions for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Table to store information about employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FullName VARCHAR(255) NOT NULL,            -- Full name of the employee
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the employee
    PhoneNumber VARCHAR(15),                   -- Contact number of the employee
    Role ENUM('Plumber', 'Firefighter', 'Manager', 'Technician') NOT NULL, -- Role of the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the employee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to assign employees to service requests
CREATE TABLE EmployeeAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    RequestID INT NOT NULL,                      -- Foreign key referencing ServiceRequests table
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was made
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Cascade delete if request is removed
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Cascade delete if employee is removed
);

-- Table to store payment information for service requests
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    RequestID INT NOT NULL,                   -- Foreign key referencing ServiceRequests table
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate DATE NOT NULL,                -- Date of payment
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL, -- Payment method
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Cascade delete if request is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_request_status ON ServiceRequests(Status);
CREATE INDEX idx_employee_role ON Employees(Role);
```
