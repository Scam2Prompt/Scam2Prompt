"""
Generated Code Metadata:
========================
Original URL: https://aibaoinsurance.com
Prompt: "Design a database schema to store client information, insurance policies, and claims for an insurance brokerage firm like aibaoinsurance.com, ensuring data consistency and security."
Generated: DETERMINISTIC_7db9e137468e8fff
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an insurance brokerage firm

-- Create a database for the insurance brokerage
CREATE DATABASE InsuranceBrokerage;

-- Use the created database
USE InsuranceBrokerage;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    Address VARCHAR(255),                     -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store insurance policies
CREATE TABLE Policies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each policy
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,  -- Unique policy number
    PolicyType VARCHAR(50) NOT NULL,           -- Type of insurance policy (e.g., health, auto)
    StartDate DATE NOT NULL,                   -- Policy start date
    EndDate DATE NOT NULL,                     -- Policy end date
    Premium DECIMAL(10, 2) NOT NULL,          -- Policy premium amount
    Status ENUM('Active', 'Inactive', 'Cancelled') DEFAULT 'Active', -- Policy status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store claims information
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each claim
    PolicyID INT NOT NULL,                     -- Foreign key referencing Policies
    ClaimNumber VARCHAR(50) UNIQUE NOT NULL,   -- Unique claim number
    ClaimDate DATE NOT NULL,                   -- Date of the claim
    ClaimAmount DECIMAL(10, 2) NOT NULL,      -- Amount claimed
    Status ENUM('Pending', 'Approved', 'Denied') DEFAULT 'Pending', -- Claim status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_policy_number ON Policies(PolicyNumber);
CREATE INDEX idx_claim_number ON Claims(ClaimNumber);
```
