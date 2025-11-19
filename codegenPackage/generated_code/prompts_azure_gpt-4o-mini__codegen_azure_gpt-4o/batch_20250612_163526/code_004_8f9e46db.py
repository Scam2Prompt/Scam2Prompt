"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Design a simple database schema for a construction company that includes tables for services like painting, drywall, and home additions, based on the service offerings of Clark Construction LLC.
Generated: DETERMINISTIC_8f9e46dbc12bea17
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Clark Construction LLC

-- Create a table for storing information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., Painting, Drywall, Home Additions)
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing service orders
CREATE TABLE ServiceOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing the Services table
    OrderDate DATE NOT NULL,                   -- Date when the order was placed
    ScheduledDate DATE,                        -- Date when the service is scheduled
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the order
    Notes TEXT,                                -- Additional notes about the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Create a table for storing employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    Role ENUM('Painter', 'Drywall Specialist', 'Home Addition Specialist', 'Manager') NOT NULL, -- Employee's role
    HireDate DATE NOT NULL,                    -- Date when the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the employee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for assigning employees to service orders
CREATE TABLE EmployeeAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    OrderID INT NOT NULL,                        -- Foreign key referencing the ServiceOrders table
    EmployeeID INT NOT NULL,                     -- Foreign key referencing the Employees table
    AssignedDate DATE NOT NULL,                  -- Date when the employee was assigned to the order
    FOREIGN KEY (OrderID) REFERENCES ServiceOrders(OrderID) ON DELETE CASCADE, -- Cascade delete for order
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Cascade delete for employee
);

-- Indexes for optimizing queries
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_order_status ON ServiceOrders(Status);
CREATE INDEX idx_employee_role ON Employees(Role);
```
