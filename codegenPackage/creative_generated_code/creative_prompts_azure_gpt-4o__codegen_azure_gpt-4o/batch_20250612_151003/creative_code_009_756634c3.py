"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Create a database schema to store user data, token holdings, reward points, and redemption history for a rewards ecosystem like Lingo.
Generated: DETERMINISTIC_756634c3bcde987a
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Rewards Ecosystem

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,             -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE,               -- User's email address
    PasswordHash VARCHAR(255) NOT NULL,               -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the user account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store token holdings for each user
CREATE TABLE TokenHoldings (
    HoldingID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each token holding record
    UserID INT NOT NULL,                              -- Foreign key referencing Users table
    TokenType VARCHAR(50) NOT NULL,                  -- Type of token (e.g., "LingoToken")
    Balance DECIMAL(18, 8) NOT NULL DEFAULT 0,        -- Token balance with precision
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is removed
);

-- Table to store reward points for each user
CREATE TABLE RewardPoints (
    RewardID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each reward record
    UserID INT NOT NULL,                              -- Foreign key referencing Users table
    Points INT NOT NULL DEFAULT 0,                    -- Reward points balance
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is removed
);

-- Table to store redemption history
CREATE TABLE RedemptionHistory (
    RedemptionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each redemption record
    UserID INT NOT NULL,                              -- Foreign key referencing Users table
    RedemptionDetails VARCHAR(255) NOT NULL,          -- Details about the redemption (e.g., item redeemed)
    PointsRedeemed INT NOT NULL,                      -- Points redeemed for this transaction
    RedemptionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of redemption
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is removed
);

-- Indexes to improve query performance
CREATE INDEX idx_user_email ON Users (Email);         -- Index for fast email lookups
CREATE INDEX idx_user_token ON TokenHoldings (UserID, TokenType); -- Compound index for user token lookups
CREATE INDEX idx_user_points ON RewardPoints (UserID); -- Index for user reward points lookups
CREATE INDEX idx_user_redemption ON RedemptionHistory (UserID); -- Index for user redemption history lookups
```
