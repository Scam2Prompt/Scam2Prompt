"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Design a database schema for storing customer projects and service requests for a carpentry business like Aluivars, focusing on iron and aluminum work.
Generated: DETERMINISTIC_6fbdf7642a5e5474
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to design the database schema for storing customer projects and service requests
-- for a carpentry business focusing on iron and aluminum work.

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table for storing projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key linking the project to a customer
    ProjectName VARCHAR(100) NOT NULL,         -- Name or title of the project
    Description TEXT,                          -- Detailed description of the project
    MaterialType ENUM('Iron', 'Aluminum') NOT NULL, -- Material type for the project
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date (if applicable)
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Enforces relationship with Customers table
);

-- Create a table for storing service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key linking the request to a customer
    ProjectID INT,                             -- Foreign key linking the request to a project (if applicable)
    RequestType ENUM('Repair', 'Maintenance', 'Inquiry') NOT NULL, -- Type of service request
    Description TEXT,                          -- Detailed description of the service request
    RequestedDate DATE NOT NULL,               -- Date when the service request was made
    Status ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending', -- Current status of the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), -- Enforces relationship with Customers table
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) -- Enforces relationship with Projects table
);

-- Create indexes to improve query performance for frequently searched fields
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_projects_customer ON Projects(CustomerID);
CREATE INDEX idx_service_requests_customer ON ServiceRequests(CustomerID);
CREATE INDEX idx_service_requests_project ON ServiceRequests(ProjectID);

-- Ensure proper error handling in the database by using appropriate constraints
ALTER TABLE Customers ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%@%.%'); -- Basic email format validation (optional but helpful)
```
