"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: Create a SQL database schema to store customer information, service requests, and appointments for a company like SOS Menuiserie.
Generated: DETERMINISTIC_b9085561f2903746
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for SOS Menuiserie

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS ServiceRequests;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (must be unique)
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store service requests made by customers
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service request
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceType VARCHAR(100) NOT NULL,           -- Type of service requested
    Description TEXT,                             -- Detailed description of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the request was made
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store appointments for service requests
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    RequestID INT NOT NULL,                        -- Foreign key referencing ServiceRequests
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Location VARCHAR(255),                         -- Location of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_request_status ON ServiceRequests(Status);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
