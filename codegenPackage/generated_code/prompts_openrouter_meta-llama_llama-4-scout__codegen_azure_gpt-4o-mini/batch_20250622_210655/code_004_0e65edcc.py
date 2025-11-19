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
-- Database schema for managing insurance policies

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for storing insurance policies
CREATE TABLE Policies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each policy
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    PolicyType ENUM('Car', 'Home', 'Life') NOT NULL, -- Type of insurance policy
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,     -- Unique policy number
    StartDate DATE NOT NULL,                      -- Policy start date
    EndDate DATE NOT NULL,                        -- Policy end date
    Premium DECIMAL(10, 2) NOT NULL,             -- Monthly premium amount
    CoverageAmount DECIMAL(10, 2) NOT NULL,      -- Coverage amount of the policy
    Status ENUM('Active', 'Expired', 'Cancelled') DEFAULT 'Active', -- Current status of the policy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing claims related to policies
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each claim
    PolicyID INT NOT NULL,                         -- Foreign key referencing Policies
    ClaimDate DATE NOT NULL,                       -- Date the claim was made
    ClaimAmount DECIMAL(10, 2) NOT NULL,          -- Amount claimed
    ClaimStatus ENUM('Pending', 'Approved', 'Denied') DEFAULT 'Pending', -- Status of the claim
    Description TEXT,                              -- Description of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing payment records
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each payment
    PolicyID INT NOT NULL,                         -- Foreign key referencing Policies
    PaymentDate DATE NOT NULL,                     -- Date the payment was made
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Method of payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_policy_number ON Policies(PolicyNumber);
CREATE INDEX idx_claim_policy ON Claims(PolicyID);
CREATE INDEX idx_payment_policy ON Payments(PolicyID);
```
