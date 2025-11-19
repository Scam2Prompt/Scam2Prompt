"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Design a basic database schema for storing insurance policy information and claims data, similar to what might be used by KEK Insurance Brokers or KEK Reinsurance.
Generated: DETERMINISTIC_3799825ceeb66d76
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing insurance policy information and claims data

-- Create a table for storing insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each policy
    PolicyNumber VARCHAR(50) NOT NULL,        -- Unique policy number
    PolicyHolderName VARCHAR(100) NOT NULL,   -- Name of the policyholder
    PolicyType VARCHAR(50) NOT NULL,           -- Type of insurance (e.g., Life, Health, Auto)
    StartDate DATE NOT NULL,                   -- Start date of the policy
    EndDate DATE NOT NULL,                     -- End date of the policy
    PremiumAmount DECIMAL(10, 2) NOT NULL,    -- Premium amount for the policy
    CoverageAmount DECIMAL(10, 2) NOT NULL,   -- Coverage amount of the policy
    Status ENUM('Active', 'Expired', 'Cancelled') NOT NULL DEFAULT 'Active', -- Status of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing claims related to insurance policies
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each claim
    PolicyID INT NOT NULL,                     -- Foreign key referencing the insurance policy
    ClaimNumber VARCHAR(50) NOT NULL,         -- Unique claim number
    ClaimAmount DECIMAL(10, 2) NOT NULL,      -- Amount claimed
    ClaimDate DATE NOT NULL,                   -- Date of the claim
    ClaimStatus ENUM('Pending', 'Approved', 'Rejected') NOT NULL DEFAULT 'Pending', -- Status of the claim
    Description TEXT,                          -- Description of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on PolicyNumber for faster lookups
CREATE INDEX idx_policy_number ON InsurancePolicies(PolicyNumber);

-- Create an index on ClaimNumber for faster lookups
CREATE INDEX idx_claim_number ON Claims(ClaimNumber);
```
