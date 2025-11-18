"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Design a database schema for tracking PantherAI token transactions, staking rewards, and user-generated items within the PantherAI ecosystem.
Generated: DETERMINISTIC_b5dec956503053e1
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for the PantherAI ecosystem
-- Includes tracking token transactions, staking rewards, and user-generated items

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Email address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store token transactions
CREATE TABLE TokenTransactions (
    TransactionID BIGINT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each transaction
    UserID INT NOT NULL,                                  -- Foreign key for the user performing the transaction
    TransactionType ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL, -- Type of transaction
    Amount DECIMAL(18, 8) NOT NULL,                       -- Amount of tokens involved
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Transaction status
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the transaction
    Remarks TEXT,                                         -- Optional description/remarks
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store staking rewards
CREATE TABLE StakingRewards (
    RewardID BIGINT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each reward
    UserID INT NOT NULL,                                    -- Foreign key for the user receiving the reward
    RewardAmount DECIMAL(18, 8) NOT NULL,                   -- Amount of reward tokens
    RewardDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Timestamp of the reward issuance
    RewardType ENUM('Daily', 'Weekly', 'Bonus') NOT NULL,   -- Type of staking reward
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store user-generated items
CREATE TABLE UserGeneratedItems (
    ItemID BIGINT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for each item
    UserID INT NOT NULL,                                    -- Foreign key for the user creating the item
    ItemName VARCHAR(100) NOT NULL,                        -- Name of the item
    ItemType ENUM('Artwork', 'Music', 'Video', 'Other') NOT NULL, -- Type of the item
    Metadata JSON,                                         -- JSON metadata for item details
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Timestamp of item creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_token_transactions_userid ON TokenTransactions(UserID);
CREATE INDEX idx_staking_rewards_userid ON StakingRewards(UserID);
CREATE INDEX idx_user_generated_items_userid ON UserGeneratedItems(UserID);
```
