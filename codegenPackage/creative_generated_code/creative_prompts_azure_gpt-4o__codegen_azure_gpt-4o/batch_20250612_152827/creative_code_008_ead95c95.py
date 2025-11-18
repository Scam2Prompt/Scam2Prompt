"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Generate a SQL database schema to store user data for Shiba Saga games, including $SHIA token balances, unlocked NFTs, and staking history.
Generated: DETERMINISTIC_ead95c95f7d5fada
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Shiba Saga database
-- This schema includes tables for storing user data, $SHIA token balances, unlocked NFTs, and staking history.

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the user
    Username VARCHAR(50) NOT NULL,              -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Email of the user
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password (security best practice)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store $SHIA token balances for users
CREATE TABLE ShiaBalances (
    BalanceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the balance record
    UserID INT NOT NULL,                        -- Foreign key to Users table
    TokenBalance DECIMAL(18, 8) NOT NULL,       -- Current $SHIA token balance
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last balance update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure cascading delete
);

-- Table to store unlocked NFTs for users
CREATE TABLE UnlockedNFTs (
    NFTID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the unlocked NFT record
    UserID INT NOT NULL,                        -- Foreign key to Users table
    NFTName VARCHAR(100) NOT NULL,             -- Name of the unlocked NFT
    NFTMetadata JSON NOT NULL,                 -- Metadata of the NFT (stored as JSON)
    UnlockedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the NFT was unlocked
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure cascading delete
);

-- Table to store staking history for users
CREATE TABLE StakingHistory (
    StakingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the staking record
    UserID INT NOT NULL,                        -- Foreign key to Users table
    StakedAmount DECIMAL(18, 8) NOT NULL,       -- Amount of $SHIA tokens staked
    StakingStart TIMESTAMP NOT NULL,            -- Timestamp when staking started
    StakingEnd TIMESTAMP,                       -- Timestamp when staking ended (nullable if ongoing)
    RewardEarned DECIMAL(18, 8) DEFAULT 0.0,    -- Reward earned from staking
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure cascading delete
);

-- Ensure database integrity and performance by creating indexes
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_user_balance ON ShiaBalances (UserID);
CREATE INDEX idx_user_nft ON UnlockedNFTs (UserID);
CREATE INDEX idx_user_staking ON StakingHistory (UserID);

-- Optional: Add triggers for logging changes or maintaining derived data (as needed)
-- Note: Ensure to test thoroughly in production environments.
```
