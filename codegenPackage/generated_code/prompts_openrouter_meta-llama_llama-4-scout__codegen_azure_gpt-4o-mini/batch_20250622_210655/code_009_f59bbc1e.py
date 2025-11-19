"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Create a SQL database schema to store customer information, service requests, and appointment schedules for a plumbing company like י.א. אינסטלציה.
Generated: DETERMINISTIC_f59bbc1ed2759a54
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Plumbing Company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS ServiceRequests;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,  -- Customer's phone number (unique)
    Email VARCHAR(100) UNIQUE,                 -- Customer's email address (optional, unique)
    Address VARCHAR(255) NOT NULL,             -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store service requests made by customers
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service request
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the service request
    ServiceType VARCHAR(100) NOT NULL,          -- Type of service requested (e.g., plumbing, installation)
    Description TEXT,                           -- Detailed description of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store appointment schedules for service requests
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    RequestID INT NOT NULL,                        -- Foreign key referencing ServiceRequests
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    PlumberAssigned VARCHAR(100),                  -- Name of the plumber assigned to the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Current status of the appointment
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_request_status ON ServiceRequests(Status);
CREATE INDEX idx_appointment_status ON Appointments(Status);
```
