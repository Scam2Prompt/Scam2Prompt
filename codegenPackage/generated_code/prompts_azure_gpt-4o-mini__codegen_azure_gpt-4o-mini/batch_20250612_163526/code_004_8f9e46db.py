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

-- Create a database for the construction company
CREATE DATABASE ClarkConstruction;

-- Use the created database
USE ClarkConstruction;

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., Painting, Drywall)
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store service requests from customers
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service request
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,               -- Employee's last name
    Position VARCHAR(50),                         -- Employee's position (e.g., Painter, Contractor)
    HireDate DATE NOT NULL,                      -- Date the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the employee was added
);

-- Table to store assignments of employees to service requests
CREATE TABLE EmployeeAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    RequestID INT NOT NULL,                      -- Foreign key referencing ServiceRequests
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees
    AssignedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the employee was assigned
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for Services
INSERT INTO Services (ServiceName, Description, Price) VALUES
('Painting', 'Interior and exterior painting services.', 1500.00),
('Drywall', 'Installation and repair of drywall.', 1200.00),
('Home Addition', 'Building additional rooms or extensions.', 25000.00);

-- Sample data insertion for Customers
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Sample data insertion for Employees
INSERT INTO Employees (FirstName, LastName, Position, HireDate) VALUES
('Mike', 'Johnson', 'Painter', '2022-01-15'),
('Sara', 'Williams', 'Contractor', '2021-06-10');
```
