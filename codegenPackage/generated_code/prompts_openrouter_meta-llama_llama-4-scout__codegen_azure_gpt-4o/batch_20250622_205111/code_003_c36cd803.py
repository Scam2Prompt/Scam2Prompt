"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: "Design a database schema to store insurance claims (siniestros) and client information for a company like Yexine Rangel Asesores de Seguros Ltda, including tables for clients, policies, and claims."
Generated: DETERMINISTIC_c36cd803ccc6317f
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Insurance Claims Management System

-- Table: Clients
-- Stores information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Policies
-- Stores information about insurance policies
CREATE TABLE Policies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policy
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL, -- Unique policy number
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    PolicyType VARCHAR(50) NOT NULL,          -- Type of policy (e.g., auto, health, life)
    CoverageAmount DECIMAL(10, 2) NOT NULL,   -- Coverage amount for the policy
    Premium DECIMAL(10, 2) NOT NULL,          -- Premium amount for the policy
    StartDate DATE NOT NULL,                  -- Policy start date
    EndDate DATE NOT NULL,                    -- Policy end date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table: Claims
-- Stores information about insurance claims
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each claim
    PolicyID INT NOT NULL,                   -- Foreign key referencing Policies table
    ClaimDate DATE NOT NULL,                 -- Date the claim was filed
    ClaimAmount DECIMAL(10, 2) NOT NULL,     -- Amount claimed
    Description TEXT,                        -- Description of the claim
    Status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Status of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE -- Cascade delete if policy is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON Clients(Email); -- Index on email for faster lookups
CREATE INDEX idx_policies_policy_number ON Policies(PolicyNumber); -- Index on policy number for faster lookups
CREATE INDEX idx_claims_status ON Claims(Status); -- Index on claim status for faster filtering
```
