"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Design a database schema to store information about customers, projects, and services offered by a fence, deck, and pergola installation company, including fields for customer satisfaction ratings and project completion dates."
Generated: DETERMINISTIC_ebc45a33555c8a23
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a fence, deck, and pergola installation company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service (e.g., Fence Installation)
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL                -- Price of the service
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each project
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    StartDate DATE NOT NULL,                     -- Project start date
    CompletionDate DATE,                         -- Project completion date
    SatisfactionRating INT CHECK (SatisfactionRating BETWEEN 1 AND 5), -- Customer satisfaction rating (1-5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_project_dates ON Projects(StartDate, CompletionDate);
```
