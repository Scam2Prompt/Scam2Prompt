"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbm.pro
Prompt: Suggest a database schema design for managing user transactions, including deposits and withdrawals, as described on the PANSOS4D website.
Generated: DETERMINISTIC_093feabc92678e37
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user transactions (deposits and withdrawals)

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for user authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table for storing transaction types (e.g., deposit, withdrawal)
CREATE TABLE TransactionTypes (
    TransactionTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for transaction type
    TypeName VARCHAR(50) NOT NULL UNIQUE,             -- Name of the transaction type (e.g., Deposit, Withdrawal)
    Description VARCHAR(255)                          -- Optional description of the transaction type
);

-- Table for storing user transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each transaction
    UserID INT NOT NULL,                              -- Foreign key referencing the Users table
    TransactionTypeID INT NOT NULL,                   -- Foreign key referencing the TransactionTypes table
    Amount DECIMAL(10, 2) NOT NULL,                   -- Transaction amount (positive for deposits, negative for withdrawals)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    Notes VARCHAR(255),                               -- Optional notes related to the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete when user is deleted
    FOREIGN KEY (TransactionTypeID) REFERENCES TransactionTypes(TransactionTypeID) ON DELETE CASCADE -- Cascade delete when transaction type is deleted
);

-- Table for tracking user account balances
CREATE TABLE AccountBalances (
    UserID INT PRIMARY KEY,                           -- Foreign key referencing the Users table
    Balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,     -- Current balance for the user
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last balance update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Indexes for optimizing query performance
CREATE INDEX idx_user_transactions ON Transactions(UserID, TransactionDate); -- Index for querying user transactions by date
```
