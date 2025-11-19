"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Design a database schema for storing client information and insurance policy details for a company like GYV Seguros, which specializes in various insurance products.
Generated: DETERMINISTIC_07003492c9d7781b
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing client information and insurance policy details
-- Database Name: InsuranceCompanyDB

-- Create Clients table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,                   -- Client's first name
    LastName VARCHAR(100) NOT NULL,                    -- Client's last name
    DateOfBirth DATE NOT NULL,                         -- Client's date of birth
    Email VARCHAR(255) UNIQUE NOT NULL,                -- Client's email address
    PhoneNumber VARCHAR(15) NOT NULL,                  -- Client's phone number
    Address TEXT NOT NULL,                             -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when client record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when client record is updated
);

-- Create InsurancePolicies table to store details of insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each policy
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,          -- Unique policy number
    ClientID INT NOT NULL,                             -- Foreign key referencing the Clients table
    PolicyType ENUM('Life', 'Health', 'Car', 'Home', 'Travel') NOT NULL, -- Type of insurance policy
    CoverageAmount DECIMAL(15, 2) NOT NULL,            -- Coverage amount for the policy
    PremiumAmount DECIMAL(15, 2) NOT NULL,             -- Premium amount to be paid by the client
    StartDate DATE NOT NULL,                           -- Start date of the policy
    EndDate DATE NOT NULL,                             -- End date of the policy
    Status ENUM('Active', 'Expired', 'Cancelled') NOT NULL, -- Status of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when policy record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when policy record is updated
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Establishing relationship with Clients table
);

-- Create Claims table to store details of claims filed against policies
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each claim
    PolicyID INT NOT NULL,                             -- Foreign key referencing the InsurancePolicies table
    ClaimDate DATE NOT NULL,                           -- Date when the claim was filed
    ClaimAmount DECIMAL(15, 2) NOT NULL,               -- Requested claim amount
    ClaimStatus ENUM('Pending', 'Approved', 'Rejected') NOT NULL, -- Status of the claim
    Description TEXT,                                  -- Description/details of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when claim record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when claim record is updated
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) -- Establishing relationship with InsurancePolicies table
);

-- Add indexes for faster lookup
CREATE INDEX idx_clients_email ON Clients (Email);
CREATE INDEX idx_policies_policy_number ON InsurancePolicies (PolicyNumber);
CREATE INDEX idx_claims_policy_id ON Claims (PolicyID);
```
