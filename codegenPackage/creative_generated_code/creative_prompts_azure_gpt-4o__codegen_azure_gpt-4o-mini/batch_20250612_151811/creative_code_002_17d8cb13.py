"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Create a database schema for KEK Insurance Brokers to manage customer information, insurance policies (e.g., accident insurance, liability insurance), and claims processing, based on the services mentioned on their site.
Generated: DETERMINISTIC_17d8cb13e724e886
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for KEK Insurance Brokers

-- Create the database
CREATE DATABASE kek_insurance_brokers;

-- Use the database
USE kek_insurance_brokers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for communication
    Phone VARCHAR(15),                         -- Optional phone number
    Address VARCHAR(255),                       -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store insurance policies
CREATE TABLE InsurancePolicies (
    PolicyID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each insurance policy
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    PolicyType ENUM('Accident', 'Liability') NOT NULL, -- Type of insurance policy
    PolicyNumber VARCHAR(50) NOT NULL UNIQUE,   -- Unique policy number
    StartDate DATE NOT NULL,                     -- Start date of the policy
    EndDate DATE NOT NULL,                       -- End date of the policy
    Premium DECIMAL(10, 2) NOT NULL,            -- Monthly premium amount
    Status ENUM('Active', 'Inactive', 'Expired') DEFAULT 'Active', -- Policy status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Relationship constraint
);

-- Table to store claims information
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each claim
    PolicyID INT NOT NULL,                       -- Foreign key referencing InsurancePolicies table
    ClaimNumber VARCHAR(50) NOT NULL UNIQUE,    -- Unique claim number
    ClaimAmount DECIMAL(10, 2) NOT NULL,        -- Amount claimed
    ClaimDate DATE NOT NULL,                     -- Date of the claim
    Status ENUM('Pending', 'Approved', 'Denied') DEFAULT 'Pending', -- Claim status
    Description TEXT,                            -- Description of the claim
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Relationship constraint
);

-- Table to store payments for insurance policies
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each payment
    PolicyID INT NOT NULL,                       -- Foreign key referencing InsurancePolicies table
    PaymentDate DATE NOT NULL,                   -- Date of the payment
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Payment method
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID) ON DELETE CASCADE -- Relationship constraint
);

-- Indexes for faster querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_policy_customer ON InsurancePolicies(CustomerID);
CREATE INDEX idx_claim_policy ON Claims(PolicyID);
CREATE INDEX idx_payment_policy ON Payments(PolicyID);

-- Note: Ensure to implement proper backup and error handling mechanisms in your application code when interfacing with this database.

-- End of schema definition
```
