"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Create a database schema to manage user accounts, transaction history, and game preferences for an online slot gaming platform like Maxslot88.
Generated: DETERMINISTIC_2dd352bfc1e34462
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database: SlotGamingPlatform
CREATE DATABASE SlotGamingPlatform;

-- Switch to the newly created database
USE SlotGamingPlatform;

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- User's unique username
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- User's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Account update timestamp
    IsActive BOOLEAN DEFAULT TRUE -- Indicates if the account is active
);

-- Table: Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL, -- FK to Users table
    Amount DECIMAL(10, 2) NOT NULL, -- Transaction amount (can be positive or negative)
    TransactionType ENUM('Deposit', 'Withdrawal', 'GameWin', 'GameLoss') NOT NULL, -- Type of transaction
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Enforce UserID referential integrity
);

-- Table: GamePreferences
CREATE TABLE GamePreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference record
    UserID INT NOT NULL, -- FK to Users table
    PreferredTheme VARCHAR(50), -- User's preferred slot game theme
    SoundEnabled BOOLEAN DEFAULT TRUE, -- Whether sound is enabled
    BetAmount DECIMAL(10, 2) DEFAULT 0.00, -- Default bet amount for the user
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Enforce UserID referential integrity
);

-- Indexes for optimization
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_user_preferences ON GamePreferences(UserID);

-- Error handling: Ensuring foreign key checks are enabled
SET FOREIGN_KEY_CHECKS = 1;

-- Ensure code adheres to production readiness by including security measures
-- For example: Password hashes are stored, and database access permissions should be configured externally.
```
