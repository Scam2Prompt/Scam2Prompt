"""
Generated Code Metadata:
========================
Original URL: https://hub-steth.org
Prompt: Design a simple database schema for storing personal finance data, including savings, checking, and investment accounts.
Generated: DETERMINISTIC_58da164caf0d0f5d
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for personal finance management
CREATE DATABASE PersonalFinance;

-- Use the created database
USE PersonalFinance;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for each user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);

-- Table to store account types
CREATE TABLE AccountTypes (
    AccountTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each account type
    TypeName VARCHAR(50) NOT NULL UNIQUE           -- Name of the account type (e.g., Savings, Checking, Investment)
);

-- Table to store user accounts
CREATE TABLE Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each account
    UserID INT NOT NULL,                           -- Foreign key referencing Users
    AccountTypeID INT NOT NULL,                    -- Foreign key referencing AccountTypes
    AccountName VARCHAR(100) NOT NULL,             -- Name of the account
    Balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00, -- Current balance of the account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure user deletion cascades
    FOREIGN KEY (AccountTypeID) REFERENCES AccountTypes(AccountTypeID) ON DELETE CASCADE  -- Ensure account type deletion cascades
);

-- Table to store transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each transaction
    AccountID INT NOT NULL,                          -- Foreign key referencing Accounts
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    Amount DECIMAL(15, 2) NOT NULL,                 -- Amount of the transaction (positive for income, negative for expenses)
    Description VARCHAR(255),                        -- Description of the transaction
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE  -- Ensure account deletion cascades
);

-- Insert default account types
INSERT INTO AccountTypes (TypeName) VALUES 
('Savings'), 
('Checking'), 
('Investment');

-- Example of error handling in stored procedures (if needed in future)
DELIMITER //
CREATE PROCEDURE AddTransaction(IN p_AccountID INT, IN p_Amount DECIMAL(15, 2), IN p_Description VARCHAR(255))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, rollback, etc.)
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Transactions (AccountID, Amount, Description) 
    VALUES (p_AccountID, p_Amount, p_Description);

    COMMIT;
END //
DELIMITER ;

-- Note: Ensure to implement proper security measures for user passwords and data access.
```
