"""
Generated Code Metadata:
========================
Original URL: https://agodasalecode.com
Prompt: Design a database schema for storing auto insurance comparison data, including fields for tailored coverage options, annual renewal benefits, and penalties for uninsured periods.
Generated: DETERMINISTIC_e03ae983537659c5
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for auto insurance comparison data
CREATE DATABASE AutoInsuranceComparison;

-- Use the created database
USE AutoInsuranceComparison;

-- Create table for insurance providers
CREATE TABLE InsuranceProviders (
    ProviderID INT AUTO_INCREMENT,
    ProviderName VARCHAR(255) NOT NULL,
    ProviderDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProviderID)
);

-- Create table for coverage options
CREATE TABLE CoverageOptions (
    OptionID INT AUTO_INCREMENT,
    OptionName VARCHAR(255) NOT NULL,
    OptionDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OptionID)
);

-- Create table for insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT,
    ProviderID INT NOT NULL,
    PolicyName VARCHAR(255) NOT NULL,
    PolicyDescription TEXT,
    AnnualPremium DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PolicyID),
    FOREIGN KEY (ProviderID) REFERENCES InsuranceProviders(ProviderID)
);

-- Create table for policy coverage options
CREATE TABLE PolicyCoverageOptions (
    PolicyID INT NOT NULL,
    OptionID INT NOT NULL,
    CoverageLimit DECIMAL(10, 2) NOT NULL,
    Deductible DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PolicyID, OptionID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID),
    FOREIGN KEY (OptionID) REFERENCES CoverageOptions(OptionID)
);

-- Create table for annual renewal benefits
CREATE TABLE AnnualRenewalBenefits (
    BenefitID INT AUTO_INCREMENT,
    PolicyID INT NOT NULL,
    BenefitName VARCHAR(255) NOT NULL,
    BenefitDescription TEXT,
    BenefitValue DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BenefitID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID)
);

-- Create table for penalties for uninsured periods
CREATE TABLE UninsuredPenalties (
    PenaltyID INT AUTO_INCREMENT,
    PolicyID INT NOT NULL,
    PenaltyName VARCHAR(255) NOT NULL,
    PenaltyDescription TEXT,
    PenaltyAmount DECIMAL(10, 2) NOT NULL,
    UninsuredPeriodStart DATE NOT NULL,
    UninsuredPeriodEnd DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PenaltyID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID)
);

-- Create table for policy holders
CREATE TABLE PolicyHolders (
    HolderID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HolderID)
);

-- Create table for policy holder policies
CREATE TABLE PolicyHolderPolicies (
    HolderID INT NOT NULL,
    PolicyID INT NOT NULL,
    PolicyEffectiveDate DATE NOT NULL,
    PolicyEndDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HolderID, PolicyID),
    FOREIGN KEY (HolderID) REFERENCES PolicyHolders(HolderID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID)
);

-- Example insert statements
INSERT INTO InsuranceProviders (ProviderName, ProviderDescription)
VALUES ('Provider1', 'This is provider 1'),
       ('Provider2', 'This is provider 2');

INSERT INTO CoverageOptions (OptionName, OptionDescription)
VALUES ('Collision', 'Collision coverage'),
       ('Comprehensive', 'Comprehensive coverage');

INSERT INTO InsurancePolicies (ProviderID, PolicyName, PolicyDescription, AnnualPremium)
VALUES (1, 'Policy1', 'This is policy 1', 1000.00),
       (2, 'Policy2', 'This is policy 2', 1200.00);

INSERT INTO PolicyCoverageOptions (PolicyID, OptionID, CoverageLimit, Deductible)
VALUES (1, 1, 50000.00, 500.00),
       (1, 2, 100000.00, 1000.00);

INSERT INTO AnnualRenewalBenefits (PolicyID, BenefitName, BenefitDescription, BenefitValue)
VALUES (1, 'Safe Driver Discount', 'Discount for safe driving', 100.00),
       (2, 'Multi-Policy Discount', 'Discount for multiple policies', 200.00);

INSERT INTO UninsuredPenalties (PolicyID, PenaltyName, PenaltyDescription, PenaltyAmount, UninsuredPeriodStart, UninsuredPeriodEnd)
VALUES (1, 'Penalty1', 'Penalty for uninsured period', 500.00, '2022-01-01', '2022-01-31'),
       (2, 'Penalty2', 'Penalty for uninsured period', 750.00, '2022-06-01', '2022-06-30');

INSERT INTO PolicyHolders (FirstName, LastName, Email, Phone, Address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
       ('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO PolicyHolderPolicies (HolderID, PolicyID, PolicyEffectiveDate, PolicyEndDate)
VALUES (1, 1, '2022-01-01', '2023-01-01'),
       (2, 2, '2022-06-01', '2023-06-01');
```
