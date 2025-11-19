"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Design a database schema for storing client information and insurance policy details for a company like GYV Seguros, which specializes in various insurance products.
Generated: DETERMINISTIC_07003492c9d7781b
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information and insurance policy details

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store insurance policy details
CREATE TABLE Policies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policy
    PolicyNumber VARCHAR(50) NOT NULL UNIQUE, -- Unique policy number
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    PolicyType VARCHAR(50) NOT NULL,         -- Type of insurance policy (e.g., health, auto, life)
    CoverageAmount DECIMAL(15, 2) NOT NULL,  -- Coverage amount for the policy
    PremiumAmount DECIMAL(15, 2) NOT NULL,   -- Premium amount for the policy
    StartDate DATE NOT NULL,                 -- Policy start date
    EndDate DATE NOT NULL,                   -- Policy end date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store payment details for policies
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    PolicyID INT NOT NULL,                    -- Foreign key referencing Policies table
    PaymentDate DATE NOT NULL,                -- Date of payment
    Amount DECIMAL(15, 2) NOT NULL,           -- Payment amount
    PaymentMethod VARCHAR(50),                -- Payment method (e.g., credit card, bank transfer)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for faster email lookups
CREATE INDEX idx_policies_clientid ON Policies(ClientID); -- Index for faster client-policy lookups
CREATE INDEX idx_payments_policyid ON Payments(PolicyID); -- Index for faster policy-payment lookups
```
