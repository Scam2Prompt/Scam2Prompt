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
-- Database schema for GYV Seguros to store client information and insurance policy details

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                       -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store insurance policy details
CREATE TABLE InsurancePolicies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each policy
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    PolicyType VARCHAR(50) NOT NULL,            -- Type of insurance policy (e.g., Health, Auto)
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,   -- Unique policy number
    StartDate DATE NOT NULL,                    -- Policy start date
    EndDate DATE NOT NULL,                      -- Policy end date
    PremiumAmount DECIMAL(10, 2) NOT NULL,     -- Monthly premium amount
    CoverageAmount DECIMAL(10, 2) NOT NULL,    -- Coverage amount
    Status ENUM('Active', 'Inactive', 'Cancelled') DEFAULT 'Active',  -- Policy status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Create an index on the email column in Clients table for faster lookups
CREATE INDEX idx_email ON Clients(Email);

-- Create an index on the policy number column in InsurancePolicies table for faster lookups
CREATE INDEX idx_policy_number ON InsurancePolicies(PolicyNumber);
```
