"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Create a SQL database schema to store information about Refund-me's customers, cases, and refunds, including relevant fields such as customer ID, case status, and refund amount.
Generated: DETERMINISTIC_ec3dbed189ead7f9
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Refund-me's customers, cases, and refunds

-- Create the database
CREATE DATABASE RefundMeDB;

-- Use the created database
USE RefundMeDB;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each case
    CustomerID INT NOT NULL,                     -- Foreign key referencing the customer
    CaseStatus ENUM('Open', 'In Progress', 'Closed') NOT NULL, -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the case was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store refund information
CREATE TABLE Refunds (
    RefundID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each refund
    CaseID INT NOT NULL,                         -- Foreign key referencing the case
    RefundAmount DECIMAL(10, 2) NOT NULL,       -- Amount of the refund
    RefundDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the refund was processed
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_case_status ON Cases(CaseStatus);
CREATE INDEX idx_refund_date ON Refunds(RefundDate);
```
