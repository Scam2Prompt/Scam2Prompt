"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Design a database schema for storing information about Loss Group Criteria's clients and their insurance policies.
Generated: DETERMINISTIC_f064eef9af8a45e8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Loss Group Criteria's clients and their insurance policies

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the client record was last updated
);

-- Table to store insurance policy information
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policy
    ClientID INT NOT NULL,                   -- Foreign key referencing the Clients table
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL, -- Unique policy number
    PolicyType VARCHAR(50) NOT NULL,         -- Type of insurance policy (e.g., health, auto, home)
    CoverageAmount DECIMAL(10, 2) NOT NULL,  -- Coverage amount for the policy
    PremiumAmount DECIMAL(10, 2) NOT NULL,   -- Premium amount for the policy
    StartDate DATE NOT NULL,                 -- Start date of the policy
    EndDate DATE NOT NULL,                   -- End date of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the policy record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the policy record was last updated
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures policies are deleted if the client is deleted
);

-- Table to store loss group criteria information
CREATE TABLE LossGroupCriteria (
    CriteriaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each criteria
    PolicyID INT NOT NULL,                     -- Foreign key referencing the InsurancePolicies table
    CriteriaName VARCHAR(100) NOT NULL,        -- Name of the loss group criteria
    Description TEXT,                          -- Description of the criteria
    ThresholdAmount DECIMAL(10, 2) NOT NULL,   -- Threshold amount for the criteria
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the criteria record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the criteria record was last updated
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Ensures criteria are deleted if the policy is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for faster lookup of clients by email
CREATE INDEX idx_policies_policy_number ON InsurancePolicies(PolicyNumber); -- Index for faster lookup of policies by policy number
CREATE INDEX idx_loss_criteria_policy_id ON LossGroupCriteria(PolicyID); -- Index for faster lookup of criteria by policy ID
```
