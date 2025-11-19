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
-- Database Schema for Facility Management Company

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Contact number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    Name VARCHAR(100) NOT NULL,                -- Name of the employee
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the employee
    PhoneNumber VARCHAR(15),                   -- Contact number of the employee
    Position VARCHAR(50),                      -- Job position of the employee
    HireDate DATE,                             -- Date the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store assignments of services to clients
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client-service assignment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services table
    StartDate DATE NOT NULL,                        -- Start date of the service
    EndDate DATE,                                   -- End date of the service (nullable for ongoing services)
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Table to store assignments of employees to services
CREATE TABLE EmployeeServices (
    EmployeeServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee-service assignment
    EmployeeID INT NOT NULL,                          -- Foreign key referencing Employees table
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services table
    AssignmentDate DATE NOT NULL,                     -- Date the employee was assigned to the service
    Role VARCHAR(50),                                 -- Role of the employee in the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE, -- Cascade delete for employee
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_employee_email ON Employees(Email);
CREATE INDEX idx_service_name ON Services(Name);
CREATE INDEX idx_client_service ON ClientServices(ClientID, ServiceID);
CREATE INDEX idx_employee_service ON EmployeeServices(EmployeeID, ServiceID);
```
