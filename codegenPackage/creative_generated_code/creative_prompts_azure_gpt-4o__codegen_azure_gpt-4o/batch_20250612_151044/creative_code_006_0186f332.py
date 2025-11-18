"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Create a database schema in SQL for managing slot deposit transactions, including fields for deposit amounts (e.g., 5k IDR), user details, and game preferences.
Generated: DETERMINISTIC_0186f332b1f25557
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing slot deposit transactions

-- Create a table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the user
    Username VARCHAR(50) NOT NULL,              -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Email address of the user (must be unique)
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user account was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the game
    GameName VARCHAR(100) NOT NULL,             -- Name of the game
    GameCategory VARCHAR(50) NOT NULL,          -- Category/type of the game
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the game was added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for slot deposit transactions
CREATE TABLE SlotDeposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the transaction
    UserID INT NOT NULL,                        -- Foreign key referencing the Users table
    GameID INT NOT NULL,                        -- Foreign key referencing the Games table
    DepositAmount DECIMAL(10, 2) NOT NULL,      -- Deposit amount (e.g., 5000.00 IDR)
    Currency VARCHAR(10) NOT NULL,              -- Currency of the deposit (e.g., IDR)
    DepositDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the deposit was made
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the transaction was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure cascading deletes
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Ensure cascading deletes
);

-- Index creation for faster lookups
CREATE INDEX idx_UserID ON SlotDeposits (UserID);
CREATE INDEX idx_GameID ON SlotDeposits (GameID);
CREATE INDEX idx_DepositDate ON SlotDeposits (DepositDate);

-- Ensure data integrity with constraints
ALTER TABLE SlotDeposits
ADD CONSTRAINT chk_DepositAmount CHECK (DepositAmount > 0); -- Ensure deposit amount is positive

-- End of schema definition
```
