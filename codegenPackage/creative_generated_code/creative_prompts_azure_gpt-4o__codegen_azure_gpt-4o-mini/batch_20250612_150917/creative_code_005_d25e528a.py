"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Write a SQL database schema for Grupo de Seguros Tempus to manage customer data, insurance policies, claims, and advisor commissions.
Generated: DETERMINISTIC_d25e528a954a4a1b
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Grupo de Seguros Tempus Database Schema

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS AdvisorCommission;
DROP TABLE IF EXISTS Claims;
DROP TABLE IF EXISTS InsurancePolicy;
DROP TABLE IF EXISTS Customer;

-- Create a table to store customer data
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email, must be unique
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record of when the customer was created
);

-- Create a table to store insurance policy details
CREATE TABLE InsurancePolicy (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each policy
    CustomerID INT NOT NULL,                     -- Foreign key to the Customer table
    PolicyType VARCHAR(50) NOT NULL,            -- Type of insurance policy
    CoverageAmount DECIMAL(10, 2) NOT NULL,     -- Coverage amount for the policy
    StartDate DATE NOT NULL,                     -- Start date of the policy
    EndDate DATE NOT NULL,                       -- End date of the policy
    Premium DECIMAL(10, 2) NOT NULL,            -- Premium amount for the policy
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store claims made by customers
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each claim
    PolicyID INT NOT NULL,                       -- Foreign key to the InsurancePolicy table
    ClaimDate DATE NOT NULL,                     -- Date the claim was made
    AmountClaimed DECIMAL(10, 2) NOT NULL,      -- Amount claimed
    Status VARCHAR(20) NOT NULL,                 -- Status of the claim (e.g., Pending, Approved, Denied)
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicy(PolicyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to manage advisor commissions
CREATE TABLE AdvisorCommission (
    CommissionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each commission record
    AdvisorName VARCHAR(100) NOT NULL,          -- Name of the advisor
    PolicyID INT NOT NULL,                       -- Foreign key to the InsurancePolicy table
    CommissionAmount DECIMAL(10, 2) NOT NULL,   -- Amount of commission earned
    CommissionDate DATE NOT NULL,                -- Date the commission was earned
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicy(PolicyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Ensure all tables are created correctly
-- Add any indexing or additional constraints as needed for performance and data integrity
```
