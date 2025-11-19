"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Develop a simple database schema to store information about clients, employees, and services provided by a youth mental healthcare company, considering the need for superior client-focused care.
Generated: DETERMINISTIC_26428b63e4d0423d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a youth mental healthcare company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Appointments;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Client's gender
    ContactNumber VARCHAR(15),                 -- Client's contact number
    Email VARCHAR(100) UNIQUE,                 -- Client's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,              -- Employee's last name
    Position VARCHAR(50) NOT NULL,              -- Employee's job position
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Employee's email address
    PhoneNumber VARCHAR(15),                     -- Employee's contact number
    HireDate DATE NOT NULL,                      -- Date the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services provided by the company
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service
    Description TEXT,                            -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointments between clients and employees
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    EmployeeID INT NOT NULL,                       -- Foreign key referencing Employees
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
