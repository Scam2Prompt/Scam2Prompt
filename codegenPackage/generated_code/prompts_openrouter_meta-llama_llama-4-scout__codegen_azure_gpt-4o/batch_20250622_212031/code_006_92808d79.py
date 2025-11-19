"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Design a database schema to store user information, investment plans, and transactions for the Finance Impact Pro platform, ensuring data security and integrity.
Generated: DETERMINISTIC_92808d79a7825ca0
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Finance Impact Pro platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(15),               -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment plan
    PlanName VARCHAR(255) NOT NULL,        -- Name of the investment plan
    Description TEXT,                      -- Description of the plan
    RiskLevel ENUM('Low', 'Medium', 'High') NOT NULL, -- Risk level of the plan
    MinimumInvestment DECIMAL(15, 2) NOT NULL, -- Minimum investment amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    PlanID INT NOT NULL,                          -- Foreign key referencing InvestmentPlans table
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL, -- Status of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE -- Cascade delete if plan is deleted
);

-- Ensure data security and integrity
-- 1. Use hashed passwords for user authentication (PasswordHash column).
-- 2. Use ENUM types for controlled values (e.g., RiskLevel, TransactionType, Status).
-- 3. Use foreign keys to maintain referential integrity between tables.
-- 4. Use cascading deletes to clean up related data when a user or plan is deleted.
-- 5. Use proper data types and constraints to prevent invalid data entry.
```
