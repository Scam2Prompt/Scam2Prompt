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

-- Create a database
CREATE DATABASE IF NOT EXISTS SOSMenuiserie;

-- Use the database
USE SOSMenuiserie;

-- Table to store customer information
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table to store service requests
CREATE TABLE IF NOT EXISTS ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceType VARCHAR(100) NOT NULL,         -- Type of service requested
    Description TEXT,                          -- Detailed description of the request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the service request was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table to store appointments
CREATE TABLE IF NOT EXISTS Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    RequestID INT NOT NULL,                       -- Foreign key referencing ServiceRequests table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    TechnicianName VARCHAR(50),                  -- Name of the technician assigned to the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the appointment was last updated
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Cascade delete if service request is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_request_status ON ServiceRequests(Status); -- Index for filtering by request status
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for sorting/filtering by appointment date
```
