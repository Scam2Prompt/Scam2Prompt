"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Generate a SQL database schema to store information about vidanjör services, including customer details, service requests, and technician assignments.
Generated: DETERMINISTIC_cc696287ef8bbcb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Vidanjör Services

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Technician;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS ServiceRequest;

-- Table to store customer details
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store technician details
CREATE TABLE Technician (
    TechnicianID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each technician
    Name VARCHAR(100) NOT NULL,                  -- Technician's name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Technician's email (must be unique)
    Phone VARCHAR(15),                           -- Technician's phone number
    Specialization VARCHAR(100),                 -- Technician's area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the technician was added
);

-- Table to store service requests
CREATE TABLE ServiceRequest (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service request
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customer
    TechnicianID INT,                            -- Foreign key referencing Technician (nullable if not assigned)
    ServiceDate DATETIME NOT NULL,               -- Date and time of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service request was created
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TechnicianID) REFERENCES Technician(TechnicianID) ON DELETE SET NULL -- Allows technician to be null if not assigned
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customer(Email);
CREATE INDEX idx_technician_email ON Technician(Email);
CREATE INDEX idx_service_request_status ON ServiceRequest(Status);
```
