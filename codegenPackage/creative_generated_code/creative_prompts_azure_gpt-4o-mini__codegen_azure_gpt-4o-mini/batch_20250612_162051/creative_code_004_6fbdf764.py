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
-- Database Schema for a Carpentry Business (Aluivars)
-- This schema is designed to store customer projects and service requests focusing on iron and aluminum work.

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Customer's email address (must be unique)
    Phone VARCHAR(15),                        -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store different types of projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    Material ENUM('Iron', 'Aluminum') NOT NULL, -- Material used for the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store service requests associated with projects
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service request
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Request creation timestamp
    ServiceType VARCHAR(100) NOT NULL,         -- Type of service requested
    Description TEXT,                           -- Detailed description of the service request
    Status ENUM('Open', 'In Progress', 'Resolved', 'Closed') DEFAULT 'Open', -- Current status of the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Foreign key constraint
);

-- Index to optimize queries on customer emails
CREATE INDEX idx_email ON Customers (Email);

-- Index to optimize querying of project statuses
CREATE INDEX idx_project_status ON Projects (Status);

-- Index to optimize querying of service request statuses
CREATE INDEX idx_service_request_status ON ServiceRequests (Status);
```
