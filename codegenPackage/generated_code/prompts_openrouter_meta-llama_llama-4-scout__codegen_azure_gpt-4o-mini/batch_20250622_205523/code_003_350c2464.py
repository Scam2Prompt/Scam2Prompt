"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Create a SQL database schema for a cleaning services company, including tables for customers, services, and appointments, with constraints and relationships.
Generated: DETERMINISTIC_350c2464fbda70b6
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the cleaning services company
CREATE DATABASE CleaningServices;

-- Use the created database
USE CleaningServices;

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                      -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table for storing service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service
    Description TEXT,                              -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the service
    Duration INT NOT NULL                          -- Duration of the service in minutes
);

-- Table for storing appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
