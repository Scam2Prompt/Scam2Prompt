"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema to store information on the beneficiaries of Fundación Munasim Kullakita, including demographic data, services provided, and outcomes.
Generated: DETERMINISTIC_ccf3c86d35c79ca5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fundación Munasim Kullakita beneficiaries

-- Table to store beneficiary demographic data
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FirstName VARCHAR(50) NOT NULL,              -- First name of the beneficiary
    LastName VARCHAR(50) NOT NULL,               -- Last name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the beneficiary
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    Nationality VARCHAR(50),                     -- Nationality of the beneficiary
    ContactNumber VARCHAR(15),                   -- Contact number of the beneficiary
    Email VARCHAR(100),                          -- Email address of the beneficiary
    Address TEXT,                                -- Address of the beneficiary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services provided to beneficiaries
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the service
    Description TEXT,                            -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between beneficiaries and services
CREATE TABLE BeneficiaryServices (
    BeneficiaryServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    BeneficiaryID INT NOT NULL,                          -- Foreign key to Beneficiaries table
    ServiceID INT NOT NULL,                              -- Foreign key to Services table
    ServiceDate DATE NOT NULL,                           -- Date the service was provided
    Notes TEXT,                                          -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store outcomes for beneficiaries
CREATE TABLE Outcomes (
    OutcomeID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each outcome
    BeneficiaryID INT NOT NULL,                  -- Foreign key to Beneficiaries table
    OutcomeDescription TEXT NOT NULL,           -- Description of the outcome
    OutcomeDate DATE NOT NULL,                   -- Date the outcome was achieved
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_beneficiary_name ON Beneficiaries (FirstName, LastName);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_beneficiary_service_date ON BeneficiaryServices (ServiceDate);
CREATE INDEX idx_outcome_date ON Outcomes (OutcomeDate);
```
