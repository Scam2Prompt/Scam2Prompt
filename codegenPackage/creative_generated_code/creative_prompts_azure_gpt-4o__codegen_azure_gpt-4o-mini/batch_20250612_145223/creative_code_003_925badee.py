"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Generate a database schema in SQL for managing loan applications, including fields relevant to TymeBank's loan application system.
Generated: DETERMINISTIC_925badee57424da3
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing loan applications in TymeBank's loan application system

-- Drop existing tables if they exist to prevent conflicts
DROP TABLE IF EXISTS LoanApplications;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS LoanStatuses;

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record last update timestamp
);

-- Create a table to store loan statuses
CREATE TABLE LoanStatuses (
    StatusID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each status
    StatusDescription VARCHAR(50) NOT NULL UNIQUE -- Description of the loan status (e.g., 'Pending', 'Approved', 'Rejected')
);

-- Insert default loan statuses
INSERT INTO LoanStatuses (StatusDescription) VALUES 
('Pending'),
('Approved'),
('Rejected'),
('Disbursed'),
('Closed');

-- Create a table to store loan applications
CREATE TABLE LoanApplications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each application
    CustomerID INT NOT NULL,                       -- ID of the customer applying for the loan
    LoanAmount DECIMAL(10, 2) NOT NULL,           -- Amount requested for the loan
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the application
    StatusID INT NOT NULL,                         -- Current status of the loan application
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),  -- Foreign key linking to Customers table
    FOREIGN KEY (StatusID) REFERENCES LoanStatuses(StatusID)    -- Foreign key linking to LoanStatuses table
);

-- Create a table to store loans issued
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each loan
    ApplicationID INT NOT NULL,                    -- ID of the corresponding loan application
    LoanAmount DECIMAL(10, 2) NOT NULL,           -- Amount of the loan issued
    InterestRate DECIMAL(5, 2) NOT NULL,          -- Interest rate for the loan
    StartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start date of the loan
    EndDate TIMESTAMP,                             -- End date of the loan (calculated upon disbursement)
    FOREIGN KEY (ApplicationID) REFERENCES LoanApplications(ApplicationID)  -- Foreign key linking to LoanApplications table
);

-- Ensure all tables have been created successfully
SELECT 'Database schema for TymeBank loan application system created successfully.' AS Message;
```
