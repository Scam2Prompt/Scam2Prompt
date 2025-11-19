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
-- Create database for insurance brokerage firm
CREATE DATABASE InsuranceBrokerage;

-- Use the database
USE InsuranceBrokerage;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    PolicyType VARCHAR(100) NOT NULL,
    PolicyNumber VARCHAR(255) UNIQUE NOT NULL,
    EffectiveDate DATE NOT NULL,
    ExpirationDate DATE NOT NULL,
    Premium DECIMAL(10, 2) NOT NULL,
    CoverageAmount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PolicyID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for claims
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT,
    PolicyID INT NOT NULL,
    ClaimDate DATE NOT NULL,
    ClaimAmount DECIMAL(10, 2) NOT NULL,
    ClaimStatus VARCHAR(50) NOT NULL DEFAULT 'Pending',
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClaimID),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE
);

-- Create table for claim updates
CREATE TABLE ClaimUpdates (
    UpdateID INT AUTO_INCREMENT,
    ClaimID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    UpdateStatus VARCHAR(50) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ClaimID) REFERENCES Claims(ClaimID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_policy_number ON InsurancePolicies (PolicyNumber);
CREATE INDEX idx_claim_policy_id ON Claims (PolicyID);

-- Create stored procedure to insert new client
DELIMITER //
CREATE PROCEDURE InsertClient(
    IN pFirstName VARCHAR(255),
    IN pLastName VARCHAR(255),
    IN pEmail VARCHAR(255),
    IN pPhone VARCHAR(20),
    IN pAddress VARCHAR(255)
)
BEGIN
    INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
    VALUES (pFirstName, pLastName, pEmail, pPhone, pAddress);
END//
DELIMITER ;

-- Create stored procedure to insert new insurance policy
DELIMITER //
CREATE PROCEDURE InsertInsurancePolicy(
    IN pClientID INT,
    IN pPolicyType VARCHAR(100),
    IN pPolicyNumber VARCHAR(255),
    IN pEffectiveDate DATE,
    IN pExpirationDate DATE,
    IN pPremium DECIMAL(10, 2),
    IN pCoverageAmount DECIMAL(10, 2)
)
BEGIN
    INSERT INTO InsurancePolicies (ClientID, PolicyType, PolicyNumber, EffectiveDate, ExpirationDate, Premium, CoverageAmount)
    VALUES (pClientID, pPolicyType, pPolicyNumber, pEffectiveDate, pExpirationDate, pPremium, pCoverageAmount);
END//
DELIMITER ;

-- Create stored procedure to insert new claim
DELIMITER //
CREATE PROCEDURE InsertClaim(
    IN pPolicyID INT,
    IN pClaimDate DATE,
    IN pClaimAmount DECIMAL(10, 2),
    IN pDescription TEXT
)
BEGIN
    INSERT INTO Claims (PolicyID, ClaimDate, ClaimAmount, Description)
    VALUES (pPolicyID, pClaimDate, pClaimAmount, pDescription);
END//
DELIMITER ;

-- Example usage:
CALL InsertClient('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');
CALL InsertInsurancePolicy(1, 'Auto', 'ABC123', '2022-01-01', '2023-01-01', 1000.00, 50000.00);
CALL InsertClaim(1, '2022-06-01', 1000.00, 'Accident on highway');
```
