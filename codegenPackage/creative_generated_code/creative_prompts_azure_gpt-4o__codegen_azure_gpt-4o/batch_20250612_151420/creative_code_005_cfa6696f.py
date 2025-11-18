"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Suggest a database schema for tracking wallet transactions, slot game bonuses, and user activity, optimized for platforms like "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_cfa6696f6dab1c52
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for tracking wallet transactions, slot game bonuses, and user activity

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,     -- Hashed password for security
    WalletBalance DECIMAL(10, 2) DEFAULT 0, -- Balance in the user's wallet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table: WalletTransactions
CREATE TABLE WalletTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique transaction identifier
    UserID INT NOT NULL, -- Reference to Users table
    TransactionType ENUM('DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'BONUS') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL, -- Transaction amount
    TransactionStatus ENUM('PENDING', 'COMPLETED', 'FAILED') NOT NULL, -- Status of transaction
    ReferenceID VARCHAR(64) NULL, -- Optional reference ID for external systems
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table: SlotGameBonuses
CREATE TABLE SlotGameBonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus
    UserID INT NOT NULL, -- Reference to Users table
    BonusType ENUM('FREE_SPINS', 'CASH_BACK', 'MATCH_DEPOSIT') NOT NULL, -- Type of bonus
    BonusAmount DECIMAL(10, 2) NOT NULL, -- Bonus amount
    ExpiryDate DATE NOT NULL, -- Expiry date for the bonus
    IsRedeemed BOOLEAN DEFAULT FALSE, -- Status of the bonus
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bonus creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table: UserActivity
CREATE TABLE UserActivity (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity log
    UserID INT NOT NULL, -- Reference to Users table
    ActivityType ENUM('LOGIN', 'LOGOUT', 'GAME_PLAY', 'TRANSACTION', 'BONUS_REDEEM') NOT NULL, -- Type of activity
    ActivityDetail TEXT NOT NULL, -- Detailed description of the activity
    ActivityTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the activity
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Indexing for faster queries
CREATE INDEX idx_user_wallet_transactions ON WalletTransactions(UserID);
CREATE INDEX idx_user_slot_game_bonuses ON SlotGameBonuses(UserID);
CREATE INDEX idx_user_activity ON UserActivity(UserID);
```
