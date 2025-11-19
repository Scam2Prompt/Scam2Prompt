"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Design a database schema for a home services management system that tracks customer requests for services like air conditioning cleaning and water leakage detection, as offered by شركة انجاز.
Generated: DETERMINISTIC_64e59ad3c1dd6ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home services management system

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's full name
    Phone VARCHAR(15) NOT NULL UNIQUE,          -- Customer's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address
    Address VARCHAR(255) NOT NULL,               -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store service types
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,    -- Name of the service (e.g., Air Conditioning Cleaning)
    Description TEXT,                             -- Description of the service
    Price DECIMAL(10, 2) NOT NULL                 -- Price of the service
);

-- Create a table to store customer service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service request
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store service technicians
CREATE TABLE Technicians (
    TechnicianID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each technician
    Name VARCHAR(100) NOT NULL,                   -- Technician's full name
    Phone VARCHAR(15) NOT NULL UNIQUE,            -- Technician's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Technician's email address
    HireDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Date when the technician was hired
);

-- Create a table to assign technicians to service requests
CREATE TABLE TechnicianAssignments (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each assignment
    RequestID INT NOT NULL,                        -- Foreign key referencing ServiceRequests
    TechnicianID INT NOT NULL,                     -- Foreign key referencing Technicians
    AssignmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the technician was assigned
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store customer feedback
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each feedback entry
    RequestID INT NOT NULL,                        -- Foreign key referencing ServiceRequests
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    Comments TEXT,                                 -- Additional comments from the customer
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the feedback was submitted
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Ensure referential integrity
);
```
