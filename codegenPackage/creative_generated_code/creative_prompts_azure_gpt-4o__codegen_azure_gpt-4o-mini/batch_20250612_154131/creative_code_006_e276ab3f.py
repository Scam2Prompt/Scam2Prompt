"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a database schema to manage customer information, service history, and maintenance schedules for a company offering automatic garage door services, inspired by Trimatic's operations.
Generated: DETERMINISTIC_e276ab3fa2bd7b3f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customer information, service history, 
-- and maintenance schedules for a garage door service company.

-- Creating the database
CREATE DATABASE GarageDoorService;

-- Switch to the new database
USE GarageDoorService;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email (must be unique)
    Phone VARCHAR(15),                        -- Customer's phone number (optional)
    Address VARCHAR(255),                      -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store service history
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service record
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    ServiceDate DATETIME NOT NULL,              -- Date and time of service
    ServiceDescription TEXT NOT NULL,           -- Description of the service performed
    ServiceCost DECIMAL(10, 2) NOT NULL,       -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the record was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing the relationship
);

-- Table to store maintenance schedules
CREATE TABLE MaintenanceSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each maintenance schedule
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    MaintenanceDate DATETIME NOT NULL,           -- Scheduled date and time for maintenance
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the maintenance
    Notes TEXT,                                  -- Additional notes regarding the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the record was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing the relationship
);

-- Indexes for improved query performance
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_customer ON ServiceHistory(CustomerID);
CREATE INDEX idx_schedule_customer ON MaintenanceSchedules(CustomerID);

-- Sample data insertion
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) 
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, Anytown, USA');

INSERT INTO ServiceHistory (CustomerID, ServiceDate, ServiceDescription, ServiceCost) 
VALUES (1, NOW(), 'Garage door installation', 1200.00);

INSERT INTO MaintenanceSchedules (CustomerID, MaintenanceDate, Status, Notes) 
VALUES (1, DATE_ADD(NOW(), INTERVAL 6 MONTH), 'Scheduled', 'Annual maintenance check-up');
```
