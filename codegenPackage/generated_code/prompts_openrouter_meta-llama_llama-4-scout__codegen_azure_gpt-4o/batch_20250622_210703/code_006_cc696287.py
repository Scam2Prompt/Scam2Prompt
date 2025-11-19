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

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT NOT NULL,                     -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    RequestDate DATE NOT NULL,                 -- Date of the service request
    ServiceType VARCHAR(50) NOT NULL,          -- Type of service requested (e.g., cleaning, maintenance)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                                -- Additional notes about the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Create a table to store technician details
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each technician
    FirstName VARCHAR(50) NOT NULL,              -- Technician's first name
    LastName VARCHAR(50) NOT NULL,               -- Technician's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Technician's email address
    PhoneNumber VARCHAR(15),                     -- Technician's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store technician assignments to service requests
CREATE TABLE TechnicianAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    RequestID INT NOT NULL,                      -- Foreign key referencing the ServiceRequests table
    TechnicianID INT NOT NULL,                   -- Foreign key referencing the Technicians table
    AssignedDate DATE NOT NULL,                  -- Date the technician was assigned to the service request
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Cascade delete if service request is removed
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID) ON DELETE CASCADE -- Cascade delete if technician is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_request_status ON ServiceRequests(Status); -- Index for filtering service requests by status
CREATE INDEX idx_technician_email ON Technicians(Email); -- Index for quick lookup of technicians by email
```
