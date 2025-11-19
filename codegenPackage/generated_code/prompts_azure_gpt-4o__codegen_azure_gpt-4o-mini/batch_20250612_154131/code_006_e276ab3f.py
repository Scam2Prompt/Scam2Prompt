"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a database schema to manage customer information, service history, and maintenance schedules for a company offering automatic garage door services, inspired by Trimatic's operations.
Generated: DETERMINISTIC_e276ab3fa2bd7b3f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customer information, service history, and maintenance schedules
-- for a company offering automatic garage door services.

-- Create the database
CREATE DATABASE GarageDoorServices;

-- Use the created database
USE GarageDoorServices;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    City VARCHAR(50),                            -- Customer's city
    State VARCHAR(50),                           -- Customer's state
    ZipCode VARCHAR(10),                         -- Customer's zip code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store service history
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service record
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ServiceDate DATE NOT NULL,                   -- Date of the service
    ServiceType VARCHAR(100) NOT NULL,           -- Type of service performed
    Description TEXT,                            -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the service
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store maintenance schedules
CREATE TABLE MaintenanceSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each maintenance schedule
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    MaintenanceDate DATE NOT NULL,               -- Scheduled date for maintenance
    Frequency ENUM('Monthly', 'Quarterly', 'Yearly') NOT NULL, -- Frequency of maintenance
    Notes TEXT,                                  -- Additional notes for the maintenance
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_customer ON ServiceHistory(CustomerID);
CREATE INDEX idx_schedule_customer ON MaintenanceSchedules(CustomerID);

-- Sample error handling for database operations (to be implemented in application logic)
-- BEGIN TRY
--     -- Database operations here
-- END TRY
-- BEGIN CATCH
--     -- Handle errors here
--     SELECT ERROR_MESSAGE() AS ErrorMessage;
-- END CATCH;
```
