"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Design a database schema to store information about clients, services, and employees for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_b664d1baa7ece98e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ashvi Facility Management Services

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS ClientServices;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactNumber VARCHAR(15),                 -- Contact number of the client
    Email VARCHAR(255) UNIQUE,                 -- Email address of the client
    Address TEXT,                               -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,          -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each employee
    EmployeeName VARCHAR(255) NOT NULL,          -- Name of the employee
    Position VARCHAR(100),                        -- Position of the employee
    ContactNumber VARCHAR(15),                   -- Contact number of the employee
    Email VARCHAR(255) UNIQUE,                   -- Email address of the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the employee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store the relationship between clients and services
CREATE TABLE ClientServices (
    ClientServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client-service relationship
    ClientID INT NOT NULL,                             -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                            -- Foreign key referencing Services
    EmployeeID INT NOT NULL,                           -- Foreign key referencing Employees
    ServiceDate DATE NOT NULL,                         -- Date when the service is provided
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',  -- Status of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the record was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_employee_name ON Employees(EmployeeName);
```
