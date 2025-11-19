"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: "Design a basic database schema for storing and managing insurance policies, including car, home, and life insurance, inspired by the services provided by Recuperación JC."
Generated: DETERMINISTIC_0e65edcc9f70e283
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Insurance Policies

-- Table to store information about policyholders
CREATE TABLE Policyholders (
    PolicyholderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policyholder
    FirstName VARCHAR(50) NOT NULL,                -- First name of the policyholder
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the policyholder
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Email address of the policyholder
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Address TEXT,                                  -- Address of the policyholder
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store general insurance policy information
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each policy
    PolicyholderID INT NOT NULL,                   -- Foreign key linking to Policyholders table
    PolicyType ENUM('Car', 'Home', 'Life') NOT NULL, -- Type of insurance policy
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,      -- Unique policy number
    StartDate DATE NOT NULL,                       -- Start date of the policy
    EndDate DATE NOT NULL,                         -- End date of the policy
    PremiumAmount DECIMAL(10, 2) NOT NULL,         -- Premium amount for the policy
    CoverageAmount DECIMAL(15, 2) NOT NULL,        -- Coverage amount for the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PolicyholderID) REFERENCES Policyholders(PolicyholderID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store car insurance-specific details
CREATE TABLE CarInsuranceDetails (
    CarInsuranceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for car insurance details
    PolicyID INT NOT NULL,                         -- Foreign key linking to InsurancePolicies table
    VehicleMake VARCHAR(50) NOT NULL,              -- Make of the vehicle
    VehicleModel VARCHAR(50) NOT NULL,             -- Model of the vehicle
    VehicleYear INT NOT NULL,                      -- Year of the vehicle
    VIN VARCHAR(17) UNIQUE NOT NULL,               -- Vehicle Identification Number
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store home insurance-specific details
CREATE TABLE HomeInsuranceDetails (
    HomeInsuranceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for home insurance details
    PolicyID INT NOT NULL,                          -- Foreign key linking to InsurancePolicies table
    PropertyAddress TEXT NOT NULL,                  -- Address of the insured property
    PropertyValue DECIMAL(15, 2) NOT NULL,          -- Value of the insured property
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store life insurance-specific details
CREATE TABLE LifeInsuranceDetails (
    LifeInsuranceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for life insurance details
    PolicyID INT NOT NULL,                          -- Foreign key linking to InsurancePolicies table
    BeneficiaryName VARCHAR(100) NOT NULL,          -- Name of the beneficiary
    BeneficiaryRelationship VARCHAR(50) NOT NULL,   -- Relationship of the beneficiary to the policyholder
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_policyholder_email ON Policyholders(Email); -- Index for quick lookup by email
CREATE INDEX idx_policy_number ON InsurancePolicies(PolicyNumber); -- Index for quick lookup by policy number
CREATE INDEX idx_vin ON CarInsuranceDetails(VIN); -- Index for quick lookup by VIN
```
