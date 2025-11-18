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
-- This schema manages customer data, insurance policies, claims, and advisor commissions.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address TEXT,                              -- Customer's physical address
    DateOfBirth DATE,                          -- Customer's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to store insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each insurance policy
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,  -- Unique policy number
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    PolicyType VARCHAR(50) NOT NULL,           -- Type of insurance (e.g., health, auto, life)
    CoverageAmount DECIMAL(15, 2) NOT NULL,    -- Coverage amount of the policy
    PremiumAmount DECIMAL(15, 2) NOT NULL,     -- Premium amount paid for the policy
    StartDate DATE NOT NULL,                   -- Start date of the policy
    EndDate DATE NOT NULL,                     -- End date of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the policy was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store insurance claims
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each claim
    PolicyID INT NOT NULL,                     -- Foreign key referencing InsurancePolicies table
    ClaimDate DATE NOT NULL,                   -- Date when the claim was filed
    ClaimAmount DECIMAL(15, 2) NOT NULL,       -- Amount claimed
    ClaimStatus ENUM('Pending', 'Approved', 'Rejected') NOT NULL, -- Status of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the claim was created
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE
);

-- Table to store insurance advisors and their commissions
CREATE TABLE Advisors (
    AdvisorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each advisor
    FirstName VARCHAR(50) NOT NULL,            -- Advisor's first name
    LastName VARCHAR(50) NOT NULL,             -- Advisor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Advisor's email address (must be unique)
    PhoneNumber VARCHAR(20),                   -- Advisor's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to store advisor commissions associated with policies
CREATE TABLE Commissions (
    CommissionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each commission record
    AdvisorID INT NOT NULL,                      -- Foreign key referencing Advisors table
    PolicyID INT NOT NULL,                       -- Foreign key referencing InsurancePolicies table
    CommissionAmount DECIMAL(15, 2) NOT NULL,    -- Commission amount for the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the commission was created
    FOREIGN KEY (AdvisorID) REFERENCES Advisors(AdvisorID) ON DELETE CASCADE,
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE
);

-- Additional indexes for optimized querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_policy_customer ON InsurancePolicies(CustomerID);
CREATE INDEX idx_claim_policy ON Claims(PolicyID);
CREATE INDEX idx_commission_policy ON Commissions(PolicyID);
CREATE INDEX idx_commission_advisor ON Commissions(AdvisorID);
```
