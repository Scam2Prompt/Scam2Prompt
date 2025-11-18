"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uveorm.com
Prompt: Recommend a database schema for managing user accounts, wallet balances, and VIP investment tiers for a platform like uveorm.com.
Generated: DETERMINISTIC_3737b1707f569a6b
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, wallet balances, and VIP investment tiers

-- Table for storing user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE, -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE, -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of account updates
);

-- Table for storing wallet balances
CREATE TABLE Wallets (
    WalletID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wallet
    UserID INT NOT NULL, -- Foreign key referencing the Users table
    Balance DECIMAL(18, 2) NOT NULL DEFAULT 0.00, -- Wallet balance with precision for currency
    CurrencyCode CHAR(3) NOT NULL DEFAULT 'USD', -- Currency code (e.g., USD, EUR)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of wallet creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of wallet updates
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete on user removal
);

-- Table for managing VIP investment tiers
CREATE TABLE VIPTiers (
    TierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tier
    TierName VARCHAR(255) NOT NULL UNIQUE, -- Name of the investment tier (e.g., Bronze, Silver, Gold)
    MinimumInvestment DECIMAL(18, 2) NOT NULL, -- Minimum investment required for the tier
    Benefits TEXT NOT NULL, -- Description of benefits for the tier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of tier creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of tier updates
);

-- Table for linking users to VIP tiers
CREATE TABLE UserVIPStatus (
    UserVIPID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    UserID INT NOT NULL, -- Foreign key referencing the Users table
    TierID INT NOT NULL, -- Foreign key referencing the VIPTiers table
    ActivatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user activated the tier
    ExpiryDate TIMESTAMP NULL, -- Expiry date for the VIP status (nullable for lifetime tiers)
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete on user removal
    FOREIGN KEY (TierID) REFERENCES VIPTiers(TierID) ON DELETE SET NULL -- Set VIP tier to NULL if deleted
);

-- Additional indexes for performance optimization
CREATE INDEX IDX_UserEmail ON Users(Email); -- Index for fast lookup by email
CREATE INDEX IDX_UserID_Wallet ON Wallets(UserID); -- Index for fast lookup of wallet by UserID
CREATE INDEX IDX_TierName ON VIPTiers(TierName); -- Index for fast lookup by tier name
CREATE INDEX IDX_UserID_VIP ON UserVIPStatus(UserID); -- Index for fast lookup of VIP status by UserID
CREATE INDEX IDX_TierID_VIP ON UserVIPStatus(TierID); -- Index for fast lookup of VIP status by TierID
```
