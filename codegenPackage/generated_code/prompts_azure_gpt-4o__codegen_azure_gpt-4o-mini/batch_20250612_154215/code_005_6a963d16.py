"""
Generated Code Metadata:
========================
Original URL: https://7054company.github.io
Prompt: Develop a database schema in SQL to track consulting, development, and support services for a company similar to 7054Company.
Generated: DETERMINISTIC_6a963d16bb53debe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking consulting, development, and support services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS SupportTickets;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Employees;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL,       -- Email address for client contact
    PhoneNumber VARCHAR(20),                   -- Phone number for client contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    EmployeeName VARCHAR(255) NOT NULL,         -- Name of the employee
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Unique email address for the employee
    PhoneNumber VARCHAR(20),                    -- Phone number for the employee
    Role ENUM('Consultant', 'Developer', 'Support') NOT NULL,  -- Role of the employee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the employee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store different services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,          -- Name of the service
    ServiceType ENUM('Consulting', 'Development', 'Support') NOT NULL,  -- Type of service
    Description TEXT,                            -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to track support tickets
CREATE TABLE SupportTickets (
    TicketID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each support ticket
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    IssueDescription TEXT NOT NULL,              -- Description of the issue
    Status ENUM('Open', 'In Progress', 'Resolved', 'Closed') DEFAULT 'Open',  -- Current status of the ticket
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the ticket was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_employee_role ON Employees(Role);
CREATE INDEX idx_service_type ON Services(ServiceType);
CREATE INDEX idx_ticket_status ON SupportTickets(Status);
```
